#Converting Logic

def convert_to_base(number: int = 0, base:int = 10, steps:bool = False) -> int:
    '''Converts input decimal number to input base'''
    hexadecimal = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    new_value = ""
    mod = 0
    div = 0
    while((div != 1) and (div != 0)):
        mod = number % base
        if base == 16 and (mod > 9 and mod < 16):
            actual_value = hexadecimal[str(mod)]
            mod = actual_value
        new_value += str(mod)
        if steps:
            print("{} mod {} = {}".format(number, base, mod))
        div = number // base
        if steps:
            print("{} div {} = {}\n".format(number, base, div))
        number = div
        if div == 0:
            if base != 16:
                return int(new_value[::-1])
            else:
                if new_value[::-1] in hexadecimal:
                    return hexadecimal[new_value[::-1]]
                return new_value[::-1]
        elif div == 1:
            new_value += str(div)
            if base != 16:
                return int(new_value[::-1])
            else:
                if new_value[::-1] in hexadecimal:
                    return hexadecimal[new_value[::-1]]
                return new_value[::-1]
    return new_value[::-1]


def convert_to_decimal(number: (int or str), base:int) -> int:
    '''Converts input number to decimal'''
    num_list = []
    nums = str(number)
    value = 0
    hexadecimal = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F":15}
    for digit in nums:
        num_list.append(digit)
    for digit in range(len(num_list)):
        if num_list[digit] in hexadecimal:
            num_list[digit] = hexadecimal[num_list[digit]]
    n = len(num_list)
    for digit in num_list:
        value += (int(digit) * (base)**(n-1))
        n -= 1
    return value
