import string
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if shift>len(alphabet):
     shift=shift%len(alphabet)
restart=True
while restart==True:
    def caeser(text,shift,direction):
        cipher_text = ""
        for i in text:
            if i.isspace() or i.isdigit() or i in string.punctuation:
                cipher_text +=str(i)
            else:
                index=alphabet.index(i)
                if direction=="encode":
                    cipher_text +=alphabet[index+shift]
                elif direction=="decode":
                    cipher_text +=alphabet[index-shift]
        print(cipher_text)
    caeser(text,shift,direction)
    a=input("If you want to restart the cipher program then enter 'Yes' otherwise enter 'No' ")
    if a=="Yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        restart=True
    else:
        print("Good Bye")
        restart=False
