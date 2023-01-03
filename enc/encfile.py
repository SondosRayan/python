def enc_func(command_line, encryption):
    clear_file_name = command_line.split()[1]
    enc_file_name = command_line.split()[2]

    clear_file = open(clear_file_name, 'r')
    enc_file = open(enc_file_name, 'w')

    clear_text = clear_file.read()
    for letter in clear_text:
        enc_file.write(encryption[letter])
    clear_file.close()
    enc_file.close()

    print(f"File {clear_file_name} was encrypted into {enc_file_name}")
