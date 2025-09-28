# # split_hex.py
# with open("../sw/code.hex","r") as f, open("../sw/code_fixed.hex","w") as out:
#     for line in f:
#         if line.startswith("@"):
#             out.write(line)  # keep address marker
#             continue
#         line = line.strip()
#         for i in range(0, len(line), 8):
#             out.write(line[i:i+8] + "\n")

# convert_riscv_hex.py
# Usage: python3 convert_riscv_hex.py hello.hex hello_fixed.hex

import sys

if len(sys.argv) != 3:
    print("Usage: python3 split_hex.py <input_hex> <output_hex>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        line = line.strip()
        if line.startswith("@") or line == "":
            f_out.write(line + "\n")
            continue
        # split line into 8-hex-char chunks (32-bit instruction)
        for i in range(0, len(line), 8):
            instr = line[i:i+8]
            if len(instr) != 8:
                continue
            # swap bytes for little-endian
            swapped = instr[6:8] + instr[4:6] + instr[2:4] + instr[0:2]
            f_out.write(swapped + "\n")
