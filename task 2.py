from PIL import Image
import numpy as np

# Encryption function: Shift the pixel values by a secret key
def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        img_array = np.array(img)

        # Encrypt by adding the key to the pixel values and taking modulus 256 to prevent overflow
        encrypted_array = (img_array + key) % 256

        # Save the encrypted image
        encrypted_img = Image.fromarray(np.uint8(encrypted_array))
        encrypted_img.save("encrypted_image.png")
        print("Image encrypted and saved as 'encrypted_image.png'")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

# Decryption function: Reverse the shift by subtracting the secret key
def decrypt_image(encrypted_image_path, key):
    try:
        encrypted_img = Image.open(encrypted_image_path)
        encrypted_array = np.array(encrypted_img)

        # Decrypt by subtracting the key from pixel values and handling negative values using modulus
        decrypted_array = (encrypted_array - key) % 256

        # Save the decrypted image
        decrypted_img = Image.fromarray(np.uint8(decrypted_array))
        decrypted_img.save("decrypted_image.png")
        print("Image decrypted and saved as 'decrypted_image.png'")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

# Menu function to let the user choose what they want to do
def main():
    while True:
        print("\nChoose an option:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Encrypt image
            image_path = input("Enter the path to the image you want to encrypt: ")
            try:
                key = int(input("Enter the encryption key (a number): "))
                encrypt_image(image_path, key)
            except ValueError:
                print("Invalid key. Please enter a valid number.")
        
        elif choice == '2':
            # Decrypt image
            image_path = input("Enter the path to the encrypted image: ")
            try:
                key = int(input("Enter the decryption key (the same key used for encryption): "))
                decrypt_image(image_path, key)
            except ValueError:
                print("Invalid key. Please enter a valid number.")
        
        elif choice == '3':
            # Quit the program
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
1