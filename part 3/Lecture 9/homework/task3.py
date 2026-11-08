class Printer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def print_page(self, pages):
        print(f"Printing {pages} pages")
class Scanner:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def scan_page(self):
        print("Scanning one page")
class AllInOne(Printer, Scanner):
    def __init__(self, brand, price):
        Printer.__init__(self, brand, price)# need to recall self as well
        Scanner.__init__(self, brand, price)
office = AllInOne("Canon", 8000)
office.print_page(3)
office.scan_page()# the function is called scan_page not scan