with open("./day15/input.txt", 'r') as f:
    lines = f.readlines()[0].split(',')

#print(lines)

def hash_code(str):
    code = 0
    for c in str:
        code += ord(c)
        code *= 17
        code %= 256
    
    return code

boxes = {}

def append_label_or_correct(box_number, current_label, new_length):
    if box_number not in boxes:
        boxes[box_number] = [[current_label, new_length]]
    
    else:
        idx = 0
        was_here = False

        for lab,_ in boxes[box_number]:
            if current_label == lab:
                boxes[box_number][idx] = [current_label, new_length]
                was_here = True
            idx += 1
        
        

        if not was_here:
            boxes[box_number].append([current_label, new_length])

def remove_label_or_none(box_number, current_label):
    if box_number in boxes:
        idx = 0
        idx_alr = -1
        for lab,_ in boxes[box_number]:
            if current_label == lab:
                idx_alr = idx
            idx += 1
        
        if idx_alr != -1:
            new_arrangement = boxes[box_number][:idx_alr] + boxes[box_number][idx_alr+1:]
            boxes[box_number] = new_arrangement


def action(prompt):
    if '=' in prompt:
        label, length = prompt.split('=')
        box_number = hash_code(label)
        append_label_or_correct(box_number, label, length)

    if '-' in prompt:
        label = prompt.strip('-')
        box_number = hash_code(label)
        remove_label_or_none(box_number, label)


for instruc in lines:
    action(instruc.strip('\n'))

print(boxes)
som = 0
for idx_box, box in boxes.items():
    for idx_content, content in enumerate(box):
        print(content)
        som += (idx_box+1) * (idx_content+1) * (int(content[1]))
    print()
print(som)
