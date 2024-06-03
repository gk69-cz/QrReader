import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
import sys
import binascii

def scan_qr_code(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None, "Image not found or invalid image format"
    
    decoded_objects = decode(img, symbols=[ZBarSymbol.QRCODE])
    
    if not decoded_objects:
        return None, "No QR code found"
    
    qr_data = decoded_objects[0].data
    try:
        qr_data_decoded = qr_data.decode('utf-8')
    except UnicodeDecodeError:
        qr_data_decoded = "Unable to decode QR data as utf-8"
    
    return qr_data, qr_data_decoded

def ascii_to_hex(ascii_str):
    return binascii.hexlify(ascii_str.encode()).decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scan_qr.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        raw_data, decoded_data = scan_qr_code(image_path)
        
        if raw_data is None:
            print(decoded_data)
        else:
            if isinstance(decoded_data, str):
                hex_data = ascii_to_hex(decoded_data)
                print(hex_data)
            else:
                print("Unable to convert data to hex")
