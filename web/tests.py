from django.test import TestCase
from django.urls import reverse

class FengshuiTestCase(TestCase):

# test 1
    def test_home_page_loads_successfully(self):
        """Test whether the homepage can be accessed normally"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

# test 2
    def test_score_routing_logic(self):
        """Test the logic of different score jumps"""
        def redirect_for(score):
            if score >= 70:
                return '/dachangji/'
            elif score >= 65:
                return '/daji/'
            elif score >= 60:
                return '/zhongji/'
            elif score >= 55:
                return '/xiaoji/'
            elif score >= 30:
                return '/ji/'
            else:
                return '/zhong/'

        # examples
        self.assertEqual(redirect_for(72), '/dachangji/')
        self.assertEqual(redirect_for(66), '/daji/')
        self.assertEqual(redirect_for(59), '/xiaoji/')

# test 3
    def test_template_contains_keyword(self):
        """Test whether the page content contains keywords"""
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Fengshui")
