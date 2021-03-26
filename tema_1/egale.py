filein = open("egale.in", 'r')
fileout = open("egale.out", 'w')
input = [int(i) for i in filein.read().split()]
#input[0] = task
list = []
for i in range(1, 100):
    for j in range(ord("1"),ord("9") + 1):
        list.append(int(chr(j) * i))
# list of good elements
if input[0] == 1:
    for i in list:
        if i >= input[1] and i <=input[2]:
            fileout.write(str(i) + " ")
    #task1 if my element is in interval I write it
else:
    lim = int(input[1] * '9')
    for i in list:
        if i > lim:
            break
        fileout.write(str(i)+" ")
    #if my element is bigger than lim I stop

