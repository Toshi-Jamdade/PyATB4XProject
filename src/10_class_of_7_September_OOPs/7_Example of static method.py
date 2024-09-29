class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class TC1:
    def runTC(self):
        ExcelReader.readExcelFile()

tc1 = TC1()
tc1.runTC()         # Reading from Excel
