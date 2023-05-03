import EDIClass

inEdifilename = "Samples/Sample_850_01_Orig.edi"
with open(inEdifilename, 'r') as file:
    fileContents = file.read()

fileContents = fileContents.replace("\n", "").replace("\r", "")
elementSeperator = fileContents[103:104]
rowSeperator = fileContents[105:106]

# print("ElementSeparator=" + elementSeperator)
# print("RowSeparator=" + rowSeperator)

# print(fileContents)

rows = fileContents.split(rowSeperator)
# print(rows)

po850 = EDIClass.PurchaseOrder850()
lastRefCode = ""
firstTime = True
foundLineItem = False

for row in rows:
    # print(row)
    elements = row.split(elementSeperator)
    for idx, el in enumerate(elements):
        elementIDNum = str.format("{0:0=2d}", idx)
        if idx == 0:
            segmentName = el
        elementsID = segmentName + elementIDNum
        print("   ", elementsID, el)
        if elementsID == "BEG02":
            po850.POType = el
        if elementsID == "BEG03":
            po850.PONum = el
        if elementsID == "BEG05":
            po850.PODate = el

        if elementsID == "REF01":
            lastRefCode = el

        if lastRefCode == "VR" and elementsID == "REF02":
            po850.VendorOrderNumber = el
        if lastRefCode == "AB" and elementsID == "REF02":
            po850.RefDemo = el

        if elementsID == "N101":
            lastRefCode = el
        if lastRefCode == "ST" and elementsID == "N102":
            po850.ShipToName = el
        if lastRefCode == "ST" and elementsID == "N103":
            po850.ShipToCode = el

        if elementsID == "PO100":
            if not firstTime:
                po850.add_lineitem(po850Line)

            po850Line = EDIClass.PurchaseOrder850LineItem()
            foundLineItem = True
            firstTime = False

        if elementsID == "PO101":
            po850Line.LineNum = el
        if elementsID == "PO102":
            po850Line.Qty = el
        if elementsID == "PO103":
            po850Line.UOM = el
        if elementsID == "PO104":
            po850Line.Price = el
        if elementsID == "PO105":
            po850Line.Basis = el
        if elementsID == "PO107":
            po850Line.PartNum = el
        if elementsID == "PID05":
            po850Line.Descr = el
        if elementsID == "DTM02":
            po850Line.DateRequested = el

        if elementsID == "CTT01":
            # Hand the last hanging POLine item that has not been written out yet
            if foundLineItem:
                po850.add_lineitem(po850Line)


print("\n=============== End of Parsing =============")
po850.print()


#
# Now you have a PO Object in memory, what do you do with it?
# Basically, the PO needs to be loaded into your system (ERP or database)
# 1) Serialize it to disk as XML or JSON for some other program to process
# 2) Build SQL statements, or call Stored Procedures to store in a database
# 3) Call an API/Library or a web Service to add the PO to your system
