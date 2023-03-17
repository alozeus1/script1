import unittest
from flask import Flask

class TestWordsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_words_endpoint(self):
        response = self.client.get('/words')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'This is the words endpoint')

if __name__ == '__main__':
    unittest.main()
