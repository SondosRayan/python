import os
import encfile
import enckey
import savekey
import loadkey
import decfile
import info


def check_valid_args(command_line, num):
    n = len(command_line.split())
    if n != num:
        print("the number of arguments does not match!")
        return False
    return True


def start():
    new_command = ""
    current_key = ""
    state = ""
    encryption = {}
    decryption = {}

    while new_command != "done":
        new_command = input("subs>")
        if not new_command or new_command.isspace():
            continue
        command = new_command.split()[0]
        if command == "newkey":
            if check_valid_args(new_command, 2):
                current_key, state, encryption, decryption = enckey.newkey_func(new_command)
        elif command == "save":
            if check_valid_args(new_command, 2):
                state = savekey.save_func(new_command, current_key, encryption, decryption)
        elif command == "load":
            if check_valid_args(new_command, 2):
                file_name = new_command.split()[1]
                if not os.path.isfile(file_name):
                    print("No such key")
                else:
                    current_key, state, encryption, decryption = loadkey.load_func(new_command)
        elif command == "enc":
            if check_valid_args(new_command, 3):
                encfile.enc_func(new_command, encryption)
        elif command == "dec":
            if check_valid_args(new_command, 3):
                decfile.dec_func(new_command, decryption)
        elif command == "info":
            if check_valid_args(new_command, 1):
                info.info_func(current_key, state, encryption, decryption)
        else:
            print("No such command !!!")


if __name__ == '__main__':
    start()

