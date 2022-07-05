class implementation_of_chaining():

    def __init__(self, bucket : int) -> None:
        """Initialization of hashing table.

        Args:
            bucket (int): Size of bucket, (List of lists)
        """
        self.BUCKET = bucket
        self.my_hash_table = [[] for x in range(bucket)]
    
    def insert(self, key: int):
        """Inserts key in hash table

        Args:
            key (int): key
        """
        my_key = key % self.BUCKET
        self.my_hash_table[my_key].append(key)
    
    def remove(self, key: int):
        """deletes keys from hash table

        Args:
            key (int): key
        """
        my_key = key % self.BUCKET
        if key in self.my_hash_table[my_key]:
            self.my_hash_table[my_key].remove(key)

    def print(self):
        print(self.my_hash_table)

    def search(self, key: int):
        """Checks if key exists

        Args:
            key (int): key
        """
        my_key = key % self.BUCKET
        return key in self.my_hash_table[my_key]


    


def driver():
    h = implementation_of_chaining(7)
    h.insert(70)
    h.print()
    h.insert(71)
    h.print()
    h.insert(9)
    h.print()
    h.insert(56)
    h.print()
    h.insert(72)
    h.print()

    print(h.search(56))

    h.remove(56)

    print(h.search(56))
    h.print()

if(__name__=="__main__"):
    driver()