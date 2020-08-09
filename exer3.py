hours = float(input("Enter hours:")) #hours worked
rate = float(input("Enter rate:")) #rate
T = 40 #total hours per week/cutoff time


if hours > T:
    OT = (hours - T)*(rate*1.5)
    OGPay = (T*rate)
    print(OT+OGPay)
else:
    OGPay = hours*rate
    print(OGPay)
