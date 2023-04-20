import unittest
from bs4 import BeautifulSoup
from web import app


class TestTemplateRendering(unittest.TestCase):

    def setUp(self):
        # Create a test client to make HTTP requests to the Flask app
        self.client = app.test_client()

    def test_home_template(self):
        # Send a GET request to the home page and check for a 200 OK status code
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Parse the response HTML using Beautiful Soup
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check that the correct title is present
        title_tag = soup.find('title')
        self.assertEqual(title_tag.string.strip(), 'TIMELY')

        # Check that the current user's name and location are present
        profile_name = soup.find(class_='profile-name')
        self.assertIsNotNone(profile_name)
        profile_location = soup.find(class_='profile-location')
        self.assertIsNotNone(profile_location)

        # Check that at least one friend card is present
        friend_card = soup.find(class_='friend-card')
        self.assertIsNotNone(friend_card)

    def test_overlaps_template(self):
        # Send a GET request to the overlaps page and check for a 200 OK status code
        # Replace with appropriate URL and/or parameters if required
        response = self.client.get('/overlaps')
        self.assertEqual(response.status_code, 200)

        # Parse the response HTML using Beautiful Soup
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check that the correct title is present
        title_tag = soup.find('title')
        self.assertEqual(title_tag.string.strip(), 'TIMELY: Friend')

        # Check that the current user's and selected user's names are present
        current_user_name = soup.find_all(class_='text-medium')[0]
        self.assertIsNotNone(current_user_name)
        selected_user_name = soup.find_all(class_='text-medium')[1]
        self.assertIsNotNone(selected_user_name)

        # Check that the timetable is present
        timetable = soup.find(class_='timetable')
        self.assertIsNotNone(timetable)

    def test_settings_template(self):
        # Send a GET request to the settings page and check for a 200 OK status code
        response = self.client.get('/settings')
        self.assertEqual(response.status_code, 200)

        # Parse the response HTML using Beautiful Soup
        soup = BeautifulSoup(response.data, 'html.parser')

        # Check that the correct title is present
        title_tag = soup.find('title')
        self.assertEqual(title_tag.string.strip(), 'TIMELY: Settings')

        # Check that the personal information form is present
        personal_info_form = soup.find(class_='settings-form')
        self.assertIsNotNone(personal_info_form)

        # Check that the add friend form is present
        friend_form = soup.find(class_='friend-form')
        self.assertIsNotNone(friend_form)


if __name__ == '__main__':
    unittest.main()
