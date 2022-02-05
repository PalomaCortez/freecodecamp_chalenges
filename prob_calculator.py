"""
This code is related to the Budget App Chalenge. The description of the requirements are on the link bellow.
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator
"""

import copy
import random


"""
first, we need to consider the input that is variable, the **kwargs helps to receive a dictionary that can have a variable lenght.
automatically understands that  'yellow=3' means
'yellow':3.
With list += value * [key] we get
['yellow', 'yellow', 'yellow=3']
I found it a nice slim way in place of a for loop.
"""

class Hat:
  def __init__(self, **kwargs):
    
    self.contents = []
    for key, val in kwargs.items():
      self.contents += val * [key]

  """
  For the draw method, 1st check if the draw number is bigger than the number of balls so the selected balls are a coppy of the hat, the hat gets empty.
  2nd the selected is a random list that needs to be removed from the original one.
  """
  def draw(self, num_balls):
    selected = []
    if num_balls > len(self.contents):
      selected = copy.deepcopy(self.contents)
      
    else:
      selected = random.sample(self.contents,  num_balls)

    for ball in selected:      
      self.contents.remove(ball)
    return selected


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0  # how many times we get the expected_balls
  for event in range(num_experiments):
    event_hat = copy.deepcopy(hat)  
    sample = event_hat.draw(num_balls_drawn)
    # sample = ['green', 'green', 'green', 'red']
    # converting in dictionary for latter comparison
    samples = {}
    
    for color in sample:
      if color not in samples:
        samples[color] = 1
      else:
        samples[color] += 1
        
    """
    In comparing the results, if there is a color in the expected that is not in the samples, a keyError will stop the process.
    """
    success = None
    try:
      for color in expected_balls.keys():
          if samples[color] < expected_balls[color]:
              success = False
              break
          success = True
    except KeyError:
      success = False
          
    if success: M += 1
    if M == 0: probability = 0
    else:
      probability = M/num_experiments
  
  return probability

