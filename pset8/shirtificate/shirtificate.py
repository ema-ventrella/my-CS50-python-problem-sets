from fpdf import FPDF
from PIL import Image

text = f"{str(input("Name: ").title().strip())} took CS50"
title = "CS50 Shirtificate"

class PDF(FPDF):
    def header(self):
        # No automatic page break
        self.set_auto_page_break(False)
        # Font
        self.set_font("helvetica", size=50)
        # Calculating width of title and setting cursor position:
        title_w = self.get_string_width(title)
        self.set_x((self.w - title_w) / 2)
        # Title
        self.cell(title_w, 60, title, ln=1, align="C")
        
        
    def add_img(self, width=180):
        # Open the image using PIL
        img = Image.open("shirtificate.png")
        
        # Calculate the position to center the image horizontally
        x = (self.w - width) / 2
        
        # Add the image to the PDF
        self.image(img, x, None, width)

    def add_text(self, text):
        # Font
        self.set_font("helvetica", size=20)
        # Calculate width of title and position cursor
        text_w = self.get_string_width(text)
        # Calculate position of text
        self.set_x((self.w - text_w) / 2)
        # Change color in white
        self.set_text_color(255, 255, 255)
        # Text
        self.cell(text_w, -240, text, align="C")

pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.add_img()
pdf.add_text(text)
pdf.output("shirtificate.pdf")
