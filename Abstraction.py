#Task-1

from abc import ABC, abstractmethod
class Employee:
    @abstractmethod
    def CalculateSalary(self):
        pass
class Fulltime(Employee):
    def __init__(self, months, sal):
        self.total = months * sal
    def calculateSalary(self):
        print("Full time employee total Salary : ", self.total)
class Freelancer(Employee):
    def __init__(self, hours, amount):
        self.FlTotal = hours * amount
    def calculateSalary(self):
        print("Freelancer total Salary : ", self.FlTotal)
class PartTime(Employee):
    def __init__(self, projects, compensation):
        self.PtTotal = projects * compensation
    def calculateSalary(self):
        print("Part time employee total Salary : ", self.PtTotal)

full = Fulltime(3,23000)
print("==========Emplyees salary details===========")
full.calculateSalary()
full = Freelancer(5,500)
full.calculateSalary()
full = PartTime(2,250)
full.calculateSalary()





#Task-2

from abc import ABC,abstractmethod
class Course(ABC):
    @abstractmethod
    def calculateFee(self):
        pass
class FreeCourse(Course):
    def __init__(self, course_name, course_fee, course_duration):
        self.__course_name = course_name
        self.__course_fee = course_fee
        self.__course_duration = course_duration
    def calculateFee(self):
        print("Course name : ",self.__course_name)
        print("Course Fee : ",self.__course_fee)
        print("Course duration : ",self.__course_duration)
class PaidCourse(Course):
    def __init__(self, course_name, course_fee, course_duration):
        self.__course_name = course_name
        self.__course_fee = course_fee-1000
        self.__course_duration = course_duration
    def calculateFee(self):
        print("Course name : ",self.__course_name)
        print("Course Fee : ",self.__course_fee)
        print("Course duration : ",self.__course_duration)
class PremiumCourse(Course):
    def __init__(self, course_name, course_fee, course_duration):
        self.__course_name = course_name
        self.__course_fee = course_fee-1500
        self.__course_duration = course_duration
    def calculateFee(self):
        print("Course name : ",self.__course_name)
        print("Course Fee : ",self.__course_fee)
        print("Course duration : ",self.__course_duration)
c=FreeCourse("Java Full stack", "Free", "3 Months")
print("============FreeCourse==========")
c.calculateFee()
c=FreeCourse("Mern stack", "25000", "4 Months")
print("============Paid Course==========")
c.calculateFee()
c=FreeCourse("Python Full stack", "75000", "6 Months")
print("============Premium Course==========")
c.calculateFee()





#Task-3

from abc import ABC,abstractmethod
class Ticket(ABC):
    @abstractmethod
    def calculatePrice(self):
        pass
class BusTicket(Ticket):
    def __init__(self, Boarding, destination, ticket_price, Num_of_passengers):
        self.__boarding = Boarding
        self.__destination = destination
        self.__ticket_price = ticket_price
        self.__number_of_passengers = Num_of_passengers
    def calculatePrice(self):
        print("Boarding : ",self.__boarding)
        print("Destination : ",self.__destination)
        print(f"Ticket Price : {self.__number_of_passengers} x {self.__ticket_price} = {self.__ticket_price * self.__number_of_passengers}")
class TrainTicket(Ticket):
    def __init__(self, Boarding, destination, ticket_price, Num_of_passengers):
        self.__boarding = Boarding
        self.__destination = destination
        self.__ticket_price = ticket_price
        self.__number_of_passengers = Num_of_passengers
    def calculatePrice(self):
        print("Boarding : ",self.__boarding)
        print("Destination : ",self.__destination)
        print(f"Ticket Price : {self.__number_of_passengers} x {self.__ticket_price} = {self.__ticket_price * self.__number_of_passengers}")
class FlightTicket(Ticket):
    def __init__(self, Boarding, destination, ticket_price, Num_of_passengers, taxes):
        self.__boarding = Boarding
        self.__destination = destination
        self.__ticket_price = ticket_price
        self.__number_of_passengers = Num_of_passengers
        self.__taxes = taxes
    def calculatePrice(self):
        print("Boarding : ",self.__boarding)
        print("Destination : ",self.__destination)
        print(f"Ticket Price : {self.__number_of_passengers} x {self.__ticket_price} + {self.__taxes * self.__number_of_passengers} = {self.__ticket_price * self.__number_of_passengers + (self.__taxes * self.__number_of_passengers)}")
t=BusTicket("Hyderabad", "visakhapatnam", 1500,3)
print("=============Bus Ticket Details===============")
t.calculatePrice()
t=TrainTicket("visakhapatnam", "vijayawada", 256,6)
print("=============Train Ticket Details===============")
t.calculatePrice()
t=FlightTicket("Bhogapuram", "New Delhi", 8950,2,250)
print("=============Flight Ticket Details===============")
t.calculatePrice()

