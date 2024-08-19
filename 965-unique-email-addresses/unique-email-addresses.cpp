class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set <string> uniqe;

        for (auto& email : emails)
        {
        int i = 0;
        string local = "";

        while (email[i] != '@' && email[i] != '+')
        {
            if (email[i] != '.')
            {
                local += email[i];
            }
            i++;
        }

        while (email[i] != '@')
            i++;
        
        string domain = email.substr(i + 1);
        email = local +'@'+ domain;
        cout << email;
        uniqe.insert(email);
        }
    return uniqe.size();
    }
};