import random


f = open("file.txt", "w")
counter = 0
list=[]
while counter < 80000:
    list.append(counter)
    print("generatin\n")
    counter+=1

f.write("80000\n")

print(len(list))
print("\n")
while len(list) != 0:
    r = random.randint(0,len(list)-1)
    print(str(r)+ " " + str(len(list)) + "\n" )
    if len(list) % 2 == 0:
        f.write(str(list[r]) + "\n")
    else: 
        if len(list) != 1:
            f.write(str(list[r]) + "\n")
        else:
            f.write(str(list[r]))
    list.pop(r)


print(counter)