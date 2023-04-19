# Some Build-in method that you can use on Strings..

#upper() method return the string in upper case;
a = "Hello, World!";
print(a.upper());

# lower() method returns the string in lower case;
print(a.lower());

 # Remove Whitespace use strip() .Whitespace is #the space before and/or after the actual text 

myString = "    Hello Programming Python   ";
print(myString.strip()); # remove all these whitespace

# the replace() method replaces a string with another string
oneStr = "One String";
print(oneStr.replace('O','H')); # replace O to H


# The split() method returns a list where the text between the specified separator becomes the list items..
mySplit = "Hello,World";
print(mySplit.split(",")) # return ['Hello','World'];

