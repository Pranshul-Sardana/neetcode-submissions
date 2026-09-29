class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Get all distances
        distance = []

        for x, y in points:
            distance.append([(x**2)+(y**2), x, y]) #()**0.5

        #Convert list to heap
        heapq.heapify(distance)
        
        #Pop heap k times and add to a new list
        res = []

        for _ in range(k):
            res.append(heapq.heappop(distance)[1:])
        
        #Return the new list
        return res