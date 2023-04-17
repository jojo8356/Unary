#unary by jojo8356, codingame
def binary_encoding(message):
    lettres = []
    for x in message:
        lettres.append(format(ord(x), '07b'))
    message = "".join(lettres)
    result = []
    current_bit = None
    count = 0
    for bit in message:
        if bit == current_bit:
            count += 1
        else:
            if current_bit is not None:
                result.append({current_bit: count})
            count = 1
            current_bit = bit
    if current_bit is not None:
        result.append({current_bit: count})
    for x in range(len(result)):
        if list(result[x].keys())[0] == "0":
            result[x] = "00 "+list(result[x].values())[0]*"0"
        elif list(result[x].keys())[0] == "1":
            result[x] = "0 "+list(result[x].values())[0]*"0"
    return " ".join(result)
# Exemple d'utilisation
message = input()
encoded_message = binary_encoding(message)
print(encoded_message)
