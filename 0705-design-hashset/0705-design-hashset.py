class MyHashSet:

    def __init__(self):
        self.num_bucket = 1009
        self.bucket = [[]for _ in range(self.num_bucket)]

    def add(self, key: int) -> None:
        bucket_idx = key % self.num_bucket
        if key not in self.bucket[bucket_idx]:
            self.bucket[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = key % self.num_bucket
        if key in self.bucket[bucket_idx]:
            self.bucket[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = key % self.num_bucket
        return key in self.bucket[bucket_idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)