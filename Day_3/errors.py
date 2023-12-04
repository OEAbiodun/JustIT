for i in dir(locals()['__builtins__']):
    if "Error" in i:
        print(i)