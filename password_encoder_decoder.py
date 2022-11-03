#Matthew Miles
#password decoder/encoder

#converts digit to decoded digit
def decode_conversion(digit):
    decode_map = {
        '0': '3',
        '1': '4',
        '2': '5',
        '3': '6',
        '4': '7',
        '5': '8',
        '6': '9',
        '7': '0',
        '8': '1',
        '9': '2',
    }
    if digit in decode_map:
        return decode_map[digit]

#parses through string and "adds" 3 to each digit in the string, which is encoding
def encode(string):
    string_list = []
    decoded_string_list = []
    result_string = ""
    #appends each digit to the string list
    for digit in string:
        string_list.append(digit)
    for i in string_list:
        decoded_string_list.append(decode_conversion(i))

    for j in decoded_string_list:
        result_string += j

    return result_string

#main dunder
if __name__ == '__main__':
    running = True
    #print menu prompt
    while running:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        #encodes password
        if option == 1:
            password_to_encode = input("Please enter your password to encode: ")
            encode_password = encode(password_to_encode)
            print("Your password has been encoded and stored! ")

        #decode password
        elif option == 2:
            pass

        #exits the program
        elif option == 3:
            running = False




