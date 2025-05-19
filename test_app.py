import unittest
from app import app

class TestTodoAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()  

    def test_update_task_gui(self):
        self.client.post('/add', data={'task': 'Original'})
        self.client.post('/update/0', data={'updated_task': 'Edited'})
        response = self.client.get('/')
        self.assertIn(b'Edited', response.data)

    def test_add_task(self):
        response = self.client.post('/tasks', json={"title": "Test Task"})
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        self.client.post('/tasks', json={"title": "Task 1"})
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

if __name__ == '__main__':
    unittest.main()
