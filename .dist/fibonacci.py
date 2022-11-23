firstnum=0
secondnum=1
lst=[]
result=0
n=int(input("enter the number the user want upto the which fibonacci :"))
while result<n:
    lst.append(secondnum)
    result=firstnum+secondnum
    firstnum=secondnum
    secondnum=result
print(lst)