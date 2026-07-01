class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #we can notice that if we find 
        #first we have to determine which row should we check to find the target value
        #if upper row's last value which is the biggest value in the upper row
        #and if it is less than target value we can discard upper rows


        #this means if we find mid row, we compare the minimum value in the middle row
        #with the target value, if the target value is less than this minimum value
        #we can dicard the lower rows including this row because it means in this middle row 
        #also doesn't contain target value

        #if the maximum value in the current middle row is less than target value
        #we can discard lower rows including this middle row

        #if the minimum value in the current middle row is greater than target value
        #we can discard upper rows not including this middle row because
        #there is a possibiliy that the target value could be in the current mid value
        #for example if the value is 12 and it is in the current mid row, and the minimum value is 10
        #if we discard the current row 

        L = 0
        R = len(matrix) - 1

        while L < R : #we don't use L<=R we will not find the answer 
        #our current objective is to remain only one row not finding answer
            mid = (L+R)//2
                    
            if target < matrix[mid][0] : #if the minimum value in the middle row is greater than target value
            #it means we have to find the left rows including current middle row, we move left pointer to the mid point
                R = mid -1
            elif matrix[mid][-1] < target : #if the maximum value in the middle row is less than target value
            #it means we have to find the right rows and discard left rows including this row
            #we move left pointer to mid + 1
                L = mid + 1
            else :
                break
        
        findRow = (L+R)//2
        print(L,R,findRow)



        L = 0
        R = len(matrix[0])-1
        print(findRow)
        while L <= R : 
            mid = (L+R)//2
            print("mid",mid, L,R)
            
            if matrix[findRow][mid] < target : 
                L = mid + 1
            elif target < matrix[findRow][mid] : 
                R = mid - 1
            else: 
                return True
        return False
