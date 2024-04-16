
import random

import datetime


class BasicAccount():
    """
    This class generates Basic Account, to open account it needs account name
    and opening balance amount.
    """
    # The number of account number is zero.
    acNumm = 0
    
    # Intializing the class
    def __init__(self,name,opening_balance): 

        self.account_name = str(name) 

        self.balance = float(opening_balance)

        BasicAccount.acNumm += 1

        self.acNum = BasicAccount.acNumm

        self.overdraft = False

    
    # String representation of the class
    def __str__(self):
        """
        Returns account holder name along with balance.
        """
        return "Account_name : {self.account_name}\nBalance : {self.balance}\noverdraft : {self.overdraft}".format(self=self)

    # Method for depositing the money in the bank account
    def deposit(self,amount):
        """
        Increase the initial balance of the account.

        Parameters:
          amount - the amount needs to be deposited

        Returns:
          None

        """
        if amount<0:

            print('Please enter a positive amount')

        else:

            self.balance += float(amount)
    
    # Method for withdrawing the amount from the account
    def withdraw(self,amount):
        """
        Withdraws the amount and updates the balance

        Parameters: 
          amount - the amount needs to be withdrawn
        
        Returns:
          None

        """
        if amount > self.balance:

            print(f"Can not withdraw £{amount}.")

        else:

            print(f"{self.account_name} has withdrawn £{amount}.New balance is £{self.balance - float(amount)} ")

            self.balance -= float(amount)
    
    # Method for getting the balance
    def getAvailableBalance(self):
        """
        Returns available balance

        Parameters:
          None
        
        Returns:
          float - the balance of the acoount

        """
        return float(self.balance)
    
    def getBalance(self):
        """
        Returns available balance

        Parameters:
          None
        
        Returns:
          float - the balance of the account.
        """
        return float(self.balance)
    
    def printBalance(self):
        """
        Prints the balance of the account

        Parameters:
          None
        
        Returns:
          None
        """
        print(f"Your account has £{self.balance}")
    
    def getName(self):
        """
        Returns the account holder name

        Parameters:
          None
        
        Returns:
          string - account holder's name
        """
        return str(self.account_name)
    
    def getAcNum(self):
        """
        Returns the account number of the account

        Parameters:
          None
        
        Returns:
          string - account number
        """
        return str(self.acNum)
    
    def issueNewCard(self):
        """
        Issue a new card to the account holder

        Parameteres:
          None
        
        Returns:
          None
        """
        self.cardNum = cardNumgenerator()
        self.cardExp = cardExpgenerator() 
        
    # Method for closing the account   
    def closeAccount(self):
        """
        Closes the account if there is no overdraft

        Parameters:
          None
        
        Returns:
          boolean - True if the account is closed, otherwise False
        """

        if self.balance >= 0:

            self.withdraw(self.balance)

            return True

        else:

            print("Can not close account because you have overdraft amount.")

            return False

    
class PremiumAccount(BasicAccount):
    """
    Premium Account is Basic Account with overdraft facility.
    """
    
    def __init__(self, name, opening_balance,initialOverdraft):
        """Intialize the attributes of parent class."""

        super().__init__(name, opening_balance)

        self.overdraftLimit = float(initialOverdraft)

        self.overdraft = True
    
    def __str__(self):
        return "Account_name : {self.account_name}\nBalance : {self.balance}\noverdraft : {self.overdraftLimit}".format(self=self)

    def withdraw(self,amount):
        """
        Withdraws the account with inputed amount and updates the balance and overdraft limit.

        Parameters:
          amount: the amount to be withdrawn
        
        Returns:
          Nothing
        """

        if self.balance<0:

            if amount > (self.overdraftLimit):

                print(f"Can not withdraw £{amount}.")

            else:

                self.overdraftLimit =- float(amount)

                self.balance -= float(amount)

                print(f"{self.account_name} has withdrawn £{amount}.New balance is £{(self.overdraftLimit)}")
        else:

            if amount > (self.balance + self.overdraftLimit):

                print(f"Can not withdraw £{amount}.")

            else:

                if amount <= self.balance:

                    self.balance -= float(amount)
                else:

                    difference = float(amount - self.balance)

                    self.overdraftLimit -= difference

                    self.balance = -difference

            print(f"{self.account_name} has withdrawn £{amount}.New balance is £{(self.overdraftLimit)}")

    
    def getAvailableBalance(self):
        """
        Returns the available balance including overdraft.

        Parameters:
          None
        
        Returns:
          float - the balance of the account
        """

        if self.balance<=0:

            return float(self.overdraftLimit)

        else:

            return float(self.balance + self.overdraftLimit)

    
    def getBalance(self):
        """
        Returns the balance.

        Parameters:
          None

        Returns:
          float - the balance of the account
        """
        return float(self.balance)

    
    def printBalance(self):
        """
        Prints the balance in the account along with overdraft limit.

        Parameters:
          None
        
        Returns:
          Nothing
        """
        print(f"Your account has £{self.balance} and overdraft limit is £{self.overdraftLimit}.")

    def setOverdraftLimit(self,newLimit):
        """
        Sets a new overdraft limit for the account.

        Parameter:
          float - the new overdraft limit
        
        Returns:
          Nothing
        """
        self.overdraftLimit = float(newLimit)
    
    def closeAccount(self):
        """
        Close the account if the account is not overdrawn.

        Parameters:
          None
        
        Returns:
          boolean - True if account closes, False otherwise
        """
        if self.balance >= 0:

            self.withdraw(self.balance)

            return True
        else:

            print("Can not close account because you have overdraft amount.")
            
            return False


def cardNumgenerator():
    """
    Generates the credit card number

    Parameter:
      None
    
    Returns:
      string - 16 digits credit card number
    """
    credit_card = []
    for i in range(16):
        credit_card_random = random.randint(0,9)
        credit_card.append(credit_card_random)
    return ''.join(str(number) for number in credit_card)

def cardExpgenerator():
    """
    Generates expiry date for the credit card number

    Parameter:
      None
    
    Returns:
     tuple - month and year of credit card expiry
    """
    card_exp_number = datetime.datetime.now() + datetime.timedelta(days=3*365)
    return (int(card_exp_number.strftime("%m")),int(card_exp_number.strftime("%y")))



