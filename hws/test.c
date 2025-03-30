# include <stdio.h>
# include <stdlib.h>

typedef struct ListNode {
    int val;
    struct ListNode* next;
} ListNode;

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy = (ListNode*)malloc(sizeof(ListNode));
    dummy->next = NULL;
    ListNode* current = dummy;
    int carry = 0;
    while (l1 || l2 || carry) {
        int a = l1 ? l1->val : 0;
        int b = l2 ? l2->val : 0;
        int sum = a + b + carry;
        carry = sum / 10;
        current->next = (ListNode*)malloc(sizeof(ListNode));
        current->next->val = sum % 10;
        current->next->next = NULL;
        current = current->next;
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }
    ListNode* result = dummy->next;
    free(dummy); // 避免内存泄漏
    return result;
}


///////////////

ListNode* createNode(int val) {
    ListNode* newNode = (ListNode*)malloc(sizeof(ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

ListNode* createList(int* nums, int size) {
    ListNode* dummy = createNode(0);
    ListNode* current = dummy;
    for (int i = 0; i < size; i++) {
        current->next = createNode(nums[i]);
        current = current->next;
    }
    return dummy->next;
}

void printList(ListNode* head) {
    while (head != NULL) {
        printf("%d", head->val);
        if (head->next != NULL) printf(" -> ");
        head = head->next;
    }
    printf("\n");
}

int main() {
    int nums1[] = {2, 4, 3};
    int nums2[] = {5, 6, 4};
    ListNode* l1 = createList(nums1, 3);
    ListNode* l2 = createList(nums2, 3);

    printf("l1: ");
    printList(l1);

    printf("l2: ");
    printList(l2);

    ListNode* result = addTwoNumbers(l1, l2);
    printf("l1 + l2: ");
    printList(result);

    free(l1);
    free(l2);
    free(result);

    return 0;
}