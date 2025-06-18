# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
#     def getLength(head: ListNode) -> int:
#         length = 0
#         while head:
#             length += 1
#             head = head.next
#         return length
    
#     dummy = ListNode(0, head)
#     length = getLength(head)
#     cur = dummy
#     for i in range(1, length - n + 1):
#         cur = cur.next
#     cur.next = cur.next.next
#     return dummy.next


# def getLength(head: ListNode) -> int:
#         length = 0
#         while head:
#             length += 1
#             head = head.next
#         return length


# l = [1, 2, 3, 4, 5]
# head = ListNode(l[0])
# current = head
# for i in l[1:]:
#     current.next = ListNode(i)
#     current = current.next
        

from time import time

def DecoCountTime(function):
    def wrapper(*args, **kargs):
        start = time()
        originalreturn = function(int(*args, **kargs))
        end = time()
        print(f"\nIt takes total {end - start} seconds!")
        return originalreturn 
    return wrapper
                  

@DecoCountTime
def eg(n):
    count = 0
    for i in range(n):
        count += i
    print(count)
    return count

# eg(int(10e7))

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits ="spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards =[Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, positon):
        return self._cards[positon]

deck = FrenchDeck()
# print(len(deck))
# print(deck.ranks.index("A"))

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.value)
    return rank_value * len(suit_values) + suit_values[card.suit]

from collections import defaultdict, Counter
from math import inf
from typing import List
from bisect import bisect_left





class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def count(upper: int) -> int:
            res = 0
            j = len(nums) - 1
            for i, x in enumerate(nums):
                while j > i and nums[j] > upper - x:
                    j -= 1
                if j == i:
                    break
                res += j - i
            return res
        return count(upper) - count(lower - 1)



        








        





        


        







