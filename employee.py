# can change the way the billie, charlie, renee, jan, robbie, and ariel objects are constructed
# can construct additional objects or objects or different types
# the total pay MUST be calculated from the parameters provided using the formulae explained
# can NOT add arguments to the get_pay and the _str_ methods



class Employee:
    def __init__(self, name, salary , wage, hours, commission, commissionVal, bonus):
        self.name = name
        self.salary = salary
        self.wage = wage
        self.hours = hours
        self.commission = commission
        self.commissionVal = commissionVal
        self.bonus = bonus

    def commissionType(self):
        if (self.commission > 0):
            return f' and receives a commission for {self.commission} contract(s) at {self.commissionVal}/contract'
        elif (self.bonus > 0):
            return f' and receives a bonus commission of {self.bonus}'
        else:
            return ''

    def contractType(self):
        if (self.salary > 0):
            return f'monthly salary of {self.salary}'
        elif (self.wage > 0):
            return f'contract of {self.wage} hours at {self.hours}/hour'
        else:
            return ''

# depends the type of contract they have and what they have done in the past month.
    def get_pay(self):
        return self.salary + (self.wage * self.hours) + self.bonus + (self.commission * self.commissionVal)
    
# produce a string explaining how the pay has been calculated.
    def _str_(self):
        contractType = self.contractType()
        commissionType = self.commissionType()
        totalPay = self.get_pay()
        return f'{self.name} works on a {contractType}{commissionType}.  Their total pay is {totalPay}.'



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 4, 200, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 3, 220, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25, 0, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 0, 0, 600)