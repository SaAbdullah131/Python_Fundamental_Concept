# Global Variable in python
x = 'awesome'; # global Variable 

def myfunc():
    name = 'SA Abdullah';
    global x;
    x= 'fantastic'; # local Variable which is just working inside of a function
    #print(x,name);

myfunc();
#print(name);
#print(x);
print('Python is' + x);