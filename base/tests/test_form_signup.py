"""Reference: https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html
"""

from django.test import TestCase

from base.forms import SignupForm


class SignupFormTests(TestCase):
    """Test for signup form
    """

    def test_form_has_fields(self):
        """Test signup form has fields
        """
        form = SignupForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)
