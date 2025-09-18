from enum import Enum
import os
from typing import get_args
from fpdf import TextStyle
from typing import Literal as Literal
from sources.control.PdfSettings import *


def get_document_structure(doc_id):
    class structure_sets_enum(Enum):
        # dodumnet ID |
        # document id_SeqNum = (TitleName,TitleLevel, DataSourceNamePrefix, DataSourceType) ##
        er_item1 = ('1. SQL Script', 'l1', '_query.sql', 'file')
        er_item2 = ('2. SQL Explain query plan', 'l1', '', 'none')
        er_item3 = ('2.1. Plain report', 'l2', '_explrep.txt', 'file')
        er_item4 = ('2.2. GRAPH report', 'l2', '_explrep_graph.txt', 'file')
    # explrep_ = ( '', '', '','' ) ##
    try:
        return (structure_sets_enum[doc_id].value)
    except KeyError as e:
        print("get_sections_detailes for " + doc_id)
        print_error(e)


SectionDetailesById = (dict) = {
    'sql': ['Courier', 'I', 8],
    'header': ['Helvetica', 'BI', 12, f'{os.getcwd()}\\sources\\control\\pchelka.png'],
    'h_default': ['Helvetica', 'BI', 12, f'{os.getcwd()}\\sources\\control\\pchelka.png'],
    'h_01': ['Times', 'I', 12, f'{os.getcwd()}\\sources\\control\\flowers.jpg'],
    'title': ['Helvetica', 'B', 33],
    'subtitle': ['Helvetica', 'I', 18],
    'toc_h': ['Helvetica', 'U', 16],
    'toc_c': ['Times', '', 12],
    'text': ['Courier', 'I', 8],
    'q1_txt': ['Courier', 'I', 8],
    'q2_txt': ['Courier', 'I', 8],
    'q3_txt': ['Courier', 'I', 8],
    'q4_txt': ['Courier', 'I', 8],
    'er_txt': ['Courier', 'I', 8],
    'graph': ['Courier', 'I', 8],
    'footer': ['Helvetica', 'I', 12]
}


TableDetailesById = (dict) = {
    'er_txt': ((1, 1, 1, 1, 18), ("JUSTIFY", "JUSTIFY", "CENTER", "CENTER",  "LEFT")),
    'q1_txt': (((1,).__add__((17,)*1)), ((("CENTER",).__add__(("LEFT",)*1)))),
    'q2_txt': (((1,).__add__((3,)*10)), ((("CENTER",).__add__(("LEFT",)*10)))),
    'q3_txt': (((1,).__add__((3,)*11)), ((("CENTER",).__add__(("LEFT",)*11)))),
    'q4_txt': ((1, 2, 2, 2, 2, 5,), ((("CENTER",).__add__(("LEFT",)*5)))),
}
TableCellDetailesById = (dict) = {
    'er_txt':
        {'col2':  [{'search': '2', 'color': 'CORAL'}],
         'col4':  [{'search': 'INDEX', 'color': 'TEA_GREEN'}, {'search': 'SCAN', 'color': 'PLATINUM'}]
         },
    'q2_txt':
        {'col4':  [{'search': '1', 'color': 'CORAL'}],
         'col5':  [{'search': '2', 'color': 'CORAL'}],
         'col6':  [{'search': '3', 'color': 'CORAL'}],
         'col7':  [{'search': '4', 'color': 'CORAL'}],
         'col8':  [{'search': '5', 'color': 'CORAL'}],
         'col9':  [{'search': '6', 'color': 'CORAL'}],
         'col10': [{'search': '7', 'color': 'CORAL'}]
         }
}
# source r/g/b info tacken from https://rgbcolorcode.com/
ColorRGB = (dict) = {
    'LAVENDER_BLASH': [255, 230, 251],
    'TEA_GREEN': [204, 255, 212],
    'BEIGE': [245, 238, 221],
    'RUDDY_BROUN': [166, 93, 57],
    'PALE_BLUE': [153, 255, 238],
    'CORAL': [255, 136, 77],
    'COOL_GREY': [140, 146, 172],
    'PLATINUM': [227, 242, 231],
    'GLITTER': [230, 238, 255],
    'LIGHT_GREY': [212, 214, 202],
    'ANTIFLASH_WHITE': (238, 240, 245),
    'BLACK': [0, 0, 0]
}


def set_textstyle_level(level_id: str, l_margin) -> (TextStyle | None):
    class textstyle_levels_enum(Enum):
        # level id | (....)
        l0 = TextStyle(font_family="Times", font_style='B', font_size_pt=16,
                       color=108, underline=True, t_margin=0, l_margin=l_margin, b_margin=5)
        l1 = TextStyle(font_family="Helvetica", font_style="I", font_size_pt=14,
                       color=88, underline=True, t_margin=0, l_margin=l_margin, b_margin=3,)
        l2 = TextStyle(font_family="Helvetica", font_style="B", font_size_pt=12,
                       color=78, underline=False, t_margin=0, l_margin=l_margin, b_margin=0,)
        l3 = TextStyle(font_family="Helvetica", font_style="B", font_size_pt=12,
                       color=68, underline=False, t_margin=0, l_margin=l_margin, b_margin=0,)
        l4 = TextStyle(font_family="Helvetica", font_style="B", font_size_pt=12,
                       color=58, underline=False, t_margin=10, l_margin=l_margin, b_margin=0,)
        l5 = TextStyle(font_family="Courier", font_style="B", font_size_pt=12,
                       color=48, underline=False, t_margin=10, l_margin=l_margin, b_margin=0,)
        # l0 = TextStyle(font_family="Times",font_style='B',font_size_pt=24,
        #             color=108,underline=True,t_margin=PDF.a4_tmargin,l_margin=PDF.a4_lmargin,b_margin=PDF.a4_bmargin,)
    try:
        return (textstyle_levels_enum[level_id].value)
    except KeyError as e:
        print(f"set_textstyles_level  {level_id}")
        print_error(e)


def print_error(err):
    print(f" Either wrong input parameter provided {err}")
    print(
        f" Or check missing settings for {err} in \n    {os.path.abspath(__file__)}")
    exit()
