import json


def save_func(command_line, key_name, encryption, decryption):
    file_name = command_line.split()[1]
    file = open(file_name, 'w')

    file.write(key_name)
    file.write("\n")

    state = f"saved in {file_name}"
    file.write(state)
    file.write("\n")

    file.write(json.dumps(encryption))
    file.write("\n")

    file.write(json.dumps(decryption))

    file.close()
    print(f"Enc/Dec keys saved in {file_name} file")
    return state
