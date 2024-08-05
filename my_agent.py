__author__ = "<your name>"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "<your e-mail>"

import numpy as np

agentName = "<your agent name>"

class RajAgent():
   """
             A class that encapsulates the code dictating the
             behaviour of the agent playing the game of Raj.

             ...

             Attributes
             ----------
             item_values : list of ints
                 values of items to bid on
             card_values: list of ints
                 cards agent bids with

             Methods
             -------
             AgentFunction(percepts)
                 Returns the card value from hand to bid with
             """

   def __init__(self, item_values, card_values):
      """
      :param item_values: list of ints, values of items to bid on
      :card_values: list of ints, cards agent bids with
      """

      self.card_values = card_values
      self.item_values = item_values

   
   def MiniMax(self, percepts, depth):
      # base case
      if(depth == 5):
        print(percepts[2])
        return percepts[2][0]
      else:
        self.MiniMax(percepts, depth + 1)
         
      

   def AgentFunction(self, percepts):

      # Extract different parts of percepts.
      bidding_on = percepts[0]
      items_left = percepts[1]
      my_cards = percepts[2]
      bank = percepts[3]
      opponents_cards = percepts[4:]
      # Currently this agent just bids the first card in its hand - you need to make it smarter!
      action = self.MiniMax(percepts, 5)
      # Return the bid
      return action