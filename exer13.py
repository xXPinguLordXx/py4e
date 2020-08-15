filename = input("Enter filename: ")
sum = 0
count = 0

try:
    fhandle = open(filename)
except:
    print("File not found")
    exit()

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        dspam = float(line[line.find(':')+1:])
        count += 1
        sum += dspam

print("Average spam confidence: ", sum/count)
