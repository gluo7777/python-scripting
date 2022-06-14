# https://docs.python.org/3/library/functools.html#functools.total_ordering
from functools import total_ordering
from dataclasses import dataclass
import heapq

@total_ordering
@dataclass
class Student:
    group: int
    name: str

    def __eq__(self, other: 'Student') -> bool:
        return self.group == other.group and self.name == other.name
    
    def __lt__(self, other: 'Student') -> bool:
        """
        if group is same, student A > B
        """
        if self.group == other.group:
            return self.name > other.name
        return self.group < other.group
    
students = []
students.append(Student(1,'William'))
students.append(Student(1,'Will'))
students.append(Student(1,'Bill'))
students.sort()

assert students[0].name == 'William'

students = []
heapq.heappush(students,Student(1,'William'))
heapq.heappush(students,Student(1,'Will'))
heapq.heappush(students,Student(2,'Bill'))
heapq.heappush(students,Student(2,'Dill'))

assert heapq.heappop(students).name == 'William'
assert heapq.heappop(students).name == 'Will'
assert heapq.heappop(students).name == 'Dill'
assert heapq.heappop(students).name == 'Bill'
assert len(students) == 0