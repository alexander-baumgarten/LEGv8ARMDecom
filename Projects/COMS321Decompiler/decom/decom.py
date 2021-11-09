import sys

if __name__ == "__main__":
    print("In main")
    f = open(sys.argv[1], "rb")
    #print(sys.argv)
    print(bin(int.from_bytes(f.read(4), byteorder='big')))