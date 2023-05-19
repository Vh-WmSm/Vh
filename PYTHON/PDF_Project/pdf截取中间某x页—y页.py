from PyPDF2 import PdfFileWriter, PdfFileReader
import os

address, name_in, name_out = input('文件地址 输入文件名 输出文件名（输出文件放在输入文件目录下）(格式：c:\\xxx name_in name_out)：').strip().split()  # strip()防止手快在末尾多打一个空格
os.chdir(address)
start_page, end_page = map(int, input('开始页 结束页（数字间空格分开）：').split())

pdf_reader = PdfFileReader("{}.pdf".format(name_in))
pdf_writer = PdfFileWriter()

for i in range(start_page - 1, end_page):
  pdf_writer.addPage(pdf_reader.getPage(i))
  
with open("{}.pdf".format(name_out), "wb") as f_w:
  pdf_writer.write(f_w)
