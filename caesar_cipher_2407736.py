"""Name: Diwash Adhikari
 University Id: 2407736"""
def welcome():
    """
    Print a welcome message for the Caesar Cipher program.
    """
    print('''Welcome to the Caesar Cipher
This program encrypts and decrypts text with the Caesar Cipher.''')
def encrypt(messege,shift_num):
    """
    Encrypts  message using the Caesar Cipher algorithm.
    Parameters:
    - message (str): The message to be encrypted.
    - shift_num (int): The number of positions each character should be shifted.
    Returns:
    str: The encrypted message.
    """
    encrypted_messege=""
    for e in messege:
        char_code = ord(e)
        shifted_code = char_code + shift_num
        if e.isalpha():
            if shifted_code>90:
                encrypted = chr((shifted_code-65) % 26 + 65)
                encrypted_messege += encrypted
            else:
                encrypted = chr(shifted_code)
                encrypted_messege += encrypted
        else:
            if e==" ":
                encrypted_messege+=" "
    return encrypted_messege
def decrypt(message, shift_num):
    """
    Decrypts  message using the Caesar Cipher algorithm.
    Parameters:
    - message (str): The message to be decrypted.
    - shift_num (int): The number of positions each character should be shifted back.
    Returns:
    str: The decrypted message.
    """
    decrypted_message = ""
    for x in message:
        char_code = ord(x)
        shifted_code = char_code - shift_num
        if x.isalpha():
            if shifted_code < 65:
                decrypted = chr((shifted_code - 65) % 26 + 65)
                decrypted_message += decrypted
            else:
                decrypted = chr(shifted_code)
                decrypted_message += decrypted
        else:
            if x == " ":
                decrypted_message += " "
    return decrypted_message
def enter_message():
    """Prompts the user to choose between encryption or decryption mode and validates the input.

   Returns:
       str: The valid mode chosen by the user ('e' for encryption, 'd' for decryption).
   """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in {'e', 'd'}:
            break
        else:
            print("Invalid Mode")
    return mode

def message_or_file():
    """
    Get user input for encryption/decryption mode and source (console or file).
    Returns:
    tuple: A tuple containing the mode ('e' or 'd'), message (str), and filename (str).
    """
    mode=enter_message()
    while True:
        source = input(
            "Would you like to read from a file (f) or the console (c)? ").lower()
        if source == 'c':
            while True:
                message = input("What message would you like to process: ").upper()
                if message == "":
                    print("Please enter a letter, word or a sentence.")
                else:
                    break
            filename = None
            break
        elif source == 'f':
            while True:
                filename = input("Enter a filename: ")
                if is_file(filename):
                    break
                else:
                    print("Invalid Filename")
            message = None
            break
        else:
            print("Invalid Input")
    return mode, message, filename
def shift_key():
    """
    Get a valid shift value from the user, ensuring it is between 0 and 25.
    Returns:
    int: The valid shift value.
    """
    while True:
        try:
            shift = int(input("What is the shift number: "))
            if shift >= 0 and shift <= 25:
                break
            else:
                print("Shift should be between 0-25.")
        except ValueError:
            print("Invalid Shift")
    return shift
def is_file(filename):
    """
    Check if a file with the given filename exists.
    Parameters:
    - filename (str): The name of the file to check.
    Returns:
    bool: True if the file exists, False otherwise.
    """
    try:
        with open(filename, 'r',encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False
def process_file(filename, mode):
    """
    Process a file for encryption or decryption using the Caesar Cipher.
    Parameters:
    - filename (str): The name of the file to be processed.
    - mode (str): The mode, 'e' for encryption or 'd' for decryption.
    Returns:
    list: A list of processed messages.
    """
    result = ''
    shift = shift_key()
    with open(filename, 'r',encoding="utf-8") as file:
        for line in file:
            uppered=line.upper()
            result += encrypt(uppered.strip(), shift) if mode == 'e' else decrypt(uppered.strip(), shift)
            result += '\n'
    return result
def write_messages(messages):
    """
    Append a list of messages to a file named 'results.txt' if the source is 'f'.
    Parameters:
    - messages (list): A list of messages to be appended to the file.
    - source (str): The source, 'c' for console or 'f' for file.
    """
    with open('results.txt', 'a',encoding="utf-8") as file:
        file.write(''.join(messages) + '\n')
def main():
    """
    The main function to run the Caesar Cipher program.
    """
    welcome()
    out = True
    while out:
        mode, message, filename = message_or_file()
        if filename:
            messages = process_file(filename, mode)
            print(messages, end='')
        else:
            messages = encrypt(message, shift_key()).upper() if mode == 'e' else decrypt(message, shift_key()).upper()
            print(messages, end='\n')

        write_messages(messages)
        while True:
            re_run = input(
                "Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if re_run not in ('y', 'n'):
                print('Invalid Input')
            elif re_run == 'y':
                break
            else:
                print("Thanks for using the program, goodbye!")
                out = False
                break

main()
