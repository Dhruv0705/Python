'''

48. Rotate Image [https://leetcode.com/problems/rotate-image/] [Medium]

Tags:

    Array
    Matrix

Companies: 
    
    Amazon | 2
    Microsoft | 2
    Google | 2
    Facebook | 2
    Apple | 2
    Adobe | 2
    Bloomberg | 2
    Oracle | 2
    Yahoo | 2
    VMware | 2
    Cisco | 2
    eBay | 2
    LinkedIn | 2
    Uber | 2
    Twitter | 2
    Snapchat | 2
    Yelp | 2


You are given an n x n 2D matrix representing an image.
    rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.

Note:
    90 degrees clockwise rotation matrix
    O(n2) time complexity
    O(1) space complexity

         Left Bound |      | Right Bound
Top Bound -         5 1 9 11
                    2 4 8 10
                    13 3 6 7
Bound Bound -       15 14 12 16

    5 will move to 11  
    11 will move to 16
    16 will move to 15
    15 will move to 5

    1 will move to 10
    10 will move to 7
    7 will move to 14
    14 will move to 5

    9 will move to 2
    2 will move to 13

'''

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # set left and right bounds to 0 and the end of the matrix
        left, right = 0, len(matrix) - 1

        # while the left bound is less than the right bound
        while left < right: 
            
            # for each value in the current layer of the matrix
            for i in range(right - left):   
                
                # set the top and bottom bounds to the current layer
                top , bottom = left, right  

                # store the top left value
                #temp = matrix[left][left + i]
                topLeft = matrix[top][left + i]
                

                # move the bottom left value to the top left
                #matrix[left][left + i] = matrix[right - i][left]
                matrix[top][left + i] = matrix[bottom - i][left]
                

                # move the bottom right value to the bottom left
                #matrix[right - i][left] = matrix[right][right - i]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                

                # move the top right value to the bottom right
                #matrix[right][right - i] = matrix[left + i][right]
                matrix[bottom][right - i] = matrix[top + i][right]
                

                # move the top left value to the top right
                #matrix[left + i][right] = temp
                matrix[top + i][right] = topLeft
            
            # move the bounds inwards
            right -= 1
            left += 1
                


