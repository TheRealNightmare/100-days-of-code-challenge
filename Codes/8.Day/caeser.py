def encrypt(text,shift):
    enc =  ""
    for x in text:
        postion = word.index(x)
        new = postion+shift
        new_letter = word[new]
        enc += new_letter
    print(f"Encoded text: {enc}")


def decrypt(text,shift):
    dec = ""
    for i in text:
        position = word.index(i)
        new = position-shift
        newletter = word[new]
        dec += newletter
    print(f"Decrypted text: {dec}")




word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

enordc = input("Type encode/decode: ").lower()
text = input("message: ").lower()
shift = int(input("enter shift value: "))

if enordc == 'encode':
    encrypt(text,shift)
elif enordc == 'decode':
    decrypt(text,shift)
