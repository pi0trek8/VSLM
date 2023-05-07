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

def calculate_broadcast(net_address, diffrence_broadcast):
    result = [int(oct) for oct in net_address.split(".")]
    diffrences = [int(oct) for oct in diffrence_broadcast.split(".")]

    for i in range(4):
        result[i] += diffrences[i]
    
    broadcast = ''
    for i in range(4):
        broadcast += str(result[i])
        if(i != 3):
            broadcast += "."
        
    return broadcast


def calculate_first_address(net_address):
    octs = [int(oct) for oct in net_address.split(".")]
    if(octs[3] < 255):
        octs[3] += 1
    else:
        octs[3] = 0
        octs[2] += 1
    
    first_add = ''
    i = 0
    for oct in octs:
        first_add += str(oct)
        if(i != 3):
            first_add += "."
        i += 1

    return first_add



def calculate_last_address(broadcast):
    octs = [int(oct) for oct in broadcast.split(".")]
    if(octs[3] > 0):
        octs[3] -= 1
    else:
        octs[3] = 255
        octs[2] -= 1
    
    add = ''
    i = 0
    for oct in octs:
        add += str(oct)
        if(i != 3):
            add += "."
        i += 1

    return add

num_device = int(sys.argv[1])
net_address = sys.argv[2]
print("Potrzebne urządzenia: " + sys.argv[1])
mask = find_mask(num_device)
print("Urzadzenia w masce: " + str(2**(32-mask) - 2))
print("Maska: " + str(mask))
mask_decimal = calculate_mask_decimal(mask)
print("Maska dziesietnie: " + mask_decimal)

diff_br = diffrence_broadcast(mask_decimal)
brodcast = calculate_broadcast(net_address, diffrence_broadcast=diff_br)


print("Broadcast: " + brodcast)

print("pierwszy adres: " + calculate_first_address(net_address))

print("ostatni adres: " + calculate_last_address(brodcast))
