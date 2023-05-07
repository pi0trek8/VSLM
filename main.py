import sys

def find_mask(num_device):
    for i in range(30, 10, -1):
        if (2**(32-i)-2) > num_device:
            break
    return i 
    

def calculate_mask_decimal(mask: int):
    result = '';
    rest = mask % 8
    num = mask // 8
    for i in range(num):
        result += "255."
    
    pow = 7
    oct = 0
    for i in range(rest):
        oct += 2**pow
        pow -=1
    result += str(oct)

    num_oct = len(result.split("."))
    if num_oct < 4:
        for num_oct in range(4 - num_oct):
            result += ".0"

    return result

def diffrence_broadcast(mask):
    octs = mask.split(".")
    result = ''
    for i in range(4):
        num = int(octs[i])
        if num < 255: 
            result += str(255 - num)
        else:
            result += "0"
        if i != 3:
            result += "."
    return result


num_device = int(sys.argv[1])
print("Urzadzenia: " + sys.argv[1])
mask = find_mask(num_device)
print("max urzadznia: " + str(2**(32-mask) - 2))
print("Maska: " + str(mask))
mask_decimal = calculate_mask_decimal(mask)
print("Maska dziesietnieL " + mask_decimal)
print("Broadcast do dodania: " + diffrence_broadcast(mask_decimal))