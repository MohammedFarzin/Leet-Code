import collections

def find_itinerary(tickets):
    graph = collections.defaultdict(list)
    for src, desc in tickets:
        graph[src].append(desc)
    
    for src in graph:
        graph[src].sort(reverse=True)

    stack = ['JFK']
    res = []

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        else:
            res.append(stack.pop())
    return res[::-1]

s = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
r_value = find_itinerary(s)
print(r_value)