class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [item*(-1) for item in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            new_weight = a-b
            print(stones, new_weight)
            if new_weight < 0:
                heapq.heappush(stones, new_weight)

        if len(stones) > 0:
            return abs(stones[0])
        else:
            return 0