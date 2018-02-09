import pytesseract
from PIL import Image,ImageEnhance

def initTable(threshold=50):
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)

	return table



im = Image.open('d:\\1.jpg')
im = im.convert('L')
print(im.histogram())

binaryImage = im.point(initTable(), '1')
binaryImage.show()
print(pytesseract.image_to_string(binaryImage, config='-psm 7'))
# text = pytesseract.image_to_string(im)
# print(text)