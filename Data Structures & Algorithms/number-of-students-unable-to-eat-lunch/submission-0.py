class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        alarm_counter = len(students)
        while sandwiches and students:
            sandwich = sandwiches[0]
            student = students[0]
            if sandwich is student:
                sandwiches.pop(0)
                students.pop(0)
                alarm_counter = len(students)
            elif alarm_counter == 0:                
                break
            else:
                students += [students.pop(0)]
                alarm_counter -= 1

        return len(students)