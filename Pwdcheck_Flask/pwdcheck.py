from flask import Flask, request, render_template, json
import requests
import hashlib
import sys

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/checkpwd', methods=['GET', 'POST'])
def checkpwd():
    def request_api_data(query_char):
        url = 'https://api.pwnedpasswords.com/range/' + query_char
        res = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(f'Error fetching:{res.status_code}, check the API and try again')
        return res

    def get_pass_leaks_count(response_hashes, our_hash_to_check):
        hashes = (line.split(':') for line in response_hashes.text.splitlines())
        for h, count in hashes:
            # print(h,count)
            if h == our_hash_to_check:
                return count
        return 0

    def pwned_api_check(pwd):
        sha1password = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
        first5_char, tail_char = sha1password[:5], sha1password[5:]
        response = request_api_data(first5_char)
        return get_pass_leaks_count(response, tail_char)

    pwd = request.json['password']
    while True:
        count = pwned_api_check(pwd)
        if count:
            return f'Your password: "{pwd}" was found {count} times...you should probably change your password'
            break
            # pwd = input(
            #     "Please Enter New password, as your previous password is found in the list of hacked passwords: ")
            # if pwd != 'STOP':
            #     count = pwned_api_check(pwd)
            # else:
            #     print(f"Hey!!! As you had entered {pwd}, We respect your word and terminated the program")
            #     break
        else:
            return f'Your password: "{pwd}" was not found... Carryon!!!'
            break


if __name__ == '__main__':
    app.run(debug=True)
