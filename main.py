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

    def pays(self, bill):
        pass


class PdfReport:
    """PdfReport"""

    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, bill, *flatmates):
        pass

    
def main():
    print("Hello from 2-flatmate-bill!")


if __name__ == "__main__":
    main()
