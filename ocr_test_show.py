import cv2
import numpy as np
from fast_plate_ocr import ONNXPlateRecognizer

def process_image(image_path, recognizer):
    # Run OCR
    result = recognizer.run(image_path)

    # Read the image using OpenCV
    image = cv2.imread(image_path)
    height, width, channels = image.shape

    # Define padding size
    padding_height = 50  # Adjust this value as needed

    # Create a new image with padding
    padded_image = np.zeros((height + padding_height, width, channels), dtype=np.uint8)
    padded_image[:height, :width] = image

    # Define font, scale, color, and thickness
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    color = (255, 0, 255)  # Red color in BGR
    thickness = 1

    # Position the text in the padded area
    text_x = 10
    text_y = height + padding_height - 10  # 10 pixels from the bottom of the padding

    # Put the text on the padded image
    cv2.putText(padded_image, result[0], (text_x, text_y), font, font_scale, color, thickness)

    # Save the modified image
    output_path = image_path.replace('.jpg', '_with_text.bmp')
    cv2.imwrite(output_path, padded_image)

    # Show the image
    cv2.imshow('Image with OCR', padded_image)
    cv2.waitKey(100)
    cv2.destroyAllWindows()

# Initialize the recognizer
m = ONNXPlateRecognizer('european-plates-mobile-vit-v2-model')

# Process each image
process_image(r'Transit\Transit_1_plate.jpg', m)
process_image(r'Transit\Transit_2_plate.jpg', m)
process_image(r'Transit\Transit_3_plate.jpg', m)
process_image(r'Transit\Transit_4_plate.jpg', m)
process_image(r'Transit\Transit_5_plate.jpg', m)
process_image(r'Transit\Transit_6_plate.jpg', m)