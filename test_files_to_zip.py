from zipfile import ZipFile
from os.path import basename
from PyPDF2 import PdfReader
import os

file_direction = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources/zip_file.zip'))


#  Созание архива
with ZipFile('resources/zip_file.zip', 'w') as zip_file:
    for folder_name, sub_folders, file_names in \
            os.walk((os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files'))):
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            zip_file.write(file_path, basename(file_path))


#   Тест для xls
def test_read_xls_from_zip():
    with ZipFile(file_direction) as zip_file:
        text = str(zip_file.read('some_xls.xls'))
        assert text.__contains__('321')


#   Тест для csv
def test_read_csv_from_zip():
    with ZipFile(file_direction) as zip_file:
        text = str(zip_file.read('some_csv.csv'))
        assert text.__contains__('csv')


#   Тест для pdf
def test_read_pdf_from_zip():
    with ZipFile(file_direction) as zip_file:
        zip_file.extract('some_pdf.pdf')
        text = PdfReader('some_pdf.pdf').pages[0].extract_text()
        assert text.__contains__('Dumm y PDF file')
