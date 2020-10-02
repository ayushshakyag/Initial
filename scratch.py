# Scratch Program to get starting in Python3
n=int(input("Enter the no. for elements to be inserted "))
a=[]
for i in  range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
    avg=sum(a)/n
    print("Average of elements in the list",round(avg,2))
