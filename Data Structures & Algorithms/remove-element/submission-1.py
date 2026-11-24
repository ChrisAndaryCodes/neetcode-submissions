class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer that tracks where to place the next valid element

        # Loop through every index in the array
        for i in range(len(nums)):

            # Check if the current element is NOT equal to val
            if nums[i] != val:

                # Copy the current element to position k
                nums[k] = nums[i]

                # Move k to the next available position
                k += 1

        # Return the number of valid elements
        return k
