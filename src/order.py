BUYSELL_ORDER  = "timestamp|order id|action|ticker|side|price|size"
MODIFY_ORDER = "timestamp|order id|action|size"

class BaseOrder:
    def __init__(self, timestamp:int, order_id:int, action:str, size:int):
        self.timestamp = timestamp
        self.order_id = order_id
        self.action = action
        self.size = size

    def is_valid(self):
        return self.size > 0

class AmendOrder(BaseOrder):
    pass


class AddOrder(BaseOrder):
    def __init__(self, ts: int, order_id:int , ticker:str,  price:float, size: int):
        super().__init__(ts, order_id, 'a', size)
        self.ticker = ticker
        self.price = price

    def is_valid(self):
        return super().is_valid() and self.price > 0


class SellOrder(AddOrder):
    def __repr__(self):
        return f'Order value: ts:{self.ts}|price:{self.price}|id:{self.id}'

    def __lt__(self, other):
      if self.price == other.price:
        return self.ts < other.ts
      return self.price < other.price

class BuyOrder(AddOrder):
    def __lt__(self, other):
        if self.price == other.price:
            return self.ts < other.ts
        return self.price > other.price
        return self.price > other.price and self.ts < other.ts

def from_string(input:str) -> Order :
    fields = input.split('|')
    if len(fields) == 4:
        action = fields[2]

        return ModifyOrder(int(fields[0]),
                           int(fields[1]),
                            fields[2],
                           int(fields[3])) if action == 'u' \
        else CancelOrder(int(fields[0]),
                           int(fields[1]),
                            fields[2],
                           int(fields[3]))
    else:
        side = fields[4]

        return BuyOrder(fields[0],
                           int(fields[1]),
                           fields[3],
                           float(fields[5]),
                           int(fields[6])) if side == 'B' else \
               SellOrder(fields[0],
                           int(fields[1]),
                           fields[3],
                           float(fields[5]), # handle the float precision
                           int(fields[6]))

