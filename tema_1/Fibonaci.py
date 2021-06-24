input = int(input())
list = [1,1]
# test is i need only the first element of Fibonnaci
if input == 1:
    print(1)
    exit(0)
# create Fibonnaci list untill I have n elements
while len(list) is not input:
    list.append(list[len(list) - 1] + list[len(list)- 2])
# just print
for i in list:
    print(i, end=" ")