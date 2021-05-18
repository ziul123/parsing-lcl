import sys

pre = """#------------------------------------------------------------
#- Deeds (Digital Electronics Education and Design Suite)
#- Rom Contents Saved on (4/18/2021, 12:36:24 AM)
#-      by Deeds (Digital Circuit Simulator)(Deeds-DcS)
#-      Ver. 2.40.330 (Jan 07, 2021)
#- Copyright (c) 2002-2020 University of Genoa, Italy
#-      Web Site:  https://www.digitalelectronicsdeeds.com
#------------------------------------------------------------
#R ROM4Kx16, id 00BE
#- Deeds Rom Source Format (*.drs)

#A 0000h
#H

"""



def imm(num):
    if num < 0:
        result = hex((1 << 16) + num)[2:]
    else:
        result = f"{num:04x}"
    return result



def parse(line):
    ops = {"addi": 0, "subi": 1, "andi":2, "ori":3, "xori":4, "beq":5, "bleu":6, "bles":7}
    #if '\n' in line:
    #    line = line[:-1]
    aux1, aux2 = line.split()
    sep = aux2.split(',')
    msh = imm(int(sep[-1]))
    op = ops[aux1]
    if len(sep) == 3:
        rd = 0
        ra = int(sep[0][1:])
        rb = int(sep[1][1:])
    else:
        rd = int(sep[0][1:])
        ra = int(sep[1][1:])
        rb = int(sep[2][1:])
    lsh = f"{rd:x}" + f"{ra:x}" + f"{rb:x}" + f"{op:x}"
    return msh, lsh
        


file = sys.argv[-1]
with open(file, 'r') as f, open("MSH.drs", 'w') as o1, open("LSH.drs", 'w') as o2:
    msh = ""
    lsh = ""
    for line in f:
        aux1, aux2 = parse(line)
        msh += aux1 + '\n'
        lsh += aux2 + '\n'
    o1.write(pre)
    o2.write(pre)
    o1.write(msh)
    o2.write(lsh)
