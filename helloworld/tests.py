from django.test import TestCase, RequestFactory
from helloworld.views import HomePageView
from django.contrib.auth.models import User
from models import Task

class HelloWorldTestCase(TestCase):
    fixtures = ['helloworld.yaml', 'users.yaml']
    def setUp(self):
        """ Setup another user to test login """
        self.credentials = {
            'username': 'testuser',
            'email': 'testemail@test.test',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        """ Test Login functionality. User status should be active if loggins with correct credentials """
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
    
    def test_home_page_logged_in(self):
        """ Test correct content is displayed after logging in """
        login = self.client.login(**self.credentials)
        response = self.client.get("/")

        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')

    def test_create_new_task(self):
        """ Test creating a new task saves it in the db """
        login = self.client.login(**self.credentials)
        response = self.client.post("/new", {'name': 'Task 3', 'description': 'Third task'})
        
        new_task = Task.objects.filter(name='Task 3').first()
        self.assertEqual(new_task.description, 'Third task')

    def test_edit_own_task(self):
        """ Test editing own task should result in updating db record """
        self.client.force_login(User.objects.filter(id=1).first())
        response = self.client.post("/edit/1dd22ae1-8aad-4378-be74-9b7dbedd9ae9", {'name': 'Critical task new', 'description': 'This is very urgent'})
        self.assertEqual(response.status_code, 302)
        
        task = Task.objects.filter(uuid='1dd22ae1-8aad-4378-be74-9b7dbedd9ae9').first()
        self.assertEqual(task.name, 'Critical task new')

    def test_edit_other_users_task(self):
        """ Test editing other user's task results in an unsucesfull request """
        self.client.force_login(User.objects.filter(id=2).first())
        response = self.client.post("/edit/1dd22ae1-8aad-4378-be74-9b7dbedd9ae9", {'name': 'Critical task new', 'description': 'This is very urgent'})
        self.assertEqual(response.status_code, 404)

    def test_mark_task(self):
        self.client.force_login(User.objects.filter(id=1).first())
        response = self.client.get("/mark/1dd22ae1-8aad-4378-be74-9b7dbedd9ae9")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(uuid='1dd22ae1-8aad-4378-be74-9b7dbedd9ae9').first().status)

    def test_delete_own_task(self):
        self.client.force_login(User.objects.filter(id=1).first())
        response = self.client.post("/delete/1dd22ae1-8aad-4378-be74-9b7dbedd9ae9")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(uuid='1dd22ae1-8aad-4378-be74-9b7dbedd9ae9').first().deleted)

    def test_delete_other_users_task(self):
        self.client.force_login(User.objects.filter(id=2).first())
        response = self.client.post("/delete/1dd22ae1-8aad-4378-be74-9b7dbedd9ae9")
        self.assertEqual(response.status_code, 404)
        self.assertFalse(Task.objects.filter(uuid='1dd22ae1-8aad-4378-be74-9b7dbedd9ae9').first().deleted)
