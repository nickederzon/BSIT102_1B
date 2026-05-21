import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active


sheet ['A1'] = "Order ID"
sheet ['B1'] = "Customer Name"
sheet['C1'] = "Product Name"
sheet['D1'] = "Quantity"
sheet['E1'] = "Price"
sheet['F1'] = "Totak"

workbook.save("ordersDB.xlsx")
