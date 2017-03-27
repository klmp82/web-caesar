def encrypt(text, rot):
    encrypted = ''
    for c in text:
        encrypted = encrypted + rotate_character(c, rot)
    return encrypted

def alphabet_position(letter):
    if letter.isupper():
        first = ord("A")
    elif letter.islower():
        first = ord("a")

    pos = ord(letter) - first

    return pos

def rotate_character(char, rot):
    if char.isalpha() == False:
        return char
    position = alphabet_position(char)
    rotated_index = position + int(rot)
    if char.isupper():
        new_char = (rotated_index % 26) + 65
    elif char.islower():
        new_char = (rotated_index % 26) + 97

    return chr(new_char)
    
