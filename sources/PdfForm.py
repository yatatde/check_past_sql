from datetime import datetime
from zoneinfo import ZoneInfo
import time
import numpy as np
from fpdf import FPDF, XPos, YPos, table
from sources.control.PdfSettings import SectionDetailesById as sd_d, TableDetailesById as td_d, ColorRGB as crgb_d, TableCellDetailesById as tcd_d
from sources.control.PdfSettings import *
from fpdf.fonts import FontFace
from fpdf.enums import TextEmphasis, VAlign
from sources.FileProcess import FileProcess as fp


def insert_paragraph(pdf, text, **kwargs):
    "Inserts a paragraph"
    pdf.multi_cell(
        w=pdf.epw,
        h=pdf.font_size,
        text=text,
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        **kwargs,
    )


def insert_table(pdf, _tdata=[' '], _cstyle=[[FontFace]], **kwargs):
    "Inserts a table"
    _row_index = 0

    with pdf.table(first_row_as_headings=True, col_widths=pdf.col_widths, line_height=pdf.line_height, text_align=pdf.text_align) as table:
        for data_row in _tdata:
            row = table.row()
            for datum in data_row:
                datum = datum
                #    , v_align=VAlign.M)
                row.cell(datum, style=_cstyle[_row_index][row.cols_count],)
            _row_index += 1
    pdf.ln()  # Line break


def render_toc(pdf, outline):
    # https://github.com/py-pdf/fpdf2/blob/5453422bf560a909229c82e53eb516e44fea1817/test/outline/test_outline.py
    pdf.y += 50
    pdf.set_font("Helvetica", size=16)
    pdf.underline = True
    pdf.x = pdf.epw/2
    pdf.y += int(pdf.h/3)
    insert_paragraph(pdf, "Table of contents:", align="L")
    pdf.underline = False
    pdf.set_font("Times", size=12)
    pdf.set_x = pdf.epw/2

    for section in outline:
        link: str = pdf.add_link(page=section.page_number)
        pdf.set_link(link, page=section.page_number)
        _text = f'{"  " * section.level} {section.name}{section.page_number.__str__()}'
        _dots__count = int((pdf.epw-pdf.l_margin - pdf.r_margin -
                           pdf.get_string_width(_text)) / pdf.get_string_width('.'))
        insert_paragraph(
            pdf, f'{"  " * section.level} {section.name} {"." * _dots__count} {section.page_number}', align="C", link=link, )

# class PDF()


class PDF(FPDF):
    _k = 0.8
    [a4_bmargin, a4_tmargin, a4_rmargin, a4_lmargin] = [
        int(15*2.83*_k), int(15*2.83*_k), int(15*2.83*_k), (15*2.83*_k)]
    margin_y0 = a4_bmargin * 0.85
    a4_footer_h = a4_tmargin 
    (logo_w, logo_h) = (a4_footer_h, a4_footer_h)
    (logo_x, logo_y) = (a4_lmargin, margin_y0)
    header_type = 'h_default'

    def header(self):
        if self.page_no() <= 2:
            return
        self.uid = self.header_type
        # image parameters: name:str path, x,y,w,h,type,lnk,title,alt_text,dims,keep_aspect_ratio
        # Colors of frame, background and text
        self.set_draw_color(crgb_d['ANTIFLASH_WHITE'][0],
                            crgb_d['ANTIFLASH_WHITE'][1], crgb_d['ANTIFLASH_WHITE'][2])
        self.set_fill_color(crgb_d['ANTIFLASH_WHITE'][0],
                            crgb_d['ANTIFLASH_WHITE'][1], crgb_d['ANTIFLASH_WHITE'][2])
        (family, style, size, logo_file) = (sd_d[self.uid][0], sd_d[self.uid][1],
                                            # family, style, size, logo file
                                            sd_d[self.uid][2], sd_d[self.uid][3])
        self.set_y(self.margin_y0)
        self.set_x(self.l_margin + self.logo_w)
        # Calculate width of title and position
        title_w = (self.w - 2 * self.l_margin)
        # Thickness of frame (1 mm)
        self.set_font(family, style, size)
        self.set_line_width(1)
        self.cell(w=title_w, h=self.logo_h, align='C', text=self.title.__str__(), border=True,
                  new_x=XPos.CENTER, new_y=YPos.TMARGIN, center=True, fill=True)
        self.image(logo_file, self.logo_x, self.logo_y, self.logo_w, self.logo_h)
        self.set_y(self.a4_bmargin/2 + 2 * self.margin_y0)

    def doc_title(self, title):
        self.set_margins(self.a4_lmargin, self.a4_tmargin, self.a4_rmargin)
        self.set_title(title=title)
        self.set_section_title_styles(
            level0=set_textstyle_level('l0', self.l_margin),  # type: ignore
            level1=set_textstyle_level('l1', self.l_margin),
            level2=set_textstyle_level('l2', self.l_margin),
            level3=set_textstyle_level('l3', self.l_margin),
            level4=set_textstyle_level('l4', self.l_margin),
            level5=set_textstyle_level('l5', self.l_margin),
        )
        self.add_page()
        self.set_y(self.h/4)
        self.set_font(sd_d['title'][0], sd_d['title']
                      [1], sd_d['title'][2])
        self.set_text_color(
            crgb_d['RUDDY_BROUN'][0], crgb_d['RUDDY_BROUN'][1], crgb_d['RUDDY_BROUN'][2])
        self.set_title(title=title)
        insert_paragraph(self, self.title, align="C")
        self.set_text_color(
            crgb_d['BLACK'][0], crgb_d['BLACK'][1], crgb_d['BLACK'][2])
        # font detailes set : family, style, size
        self.set_font(sd_d['subtitle'][0],
                      sd_d['subtitle'][1], sd_d['subtitle'][2])
        self.set_y(self.h / 2)
        _local_time = time.localtime()
        _local_time_ISO = datetime.isoformat(datetime(*_local_time[:6]))
        insert_paragraph(self, f'generated at {_local_time_ISO}', align="C")

    def footer(self):
        if self.page_no() <= 1:
            self.page_break_trigger
            return
        self.set_font(sd_d['footer'][0], sd_d['footer'][1],
                      sd_d['footer'][2])   # family, style, size
        self.set_y(-self.a4_tmargin * 0.75 -
                   self.a4_footer_h *0.4 - self.margin_y0 *0.55)
        self.set_fill_color(
            crgb_d['BEIGE'][0], crgb_d['BEIGE'][1], crgb_d['BEIGE'][2])
        _pageNum = 'Page ' + str(self.page_no()) + ' of {nb}'
        self.cell(w=self.w - self.r_margin - self.l_margin,
                  h=self.a4_footer_h, fill=True, text=_pageNum, align='C',
                  new_x=XPos.CENTER, new_y=YPos.BMARGIN, center=True)
        self.page_break_trigger


