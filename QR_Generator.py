import qrcode
import os

def create_qr_code(url, output_dir):
    """
    Generates a QR code for a given URL and saves it as an image file.
    
    Args:
        url (str): The URL to encode in the QR code.
        output_dir (str): The directory to save the QR code image.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,  # Size of each box in the QR grid
        border=4,  # Thickness of the border
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code
    filename = os.path.join(output_dir, "qrcode.png")
    img.save(filename)

    print(f"QR Code generated and saved at: {filename}")

def main():
    print("QR Code Generator")
    url = input("Enter the URL to generate a QR code: ").strip()
    if not url.startswith(("http://", "https://")):
        print("Invalid URL. Make sure it starts with 'http://' or 'https://'.")
        return

    output_dir = "generated_qrcodes"
    create_qr_code(url, output_dir)

if __name__ == "__main__":
    main()
