alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(text,shift):
    cipher_text=""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text +=char

    print(f"The encrypted message is: {cipher_text}")
        

def decryption(text,shift):
    plain_text=""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text +=char
    print(f"The decrypted message is: {plain_text }")

cond=True

while cond:
    what_to_do=input("Enter 'encrypt' for encryption or 'decrypt' for decryption: ")
    text=input("Enter the message you want to encrypt or decrypt: ")
    shift=int(input("Enter the shift you want: "))
    if what_to_do == "encrypt":
        encryption(text,shift)

    elif what_to_do == "decrypt":
        decryption(text,shift)


    value=input("Do you want to continue? (yes/no): ")
    if value.lower() == "no":
        cond=False
        print("Thank you for using the Caesar Cipher program!")
    elif value.lower() == 'yes':
        cond=True