from pypdf import PdfReader

reader = PdfReader("tmp/pdf_file1.pdf")

print(reader.pages)

print(reader.pages[1].extract_text())

assert "Alexander" in reader.pages[1]


