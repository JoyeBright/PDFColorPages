import sys
from .detector import count_color_pages

def main():
    if len(sys.argv)!=2:
        print("Usage: pdfcolorpages file.pdf")
        return
    total,colors=count_color_pages(sys.argv[1])
    print(f"Total pages: {total}")
    print(f"Color pages: {len(colors)}")
    print(f"Color page numbers: {colors}")
