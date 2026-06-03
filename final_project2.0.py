import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet['A1'] = "supply_name"
sheet['B1'] = "category"
sheet['C1'] = "quantity"
sheet['D1'] = "unit_price"

workbook.save("QUEBRADO_database.xlsx")