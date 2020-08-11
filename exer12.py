filename = input("Enter filename: ")

try:
    fhandle = open(filename)
except:
    print("File not found")
    exit()

for line in fhandle:
    print(line.strip().upper())
