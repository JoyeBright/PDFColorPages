# pdfcolorpages

A small tool that checks how many pages in a PDF document contain color.  
Useful when print companies ask how many color pages your document has.

## Installation

Install the package from the project folder:

```bash
pip install .
```

## Usage

Run the command on a PDF file:

```bash
pdfcolorpages your_document.pdf
```

## Example Output

Total pages: 152 <br>
Color pages: 37<br>
Color page numbers: [3, 4, 10, 11, 35, 36, ...]<br>

## Python Usage

You can also use the function directly in Python:

```python
from pdfcolorpages import count_color_pages

total, color_pages = count_color_pages("your_document.pdf")
print(total)
print(color_pages)
