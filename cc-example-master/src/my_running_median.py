# example of running median program
import os

files = os.listdir("../wc_input")
files.sort()
# loop through files
wordcount = []
for filename in files:
	if not filename.startswith('.'):
	    #open() opens file and `with` statement closes file.
	    with open('../wc_input/' + filename) as f:
	    	for line in f:
	    		wordcount.append(len(line.split()))
	    		wordcount.sort()
	    		half = len(wordcount)/2
	    		if len(wordcount) % 2:
	    			print wordcount[half]
	    		else:
	    			print (wordcount[half-1] + wordcount[half])/2.0