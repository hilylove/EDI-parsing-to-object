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


print("\n=============== End of Parsing =============")
po850.print()
