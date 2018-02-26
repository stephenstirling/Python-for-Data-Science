filename = input("Enter a file: ")
openfile = open(filename)
#This creates a variable that will contain all of the text from the text file that's opened
dictionary = dict()
#Creates a blank dictionary to store all of words
for word in openfile:
    #Now that the file is open we are applying the for loop to all of the content from the opened file
	word = word.rstrip()
    #Strips all the white space from the text that we opened
	word_split = word.split()
    #Creates a new variable and takes all of the different words we have in the text and splits them into separate strings
	for w in word_split:
		if w in dictionary:
			dictionary[w] = dictionary[w] + 1
            #The words are split into individual strings. This adds the words as keys to the dictionary and adds the number of times they appear.
		else:
			dictionary[w] = 1

print(dictionary)





