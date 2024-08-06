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

   
   """
      Where we are at the moment:
      - the minimax goes to the bottom and simply returns the bank value
      - now we need a way to remove cards from the lists to proerly simulate the game being played
      - each time min places a card we need to update the bank value so that we can rank the game
      - also need to handle negative inputs
      - i reckon i convert the lists of turns into mutable lists i can remove items from then the game can be properly simulated
      """
   def MiniMax(self, percepts, bidding_on, items_left, my_cards, opponents_cards, bank, state, depth, Maxturn):
        if(depth == 0):
            # bank is how you evaluate the state of the game
            print(bank)
            return bank
        if(Maxturn):
           maxEval = float('-inf')
           for card in my_cards:
              if(card == state): continue
              state = card
              tempVal = self.MiniMax(percepts, bidding_on, items_left, my_cards, opponents_cards, bank, state, depth - 1, False)
              maxEval = max(maxEval, tempVal)
           return maxEval
        else:
           minEval = float('inf')
           for card in opponents_cards:
              tempVal = self.MiniMax(percepts, bidding_on, items_left, my_cards, opponents_cards, bank, state, depth - 1, True)
              minEval = min(minEval, tempVal)
           return minEval

   def AgentFunction(self, percepts):
      # Extract different parts of percepts.
      bidding_on = percepts[0]
      items_left = percepts[1]
      my_cards = percepts[2]
      bank = percepts[3]
      opponents_cards = percepts[4:]
    #   print(percepts)
    #   print("BANK")
    #   print(bank)
    #   print(bidding_on)
    #   print(items_left)
    #   print(my_cards)
    #   print(opponents_cards)
      action = my_cards[0]
      bestMove = float('-inf')
      for card in my_cards:
         newBank = self.MiniMax(percepts, bidding_on, items_left, my_cards, opponents_cards, bank, card, len(opponents_cards), False)
         if(newBank > bestMove):
            print(card)
            print(newBank)
            action = card
            bestMove = newBank
      return action