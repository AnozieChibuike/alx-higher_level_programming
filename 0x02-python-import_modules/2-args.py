#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_length = len(sys.argv)
    print("{} arguments:".format(arg_length - 1))
    for i in range(1, arg_length):
        print("{}: {}".format(i, sys.argv[i]))