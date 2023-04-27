# Remove Item
ourTeacher = ['sovon','obaidur','mehedi','harun'];
print("Before remove\n",ourTeacher);
ourTeacher.remove('harun');
print("After remove\n",ourTeacher);

# pop() method for remove specified index
ourTeacher.pop(1); # if we don not specified the index the pop() method remove the last item
print("After pop\n",ourTeacher);
del ourTeacher[0];
print(ourTeacher);

onionPrice =[20,45,200,160];
print("Before Clear \n",onionPrice);
onionPrice.clear();
print("After Clear\n",onionPrice);
