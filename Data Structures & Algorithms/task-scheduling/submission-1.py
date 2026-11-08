class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get element frequency. Convert it to a maxHeap (-ve for python)
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)

        # Have a staging queue for elements under wait. ([counts, Available time])
        q = deque()
        
        # Initiate time
        t = 0

        # While elements in maxHeap or q
        while maxHeap or q:
            # Increment time
            t += 1

            # Process elements in  maxHeap
            if maxHeap:
                # Pop counts/freq from heap
                count = 1 + heapq.heappop(maxHeap)

                # If we find an element
                if count:
                    # Increment the count, add wait time, and append in the queue
                    q.append([count, t + n])

            # Process element in queue
            # If queue is not empty and the top element time matches
            if q and q[0][1] == t:
                # Push element to maxHeap         
                heapq.heappush(maxHeap, q.popleft()[0])

        # Return time
        return t