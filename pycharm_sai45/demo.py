'''
s = list(map(int,input().split()))

print(s)

bh = [a for a in s if a!=max(s)]

print(bh)

if max(s)**2 == (bh[0]**2 + bh[1]**2):
    print("yes")
else:
    print("no")
'''

print("*************"+'\033[91m'+"BILL"+'\033[91m'+"*************")