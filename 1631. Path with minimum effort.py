import math
from heapq import heappop, heappush
def minimum_effort_path(heights):
    rows, cols = len(heights), len(heights[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
    dist[0][0] = 0
    min_heap = [(0, 0, 0)]

    while min_heap:
        effort, x, y = heappop(min_heap)

        if x == rows-1 and y == cols-1:
            return effort
        

        for dx, dy in directions:
            nx, ny = x +dx, y + dy

            if 0 <= nx < rows and  0 <= ny < cols:
                new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))

                if new_effort < dist[nx][ny]:
                    dist[nx][ny] = new_effort
                    heappush(min_heap, (new_effort, nx, ny))