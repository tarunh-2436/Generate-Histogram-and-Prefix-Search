
# Question 1
'''
Write a Python program that reads all the given text files and performs the following :

Prepares the set of words appearing in ther given text files and stores them as "words.txt"

Prepares a bag of words that records how many times each word is appearing in the given text files
and stores them as "words-histogram.txt"
'''
# Question 2
'''
Write another Python program that reads "words.txt" and "words-histogram.txt" files and does the
following until 'EOFError' is raised:

Reads input text 'prefix' from the console and prints all the words that start with that 'prefix'.
The output words should be in the descending order of their appearance count. Your program should
continue to do this until 'EOFError' is raised (which can be acheived by pressing ctrl + D)
'''

import os

# Function to generate list of words from Directory
def Generate_Word_List(Directory) :

    try :
        # Obtaining a list of all objects in a directory
        Directory_List = os.listdir(Directory)

    # Handling cases where <Directory> is a file and cannot use listdir
    except NotADirectoryError :
        pass

    else :
        for Directory_Object in Directory_List :

            # Filtering text files out of all elements in directory
            if Directory_Object.endswith('.txt') :
                try :
                    f = open(Directory + '\\' + Directory_Object)
                    Text = f.read()

                # Handling error where unknown characters are in text file
                except UnicodeDecodeError :
                    pass
                else :

                    # Splitting the contents of the text file into a list
                    Words = Text.split() 
                    for Word in Words :
        
                        # Filtering Special Characters
                        Updated_Word = '' 
                        for Character in Word :
                            if Character not in '.?!@#$%^&*()_+-=[]{};:"\|,<.>/\'' :
                                Updated_Word += Character
        
                    # Getting a list of words to be entered into the file
                        if Updated_Word != '' : 
                            Updated_Word = Updated_Word.lower()
                            Word_List.append(Updated_Word)
                            
                    f.close()

            elif '.' not in Directory_Object :

                # Searching through sub directories
                Generate_Word_List(Directory + '\\' + Directory_Object)
                
# Function to write list of words in file words.txt
def Write_Words_In_File(Word_List) :
    f=open('words.txt','w')

    for Word in Word_List :
        f.write(Word) 
        f.write('\n')
            
    f.close()

# Function to generate a histogram from words in words.txt
def Generate_Histogram(File_Name) :
    f = open(File_Name)
    Text = f.read()
    Words = Text.split()

    Histogram = {}
    for Word in Words :
        if Word not in Histogram :
            Histogram[Word] = 1
        else :
            Histogram[Word] += 1

    return Histogram

# Function to sort histogram based on frequency
def Sort_Histogram(Histogram) :
    Items=list(Histogram.items()) 
            
    for i in range(len(Items)-1) :
        for j in range(len(Items)-i-1) :
            if Items[j][1] < Items[j+1][1] :
                Items[j], Items[j+1] = Items[j+1], Items[j]
            
    Sorted_Histogram =  dict(Items)
    return Sorted_Histogram

# Function to write contents of histogram in file word_histogram.txt
def Write_Histogram_In_File(Histogram) :
    f = open('words-histogram.txt','w')
            
    for Word,Frequency in Histogram.items() :
        f.write(Word)
        f.write(' : ')
        f.write(str(Frequency))
        f.write('\n')
        
    f.close()

# Function to search words based on prefix
def Search_Prefix(Histogram_File) :
    prefix = input('Enter prefix to search based on : ')
    Histogram = open(Histogram_File)
    print('\nThe words that start with "' + prefix + '" are :')

    for row in Histogram :
        elements = row[:-1].split(' : ')
        Word, Frequency = elements
        if Word.startswith(prefix) :
            print(row[:-1])

    



# Defining The Directory To Search In
Directory = "C:\\Users\\tarun\\OneDrive - SSN-Institute\\Desktop\\Tarun College Python\\python-3.11.3-docs-text"

# Initialising The List Of Words
Word_List = [] 

Generate_Word_List(Directory)
Write_Words_In_File(Word_List)
Histogram = Generate_Histogram('words.txt')
Sorted_Histogram = Sort_Histogram(Histogram)
Write_Histogram_In_File(Sorted_Histogram)
Search_Prefix('words-histogram.txt')
