l = []
n = int(input("Enter the Total Number of List Elements: "))
for i in range(1, n + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    l.append(value)
i = 0
while(i < n):
    j = i + 1
    while(j < n):
        if(l[i] > l[j]):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
        j = j + 1
    i = i + 1

print("Element After Sorting List in Ascending Order is : ", l)
l.sort(reverse=True)
print("Element After Sorting List in Descending Order is : ", l)