class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = defaultdict(str) # email -> parent
        email_to_name = defaultdict(str) # email -> account name
        size = defaultdict(str) # size of the current representative

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(x, y):
            repx, repy = find(x) , find(y)

            if repx != repy:
                if size[repx] >= size[repy]:
                    parent[repy] = repx
                    size[repx] += size[repy]
                else:
                    parent[repx] = repy
                    size[repy] += size[repx]

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = first_email
                email_to_name[email] = name
                union(first_email, email)

        grouped_emails = defaultdict(list)
        for email, par in parent.items():
            rep = find(email)
            grouped_emails[rep].append(email)

        ans = []
        for eamil, emails in grouped_emails.items():
            name = email_to_name[eamil]
            cur = [name] + sorted(emails)
            ans.append(cur)
        
        return ans