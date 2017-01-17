# The below models Bank Enviroment where transactions like withdraw, deposit, etc occur
class BankAcc():
  def deposits():
    pass
  
  def withdraws():
    pass
  
class SavingsAccount(BankAcc):
  def __init__(self):
    self.balance = 1750
    
def withdraws(self,amount):
      if type(amount) == int and amount != "":
        if amount > 0:
          if (self.balance-amount) > 0:
            if (self.balance -amount) > 200:
              self.balance-=amount
              return self.balance
            else:
              return 'Sorry, you cannot withdraw beyond the minimum balance in your account '
          else:
            return 'Sorry, you cannot withdraw beyond the current balance in your account '
        else:
          return 'Invalid withdraw amount'
      else:
        raise ValueError()
  
def deposits(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid deposit amount'

    else:
      raise ValueError()

 
      
class CurrentAccount(BankAcc):
  def __init__(self):
    self.balance = 0
    
  def withdraws(self,amount):
    if type(amount) ==  int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:

          self.balance-=amount
          return self.balance

        else:
          return 'Sorry, you cannot withdraw beyond the current balance in your account '
      else:
        return 'Invalid withdraw amount'
    else:
      raise ValueError()
      
  def deposits(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid deposit amount'

    else:
      raise ValueError()

  