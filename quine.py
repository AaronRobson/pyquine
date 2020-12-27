def f():
    a = "def f():\n    a = %r\n    print(a %% a)\n\n\nif __name__ == '__main__':\n    f()"
    print(a % a)


if __name__ == '__main__':
    f()
