from django.test import TestCase
from littlelemon.restaurant.views import MenuItemsView

class MyTestCase(TestCase):

    def test_my_view(self):
        # Create an instance of the view
        view = MenuItemsView()

        # Call the view with some arguments
        response = view(request, args, kwargs)

        # Assert that the response is what you expect
        self.assertEqual(response.status_code, 200)