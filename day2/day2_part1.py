RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def id_ifnot_overflow(line):
    if line.count(':') != 1:
        print("erreure")
        return -1

    meta, main = line.split(':')
    id = int(meta.split(' ')[1])

    main = main.replace(";", ",").strip().split(',')
    for elem in main:
        elem = elem.strip()
        if elem.count(' ') != 1:
            print(elem)
            print(main)
            print("erreur")
        compte, color = elem.split(' ')
        if color == "blue" and int(compte) > BLUE_MAX:
            return 0
        if color == "green" and int(compte) > GREEN_MAX:
            return 0
        if color == "red" and int(compte) > RED_MAX:
            return 0

    return id


with open("input.txt", 'r') as f:
    lignes = f.readlines()
    print(sum([id_ifnot_overflow(line) for line in lignes]))
