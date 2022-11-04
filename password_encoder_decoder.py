#Matthew Miles
#password decoder/encoder


# new change to the code
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

# function for menu option 2:
# decodes each individual digit and adds to res string, returns res
def decode(password):
    res = ''
    for char in password:
        res += str((int(char) + 7) % 10)
    return res

#main dunder
if __name__ == '__main__':

    running = True

    # when a password is encoded, it is stored into the below variable for use in option 2
    encode_password = ''

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
            decoded_password = decode(encode_password)
            print(f'The encoded password is {encode_password}, and the original password is {decoded_password}.')

        #exits the program
        elif option == 3:
            running = False




