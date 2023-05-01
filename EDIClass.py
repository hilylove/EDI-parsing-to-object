
# Define Classes


class PurchaseOrder850:
    def __init__(self):
        self.PONum = ""
        self.PODate = ""
        self.POType = ""
        self.VendorOrderNumber = ""  # from REF*VR
        self.RefDemo = ""  # from REF*AB
        self.ShipToName = ""  # from N102
        self.ShipToCode = ""  # from N103

    def print(self):
        print("PONum=" + self.PONum + " PODate:" +
              self.PODate + " Type: "+self.POType + " VendorRefNum: " +
              self.VendorOrderNumber + " RefDemo: "+self.RefDemo +
              " ShipToCode: " + self.ShipToCode + " ShipToName: " + self.ShipToName)


# demo how to use object/class variable
# po850 = PurchaseOrder850()
# po850.PONum = "Test"
# po850.POType = "NE"
# po850.PODate = "20230501"

# po850.print()
