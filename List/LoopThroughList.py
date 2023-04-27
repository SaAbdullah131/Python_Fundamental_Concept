## Loop through list

myFriends = ['sumon','ajoy','ashik','raihan','bikash'];

for friend in myFriends:
    print(friend);

# print all items by referring to their index number;

thisList = ['apple','banana','cherry'];

print('\n\n');
length = len(thisList);
print(length);
for list in range(len(thisList)-1):
    print(thisList[list]);

print("\n Using While loop");
i = 0;

while i < length:
    print(thisList[i]);
    i+=1;

