### Problem 1700. Number of Students Unable to Eat Lunch (Easy): https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

### Tags: Queue
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = []
        rotations = 0
        i = 0
        while(students and rotations != len(students)):
            if(students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
                rotations = 0
            else:
                popped = students.pop(0)
                students.append(popped)
                rotations += 1
        return rotations

### Using Queue

from queue import Queue
class Solution2:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = Queue()
        sw = Queue()
        for i in range(len(students)):
            st.put(students[i])
            sw.put(sandwiches[i])
        rotations = 0
        while(st.qsize() != 0 and rotations != st.qsize()):
            if(st.queue[0] == sw.queue[0]):
                st.get()
                sw.get()
                rotations = 0
            else:
                popped = st.get()
                st.put(popped)
                rotations += 1
        return rotations

class Solution3:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        type_1 = 0
        type_0 = 0
        for pref in students:
            if(pref == 1):
                type_1 += 1
            else:
                type_0 += 1
        for stype in sandwiches:
            if((stype == 1 and type_1 == 0) or (stype == 0 and type_0 == 0)):
                break
            if(stype == 1):
                type_1 -=1
            else:
                type_0 -=1
        return max(type_1,type_0)