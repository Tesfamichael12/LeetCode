/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        // first let's find the middel of the lined list 
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        // now let's revers the second half of the linked list
        ListNode* prv = nullptr;
        ListNode* cur = slow;
        ListNode* temp;
        while (cur != nullptr)
        {
            temp = cur->next;
            cur->next = prv;
            prv = cur;
            cur = temp;
            
        }

        // Now merge the first and the second halfs
        ListNode* first = head;
        ListNode* second = prv;
        while (second->next != nullptr)
        {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;

            first->next = second;
            second->next = temp1;

            first = temp1, second = temp2;
        }
    }
};