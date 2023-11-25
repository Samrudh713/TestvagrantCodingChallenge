gstUmb = 12
gstLeat = 18
gstCigar = 28
gstHoney = 0

unitLeat = 1100
unitUmb = 900
unitCigar = 200
unitHoney = 100

quaLeat = 1
quaUmb = 4
quaCigar = 3
quaHoney = 2

print("enter umberella gst")
gst = input()

print("enter umberella unit price")
unit = input()

print("enter umberella quantity")
quantity = input()

totGstOfPro1 = (int(gst)*int(unit)*int(quantity))/100 * 0.95

print("the total gst of wallet is " + str(totGstOfPro1))

print("enter Leather wallet gst")
gst = input()

print("enter wallet unit price")
unit = input()

print("enter wallet quantity")
quantity = input()

totGstOfPro2 = (int(gst)*int(unit)*int(quantity))/100 * 0.95

print("the total gst of wallet is " + str(totGstOfPro2))

print("enter cigeratte gst")
gst = input()

print("enter cigeratte unit price")
unit = input()

print("enter cigeratte quantity")
quantity = input()

totGstOfPro3 = (int(gst)*int(unit)*int(quantity))/100

print("the total gst of cigeratte is " + str(totGstOfPro3))

print("enter honey gst")
gst = input()

print("enter honey unit price")
unit = input()

print("enter honey quantity")
quantity = input()

totGstOfPro4 = (int(gst)*int(unit)*int(quantity))/100

print("the total gst of honey is " + str(totGstOfPro4))

print("the highest gst a product can pay is of INR " + max(totGstOfPro1, totGstOfPro2, totGstOfPro3, totGstOfPro4) + "and the product is cigeratte" )
# part 2 below 

totAmtofLeath = (unitLeat) - totGstOfPro2
totAmtofUmb = (unitUmb*4) - totGstOfPro1
totAmtofCigeratte = (unitCigar*3) - totGstOfPro2
totAmtofHoney = (unitHoney*2) - totGstOfPro4

print("the total amount to be paid to the shopkeeper is " + (totAmtofLeath + totAmtofUmb + totAmtofCigeratte + totAmtofHoney))