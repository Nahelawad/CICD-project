import unittest
import json
from app import app

class TestTodoAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_task(self):
        response = self.app.post('/tasks', json={"title": "Test Task"})
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        self.app.post('/tasks', json={"title": "Task 1"})
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

if __name__ == '__main__':
    unittest.main()
