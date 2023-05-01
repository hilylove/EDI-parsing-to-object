inEdifilename = "Samples/Sample_850_01_Orig.edi"
with open(inEdifilename, 'r') as file:
    fileContents = file.read()

fileContents = fileContents.replace("\n", "").replace("\r", "")
elementSeperator = fileContents[103:104]
rowSeperator = fileContents[105:106]

print("ElementSeparator=" + elementSeperator)
print("RowSeparator=" + rowSeperator)

# print(fileContents)

rows = fileContents.split(rowSeperator)
# print(rows)

for row in rows:
    # print(row)
    elements = row.split(elementSeperator)
    for idx, el in enumerate(elements):
        elementIDNum = str.format("{0:0=2d}", idx)
        if idx == 0:
            segmentName = el
        elementsID = segmentName + elementIDNum
        print("   ", elementsID, el)
