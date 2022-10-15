#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix) #Initializing n as the length of the martix
        for i in range(n-2, -1, -1):    #For every element from n-2 from the bottom of the matrix
            for j in range(n):  
                if j==0:    #If the the element is in first column the matrix[i][j] is equal to minimum between martrix[i+1][j] and matrix[i+1][j+1]
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j+1])
                elif j==n-1:     #If the the element is in last column the matrix[i][j] is equal to minimum between martrix[i+1][j] and matrix[i+1][j-1]
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j-1])
                else:   #Else matrix[i][j] is equal to minimum between martrix[i+1][j-1] and matrix[i+1][j+1]
                    matrix[i][j] += min(matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1])
                    
        return min(matrix[0])   #Return the minimum in the first row