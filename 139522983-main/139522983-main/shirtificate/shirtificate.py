from fpdf import FPDF
class PDF(FPDF):
    def main(self):
        self.image("Shirtificate.png",10,65,190,190)
        self.set_font("helvetica", "B", 50)
        self.cell(0, 60, "CS50 Shirtificate")
        self.set_font("helvetica", "B", 50)
        self.set_text_color(255,255,255)
        self.text(x=47.5,y=140,txt=f"{name} took CS50")


name = input("What's your name? ")
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
