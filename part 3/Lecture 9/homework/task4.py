class Printer:
    def __init__(self, brand):
        self.brand=brand
        self.pages_printed=0
    def print_document(self,pages):
        self.pages_printed=self.pages_printed+pages
        print(f"Printing {pages} pages")
class Scanner:
    def __init__(self,resolution):
        self.resolution=resolution
        self.scans_done=0
    def scan_page(self):
        self.scans_done=self.scans_done+1
        print("Scanned one document")
class AllInOne(Printer,Scanner):
    def __init__(self,brand,resolution):
        Printer.__init__(self,brand)
        Scanner.__init__(self,resolution)
    def report(self):
        print(f"{self.brand} printed {self.pages_printed} pages in total")
        print(f"{self.scans_done} scans done at {self.resolution} dpi")
brand=input()
resolution=int(input())
pages=int(input())
pages1=int(input())
scans=int(input())
Scan=AllInOne(brand,resolution)
Scan.print_document(pages)
Scan.print_document(pages1)
for a in range(scans):
    Scan.scan_page()
Scan.report()