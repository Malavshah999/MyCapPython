#Fibonacci Series 

number=int(input("Enter the number till which u need Fibonacci series"))
first  =0                                        
second = 1                   
if number>0:
    print(first,second,end=" ")
    for i in range(2,number):
        next=first+second                           
        print(next,end=" ")
        first=second
        second=next
   
else:
     print("For series Enter a number Greater than 0")
