from django.test import TestCase
from models import Post


# Create your tests here.
class PostTests(TestCase):

    """Docstring for PostTests. """
    def test_str(self):
        """TODO: Docstring for test_str.
        :returns: TODO

        """
        my_title = Post(title="This is a basic title for a basic test case")
        self.assertEquals(
            str(my_title), 'This is a basic title for a basic test case',
        )
