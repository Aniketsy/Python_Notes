#---------------------------OOPs------------------------------#

# basic
#- they all us to logicaly group our data and functions in a way that's easy to reuse and also
# to build upon if needed

#method -- function asssociated with class

class Employee:
    pass    # to keep empty

# class is blue print to creating instances
emp_1 = Employee()
emp_2 = Employee()

#print(emp_1)  #<__main__.Employee object at 0x14e6161694c0>
#print(emp_2)  #<__main__.Employee object at 0x14e616169430>

# creating instance variable
emp_1.first = 'Aniket'
emp_1.first = 'Singh'
emp_1.email = 'aniket@43.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.first = 'User'
emp_2.email = 'Test@43.com'
emp_2.pay = 60000

print(emp_1.email)   #
print(emp_2.email)   #

#   so by doing like this we something miss some data and that can cause errors, and making like this dont make
# sense sp we do automatically by using special

# special __init__ method  (other language constructor)

class Employee:

    def __init__(self, first, last, pay):  # self is instance  others are arguments
        self.first = first
        self.last = last
        self.pay = pay
        self.email = ffirst + '.' + last + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Aniket', 'Singh', 50000)
emp_2 = Employee('Test', 'User', 6000)

print(emp_1.email)   #
print(emp_2.email)


# now lets see how to do some action in class - like lets get full name, not manually
print('{} {}'.format(emp_1.first, emp1.last))   # this is manually

# lets create a method to do this see above
print(emp_1.fullname())   # make sure gto have parenthesis to get the value


# common mistake during making methods, forgetting self--- we will get error

# we can also run these methods y using class itself
emp_1.fullname()  # we dont need instance here 
Employee.fullname(emp_1)  # but by class we need instance to identify
 

#------------------------------------- class variables ------------------------------#
# are variabes that are shared among all instance of the clases , these should be same for each instance
#lets say company give annual raises every year
class Employee:

    num_of_emp =0
    
    raise_amount = 1.04  # we can also access from class itself like Employee.raise_amount

    def __init__(self, first, last, pay):  # self is instance  others are arguments
        self.first = first
        self.last = last
        self.pay = pay
        self.email = ffirst + '.' + last + '@company.com'

        Employee.num_of_emp +=1   # here we dont need self, as we're overriding


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay = int(self.pay * 1.04)   # intead lets put in class variable as we need to raise again and again
        self.pay = int(self.pay * self.raise_amount ) # we need intance to use else, it will give name error

emp_1 = Employee('Aniket', 'Singh', 50000)
emp_2 = Employee('Test', 'User', 6000)

print(emp1.pay)   # 50000
emp_1.apply_raise()
print(emp_1.pay)  # 52000

#print(Employee.__dict__)  # show all the thing which we have in class


# lets say we want to keep track the number of employee 
print(Employee.num_of_emps)  #this will give 0
emp_1 = Employee('Aniket', 'Singh', 50000)
emp_2 = Employee('Test', 'User', 6000)

print(Employee.num_of_emps)  #this will give 2


#-------------------------------------- class methods --------------------------------------------------#

# regular method, class method, static method

class Employee:

    num_of_emp =0
    raise_amount = 1.04 

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = ffirst + '.' + last + '@company.com'

        Employee.num_of_emp +=1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay = int(self.pay * 1.04)  
        self.pay = int(self.pay * self.raise_amount )

#------------------
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

#--------------------static method, they dont pass, self, or class
    @staticmethod #this is decorator 
    def is_workday(day):  # if we are not using self(instance), or class they we need not to be regular or class method
        if day.weekday() == 5 or if day.weekday() ==6:
            return False
        return True


Employee.set_raise_amt(1.05)   #----- after this all will 1.05
print(Employee.raise_amt) #1.04
print(em1.rasie_amt)   #1.04  
print(emp_2.raise_am) #1.04


emp_str_1 = 'john-Doe-72000'
emp_str_2 = 'steve-smith-30000'
emp_str_3 = 'jane-Doe-72000'

#first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee,from_string(emp_str_1)

print(emp_1.email)   #now this will work
print(emp_2.email)

