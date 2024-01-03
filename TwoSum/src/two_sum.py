def two_sum(nums: [int], target: int) -> [int]:
    previous_map = {}  # value : index

    for index, number in enumerate(nums):
        """
        index, number 
        """
        diff = target - number
        if diff in previous_map:
            return [previous_map[diff], index]
        previous_map[number] = index
