
from Student import Student
from Date import Date

s1 = Student("John" ,Date(6,1,1999),90)
s2 = Student("Marry",Date(10,8,1997),80)

s1.setName(input())
s2.setDate( Date( input(), input(), input() ) )

s1.toString()
s2.toString()