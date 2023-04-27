fruits = ['apple','banana','cherry','kiwi','mango'];

newList = [];

for x in fruits:
    if 'a' in x:
        newList.append(x)
      
print(newList,"\n");

myFriend = ["Sumon",'Ajoy','Prosanjeet','Moon'];
newFriendList = [friend for friend in myFriend if "u" in friend];
print(newFriendList);