#String Length and Slicing 
str = "Python String"
str_len=len(str)
print(str_len)

#slicing string 
str='python string'
#str[0]="j" #Stings are immutable you cannot change the string.
print(str[0:2])
new_str= "j"+str[1:];#updating 
print(new_str,str)
