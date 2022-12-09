# Given an array a, your task is to apply the following mutation to it:

# Array a mutates into a new array b of the same length
# For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + array[i + 1]
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it is considered to be 0
# For example, b[0] equals 0 + a[0] + a[1]

def mutation(a):
# initialize b array     
    b = []      
    # base case: the size of array a is one     
    if(len(a)==1):         
        # a[-1] and a[1] do not exist         
        b.append(0 + a[0] + 0)         
        # return array b         
        return b     
        # for each i from 0 to a.length - 1     
    for i in range(len(a)):         
        # a[i-1] does not exist         
        if(i==0):             
            b.append(0 + a[i] + a[i+1])

        # a[i+1] does not exist         
        elif(i==len(a)-1):             
            b.append(a[i-1] + a[i] + 0)         
                
        # all elements exist         
        else:             
            b.append(a[i-1] + a[i] + a[i+1])     
            # return array b     
            return b  

# main method for testing mutation function 
if __name__ == "__main__":      
    # take input from the terminal     
    print("Enter array :",end=" ")     
    a = [int(i) for i in input().split(" ")]      # call muatation(a) function     b = mutation(a)      # print mutated array      print("Mutated array: ",b)