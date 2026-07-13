class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Agar array khali hai, toh 0 return karein
        if not nums:
            return 0
            
        # Pehla element hamesha unique hota hai, toh left pointer ko 1 se start karenge
        l = 1
        
        # Right pointer ko 1 se lekar poore array ke end tak chalayenge
        for r in range(1, len(nums)):
            # Agar current element apne peeche waale element ke barabar NAHI hai, 
            # matlab hume ek naya unique element mil gaya hai!
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]  # Naye unique element ko left pointer ki jagah par daal dein
                l += 1             # Left pointer ko aage badhayein
                
        # l hi hamara k hai (total unique elements ka count)
        return l
        