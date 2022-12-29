class CS50PLecture7:

    class ObjectOrientedProgramming:
            
        class Student:
            
            '''
            name = input("Name: ")
            house = input("House: ")
            print(f"{name} from {house}")
            '''

class AbstractOOP:
                
    # We can create functions to abstract away parts of this program.
    def main():
        name = AbstractOOP.get_name()
        house = AbstractOOP.get_house()
        print(f"{name} from {house}")


    def get_name():
        return input("Name: ")


    def get_house():
        return input("House: ")

class TupleOOP:

    # A tuple is a sequences of values. Unlike a list, a tuple can’t be modified. In spirit, we are returning two values.
    # tuples are immutable, meaning we cannot change those values. Immutability is a way by which we can program defensively.
    def main():
        student = TupleOOP.get_student()
        if student[0] == "Padma":
            student[1] = "Ravenclaw"

        # index into tuples using student[0] or student[1].
        print(f"{student[0]} from {student[1]}")

        '''
        name, house = CS50PLecture6.ObjectOrientedProgramming.Student.TupleOOP.get_student()
        print(f"{name} from {house}")
        '''

    def get_student():
        name = input("Name: ")
        house = input("House: ")

        # return both items to a variable called student
        return (name, house)


    if __name__ == "__main__":
        main()
            
class ListOOP:
                
    # lists are mutable. 
    def main():
        student = ListOOP.get_student()
        if student[0] == "Padma":
            student[1] = "Ravenclaw"
        print(f"{student[0]} from {student[1]}")

        '''
        name, house = CS50PLecture6.ObjectOrientedProgramming.Student.TupleOOP.get_student()
        print(f"{name} from {house}")
        '''

    def get_student():
        name = input("Name: ")
        house = input("House: ")

        # return both items to a variable called student
        return [name, house]


    if __name__ == "__main__":
        main()

            
