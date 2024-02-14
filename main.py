alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
    cipher_Text = ''
    shift = shift % 26
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_Position = position + shift
            cipher_Text += alphabet[new_Position]
        else:
            cipher_Text += char
    print(f'{direction}d text: {cipher_Text}')

direction = input("Type 'encode' to encrypt or 'decode' to decrypt and 'exit' to stop \n ")

while direction != 'exit':
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    match direction:
        case 'encode':
            caesar(text, shift, direction)
        case 'decode':
            caesar(text, shift, direction)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")



