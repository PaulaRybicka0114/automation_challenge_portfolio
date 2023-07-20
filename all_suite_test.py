import unittest

from unittest.loader import makeSuite
pip
from test_cases.login_to_the_system import TestLoginPage
from test_cases.add_a_player_tc import TestDashboard
from test_cases.add_a_player_tc import TestPlayerForm

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestDashboard))
   test_suite.addTest(makeSuite(TestPlayerForm))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())