def isGoodMatrixCheck(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            return False
        else:
            dic[arr[i]] = i
    return True
def isGoodMatrix(matrix):
    for i in range(len(matrix)):
        if isGoodMatrixCheck(matrix[i]) == False:
            return "matrix is not good"
    return "Matrix is Good"
print(isGoodMatrix([[1,2,3],[2,1,3],[4,5,6]])) 