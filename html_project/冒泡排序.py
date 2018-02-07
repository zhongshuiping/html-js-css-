array = [1,2,3,4,5]
for i in range(len(array)-1):
    for j in range(len(array)-1-i):
        if array[j+1] > array[j]:
            array[j],array[j+1] = array[j+1],array[j]

print(array)

for i in range(4):
    print(i)