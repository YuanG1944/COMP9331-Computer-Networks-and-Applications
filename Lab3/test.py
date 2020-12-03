try:
    f = open("123.html")
    c = f.read()
    print(c)
except FileNotFoundError:
    print("404")