class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = {}

        for s in students:
            if s not in cnt:
                cnt[s] = 0
            cnt[s] += 1
        
        for sandwich in sandwiches:
            if sandwich in cnt and cnt[sandwich] > 0:
                cnt[sandwich] -=1
                res -=1
            else:
                return res    
        
        return res  

