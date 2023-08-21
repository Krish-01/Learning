def even_num(n):
    try:
        return [i for i in range(n+1) if i%2==0]
    except Exception as e:
        return e
       