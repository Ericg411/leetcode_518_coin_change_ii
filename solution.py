from typing import List
import bisect

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        total = 0
        history = set()
        
        def recurse(current):
            nonlocal total
            for i in range(len(coins)):
                if current.total > amount:
                    return
                elif current.total == amount and tuple(current.num_list) not in history:
                    total += 1
                    history.add(tuple(current.num_list))
                    return
                current.update(coins[i])
                recurse(current)
                current.delete(coins[i])

        recurse(TestObj([], 0))        
        return total

class TestObj:
    def __init__(self, num_list, total):
        self.num_list = num_list
        self.total = total

    def update(self, num):
        bisect.insort_left(self.num_list, num)
        self.total += num

    def delete(self, num):
        self.num_list.remove(num)
        self.total -= num