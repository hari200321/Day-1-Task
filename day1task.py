# Write a python programme to calculate the total number of vowels A,E,I,O,U in the string "Guvi geeks network private limited "?

# Given string
input_string = "Guvi geeks network private limited"

# Convert the string to lowercase to simplify counting
input_string = input_string.lower()

# Initialize count variables
count_a = count_e = count_i = count_o = count_u = 0

# Count each vowel in the string
for char in input_string:
if char == 'a':
count_a += 1
elif char == 'e':
count_e += 1
elif char == 'i':
count_i += 1
elif char == 'o':
count_o += 1
elif char == 'u':
count_u += 1

# Calculate the total count of vowels
total_vowels = count_a + count_e + count_i + count_o + count_u

# Display the total count of each vowel and the total count of all vowels
print(f"Total count of 'A': {count_a}")
print(f"Total count of 'E': {count_e}")
print(f"Total count of 'I': {count_i}")
print(f"Total count of 'O': {count_o}")
print(f"Total count of 'U': {count_u}")
print(f"Total count of all vowels: {total_vowels}")

#2) Create a Pyramid of numbers from 1to20 using for loop

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()


    #3) 










    #4) write a program that takes a string and retunrs the number of unique characters in it

 
# Program to count the number of
# unique characters in a string
def cntDistinct(st):
 
    # Set to store unique characters
    # in the given string
    s = set([])
 
    # Loop to traverse the string
    for i in range(len(st)):
 
        # Insert current character
        # into the set
        s.add(st[i])
 
    # Return Answer
    return len(s)
 
# Driver Code
if __name__ == "__main__":
 
    st = "geeksforgeeks"
    print(cntDistinct(st))


   #  5) write a program that takes a string and retunrs true if it is a palindrome,false otherwise
   
str_1 = input (“Enter the string to check if it is a palindrome: “)

str_1 = str_1.casefold ()

rev_str = reversed (str_1)

if (list str_1) == list (rev_str):

              print (“The string is a palindrome.”)

else:

              print (“The string is not a palindrome.”) 
        


#6)  write a program that takes two strings and returns the longest common substrinf between them.

string1 = input('Give 1. word: ')
string2 = input('Give 2. word: ')
answer = ""
len1, len2 = len(string1), len(string2)
for i in range(len1):
    for j in range(len2):
        lcs_temp=0
        match=''
        while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and   string1[i+lcs_temp] == string2[j+lcs_temp]):
            match += string2[j+lcs_temp]
            lcs_temp+=1
        if (len(match) > len(answer)):
            answer = match

print(answer)


#7)  write a program that takes a string and returns the most frequent characters in it


import string

def find_max_letter_count(word):

    alphabet = string.ascii_lowercase
    dictionary = {}

    for letters in alphabet:
        dictionary[letters] = 0

    for letters in word:
        dictionary[letters] += 1

    dictionary = sorted(dictionary.items(), 
                        reverse=True, 
                        key=lambda x: x[1])

    for position in range(0, 26):
        print dictionary[position]
        if position != len(dictionary) - 1:
            if dictionary[position + 1][1] < dictionary[position][1]:
                break

find_max_letter_count("helloworld")


# 8) write a program that takes a string and returns true if it is an anagram of another string,false otherwise 


# function to check if two strings are
# anagram or not 
def check(s1, s2):
    
    # the sorted strings are checked 
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.")         
        
# driver code  
s1 ="listen"
s2 ="silent" 
check(s1, s2)

# 9) 
