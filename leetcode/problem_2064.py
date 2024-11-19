### Problem 2064. Minimized Maximum of Products Distributed to Any Storeclass Solution:
### tags: array, Binary Search

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(quantity):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / quantity)
            return stores <= n
        start = 1
        end = max(quantities)
        result = 0
        while(start <= end):
            quantity =  start + (end - start) // 2
            if(can_distribute(quantity)):
                result = quantity
                end = quantity - 1
            else:
                start = quantity + 1

        return result