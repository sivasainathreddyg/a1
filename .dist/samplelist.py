sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
list1=[]
list2=[]
for x,y in sample_list:
    list1.append((y,x))
list1.sort()
for a,b in list1:
    list2.append((b,a))
print(list2)