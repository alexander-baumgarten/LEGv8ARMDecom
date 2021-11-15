import sys

instruction_dict = [
  ["ADD", 0b10001011000, "R"],
  ["ADDI", 0b1001000100, "I"],
  ["AND", 0b10001010000, "R"],
  ["ANDI", 0b1001001000, "I"],
  ["B", 0b000101, "B"],
  ["BL", 0b100101, "B"],
  ["BR", 0b11010110000, "R"],
  ["CBNZ", 0b10110101, "CB"],
  ["CBZ", 0b10110100, "CB"],
  ["DUMP", 0b11111111110, "DUMP"],
  ["EOR", 0b11001010000, "R"],
  ["EORI", 0b1101001000, "I"],
  ["HALT", 0b11111111111, "HALT"],
  ["LDUR", 0b11111000010, "D"],
  ["LSL", 0b11010011011, "R"],
  ["LSR", 0b11010011010, "R"],
  ["ORR", 0b10101010000, "R"],
  ["ORRI", 0b1011001000, "I"],
  ["PRNL", 0b11111111100, "PRNL"],
  ["PRNT", 0b11111111101, "PRNT"],
  ["STUR", 0b11111000000, "D"],
  ["SUB", 0b11001011000, "R"],
  ["SUBI", 0b1101000100, "I"],
  ["SUBIS", 0b1111000100, "I"],
  ["SUBS", 0b11101011000, "R"],
  ["MUL", 0b10011011000, "R"]
]

def decodeBytes(current_byte):
    if current_byte == 0b0:
        return 0
    for instruction in instruction_dict:
        if current_byte.startswith(bin(instruction[1])):
            return instruction
    return "ERR"

def decodeRInstruction(instruction):
    print(instruction[2:])
    opcode = instruction[2:13]
    Rm = instruction[13:18]
    shamt = instruction[18:24]
    Rn = instruction[24:29]
    Rd = instruction[29:]
    print(opcode + " " + Rm + " " + shamt + " " + Rn + " " + Rd)


if __name__ == "__main__":
    f = open(sys.argv[1], "rb")
    while True:
        current_byte = bin(int.from_bytes(f.read(4), byteorder='big'))
        if current_byte == bin(0b0):
            break
        else:
            instruction = decodeBytes(current_byte)
            if instruction == "ERR":
                print("ERROR: Failure reading opcode. Result: " + instruction + ". Input: " + current_byte)
                exit()
        if instruction[2] == "R":
            decodeRInstruction(current_byte)
            #g = str(current_byte)[2:13]
            #print(g)
        elif instruction[2] == "I":
            print("I")
        elif instruction[2] == "D":
            print("D")
        elif instruction[2] == "B":
            print("B")
        elif instruction[2] == "CB":
            print("CB")
        elif instruction[2] == "DUMP":
            print("DUMP")
        elif instruction[2] == "HALT":
            print("HALT")
        elif instruction[2] == "PRNL":
            print("PRNL")
        elif instruction[2] == "PRNT":
            print("PRNT")
        else:
            print("ERROR: Failure in reading instruction class. Instruction: " + instruction[0] + ". Type: " + instruction[2])
            exit(1)
