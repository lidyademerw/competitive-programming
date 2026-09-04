class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stqueue=deque(students)
        count=0
        while len(stqueue)>0 and count<len(stqueue):
            if stqueue[0]==sandwiches[0]:
                stqueue.popleft()
                sandwiches.pop(0)
                count=0
            else:
                x=stqueue.popleft()
                stqueue.append(x)
                count+=1
        return len(stqueue)


        