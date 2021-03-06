import json
import unittest
from time import time
from unittest.mock import MagicMock

from mergeit.scripts.server import init_logging


class ResponseMock(MagicMock):

    def __init__(self, data, status_code=200, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = data if isinstance(data, str) else json.dumps(data)
        self.status_code = status_code


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.push_handler_mock = MagicMock()


class MergeitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        init_logging('/tmp/mergeit_test_logs_{}'.format(int(time())), 'foo')
