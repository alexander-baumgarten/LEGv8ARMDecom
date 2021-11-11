import sys

if __name__ == "__main__":
    print("In main")
    f = open(sys.argv[1], "rb")
    #while(f.readable())
    #bin(int.from_bytes(f.read(4), byteorder='big'))
def decodeBytes():
    print("in decodeBytes")