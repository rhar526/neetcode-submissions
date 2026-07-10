class Node:
    def __init__(self, key, val):
        self.k, self.v = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.lru, self.mru = Node(0,0), Node(0,0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def rem(self, node):
        prv, nxt = node.prev, node.next
        node.prev.next, node.next.prev = nxt, prv

    def ins(self, node):
        mruPrv = self.mru.prev
        mruPrv.next = node
        node.prev = mruPrv
        self.mru.prev = node
        node.next = self.mru

    def get(self, key: int) -> int:
        if key in self.cache:
            self.rem(self.cache[key])
            self.ins(self.cache[key])
            return self.cache[key].v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.rem(self.cache[key])
            self.cache.pop(key)
        self.cache[key] = Node(key, value)
        self.ins(self.cache[key])

        if len(self.cache) > self.capacity:
            self.cache.pop(self.lru.next.k)
            self.rem(self.lru.next)


