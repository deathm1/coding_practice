class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(acc) for acc in accounts)
    
    def maximumWealth2(self, accounts: List[List[int]]) -> int:
        my_var = 0
        for row in accounts:
            my_sum = sum(row)
            if(my_sum>my_var):
                my_var = my_sum
        return my_var