# sorting items in list

number = [12,2,45,343,0,234,1]; 
number.sort(); # when we use sort in number it return ascending order
number.sort(reverse=True); # when we use sort in number it return descending order
print(number);

myFriend = ["Sumon","Moon","ajoy","Shanto"];
myFriend.sort();
myFriend.sort(reverse=True);

print(myFriend);

# Customize sort function

def myFunction(n):
    return abs(n-50);

numberList = [100,50,65,82,23];
numberList.sort(key = myFunction)
print(numberList);

# insensitive sort()

myFruits = ['banana','Orange','Kiwi','cherry'];
#myFruits.sort();
#print(myFruits);
myFruits.reverse();
print(myFruits);

