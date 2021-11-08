import sys

if __name__ == "__main__":
    print("In main")
    f = open(sys.argv[1], "rb")
    print(f.read(5))