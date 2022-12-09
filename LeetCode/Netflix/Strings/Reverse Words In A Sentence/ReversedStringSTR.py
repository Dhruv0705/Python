
# Method 1 (Simple): Generate all words separated by space. One by one reverse words and print them separated by space. 
# Method 2 (Space Efficient): We use a stack to push all words before space. As soon as we encounter a space, we empty the stack. 

# Python3 program to reverse individual words
# in a given string using STL list
 
# reverses individual words of a string
def reverseWords(string):
    st = list()
 
    # Traverse given string and push all characters
    # to stack until we see a space.
    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])
 
        # When we see a space, we print
        # contents of stack.
        else:
            while len(st) > 0:
                print(st[-1], end= "")
                st.pop()
            print(end = " ")
 
    # Since there may not be space after
    # last word.
    while len(st) > 0:
        print(st[-1], end = "")
        st.pop()
 
# Driver Code
if __name__ == "__main__":
    string = "Hello World"
    reverseWords(string)

# Method 2 
# Python code to reverse words
 
s = " Geeks for Geeks"
l = []

# splitting the string
s = s.split()
for i in s:
    
    # reversing each word
    l.append(i[::-1])
# printing string using join
 
# function after reversing the
# words
 
 
print(" ".join(l))