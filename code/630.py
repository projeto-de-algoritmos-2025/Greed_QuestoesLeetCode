import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        
        tempo_total = 0
        heap_max = []  
        
        for duracao, lastDay in courses:
            heapq.heappush(heap_max, -duracao)
            tempo_total += duracao
            
            if tempo_total > lastDay:
                maior_duracao = -heapq.heappop(heap_max)
                tempo_total -= maior_duracao
        
        return len(heap_max)
