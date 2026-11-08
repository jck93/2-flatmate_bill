from fpdf import FPDF


def main():
    john = Flatmate("John", 20)
    mary = Flatmate("Mary", 25)
    dean = Flatmate("Dean", 10)
    bill = Bill(120, "Nov '26")
    pdf_report = PDFReport("bill.pdf")
    pdf_report.generate(bill, john, mary, dean)


class Bill:
    """Bill"""

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """Flatmate"""

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, *flatmates):
        weight = self.days_in_house / sum(f.days_in_house for f in flatmates)
        return weight * bill.amount
        

class PDFReport:
    """PdfReport"""

    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, bill, *flatmates):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.set_font(family="Times", size=24, style="B")
        pdf.add_page()
        pdf.image("house.png", w=100, h=100)
        pdf.cell(w=0, h=40, txt="Flatmates Bill", border=0, align="C", ln=1)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=100, h=40, txt="Period: ", border=0, align="C")
        pdf.cell(w=100, h=40, txt=bill.period, border=0, align="C", ln=1)
        pdf.set_font(family="Times", size=16)
        for f in flatmates:
            pdf.cell(w=100, h=40, txt=f.name, border=0, align="C")
            pdf.cell(w=100, h=40, txt=f"{f.pays(bill, *flatmates):.2f}", border=0, align="C", ln=1)
        pdf.output(self.filename)

    
if __name__ == "__main__":
    main()

