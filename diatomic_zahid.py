frequent_words = ['Th', 'is', 'a ', 'to', 'of', 'in', 'ed', 'oo', 'el', 'li']
replace_chars = ['@', '$', '%', '^', '&', '*', '_', '+', ';', '|']


def diatomic(input_string):
    result = ''
    length = len(input_string)
    idx = 0
    while idx < length:
   
        single_character = input_string[idx]
        double_character = single_character
        if idx < length-1:
            double_character += input_string[idx+1]

        if single_character in frequent_words:
   
            found_idx = frequent_words.index(single_character)
            result += replace_chars[found_idx]

        elif double_character in frequent_words:
    
            found_idx = frequent_words.index(double_character)
            result += replace_chars[found_idx]
            idx = idx+1

        else:
          
            result+=single_character
        idx+=1
    return result


with open('input.txt', 'r') as file:
    input_string = file.read()

    encoded_result = diatomic(input_string)

    with open('output.txt', 'w') as output:
        output.write(encoded_result)
    print(encoded_result)

