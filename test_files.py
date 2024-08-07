import pytest
import csv
import zipfile
from pypdf import PdfReader


def test_csv():
    with zipfile.ZipFile('zipped/zipped_files.zip') as zip_file:
        with zip_file.open('csv_file.csv') as csv_file:
            content = csv_file.read().decode('utf-8-sig')
            csvreader = list(csv.reader(content.splitlines()))
            second_row = csvreader[2]

            assert second_row[0] == 'vlada'
            assert second_row[1] == 'shtefan'

def test_pdf():
    with zipfile.ZipFile('zipped/ziiped_files.zip') as zip_file:
        with zip_file.open('Ischenko.pdf') as pdf_file:
            reader = PdfReader('Ischenko.pdf')
            