class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        def dfs(node):
            visited.add(node)
            for adj in rooms[node]:
                if adj not in visited:
                    dfs(adj)
        
        dfs(0)
        return True if len(rooms) == len(visited) else False