class PdfForm():
    def __init__(self, pdf, unit_name='', unit_id=''):
        self.pdf = pdf
        self.un = unit_name
        self.uid = unit_id

    def get_tab_cells_style(self, _td=['']):
        # tabs_count=[ j-1 for j, line in enumerate(_tdata) if line[0].find("SN") == 0]
        _ds = FontFace(family=sd_d[self.uid][0], emphasis=sd_d[self.uid][1], size_pt=sd_d[self.uid][2],
                       color=self.pdf.text_color, fill_color=None)
        _headings_font_style = FontFace(family='Times', emphasis=TextEmphasis.B, size_pt=9,
                                        color=crgb_d['RUDDY_BROUN'], fill_color=crgb_d['GLITTER'])
        _csn = [[_headings_font_style if (k == 0 or n == 0 or _td[n][0] == 'SN') else _ds for k in range(
            len(_td[0]))] for n in range(len(_td))]
        if self.uid in tcd_d:
            if not len(tcd_d[self.uid]) == 0:
                _tcd_d_keys = list(tcd_d[self.uid].keys())
                _tcd_d_values = list(tcd_d[self.uid].values())
                _tcd_d_idx = [int(key.strip('col')) for key in _tcd_d_keys]
                for n in range(len(_td)):
                    _csn[n][0] = _headings_font_style
                    for k in _tcd_d_idx:
                        for i in range(len(_tcd_d_keys)):
                            for j in range(len(_tcd_d_values[i])):
                                if int(_tcd_d_keys[i].strip('col')) == k:
                                    try:
                                        _cell_datum = _td[n][k].lower().split()
                                        _search_value = _tcd_d_values[i][j]['search'].lower(
                                        )
                                        _cell_datum.index(_search_value)
                                        _csn[n][k] = FontFace(family=sd_d[self.uid][0], emphasis='BI', size_pt=sd_d[self.uid][2],
                                                              color=self.pdf.text_color, fill_color=crgb_d[_tcd_d_values[i][j]['color']])
                                    except ValueError:
                                        # dictionary value not found in cell datum - no problem
                                        pass
        return (_csn)

    def form_table(self):
        _tdata: list = []
        sub_tab_name: str = ''
        self.pdf.col_widths = td_d[self.uid][0]
        self.pdf.line_height = 1.7 * self.pdf.font_size
        self.pdf.text_align = td_d[self.uid][1]
        self.pdf.set_line_width(.0001)
        self.pdf.set_draw_color(crgb_d['COOL_GREY'])
        for line in fp().read_file(fname=self.un, read_mode='r', by_line=True):
            _line = eval(line.__str__())
            if not line.__str__().startswith('"SubTab"'):
                _tdata.append(_line)
            else:
                if len(_tdata) > 0:
                    _cells_style = PdfForm.get_tab_cells_style(
                        self, _td=_tdata)
                    self.pdf.start_section(sub_tab_name, level=1, strict=True)
                    # insert_paragraph(self.pdf, sub_tab_name)
                    insert_table(self.pdf, _tdata=_tdata, _cstyle=_cells_style)
                    _tdata = []
                    sub_tab_name = _line[2]
                else:
                    sub_tab_name = _line[2]
        _cells_style = PdfForm.get_tab_cells_style(self, _td=_tdata)
        if len(sub_tab_name) > 0:
            self.pdf.start_section(sub_tab_name, level=1, strict=True)
            # insert_paragraph(self.pdf, sub_tab_name)
        insert_table(self.pdf, _tdata=_tdata, _cstyle=_cells_style)

    def form_section(self):
        self.pdf.set_line_width(-1)
        # family, style, size
        self.pdf.set_font(sd_d[self.uid][0],
                          sd_d[self.uid][1], sd_d[self.uid][2])
        # Read text file
        self.pdf.ln()
        _sdata: bytes = bytes(fp().read_file(
            fname=self.un, read_mode='rb'))
        insert_paragraph(self.pdf, _sdata.decode('utf-8'))
        self.pdf.ln()  # Line break

    def print_report(self):
        self.pdf.ln(20)  # Line break
        self.pdf.output(self.un)
