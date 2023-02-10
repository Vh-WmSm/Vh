from PIL import Image
import pytesseract


img_address = input('截图位置(不填则默认桌面)：')
if img_address == '':
    img_address = 'c:\\users\\vh\\desktop'
img_name = input('文件名(.png不用写)')
judge = input('英文1；中文2：')
img = Image.open(img_address + '\\{}.png'.format(img_name))
if judge == '1':
    text = pytesseract.image_to_string(img)

else:
    text = ''.join(pytesseract.image_to_string(img, lang='chi_sim').split())
print(text)
input()
