import json
from django.http import response
from django.test     import TestCase, Client

from postings.models import Posting
from users.models    import User
  
class PostingTest(TestCase) :
    def setUp(self) :
        user = User.objects.create(email="test@test.gmail.com", password="test1234!")
        Posting.objects.bulk_create([Posting(user_id=user.id ,title=f'{i}'+'번째 title', content=f'{i}'+'번째 content') for i in range(11)])
    
    def tearDown(self) :
        User.objects.all().delete()
        Posting.objects.all().delete()
    
    def test_posting_create_success(self) :
        client = Client()

        headers = {'HTTP_Authorization' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.zZ8gW9Xqg2Qy4ilOjv1iQWM-XqpaU-AVgVfz7FkUzfQ'}
  
        posting = {
            'title'   : "unit test title",
            'content' : "unit test content",
        }

        response = client.post('/postings', json.dumps(posting), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), 
            {
                'message' : 'create new posting'
            }
        )
    
    def test_posting_create_key_error(self) :
        client = Client()

        headers = {'HTTP_Authorization' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.zZ8gW9Xqg2Qy4ilOjv1iQWM-XqpaU-AVgVfz7FkUzfQ'}
  
        posting = {
            'titt' : "title key error",
            'content' : 'title key error content'
        }

        response = client.post('/postings', json.dumps(posting), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'KeyError'
        })

    def test_posting_get_list(self) :
        client = Client()

        response = client.get('/postings')
        self.assertEqual(response.status_code, 200)

    def test_posting_patch_success(self) :
        client = Client()

        headers = {'HTTP_Authorization' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.zZ8gW9Xqg2Qy4ilOjv1iQWM-XqpaU-AVgVfz7FkUzfQ'}
  
        posting = {
            'title'   : 'patch title',
            'content' : 'patch content',
        }

        response = client.patch('/postings/3', json.dumps(posting), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),{
            'message' : 'update posting'
        })
    
    def test_posting_delete_success(self) :
        client = Client()

        headers = {'HTTP_Authorization' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.zZ8gW9Xqg2Qy4ilOjv1iQWM-XqpaU-AVgVfz7FkUzfQ'}

        response = client.delete('/postings/2', **headers)

        self.assertEqual(response.status_code,201)
        self.assertEqual(response.json(),{
            'message' : 'Delete Success'
        })

    def test_posting_delete_decode_error(self) :
        client = Client()

        headers = {'HTTP_Authorizations' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.zZ8gW9Xqg2Qy4ilOjv1iQWM-XqpaU-AVgVfz7FkUzfQ'}

        response = client.delete('/postings/8', **headers)
        
        self.assertEqual(response.status_code,401)
        self.assertEqual(response.json(),{
            'message' : 'DECODE ERROR'
        })