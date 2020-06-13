class CCourse:
    Name = ''
    Date = ''
    TimeIndex = 0;

    def __init__(self, name, date, timeIndex):
        self.Name = name
        self.Date = date
        self.TimeIndex = timeIndex

class CPerson:
    Prename = ''
    Lastname = ''
    Courses = []
    Hashcode = 0

    def __init__(self, hashcode, prename, lastname, course):
        self.Prename = prename
        self.Lastname = lastname
        self.Hashcode = hashcode
        self.Courses = [course]

    def addCourse(self, course):
        self.Courses.append(course)

    def sortByDate(self):
        self.Courses.sort(key=lambda CCourse: CCourse.TimeIndex)
