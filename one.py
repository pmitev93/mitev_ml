import PyPDF2
import re
from codes_stuff import codes_list
from jaraco import clipboard

class Card:

    def __init__(self, pos):
        pdf_file = open(pos, 'rb')
        self.name = pos
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        date1 = read_pdf.documentInfo["/CreationDate"]
        self.date = date1[2:10]
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        self.page_content = page.extractText()

    def eik_extract(self):
        pattern_eik = re.compile(r'\d{9}')
        eiks_found = pattern_eik.findall(self.page_content)
        return eiks_found

    def code_extract(self):
        for code in codes_list:
            if code in self.page_content:
                return code

    def direction(self):
        ml = 0
        for eik in Card.eik_extract(self):
            if eik == '112106418':
                ml +=1
            else:
                real_eik = eik
        if ml ==1:
            # print("съхранение")
            return real_eik
        elif ml>1:
            # print("обезвреждане")
            return eik



a = Card('win_scan200_yellow.pdf')
#
# print(a.page_content)
# print(a.direction())
# print(type(a.eik_extract()))
# print(a.direction())

# clipboard.copy(a.name)
# clipboard.copy(a.date)


# print(b)
