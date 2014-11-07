class Student:
    def __init__(self, id, name, gender, year_of_birth, city):
        self.id = id
        self.name = name
        self.gender = gender
        self.year_of_birth = year_of_birth
        self.city = city

    def printInfo(self):
        print "ID:%s NAME:%s GENDER:%s YEAR_OF_BIRTH:%s CITY:%s" % (self.id, self.name, self.gender, self.year_of_birth, self.city)


if __name__ == '__main__':
    stu = Student('200200023', 'Alex', 'M', 2394, 'BEIJING')
    stu.printInfo()
