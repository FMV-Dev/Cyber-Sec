key = 5

user_key = int(input("Enter the key: "))
if user_key == key:

    message = input("Enter your message: ").lower()
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    
    encrypt_input = input("Do you want to encrypt?")
    if encrypt_input.lower() == "yes": 
        encrypted_text = ""
        for i in range(len(message)):
            index = alphabets.index(message[i])
            index += key
            new_letter = alphabets[index]
            encrypted_text += new_letter
        print(encrypted_text)

    else:
        decrypted_text = ""
        for i in range(len(message)):
            index = alphabets.index(message[i])
            index -= key
            new_letter = alphabets[index]
            decrypted_text += new_letter
        print(decrypted_text)

else:
    print("You have the wrong key")
