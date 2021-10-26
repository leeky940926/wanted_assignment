import json
import bcrypt
from django.http import response
from django.test  import TestCase, Client, client

from users.models import User

class SignUpTest(TestCase) :

    def setUp(self) :
        User.objects.create(email='test@gmail.com', password='test1234!')

    def tearDown(self) :
        User.objects.all().delete()
    
    def test_success_sign_up(self) :
        client = Client()
        user = {
            'email'    : 'test@test.com',
            'password' : 'test1234!'
        }

        response = client.post('/users/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),{
            'message' : 'Success'
        })
    
    def test_success_sign_up_duplicated_email_error(self) :
        client = Client()
        user = {
            'email'    : 'test@gmail.com',
            'password' : 'test1234!'
        } 

        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(), {
            'message' : 'EMAIL ALREADY EXISTS'
        })

    def test_success_sign_up_email_regular_expression_validation_error(self) :
        client = Client()
        user = {
            'email'    : 'test',
            'password' : 'test1234!'
        }

        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'EMAIL VALIDATION ERROR'
        })
    
    def test_success_sign_up_password_regular_expression_validation_error(self) :
        client = Client()
        user = {
            'email'    : 'test@test.com',
            'password' : '132'
        }

        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'PASSWORD VALIDATION ERROR'
        })
    
class SigninTest(TestCase) :

    def setUp(self) :
        User.objects.create(email='test@gmail.com', password=bcrypt.hashpw('test1234!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'))
    
    def tearDown(self) :
        User.objects.all().delete()
    
    def test_success_sign_in_success(self) :
        client = Client()
        login_info = {
            'email'    : 'test@gmail.com',
            'password' : 'test1234!'
        }

        response = client.post('/users/signin', json.dumps(login_info), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            'access_token' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.zZ8gW9Xqg2Qy4ilOjv1iQWM-XqpaU-AVgVfz7FkUzfQ'
        })
    
    def test_success_sign_in_email_not_exist_error(self) :
        client = Client()
        login_info = {
            'email'    : 'dddd',
            'password' : 'test1234!'
        }

        response = client.post('/users/signin', json.dumps(login_info), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{
            'message' : 'USER_DOES_NOT_EXIST'
        })