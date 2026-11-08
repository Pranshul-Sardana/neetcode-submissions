class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get the frequency of items. Use it to create a maxheap (Python minheap)
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)

        # Stage the currently inactive elements in a queue # [Frequency, Time to use]
        q = deque()

        # Initiate time
        t = 0

        # While there are elements in the heap or queue
        while maxHeap or q:
            # Increment time
            t += 1

            # If elements in heap
            if maxHeap:
                # Pop elements
                count = 1 + heapq.heappop(maxHeap)
                # Add in queue
                if count:
                    q.append([count, t + n])

            # If time to use, add elemets to heap
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])


        # Return time
        return t