class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        if self._capacity < 0:
            raise ValueError("Capacity must be positive")
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError("Jar is full")

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError("Jar is empty")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
