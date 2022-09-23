from .order import AddOrder, AmendOrder, BaseOrder, BuyOrder, SellOrder ,from_string
from heapq import  heappush, heappop

import logging

class Book:

    def __init__(self, ticker):
        self.buy_orders = []
        self.sell_orders = []
        self.order_ids = []

    def contains_order(self, order:BaseOrder) -> bool:
        return self.order_ids.contains(order.order_id)

    def process_order(self, order:BaseOrder) -> None:
        if isinstance(order, AmendOrder):
            self._handle_amend(order)
        else:
            self._handle_add(order)

    def _handle_amend(self, order):
        if order.action == 'c':
            self._cancel_order(order)
        else:
            self._amend_order(order)

    def _cancel_order(self, order):
        pass

    def _amend_order(self, order):
        pass

    def _handle_buysell(self, order:AmendOrder):

        holder = self.buy_orders if isinstance(order, BuyOrder) \
                    else self.sell_orders
        heappush(holder, order)

    def get_best_bid(self):
        return self.buy_orders.nsmallest(1)

    def get_best_ask(self):
        return self.sell_orders.nsmallest(1)


class OrderBook:
    def __init__(self):
        self.books = {}

    def process_order(self, input_str:str)  -> None:
        try:
            order = from_string(input_str)
            if order.is_valid():
                if isinstance(order, AmendOrder):
                    self.process_amend(order)
                else:
                    self.process_add(order)
        except Exception :
            logging.info(f'Cannot handle {input_str}')

    def process_add(self, order:AddOrder) -> None:
        ticker = order.ticker
        if ticker not in self.books.keys():
            ticker_book = OrderBook()
            self.books[ticker] = ticker_book
            
        self.books.get(ticker).process_order(order)

    def process_amend(self, order:BaseOrder) -> None:
        for book in self.books.values():
            if book.contains(order.order_id):
                book.process_order(order)
                return

    def get_best_bid(self, ticker):
        return self.books[ticker].get_best_bid()

    def get_best_ask(self, ticker):
        return self.books[ticker].get_best_ask()