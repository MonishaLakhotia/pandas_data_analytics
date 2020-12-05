import pdfplumber
from py_linq import Enumerable
from pandas_data_analytics.text_parser.parser import Parser


def from_pdf(pdf_loc, settings):
    parser = Parser(parser_settings)
    with pdfplumber.open(pdf_loc) as pdf:
        all_txt = Enumerable(pdf.pages).aggregate(
            lambda acc, page: acc+page.extract_text(), "")
        result = parser.parse(all_txt)
        return result


def from_txt(txt, settings):
    parser = Parser(parser_settings)
    result = parser.parse(txt)
    return result
