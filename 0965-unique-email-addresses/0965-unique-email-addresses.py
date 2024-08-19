class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqe = set()
        for email in emails:
            i, local1 = 0, [] * 51 # since strings are imutable adding a character to a string taks O(n) each time so we should first store the characters in a list and then join them together

            while email[i] not in ['@', '+']:
                if email[i] != '.':
                    local1.append(email[i])
                i += 1
            local = ''.join(local1)
            while email[i] != '@':
                i += 1
            domain = email[i + 1 :]
            uniqe.add((local, domain))

        return len(uniqe)