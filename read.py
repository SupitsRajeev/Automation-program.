def read_file():
    key_dictionary = {}
    with open("laptop.txt", "r") as f:
        list_id = 1 
        for line in f:
            line = line.replace("\n", "")
            key_dictionary.update({list_id: line.split(",")})
            list_id += 1
    return key_dictionary