def lzw_encode(input_string):
    dictionary = {chr(i): i for i in range(256)}  
    next_code = 256  
    result = []  
    current_sequence = ""  

    for char in input_string:
        current_sequence += char
        if current_sequence not in dictionary:
       
            dictionary[current_sequence] = next_code
            next_code += 1

            result.append(dictionary[current_sequence[:-1]])
            current_sequence = char


    result.append(dictionary[current_sequence])

    return result


with open('input.txt', 'r') as file:
    input_string = file.read()

    encoded_result = str(lzw_encode(input_string))

    with open('output.txt', 'w') as output:
        output.write(encoded_result)
    print(encoded_result)

