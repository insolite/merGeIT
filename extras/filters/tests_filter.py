import unittest
from runner import Filter


class TestsFilter(Filter):

    def run(self, source_match, source_branch, target_branch):
        all_tests = unittest.TestLoader().discover(self.push_handler.config['path'], pattern='*.py')
        unittest.TextTestRunner().run(all_tests)