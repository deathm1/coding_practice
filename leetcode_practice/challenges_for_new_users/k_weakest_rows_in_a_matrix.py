class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        my_rank_list = []
        for i in range(len(mat)):
            my_rank_list.append([mat[i].count(1), i])
        return [i[1] for i in sorted(my_rank_list)[:k]]
                