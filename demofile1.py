# import a function from another file
import demofile2 as demo2;


def sumOfTwoInt(a,b):
   sum  = a + b 
   return sum

# calling the sum function
print(f"sum of 3+4 is:  {sumOfTwoInt(3,4)}")
# another way of printing a str and and int. spereate with comma ","
#print(f"sum of 3+4 is: ",  sumOfTwoInt(3,4))

# calling the product function that is imported from another .py file
print("product of 3*4 is: " + str(demo2.productOfTwoInt(3,4)))