import string


def print_dic(my_dict):
    if not my_dict:
        return
    all_letters = string.ascii_lowercase
    print("\t", all_letters)
    all_values = ""
    for letter in all_letters:
        all_values += my_dict[letter]
    print("\t", all_values)


def info_func(curr_key, state, encryption, decryption):
    print("Current key: ", curr_key)
    print("state: ", state)
    print("Encryption:")
    print_dic(encryption)
    print("Decryption:")
    print_dic(decryption)
