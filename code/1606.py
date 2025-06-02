import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = SortedList([i for i in range(k)])
        queue = []
        handled = [0] * k

        for i, (start, time) in enumerate(zip(arrival, load)):
            while queue and queue[0][0] <= start:
                _, idx = heapq.heappop(queue)
                free.add(idx)

            if not free:
                continue

            pos = free.bisect_left(i % k)
            if pos == len(free):
                pos = 0
            target = free[pos]

            heapq.heappush(queue, (start + time, target))
            free.remove(target)
            handled[target] += 1

        max_handled = max(handled)
        return [i for i, count in enumerate(handled) if count == max_handled]
        