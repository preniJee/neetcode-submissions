class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            current_load = 0
            needed_days = 1

            for weight in weights:
                if current_load + weight > capacity:
                    needed_days += 1
                    current_load = 0
                current_load += weight

            return needed_days <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left