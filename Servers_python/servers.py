#!/usr/bin/python
# -*- coding: utf-8 -*-
#Michal Welna 302935

from typing import Optional, List, Dict
from abc import ABC, abstractmethod
import re


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price



class TooManyProductsFoundError(Exception):
    pass


class Server(ABC):
    def __init__(self, product_list: List[Product]):
        self.product_list = product_list

    def list_to_dict(self) -> Dict[str,Product]:
        dict_prod = {}
        for product in self.product_list:
            dict_prod[product.name] = product
        return dict_prod

    n_max_returned_entries = 3

    @abstractmethod
    def get_searched_products(self, n: int = 1):
        pass


class ListServer(Server):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_searched_products(self, n :int) -> List[Product]:
        list_products = []
        for prod in self.product_list:
            letters = re.split('(\d+)', prod.name)[0]
            numbers = re.split('(\d+)', prod.name)[1]
            if len(letters) == n and 2<=len(numbers)<=3:
                list_products.append(prod)
        if len(list_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError
        if not list_products:
            return list_products
        return sorted(list_products, key = lambda product: product.price)


class MapServer(Server):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_prod = self.list_to_dict()

    def get_searched_products(self, n: int) -> List[Product]:
        list_products = []
        for name in self.dict_prod.keys():
            letters = re.split('(\d+)', name)[0]
            numbers = re.split('(\d+)', name)[1]
            if len(letters) == n and 2<=len(numbers)<=3:
                list_products.append(self.dict_prod[name])
        if len(list_products) > self.n_max_returned_entries:
            raise TooManyProductsFoundError
        if list_products is []:
            return list_products
        return sorted(list_products, key = lambda product: product.price)



class Client:
    def __init__(self, server : Server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            searched_products = self.server.get_searched_products(n_letters)
            if not searched_products:
                return None
        except TooManyProductsFoundError:
            return None


        total_price = 0
        for prod in searched_products:
            total_price+=prod.price

        return total_price
