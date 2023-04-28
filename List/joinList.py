# join list

# join using + operator
list1 = ['a','b','c'];
list2 = [1,2,3,4];
list3 = list1 + list2;
print(list3)

for x in list1:
    list2.append(x);
print(list2);

# using extend() method 

list2.extend(list1);
print("Using extend method\n",list2);

