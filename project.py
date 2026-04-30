# dictionary (like a table)
opcodes = {
    "JNS": "0",  #jump and store (stores the address to return back , and jump toanother location )
    "LOAD": "1",
    "STORE": "2",
    "ADD": "3",
    "SUBT": "4",
    "INPUT": "5",
    "OUTPUT": "6",
    "HALT": "7",
    "SKIPCOND": "8",
    "JUMP": "9",
    "CLEAR": "A",

    "ADDI": "B",
    "JUMPI": "C",
    "LOADI": "D",
    "STOREI": "E"
}

no_operand = ["INPUT", "OUTPUT", "HALT", "CLEAR"]
directives = ["DEC", "HEX"]

labels = {}  #store variables address which are lables ex X,Y   # {} -> means dictionary (mapping "key -> value")
lines = []   #it read file line by line and store it here       #[] -> means it is a list 

def clean_line(line):
    # Remove comments
    if "/" in line:
        line = line[:line.index("/")]

    # Remove spaces at start and end
    line = line.strip()

    # Replace commas with spaces
    line = line.replace(",", " ")

    # Split line into words
    return line.split()


# Step 1: Read and clean input.asm
try:
    with open("input.asm", "r") as file:

        for line_number, line in enumerate(file, 1):
            parts = clean_line(line)

            if len(parts) == 0:
                continue

            lines.append((line_number, parts))

except FileNotFoundError:
    print("Error: input.asm not found")
    exit()

address = 0

for line_number, parts in lines:
    first = parts[0].upper()

    # CASE 1: label
    if first not in opcodes and first not in directives:
        label = parts[0].upper()

        if label in labels:
            print(f"Error at line {line_number}: Duplicate label '{label}'")
            exit()

        labels[label] = address

        
        if len(parts) > 1:
            address += 1

    else:
        address += 1

machinecode = []
for line_number, parts in lines:
    instruction = parts[0].upper()
    operand_index = 1
    if instruction not in opcodes and instruction not in directives:
        if len(parts) == 1:
            continue  # This line only contains a label, no instruction to process
        instruction = parts[1].upper()
        operand_index = 2
        
    elif instruction in no_operand:
        opcode = opcodes[instruction]
        machinecode.append(opcode + "000")

    elif instruction in directives:
        if len(parts) < 2:
            print(f"Error at line {line_number}: Missing operand for directive '{instruction}'")
            exit()
        second = parts[operand_index].upper()
        try:
            if instruction == "DEC":
                operand = int(second)
            else:  # HEX
                operand = int(second, 16)
        except ValueError:
            print(f"Error at line {line_number}: Invalid operand '{second}' for directive '{instruction}'")
            exit()

        machinecode.append(f"{operand:03X}")  #f"{operand:03X}" -> means convert operand to hexadecimal and make it 3 digits long (with leading zeros if necessary)    

    elif instruction in opcodes:
        opcode = opcodes[instruction]
        if len(parts) < 2:
            print(f"Error at line {line_number}: Missing operand for instruction '{instruction}'")
            exit()
        second = parts[operand_index].upper()
        if second in labels:
            operand = labels[second]
        else:
            try:
                operand = int(second)
            except ValueError:
                print(f"Error at line {line_number}: Invalid operand '{second}'")
                exit()

        machinecode.append(opcode + f"{operand:03X}")  #f"{operand:03X}" -> means convert operand to hexadecimal and make it 3 digits long (with leading zeros if necessary)
        

    else:
        print(f"Error at line {line_number}: Unknown instruction or directive '{instruction}'")
        exit()  
        

binarycode = []

for code in machinecode:
    binary = format(int(code, 16), "016b")
    binarycode.append(binary)

try:
    with open("output.txt", "w") as file:
        for code in machinecode:
            file.write(code + "\n")
except IOError:
    print("Error: Could not write to output.txt")
    exit()

try:
    with open("output_binary.txt", "w") as file:
        for code in binarycode:
            file.write(code + "\n")
except IOError:
    print("Error: Could not write to output_binary.txt")
    exit()



        

              

   
