def decrypt(cipher):
    decrypted_message = ""
    i = 0
    while i < len(cipher):
        if cipher[i] == ".":
            i += 1
        elif cipher[i:i+2] == "..":
            decrypted_message = decrypted_message[:-1]
            i += 2
        else:
            decrypted_message += cipher[i]
            i += 1
    return decrypted_message

if __name__ == "__main__":
    cipher = input()
    decrypted_message = decrypt(cipher)
    print(decrypted_message)
