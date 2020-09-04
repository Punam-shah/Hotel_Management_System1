import unittest
from assignment.qry import *


class unit_testing(unittest.TestCase):
    mgt = Check_in()

    def test_add_guest(self):
        result = self.mgt.add('8/30/20-1:10-PM', 'Punam Shah', 'ktm', '+9779874563210', '1', 'Card-15000')
        self.assertTrue(result)


    def test_add_room(self):
        result = self.mgt.add_room('Punam Shah', 101, 'Deluxe')
        self.assertTrue(result)

    def test_update_guest(self):
        result = self.mgt.update('8/30/20-1:10-PM', 'Punam Shah', 'ktm', '+9779874563210', '1', 'Card-15000','8/30/20-1:10-PM')
        self.assertTrue(result)

    def test_update_room(self):
        result = self.mgt.update_room('8/30/20-1:10-PM', 'Punam Shah',  '101', 'Deluxe')
        self.assertTrue(result)



    def test_checkout(self):
        result = self.mgt.check_out('8/30/20-1:10-PM', 'Punam Shah', '118')
        self.assertTrue(result)







