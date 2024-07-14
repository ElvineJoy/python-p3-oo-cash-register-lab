#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transactions = []

  def add_item(self, item, price, quantity=1):
    for _ in range(quantity):
      self.items.append(item)

    self. total += price * quantity
    self.last_transactions.append({
      'item': item,
      'price': price,
      'quantity': quantity,
      'total': price * quantity
    })

  def apply_discount(self):
    if self.discount:
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f'After the discount, the total comes to ${self.total}.')
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.last_transactions:
      last_transaction = self.last_transactions.pop()
      self.total -= last_transaction['total']
      for _ in range(last_transaction['quantity']):
        self.items.remove(last_transaction['item'])





    