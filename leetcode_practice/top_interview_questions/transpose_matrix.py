class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        store = []
        for i in range(m):
            my_temp_arr = []
            for j in range(n):
                my_temp_arr.append(matrix[j][i])
            store.append(my_temp_arr)
        return store