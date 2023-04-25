# string in python


# double and single quote are work same here
print("Hello");
print('Hello');

# Assign string to a variable 
a = "Hello ";
print(a);

# Multiline String
h ='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. '''
print(h);

# String Are Array
vari = "Hello ,World !";
print(vari[1]);

# Looping through a String
for r in 'banana':
    print(r)

# String Length
print('length is : ',len(vari));

# Check String 
txt = " The best things in life are free!";
print('free' in txt); # it return boolean value that means True or False;

if 'free' in txt:
    print ("Yes,'free' is present");

print("expensive" not in txt); # expensive not in txt this is true cause expensive does not exist in txt;

if 'expensive' not in txt: 
    print("No, 'expensive' is Not Present");

for x in 'banana':
    print(x);    
print(len('banana'));
