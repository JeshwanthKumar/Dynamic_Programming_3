#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution(object):
    def minCost(self, costs):
        for i in range(len(costs)-1, -1, -1):       #For every costs from the last of the array
            costs[i][0] += min(costs[i+1][1], costs[i+1][2])    #For the first house in a row the paint is selected by choosing minimum between costs[i+1][1], costs[i+1][2]
            costs[i][1] += min(costs[i+1][0], costs[i+1][2])    #For the second house in a row the paint is selected by choosing minimum between costs[i+1][0], costs[i+1][2]
            costs[i][2] += min(costs[i+1][0], costs[i+1][1])    #For the third house in a row the paint is selected by choosing minimum between costs[i+1][0], costs[i+1][1]
    
        return min(costs[0])    #Return the minimum value from the first row