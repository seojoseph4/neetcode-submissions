class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            m = (l + r) // 2

            days_used = 1
            curr_weight = 0

            for weight in weights:
                if curr_weight + weight > m:
                    days_used += 1
                    curr_weight = weight
                else:
                    curr_weight += weight

            if days_used <= days:
                # Capacity works, try a smaller capacity
                r = m - 1
            else:
                # Capacity is too small
                l = m + 1

        return l