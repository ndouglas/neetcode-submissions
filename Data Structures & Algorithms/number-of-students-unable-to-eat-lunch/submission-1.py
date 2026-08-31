class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        alarm_counter = len(students)
        while sandwiches and students:
            if sandwiches[0] is students[0]:
                sandwiches.pop(0)
                students.pop(0)
                alarm_counter = len(students)
            elif alarm_counter == 0:                
                break
            else:
                students += [students.pop(0)]
                alarm_counter -= 1
        return len(students)