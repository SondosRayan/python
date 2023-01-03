def dec_func(command_line, decryption):
    dec_file_name = command_line.split()[1]
    clear_file_name = command_line.split()[2]

    dec_file = open(dec_file_name, 'r')
    clear_file = open(clear_file_name, 'w')

    dec_text = dec_file.read()
    for letter in dec_text:
        clear_file.write(decryption[letter])
    clear_file.close()
    dec_file.close()

    print(f"File {dec_file_name} was decrypted into {clear_file_name}")
