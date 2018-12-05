#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for i in list:
        if i[0] is '_' and i[1] is '_':
            pass
        else:
            print("{0}".format(i))
