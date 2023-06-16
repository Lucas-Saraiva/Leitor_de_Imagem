import cv2
import pytesseract


arq = input(str('Arquivo a converter: '))

img = cv2.imread(arq)

caminho = r"C:\Users\lucas\AppData\Local\Programs\Tesseract-OCR"

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

str_img = pytesseract.image_to_string(img)

print(str_img)
