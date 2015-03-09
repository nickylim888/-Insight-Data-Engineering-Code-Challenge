import os;
from collections import Counter

files = os.listdir("../wc_input")
allwords = []

# loop through files
for filename in files:

    #open() opens file and `with` statement closes file
    with open('../wc_input/' + filename) as f:

        #create a list of all words fetched from file
        words = [word for line in f for word in line.split()]
        allwords.extend(words)
print "Total word count is", len(words)

#run collections.Counter
c = Counter(words)
for word, count in c.most_common():
   print word, count

