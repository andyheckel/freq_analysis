#!/usr/bin/python3

#This program will perform frequency analysis on a given text. Note that the
#text MUST be titled encrypted.txt (unless renamed in the code
#and located in the same directory as this script for it to work.

#open the encrypted text file for reading. The variable encrypted_text is set to
#the string value of this file. An empty dictionary frequencies is created.
frequencies = {}
with open("encrypted.txt", "r") as f:
    encrypted_text = f.read()
#create an empty string nospace and an empty list char_list
nospace = ""
char_list = []
#parses through each character in the string encrypted_text. If the character
#is NOT a space, it is added to the string nospace. This will result in a string
#equal to the original encrypted text with the spaces removed.
for i in encrypted_text:
    if(i != " "):
        nospace += i
#print(nospace)
#Parses through each character in the string nospace. Adds each character to the
#list char_list. A new set (char_set) is created from char_list, thereby removing
#duplicate characters and making the frequency analysis more readable. 
for i in nospace:
    char_list.append(i)
    char_set = set(char_list)
#Parses each character in char_set. Each character is set to a key in frequencies, and its value is
#obtained by dividing the count of each character by the total length of nospace.

for i in char_set:
    frequencies[i] = (nospace.count(i)/len(nospace))

#Prints the frequencies of each character (via the dictionary frequencies). Note that the first print operation
#will output an unsorted list. This was my original code, which worked well enough for
#the purpose of this assignment.
#print(frequencies)

sort_list = sorted(frequencies.items(), key=lambda x:x[1],reverse=True)
print(sort_list)



