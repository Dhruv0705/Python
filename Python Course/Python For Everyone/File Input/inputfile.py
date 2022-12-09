# Ask for the file name
name = input("Enter a file: ")

# Open the file name
handle = open(name)

counts = dict()

# Iteration to check each line in file
for line in handle:

    # split each line into words 
    words = line.split()

    # Word iteration 
    for word in words:

        # for every line add +1 for each count (histogram)
        counts[word] = counts.get(word, 0 ) + 1

# Finds the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
