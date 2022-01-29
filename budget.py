"""
This code is related to the Budget App Chalenge. The description of the requirements are on the link bellow.
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
"""


class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0.00
        self.ledger = []
    
    def __repr__(self):
      spacer = ((15-(int(len(self.name)/2)))*'*')
      top = f"{spacer}{self.name}{spacer}"
      body = self.get_ledger()
      bottom = f"Total: {self.balance}"
      return f"{top}\n{body}{bottom}"

        
    def get_balance(self):
        return self.balance

    
    def check_funds(self, amount):
        self.amount = 0.00
        if self.balance >= amount:
            return True
        else:
            return False
 

    def deposit(self, amount, description=""):
        self.amount = 0.00
        self.balance += float("{0:.2f}".format(amount))
        self.description = ""
        self.ledger.append({"amount": float("{0:.2f}".format(amount)), "description": description})

        
    def withdraw(self, amount, description=""):
        self.amount = 0.00
        if self.check_funds(amount) == True:
            self.balance += -1*float("{0:.2f}".format(amount))
            self.description = ""
            self.ledger.append({"amount": float("-{0:.2f}".format(amount)), "description": description})
            return True
        return False

        
    def transfer(self, amount, other):
        if self.check_funds(amount) == True:
            description_to = f"Transfer to {other.name}"
            description_from = f"Transfer from {self.name}"
            self.withdraw(amount, description_to)
            other.deposit(amount, description_from)
            return True
        return False
        
    def get_ledger(self):
        ldg = ""
        for i in range(len(self.ledger)):
            value = format(self.ledger[i]['amount'],'.2f')
            ledger_line = f"{self.ledger[i]['description'][:23]:<23}"f"{value:>7}\n"
            ldg += ledger_line
        return ldg



def create_spend_chart(categories):

  # getting withdraws values and percentages
  expenses = {}
  total = 0
  for categ in categories:
    c_exp = 0
    for item in categ.ledger:
      value = item['amount']
      if value < 0:
        c_exp += -value
    expenses[categ.name] = c_exp
    total += c_exp
  for key, value in expenses.items():
    expenses[key] = (value/total)*100  
 
  top_chart = "Percentage spent by category\n"
  for p in range(100, -1, -10):
      top_chart += f"{str(p)+'|':>4}"
      for perc in expenses.values():
        if perc >= p:
          top_chart += " o "
        else:
          top_chart += "   "  # very necessary to get the percentages in the correct order.
      top_chart += " \n"  # need to have an space before new line to complete the spacings
  
  x_axis = ('-'*(3*len(categories)+1))

  print(expenses.keys())
  # Extenting the names length so we get the correct labels.
  size = (len(max(expenses.keys(), key=len)))
  labels = [names.ljust(size) for names in expenses.keys()]
  
  """"
  Spliting the letters on the formated string:
  One way of doing it is with an while loop. 
  However, the writting bellow avoids it.
  Important! There is a need of spacing before the newline to complete the spacings required
  """
  botton_chart= ""
  for name in zip(*labels):
    botton_chart += f"     {'  '.join(name)}  \n"
      

  # There is a final error, we need to remove an extra line.
  fullchart = (f"{top_chart}    {x_axis}\n{botton_chart}").rstrip('\n')
  return (fullchart)
  


