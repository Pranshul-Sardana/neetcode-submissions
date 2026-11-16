class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get frequencies
        counts = Counter(tasks)
        
        # Convert frequencies into a min-heap (-ve of max operations)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        # Initaite a deque as a staging area [frequency, time when available]
        q = deque([])

        # Initiate time needed
        t = 0


        # While elements in the heap or the deque
        while q or max_heap:
            # Increment time
            t += 1

            # If elements in heap
            if max_heap:
                # Pop the max (min) element from the heap and incremenent the count (because we are using -ves)
                # If element exists, stage the element to the deque
                item = 1+heapq.heappop(max_heap)
                if item:
                    q.append([item, t+n])

            # If elements in deque and time for the first element reached
            if q and q[0][1] == t:
                # Pop the element from deque and push it in the heap
                heapq.heappush(max_heap,  q.popleft()[0])
               


        # Return time needed
        return t