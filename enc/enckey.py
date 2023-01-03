import random


def check_valid_newkey(command_line):
    num = len(command_line.split())
    if num != 2:
        print("the number of arguments does not match!")
        return False
    return True


def make_key():
    az_list = [chr(i) for i in range(97, 97+26)]
    shuffled = az_list.copy()
    random.shuffle(shuffled)
    key_dict = {az_list[i]: shuffled[i] for i in range(len(az_list))}
    return key_dict


def make_dec(enc_key):
    reversed_key_val = {enc_key[item]: item for item in enc_key}
    return reversed_key_val


def newkey_func(command_line):
    key_name = command_line.split()[1]
    enc_key = make_key()
    dec_key = make_dec(enc_key)
    print(f"A new key called {key_name} was created")
    return key_name, "not saved", enc_key, dec_key
