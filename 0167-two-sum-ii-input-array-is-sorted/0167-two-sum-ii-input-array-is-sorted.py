class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            
            if i <=target:
                m=target-i
                if m==i:
                    return [numbers.index(i)+1,numbers.index(m)+2]
                elif m in numbers:
                    return [numbers.index(i)+1,numbers.index(m)+1]
            else:
                return [numbers.index(i)+1,numbers.index(i)+2]


            # 9-first number(if first number<9) = 7  is 7 in numbers (if yes)index(7)+1
            #else 
        