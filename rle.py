def run_length_encoding(input_string):
    if not input_string:
        return ""

    encoded_string = ""
    count = 1

    for i in range(1, len(input_string)):
        print(i, input_string[i], len(input_string))
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += input_string[i - 1] + str(count)
            count = 1


    encoded_string += input_string[-1] + str(count)

    return encoded_string


with open('input.txt', 'r') as file:
    input_string = file.read()

    encoded_result = run_length_encoding(input_string)

    with open('output.txt', 'w') as output:
        output.write(encoded_result)
    print(encoded_result)



