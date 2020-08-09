#input grade:
score = input("Enter score:")
try:
    score = float(score)
except:
    score = -1
    print('Bad score')
    exit()

if score >= 1:
    print('Bad score')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score > 0.0:
    print('F')
else:
    print('Bad score')
