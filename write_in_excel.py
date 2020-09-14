import xlsxwriter
class Excel_report:
    #initializing the workbook and worksheet
    def __init__(self,file_name):
        self.workbook = xlsxwriter.Workbook(file_name+".xlsx")
        self.worksheet = self.workbook.add_worksheet()
    #defining style for headers of excel file
    def set_style(self,style):
        self.style = self.workbook.add_format({style:True})
    #setting the headers of excel file(report)
    def set_headers(self,headers):
        self.headers = headers
        headers.insert(0,"directory")
        for i,head in enumerate(headers):
            self.worksheet.write(0,i,head,self.style)
    #filling the data into file according to headers
    def fill_data(self,data):
        x = 1
        for k,v in data.items():
            self.worksheet.write(x,0,k)
            for k1,v1 in v.items():
                self.worksheet.write(x,self.headers.index(k1),v1)
            x +=1
    #closing the current workbook
    def close(self):
        self.workbook.close()
