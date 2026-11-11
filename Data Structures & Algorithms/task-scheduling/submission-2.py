class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get frequency
        counts = Counter(tasks)

        # Convert to maxheap (-ve of min element)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)

        # Initiate a deque staging area
        q = deque()

        # Initate time
        t = 0

        # while staging area or maxHeap
        while q or maxHeap:
            # Increase time
            t += 1

            # If maxHeap
            if maxHeap:
                # Pop element and add 1 (reducing frequency in maxheap)
                item = 1 + heapq.heappop(maxHeap)
                # If element, add it to the staging area [changed frequency, time available]
                if item:
                    q.append([item, n+t])

            # if deque and time reached for 0th element,
            if q and q[0][1] == t:
                # Pop element frequency from the left of the dq, push it ot the max heap
                heapq.heappush(maxHeap, q.popleft()[0])

        # Return time
        return t
