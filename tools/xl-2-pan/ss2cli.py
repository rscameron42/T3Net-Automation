#! python3
# ss2cli.py - get data from spread-sheets and output code for pasting into Panorama CLI session

import openpyxl
import openpyxl.worksheet.table

wb = openpyxl.load_workbook('wb23.xlsx')
sheet = wb['Sheet1']

for ws in wb.worksheets:
    print("Worksheet %s include %d tables:" % (ws.title, len(ws._tables)))
    for tbl in ws._tables:
        print(" : " + tbl.displayName)
        print("   -  name = " + tbl.name)
        print("   -  type = " + (tbl.tableType if isinstance(tbl.tableType, str) else 'n/a'))
        print("   -  range = " + tbl.ref)
        print("   -  #cols = %d" % len(tbl.tableColumns))
        
        print()
        print(tbl)
        print()
        
        for col in tbl.tableColumns:
            print("     : " + col.name)
    

