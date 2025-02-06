from typing import Any


class HashMap:
    DEFAULT_SIZE = 16

    def __init__(self, size: int = DEFAULT_SIZE):
        self.size = size
        self.buckets: list[list[tuple[str, Any]]] = [[] for _ in range(size)]

    def get(self, key: str, default: Any = None):
        hashed_key = hash(key) % self.size
        bucket = self.buckets[hashed_key]

        for (k, v) in bucket:
            if key == k:
                return v
        
        return default

    def put(self, key: str, value: Any):
        # Get the bucket
        hashed_key = hash(key) % self.size
        bucket = self.buckets[hashed_key]

        # Check for duplicates
        for i, (k, _) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return

        # Add to the bucket
        bucket.append((key, value))
        self.buckets[hashed_key] = bucket


def run():
    hash_map = HashMap()

    hash_map.put("name", "John Doe")
    hash_map.put("age", 24)

    print(hash_map.get("name"))
    print(hash_map.get("age"))
    print(hash_map.get("none"))
    print(hash_map.get("one", 1))

if __name__ == "__main__":
    run()
