def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char

    return result


print("===== Caesar Cipher Tool =====")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ")

if choice == 'e':
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)

elif choice == 'd':
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")