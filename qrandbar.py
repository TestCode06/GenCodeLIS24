import os
import random
import barcode
from barcode.writer import ImageWriter
import qrcode

def create_directories():
    if not os.path.exists('barcodes_hexadecimal_jpg'):
        os.makedirs('barcodes_hexadecimal_jpg')
    if not os.path.exists('qrcodes_hexadecimal_jpg'):
        os.makedirs('qrcodes_hexadecimal_jpg')

def generate_barcode(data):
    try:
        data_str = str(data)
        CODE128 = barcode.get_barcode_class('code128')
        code128 = CODE128(data_str, writer=ImageWriter(format='JPEG'))
        filename = f'barcodes_hexadecimal_jpg/{data_str}_bar'  # Ensure .jpg extension
        code128.save(filename)
        print(f"Barcode saved as {filename}")
    except barcode.errors.BarcodeError as e:
        print(f"BarcodeError: {e}")
    except Exception as e:
        print(f"Error generating barcode: {e}")

def generate_qrcode(data):
    try:
        if not data:
            raise ValueError("QR code data cannot be empty.")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f'qrcodes_hexadecimal_jpg/{data}_qr.jpeg')  # Changed extension to .jpg
        print(f"QR code saved as qrcodes_hexadecimal_jpg/{data}_qr.jpeg")
    except Exception as e:
        print(f"Error generating QR code: {e}")

def main():
    create_directories()
    for i in range(0x10000, 0x100000):
        hex_str = hex(i)[2:].upper()
        hex_str = hex_str.replace('E', 'U')
        generate_barcode(hex_str)
        generate_qrcode(hex_str)
        print(f"Barcode and QR code for {hex_str} have been generated and saved.")

if __name__ == "__main__":
    main()