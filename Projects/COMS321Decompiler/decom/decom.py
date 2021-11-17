import sys

### Denotes done

instruction_dict = [
  ["ADD", 0b10001011000, "R"], ###
  ["ADDI", 0b1001000100, "I"], ###
  ["AND", 0b10001010000, "R"], ###
  ["ANDI", 0b1001001000, "I"], ###
  ["B", 0b000101, "B"],
  ["BL", 0b100101, "B"],
  ["BR", 0b11010110000, "R"], ###
  ["CBNZ", 0b10110101, "CB"],
  ["CBZ", 0b10110100, "CB"],
  ["DUMP", 0b11111111110, "DUMP"],
  ["EOR", 0b11001010000, "R"], ###
  ["EORI", 0b1101001000, "I"], ###
  ["HALT", 0b11111111111, "HALT"],
  ["LDUR", 0b11111000010, "D"], ###
  ["LSL", 0b11010011011, "R"], ###
  ["LSR", 0b11010011010, "R"], ###
  ["ORR", 0b10101010000, "R"], ###
  ["ORRI", 0b1011001000, "I"], ###
  ["PRNL", 0b11111111100, "PRNL"],
  ["PRNT", 0b11111111101, "PRNT"],
  ["STUR", 0b11111000000, "D"], ###
  ["SUB", 0b11001011000, "R"], ###
  ["SUBI", 0b1101000100, "I"], ###
  ["SUBIS", 0b1111000100, "I"], ###
  ["SUBS", 0b11101011000, "R"], ###
  ["MUL", 0b10011011000, "R"] ###
]

def decodeBytes(current_byte):
    if current_byte == 0b0:
        return 0
    for instruction in instruction_dict:
        if current_byte.startswith(bin(instruction[1])):
            return instruction
    return "ERR"

def decodeRInstruction(instruction, instruction_info):
    opcode = instruction[2:13]
    Rm = instruction[13:18]
    shamt = instruction[18:24]
    Rn = instruction[24:29]
    Rd = instruction[29:]
    print(opcode + " " + Rm + " " + shamt + " " + Rn + " " + Rd)
    if instruction_info[0] == "ADD" or "AND" or "EOR" or "ORR" or "SUB" or "SUBS" or "MUL":
        print(instruction_info[0] + " X" + str(int(Rd, 2)) + ", X" + str(int(Rn, 2)) + ", X" + str(int(Rm, 2)))
    elif instruction_info[0] == "BR":
        print(instruction_info[0] + " X" + str(int(Rd, 2)))
    elif instruction_info[0] == "LSL" or "LSR":
        print(instruction_info[0] + " X" + str(int(Rd, 2)) + ", X" + str(int(Rn, 2)) + ", #" + str(int(shamt)))
    else:
        print("Error decoding R type instruction. Instruction data: " + instruction_info +
              ". Instruction binary: " + instruction)


def decodeIInstruction(instruction, instruction_info):
    opcode = instruction[2:12] 
    ALU_immediate = instruction[12:23]
    Rn = instruction[23:29]
    Rd = instruction[29:]
    print(opcode + " " + ALU_immediate + " " + Rn + " " + Rd)
    if instruction_info[0] == "ADDI" or "ANDI" or "ORRI" or "SUBI" or "EORI" or "SUBIS": 
        print(instruction_info[0] + " X" + str(int(Rd, 2)) + ", X" + str(int(Rn, 2)) + ", #" + str(int(ALU_immediate, 2)))
    else:
        print("Error decoding I type instruction. Instruction data: " + instruction_info +
              ". Instruction binary: " + instruction)


def decodeDInstruction(instruction, instruction_info):
    print(str(instruction))
    opcode = instruction[2:13]
    DT_addreess = instruction[13:22]
    op = instruction[22:24]
    Rn = instruction[24:29]
    Rd = instruction[29:]

    print(opcode + " " + DT_addreess + " " + op + " " + Rn + " " + Rd)
    
    if instruction_info[0] == "STUR" or "LDUR":
        print(instruction_info[0] + " X" + str(int(Rd, 2)) + ", [X" + str(int(Rn, 2)) + ", #" + str(int(DT_addreess, 2)) + "]")
    else:
        print("Error decoding D type instruction. Instruction data: " + instruction_info +
              ". Instruction binary: " + instruction)


def decodeBInstruction(instruction, instruction_info):
    opcode = instruction[2:8]
    BR_Address = instruction[8:]

    
    print("In decodeB")


def decodeCBInstruction(instruction, instruction_info):
    print("In decodeCB")


def decodeDUMPInstruction(instruction, instruction_info):
    print("In decodeDUMP")


def decodeHALTInstruction(instruction, instruction_info):
    print("In decodeHALT")


def decodePRNLInstruction(instruction, instruction_info):
    print("In decodePRNL")


def decodePRNTInstruction(instruction, instruction_info):
    print("In decodePRNT")


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
            decodeRInstruction(current_byte, instruction)
        elif instruction[2] == "I":
            decodeIInstruction(current_byte, instruction)
        elif instruction[2] == "D":
            decodeDInstruction(current_byte, instruction)
        elif instruction[2] == "B":
            decodeBInstruction(current_byte, instruction)
        elif instruction[2] == "CB":
            decodeCBInstruction(current_byte, instruction)
        elif instruction[2] == "DUMP":
            decodeDUMPInstruction(current_byte, instruction)
        elif instruction[2] == "HALT":
            decodeHALTInstruction(current_byte, instruction)
        elif instruction[2] == "PRNL":
            decodePRNLInstruction(current_byte, instruction)
        elif instruction[2] == "PRNT":
            decodePRNTInstruction(current_byte, instruction)
        else:
            print("ERROR: Failure in reading instruction class. Instruction: " + instruction[0] + ". Type: " + instruction[2])
            exit(1)
