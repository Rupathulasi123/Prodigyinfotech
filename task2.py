from PIL import Image
import numpy as np


def encrypt_image(image_path, key):

    image = Image.open(image_path)
    image_array = np.array(image)


    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

    return encrypted_image


def decrypt_image(image_path, key):

    image = Image.open(image_path)
    image_array = np.array(image)


    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))

    return decrypted_image


def main():
    while True:
        print("\nImage Encryption Tool")
        print("1. Encrypt an Image")
        print("2. Decrypt an Image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypted_image = encrypt_image(image_path, key)
            encrypted_image.save("encrypted_image.png")
            print("Encrypted image saved as 'encrypted_image.png'")

        elif choice == '2':
            image_path = input("Enter the path to the image to decrypt: ")
            key = int(input("Enter the decryption key (an integer): "))
            decrypted_image = decrypt_image(image_path, key)
            decrypted_image.save("decrypted_image.png")
            print("Decrypted image saved as 'decrypted_image.png'")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
