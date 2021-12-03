# this pattern is all about reverse of the right angle triangle with full of the stars
for i in range(1,10) :
    for j in range(10,i,-1):
        print(' * ', end = ' ')
    print()