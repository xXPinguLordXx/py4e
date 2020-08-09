T = 40 #total hours per week/cutoff time

#input hours worked:
hours = input("Enter hours:")
try:
    hours = float(hours)
except:
    hours = -1
    print('Error, please enter numeric input')
    exit()

#input rate worked:
rate = input("Enter rate:")
try:
    rate = float(rate)
except:
    rate = -1
    print('Error, please enter numeric input')
    exit()

#computation:

if hours > T:
    OT = (hours - T)*(rate*1.5)
    OGPay = (T*rate)
    print(OT+OGPay)
else:
    OGPay = hours*rate
    print(OGPay)
