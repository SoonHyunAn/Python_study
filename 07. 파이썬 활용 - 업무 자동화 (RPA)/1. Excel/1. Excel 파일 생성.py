from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Basic Sheet"
wb.save("Sample.xlsx")
wb.close()