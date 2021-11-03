# HW2
#Due Date: 02/20/2021, 11:59PM

"""
### Collaboration Statement:

"""

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        return "{}({}): {}".format(self.cid, self.credits, self.cname)

    __repr__ = __str__

    def __eq__(self, other):
        if type(self) == Course and type(other) == Course:
            return self.cid == other.cid
        return False



class Catalog(Course):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
        >>> isinstance(C.courseOfferings['CMPSC132'], Course)
        True
    '''
    def __init__(self):
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        if cid in self.courseOfferings:
            return "Course already added"
        else:
            self.courseOfferings[cid] = Course(cid, cname, credits)
            return "Course added successfully"

    def removeCourse(self, cid):
        if cid in self.courseOfferings:
            self.courseOfferings.pop(cid)
            return "Course removed successfully"
        else:
            return "Course not found"


class Semester(Course):
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.addCourse(Course(42, 'name',"zero credits"))
        'Invalid course'
        >>> semester.courses
        [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
    '''

    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = []



    def __str__(self):
        if not self.courses:
            return "No courses"
        else:
            return ", ".join([str(course.cid) for course in self.courses])

    __repr__ = __str__

    def addCourse(self, course):
        if course in self.courses:
            return "Course already added"
        elif type(course.cid) != str or type(course.cname) != str or type(course.credits) != int:
            return "Invalid course"
        else:
            self.courses.append(course)
            return None

    def dropCourse(self, course):
        if course not in self.courses:
            return "No such course"
        elif type(course.cid) != str or type(course.cname) != str or type(course.credits) != int:
            return "Invalid course"
        else:
            self.courses.remove(course)
            return None

    @property
    def totalCredits(self):
        total = 0
        for course in self.courses:
            total += course.credits
        return total

    @property
    def isFullTime(self):
        if self.totalCredits >= 12:
            return True
        return False


class Loan:
    '''
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    '''


    def __init__(self, amount):
        self.loan_id = self.__loanID
        self.amount = amount


    def __str__(self):
        return "Balance: ${}".format(self.amount)

    __repr__ = __str__


    @property
    def __loanID(self):
        return random.randint(10000, 99999)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        self.name = name
        self._ssn = ssn

    def __str__(self):
        return "Person({}, ***-**-{})".format(self.name, self._ssn[7:])

    __repr__ = __str__

    def get_ssn(self):
        return self._ssn

    def __eq__(self, other):
        if type(self) == Person and type(other) == Person:
            return self._ssn == other._ssn
        return False


class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        self.supervisor = supervisor
        self.name = name
        self._ssn = ssn


    def __str__(self):
        return "Staff({}, {})".format(self.name, self.id)

    __repr__ = __str__


    @property
    def id(self):
        return "905" + "".join(letter[0].lower() for letter in self.name.split()) + self._ssn[7:]

    @property
    def getSupervisor(self):
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        if type(new_supervisor) == Staff:
            self.supervisor = new_supervisor
            return "Completed!"
        return None


    def applyHold(self, student):
        if type(student) == Student:
            student.hold = True
            return "Completed!"
        return None

    def removeHold(self, student):
        if type(student) == Student:
            student.hold = False
            return "Completed!"
        return None

    def unenrollStudent(self, student):
        if type(student) == Student:
            student.active = False
            return "Completed!"
        return None




class Student(Person, Semester, Course):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        self.name = name
        self._ssn = ssn
        self.year = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()


    def __str__(self):
        return "Student({}, {}, {})".format(self.name, self.id, self.year)

    __repr__ = __str__

    def __createStudentAccount(self):
        if self.active == True:
            return StudentAccount(self)
        return None


    @property
    def id(self):
        return "".join(letter[0].lower() for letter in self.name.split()) + self._ssn[7:]

    def registerSemester(self):
        if self.active == True and self.hold == False:
            self.semesters[len(self.semesters)+1] = Semester(len(self.semesters)+1)
            if len(self.semesters) == 1 or len(self.semesters) == 2:
                self.year = "Freshman"
            elif len(self.semesters) == 3 or len(self.semesters) == 4:
                self.year = "Sophomore"
            elif len(self.semesters) == 5 or len(self.semesters) == 6:
                self.year = "Junior"
            elif len(self.semesters) > 6:
                self.year = "Senior"
            return None
        else:
            return "Unsuccessful operation"


    def enrollCourse(self, cid, catalog, semester):
        if self.active != True or self.hold != False:
            return "Unsuccessful operation"
        else:
            if cid not in catalog.courseOfferings:
                return "Course not found"
            elif catalog.courseOfferings[cid] in self.semesters[semester].courses:
                return "Course already enrolled"
            else:
                self.semesters[semester].courses.append(catalog.courseOfferings[cid])
                self.account.balance += catalog.courseOfferings[cid].credits * self.account.ppc
                return "Course added successfully"


    def dropCourse(self, cid, semester):
        if self.active == True and self.hold == False:
            for course in self.semesters[semester].courses:
                if course.cid == cid:
                    self.semesters[semester].courses.remove(course)
                    return "Course dropped successfully"
            else:
                return "Course not found"
        else:
            return "Unsuccessful operation"

    def getLoan(self, amount):
        if self.active != True:
            return "Unsuccessful operation"
        elif len(self.semesters) == 0 or self.semesters.get(max(self.semesters.keys())).isFullTime == False:
            return "Not full-time"
        else:
            loan = Loan(amount)
            self.account.loans[loan.loan_id] = loan
            self.account.makePayment(loan.amount)
            return None




class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
    '''
    ppc = 1000

    def __init__(self, student):
        self.student = student
        self.balance = 0
        self.loans = {}


    def __str__(self):
        return"Name: {}\nID: {}\nBalance: ${}".format(self.student.name, self.student.id, self.balance)

    __repr__ = __str__


    def makePayment(self, amount):
        self.balance -= amount
        return self.balance


    def chargeAccount(self, amount):
        self.balance += amount
        return self.balance




####################### STAND ALONE FUNCTION ###############################################


def createStudent(person):
    """
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
        >>> isinstance(s, Student)
        True
    """
    return Student(person.name, person._ssn, "Freshman")
