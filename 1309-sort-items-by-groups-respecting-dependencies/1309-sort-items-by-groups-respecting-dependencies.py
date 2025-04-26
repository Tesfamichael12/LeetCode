class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # assign invalid groups
        for i, g in enumerate(group):
            if g == -1:
                group[i] = m
                m += 1

        items_graph = defaultdict(list)
        items_indegree = defaultdict(int)

        groups_graph = defaultdict(list)
        groups_indegree = defaultdict(int)
        for i, before in enumerate(beforeItems):
            for node in before:
                items_graph[node].append(i)
                items_indegree[i] += 1

                if group[node] != group[i]:
                    groups_graph[group[node]].append(group[i])
                    groups_indegree[group[i]] += 1
        
        def top_sort(graph, indegree, nodes): # general function for top sort
            qu = deque([ node for node in nodes if node not in indegree ])
            ans = []
            while qu:
                cur = qu.popleft()
                ans.append(cur)
                for child in graph[cur]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        qu.append(child)
            
            return ans if len(ans) == len(nodes) else []
        
        all_items = list(range(n))
        sorted_items = top_sort(items_graph, items_indegree, all_items)
        if not sorted_items: return []

        all_groups = list(range(m))
        sorted_groups = top_sort(groups_graph, groups_indegree, all_groups)
        if not sorted_groups: return []

        grouped_items = defaultdict(list)
        for item in sorted_items:
            grouped_items[group[item]].append(item)
        
        final_ans = []
        for g in sorted_groups:
            final_ans.extend(grouped_items[g])
        
        return final_ans