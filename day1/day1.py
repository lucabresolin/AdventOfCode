# PART 1
def get_number(txt):
    first_number = None
    last_number = None

    for char in txt:
        if char.isnumeric():
            if first_number is None:
                first_number = int(char)
            last_number = int(char)

    return first_number * 10 + last_number


# PART 2
def convert_number(txt: str):
    dicto = {
        "one": "o1ne",
        "two": "t2wo",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for key, value in dicto.items():
        txt = txt.replace(key, value)

    return txt


with open("input.txt", 'r') as f:
    lines = f.readlines()
    rep_1 = sum(get_number(line) for line in lines)
    rep_2 = sum(get_number(convert_number(line)) for line in lines)
    print(f"Reponse 1 : {rep_1}, Reponse 2 : {rep_2}")
