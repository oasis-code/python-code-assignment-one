#a function that takes two lists
def fizzbuzz(list1,list2):

#combining two lists
   newlist = list1+list2

#combined length of both lists 
   mylist=len(newlist)

# conditions
   if(mylist %3==0 and mylist % 5==0):
        print ("fizzbuzz")

   elif(mylist %3==0):
        print ("fizz")
        
   elif(mylist %5==0):
        print ("buzz")

   else:
        print ("mylist")  

if __name__ == "__main__":
        fizzbuzz(["a","b","c","d"],["e","f","g","h","i","j"]) #calling the function in main

