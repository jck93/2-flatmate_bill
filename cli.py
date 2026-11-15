from main import Bill, Flatmate, PDFReport


def main():
    print()
    amount = float(input("Bill amount >>> "))
    period = input("Bill period >>> ")
    bill = Bill(amount, period)
    flatmates = []
    while True:
        name = input("Flatmate name ('q' to quit) >>> ")
        if name == "q":
            break
        genitive = name + ("'" if name[-1] == "s" else "'s")
        days_in_house = int(input(f"{genitive} days in house >>> "))
        flatmates.append(Flatmate(name, days_in_house))
    pdf_report = PDFReport("bill.pdf")
    pdf_report.generate(bill, *flatmates)
    print("pdf successfully generated")
    print()
    

if __name__ == "__main__":
    main()

