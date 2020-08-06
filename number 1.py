#definining a fuction called vowel
def vowel(word):
    
    vowels = "aeiou" #sring of all vowels

    string = word.lower() #returning the original string. this string contains duplicates

    newstring = set(string) # removing duplicates in the original string

    count = len(string)-len(newstring) #getting the number of duplicates

    vowelstring = "" #string of vowels contained in last string

#adding vowels from the last string to the vowel string
    for x in vowels:
        if x in newstring:
            vowelstring += str(x)

    return (vowelstring, count)

if __name__ == "__main__": #running the file directly and not imported

    print(vowel("andinda ruth"))
    