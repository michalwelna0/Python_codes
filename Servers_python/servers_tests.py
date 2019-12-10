#!/usr/bin/python
# -*- coding: utf-8 -*-
#Michal Welna 302935

import unittest
from collections import Counter

from servers import Server, ListServer, Product, Client, MapServer, TooManyProductsFoundError

server_types = (ListServer, MapServer)


class ServerTest(unittest.TestCase):

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))


class ClientTest(unittest.TestCase):

    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))


class TooManyProductsTest(unittest.TestCase):

    def test_raise_error(self):
        products = [Product('PP234',2), Product('PP235',3),Product('PP236',4),Product('PP237',5)]
        for server_type in server_types:
            server = server_type(products)
            with self.assertRaises(TooManyProductsFoundError):
                prods = server.get_entries(2)


class CheckIfSorted(unittest.TestCase):

    def test_IfSorted(self):
        products = [Product('PP234',500), Product('PP235',520), Product('PP236',30)]
        for server_type in server_types:
            server = server_type(products)
            prods = server.get_entries(2)
            self.assertEqual([products[2],products[0],products[1]],prods)

class CheckIfisNoneinListServer(unittest.TestCase):

    def test_None_If_tooMany(self):
        products = [Product('PP234', 2), Product('PP235', 3), Product('PP236', 4), Product('PP237', 5)]
        server = ListServer(products)
        client = Client(server)
        prod = client.get_total_price(2)
        self.assertEqual(prod,None)

    def test_None_If_not_enough(self):
        products = []
        server = ListServer(products)
        client = Client(server)
        prod = client.get_total_price(2)
        self.assertEqual(prod, None)

class CheckIfisNoneinMapServer(unittest.TestCase):

    def test_None_If_tooMany(self):
        products = [Product('PP234', 2), Product('PP235', 3), Product('PP236', 4), Product('PP237', 5)]
        server = MapServer(products)
        client = Client(server)
        prod = client.get_total_price(2)
        self.assertEqual(prod,None)

    def test_None_If_not_enough(self):
        products = []
        server = MapServer(products)
        client = Client(server)
        prod = client.get_total_price(2)
        self.assertEqual(prod, None)


class NotEnoughProductsTest(unittest.TestCase):

    def test_return_emptyList_fromListServer(self):
        products = []
        prod = ListServer(products)
        emptylist = prod.get_entries(2)
        self.assertEqual(emptylist,[])

    def test_return_emptyList_fromMapServer(self):
        products = []
        prod = MapServer(products)
        emptylist = prod.get_entries(2)
        self.assertEqual(emptylist,[])




if __name__ == '__main__':
    unittest.main()