from unittest import TestCase
from hello_world.core import get_message


class HelloworldTestCase(TestCase):
    def test_helloworld(self):
        self.assertEqual(get_message(), 'Hello World!')
