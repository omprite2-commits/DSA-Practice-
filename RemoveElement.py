class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # k pointer shuruat mein valid elements ko store karne ke liye index track karega
        k = 0
        
        # Poore array par loop chalayein
        for i in range(len(nums)):
            # Agar current element 'val' ke barabar NAHI hai, toh yeh hamare kaam ka hai
            if nums[i] != val:
                nums[k] = nums[i]  # Is valid element ko k-th position par daal dein
                k += 1             # k ko ek step aage badhayein
                
        # k hi un elements ka total count hai jo 'val' ke barabar nahi hain
        return k