import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if len(points) <= k:
            return points 

        def get_distance(x, y):
            print(x, y)
            return math.sqrt(x**2 + y**2)

        
        heap = []
        heapq.heapify(heap)



        # iterate over the points , get distance, while heap size is in range of k
        # push pop  (-distance, (x,y))
        for x,y in points:
            distance = get_distance(x,y)
            pair = (-distance, (x,y))
            print(pair)

            heapq.heappush(heap, pair)
            if len(heap) > k:
                heapq.heappop(heap)
            print(heap)
      
        k_closest = [point  for d,point in heap]
        print(k_closest)

        return k_closest


        