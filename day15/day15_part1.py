with open("./day15/input.txt", 'r') as f:
    lines = f.readlines()[0].split(',')

#print(lines)

def hash_code(str):
    code = 0
    for c in str:
        code += ord(c)
        code *= 17
        code %= 256
    
    return code

print(sum([hash_code(tct.strip('\n')) for tct in lines]))
