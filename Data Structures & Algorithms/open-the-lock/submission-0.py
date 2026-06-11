from collections import deque
from typing import List

class Solution:
    def get_neis(self, lock):
        res = []
        for i in range(4):
            digit = int(lock[i])

            for move in [-1, 1]:
                new_digit = (digit + move) % 10
                nei = lock[:i] + str(new_digit) + lock[i+1:]
                res.append(nei)

        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        start = "0000"
        if start in dead:
            return -1
        if start == target:
            return 0

        q = deque([(start, 0)])
        seen = {start}

        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns

            for nei in self.get_neis(lock):
                if nei not in dead and nei not in seen:
                    seen.add(nei)
                    q.append((nei, turns + 1))

        return -1