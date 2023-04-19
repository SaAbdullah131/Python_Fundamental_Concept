# To concatenate or combine ,two string you use the + operator

a = "hello";
b = "World !";
c = a+" " + b;
print(c);

# We can combine strings and number by using the formate() method
age = 26;
text="My Name is SA Abdullah, and i am {}";
print(text.format(age)); 

quantity = 3;
itemno = 567;
price = 49.95;
myOrder =" I Want {} pieces of item {} for {} dollars";
print(myOrder.format(quantity,itemno,price));
myOrder = " I Want to Pay {2} Dollars for {0} pieces of item{1}";
print(myOrder.format(quantity,itemno,price));
