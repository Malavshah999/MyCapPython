#Taking radius of circle as input 
r = float(input ("Input the radius of the circle : "))

#Printing Area as output 
print ("The area of the circle is: " + str(3.141592653589793238 *r*r))

#Take a filename and print its extension 
filename = input("Enter a filename :")
fileex = filename.split(".")
print("Extension of file is :" + fileex[-1])

