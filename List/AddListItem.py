# append() method for add item in the last position

semesterSubjectList = ['network security','data mining','industrial operation'];

#append()
semesterSubjectList.append('image processing');
# insert() method
semesterSubjectList.insert(1,'compiler');
print(semesterSubjectList);

soFarSemesterSubject = ['object oriented programming','data structure','dynamic programming','structure programming'];
print("Before Extend")
print(soFarSemesterSubject);

# extend() method added end of the list
soFarSemesterSubject.extend(semesterSubjectList);
print("After extend");
print(soFarSemesterSubject);

fruitsList = ['apple','banana','cherry']; # data type list
newFruitsList = ('kiwi','lemon'); # data type tuple
print('Before extend list and tuple');
print(fruitsList);
print("After Extend")
fruitsList.extend(newFruitsList);
print(fruitsList);

