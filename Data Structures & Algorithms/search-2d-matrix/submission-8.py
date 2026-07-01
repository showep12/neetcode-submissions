class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #right most value
        #there is two sort of orderded lists
        #1) we can find the row which contain the target value
        #2) loop the row with binary search
        #3)

        """
        find the mid row and then check the value
        if the leftmost value is 
        if (matrix[mid][0] < target) : target could be in the mid row
        
        If matrix[mid][-1] < target, then the target cannot be in the current mid row.
        Since every value in the current row and all rows above it is less than the target,
        we move startRow to mid + 1 and discard those rows.

        If matrix[mid][0] > target, then the target cannot be in the current mid row.
        Since every value in the current row and all rows below it is greater than the target,
        we move endRow to mid - 1 and discard those rows.

        if (matrix[mid][-1] > target) : target could be in the mid row

        while TopStartRow <= BottomEndRow:
         # If TopStartRow exceeds BottomEndRow, the target does not exist.
         “The loop continues as long as there is at least one possible row left to check.”

        1) less than the target then move start point to mid value because under move point 
    
        2) greater than target then move end point to mid value because  
        """
        TopStartRow, BottomEndRow = 0, len(matrix) - 1
        print(TopStartRow,BottomEndRow)
        midRow = 0
        while (TopStartRow <= BottomEndRow) : #if TopStartRow > BottomEndRow, there is no target value
            midRow = (TopStartRow + BottomEndRow)//2

            # “the first element of the mid row in the matrix”
            #“matrix at midRow, index zero” / “matrix midRow zero”
            #“the element at row midRow and column zero”
            if (matrix[midRow][0] > target) : 
                # If the leftmost value of the mid row is greater than the target,
                # the target must be in the rows above.
                BottomEndRow = midRow - 1
            elif (matrix[midRow][-1] < target) : 
                # If the rightmost value of the mid row is less than the target,
                # the target must be in the rows below.
                TopStartRow = midRow + 1
            else : #target is greater or equal than leftmost value and less or equal than right most value 
                   #it means we found the target row
                # The target is within the range of this row,
                # so this is the target row.
                break


        # The row range no longer overlaps, so the target cannot exist.
        if (TopStartRow > BottomEndRow) : 
            return False

        startCol = 0
        endCol = len(matrix[0]) -1

        while (startCol <= endCol) :
            midCol = (startCol + endCol)//2
            midValue = matrix[midRow][midCol]
            if (midValue == target) :
                return True
            elif (midValue < target) : 
                startCol = midCol + 1
            #if midValue is greater than target we can remove the 
            #it means over than midValue is not the candidate we can remove the range
            #it means we change the endPoint under the midPoint
            elif (midValue > target) : 
                endCol = midCol - 1
        return False


        # #m by n two-dimensional integer array
        # #big-O of log m times n 
        # #Each row is sorted in ascending order, allowing duplicates.”
        # #if we go to right, the number never decrease
        # #
        # #First we search the range o
        # #각 Row의 시작점들을 binary search로 찾는다 -> 즉 각 sublist의 first 
        # #if the target value is over than first value of startRow
        # #check the endRow's value, if the value of endRow's firstindex is also greater 
        # #then we have to find endRow if it isn't, we have to find startRow

        # startRow = 0
        # endRow = len(matrix) -1
        
        # while (startRow <= endRow) :
        #     midRow = (startRow + endRow)//2
        #     midValue = matrix[midRow][0]
            
        #     if (midValue == target) :
        #         return True
        #     elif (midValue < target) : 
        #         startRow = midRow + 1
        #     #if midValue is greater than target we can remove the 
        #     #it means over than midValue is not the candidate we can remove the range
        #     #it means we change the endPoint under the midPoint
        #     elif (midValue > target) : 
        #         endRow = midRow - 1
        
        # targetRow = 0
        
        # print(startRow)
        # print(endRow)
        # if (startRow != endRow) :  #if startRow > endRow
        #     return False
            
        # else :
        #     if (matrix[startRow][0] < target) : 
        #         targetRow = startRow
        #     elif : #if matrix[startRow][0] >= target
        #         targetRow = startRow - 1

        
        
        # startCol = 0
        # endCol = len(matrix[0]) -1

        # while (startCol <= endCol) :
        #     midCol = (startCol + endCol)//2
        #     midValue = matrix[targetRow][midCol]
        #     if (midValue == target) :
        #         return True
        #     elif (midValue < target) : 
        #         startCol = midCol + 1
        #     #if midValue is greater than target we can remove the 
        #     #it means over than midValue is not the candidate we can remove the range
        #     #it means we change the endPoint under the midPoint
        #     elif (midValue > target) : 
        #         endCol = midCol - 1
        # return False