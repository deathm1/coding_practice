from heapq import merge


class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n_list = nums1[:m] + nums2

        my_n_list = []
        

        for i in range(0, len(n_list)-1):
            if(n_list[i]>n_list[i+1]):
                a = n_list[i]
                b = n_list[i+1]
                my_n_list.append(b)
                my_n_list.append(a)

                
                
        nums1=n_list
        return my_n_list
            
        
    def merge1(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1
        
        for d in range(m+n-1, -1, -1):

            
            if p2 < 0:
                return
            
            if p1 >= 0 and nums1[p1] > nums2[p2]:                
                nums1[d] = nums1[p1]
                p1 -= 1
            else:
                nums1[d] = nums2[p2]
                p2 -= 1


my_objs = Solution()



my_objs = merge([1,2,3,0,0,0], 3, [2,5,6], 3)

print(my_objs)


            