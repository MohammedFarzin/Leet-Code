def minCostConnectPoints(points) -> int:
        d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
        while d:
            x, y = min(d, key=d.get)  
            for x1, y1 in d:          
                d[(x1, y1)] = min(d[(x1, y1)], abs(x-x1)+abs(y-y1))
        return res

p = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(minCostConnectPoints(p))