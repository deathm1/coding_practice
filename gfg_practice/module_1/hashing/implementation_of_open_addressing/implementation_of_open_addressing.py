class implementation_of_open_addressing():

    def __init__(self, bucket : int) -> None:
        """Initialization of hashing table.

        Args:
            bucket (int): Size of bucket, (List of lists)
        """
        self.BUCKET = bucket
        self.my_hash_table = [-1] * bucket
        self.size = 0

    def hash(self, key:int):
        return key%self.BUCKET
    
    def insert(self, key: int):
        if self.size == self.BUCKET:
            return False
        if self.search(key) == True:
            return False
        
        current_position = self.hash(key)
        t = self.my_hash_table


        while t[current_position] not in (-1,-2):
            # this is circular traversal, if first_position is 6 then first_position becomes 0
            current_position = (current_position+1) % self.BUCKET
        
        # perform insertion
        t[current_position] = key
        self.size = self.size + 1
        return True

    def remove(self, key: int):
        h = self.hash(key)
        t = self.my_hash_table

        first_position = h

        while t[first_position] != -1:
            if t[first_position] == key:
                t[first_position] = -2
                return True

            # this is circular traversal, if first_position is 6 then first_position becomes 0
            first_position = (first_position + 1) % self.BUCKET
            
            # when we come back to the original / start position
            if first_position == h:
                return False
        return False

    def print(self):
        print(self.my_hash_table)

    def search(self, key: int):
        h = self.hash(key)
        t = self.my_hash_table

        first_position = h

        while t[first_position] != -1:
            if t[first_position] == key:
                return True

            # this is circular traversal, if first_position is 6 then first_position becomes 0
            first_position = (first_position + 1) % self.BUCKET
            
            # when we come back to the original / start position
            if first_position == h:
                return False
        return False



    


def driver():
    h = implementation_of_open_addressing(7)
    h.insert(49)
    h.insert(50)
    h.insert(51)
    h.insert(63)
    h.insert(68)
    h.insert(69)
    
    h.print()

    h.remove(49)
    h.print()

    h.remove(63)
    h.print()

    h.remove(64)
    h.print()

if(__name__=="__main__"):
    driver()