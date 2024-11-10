from fast_plate_ocr import ONNXPlateRecognizer

m = ONNXPlateRecognizer('european-plates-mobile-vit-v2-model')
print(m.run(r'Transit\Transit_1_plate.JPG'))
print(m.run(r'Transit\Transit_2_plate.jpg'))
print(m.run(r'Transit\Transit_3_plate.jpg'))
print(m.run(r'Transit\Transit_4_plate.jpg'))
print(m.run(r'Transit\Transit_5_plate.jpg'))
print(m.run(r'Transit\Transit_6_plate.jpg'))