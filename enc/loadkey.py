import json


def load_func(command_line):
    file_name = command_line.split()[1]
    file = open(file_name, 'r')
    file_text = file.read().splitlines()
    file.close()

    key_name = file_text[0]
    state = file_text[1]
    enc_key = json.loads(file_text[2])
    dec_key = json.loads(file_text[3])
    print(f"Key {key_name} from file {file_name} loaded")
    return key_name, state, enc_key, dec_key
