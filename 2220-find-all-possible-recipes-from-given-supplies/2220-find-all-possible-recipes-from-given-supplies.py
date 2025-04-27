class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        re = set(recipes)
        supplies = set(supplies)
        issupplied = {}
        for r in recipes:
            issupplied[r] = True

        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] in re:
                    graph[ingredients[i][j]].append(recipes[i])
                    indegree[recipes[i]] += 1
                else:
                    if ingredients[i][j] not in supplies:
                        issupplied[recipes[i]] = False

        qu = deque( [node for node in recipes if node not in indegree and issupplied[node] == True] )
        order = []
        while qu:
            cur = qu.popleft()
            order.append(cur)
            for child in graph[cur]:
                indegree[child] -= 1
                if indegree[child] == 0 and issupplied[child] == True:
                    qu.append(child)

        return order
        
