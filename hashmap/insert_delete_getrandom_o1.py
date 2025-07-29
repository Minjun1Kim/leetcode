class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        in_map = val not in self.val_to_idx

        if in_map:
            self.val_to_idx[val] = len(self.lst)
            self.lst.append(val)

        return in_map

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last_val = self.lst[-1]

        # move last_val into idx
        self.lst[idx] = last_val
        self.val_to_idx[last_val] = idx

        # pop last and delete val mapping
        self.lst.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        random_int = random.randint(0, len(self.lst)-1)
        return self.lst[random_int]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
