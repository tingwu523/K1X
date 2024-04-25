import pypdf

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf_object = None

    def read_pdf(self):
        self.pdf_object = pypdf.PdfReader(self.file_path)

    def extract_line_item_sum(self):
        total_sum = 0
        for page in self.pdf_object.pages:
            text = page.extract_text()
            lines = text.split('\n')[10:]
            for i in range(len(lines)):
                if i == 0:
                    number = int(lines[i].split()[-1])
                    total_sum += number
                else:
                    number = int(lines[i])
                    total_sum += number
        return total_sum

pdf_reader = PDFReader('path/of/the/pdf/file')
pdf_reader.read_pdf()
total = pdf_reader.extract_line_item_sum()
print("Total sum of line items:", total)
