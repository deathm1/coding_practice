class Solution:
    def naiveSolution(self, ransomNote: str, magazine: str) -> bool:
        my_rnote = ransomNote
        my_mag = list(magazine)
        for letter in my_rnote:
            if letter in my_mag:
                my_mag.remove(letter)
            else:
                return False
        return True
    def efficientSolution(self, ransomNote: str, magazine: str) -> bool:
        for set_element in set(ransomNote):
            if(magazine.count(set_element)<ransomNote.count(set_element)):
                return False
        return True

my_obj = Solution()

print(my_obj.efficientSolution("aa", "aab"))