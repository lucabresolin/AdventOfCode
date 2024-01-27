def get_max_and_multiply(line):
    if line.count(':') != 1:
        print("erreure")
        return -1

    meta, main = line.split(':')

    blue_max = 0
    green_max = 0
    red_max = 0

    main = main.replace(";", ",").strip().split(',')
    for elem in main:
        elem = elem.strip()
        if elem.count(' ') != 1:
            print(elem)
            print(main)
            print("erreur")
        compte, color = elem.split(' ')
        if color == "blue" and int(compte) > blue_max:
            blue_max = int(compte)
        if color == "green" and int(compte) > green_max:
            green_max = int(compte)
        if color == "red" and int(compte) > red_max:
            red_max = int(compte)

    return blue_max * red_max * green_max


with open("input.txt", 'r') as f:
    lignes = f.readlines()
    print(sum([get_max_and_multiply(line) for line in lignes]))
