import json

from django.http  import JsonResponse
from django.views import View

from postings.models import Posting
from users.utils     import login_decorator

class PostingView(View) :
    @login_decorator
    def post(self, request) :
        try :
            data = json.loads(request.body)

            title      = data['title']
            content    = data['content']
            posting_id = data.get('posting_id', None)

            if posting_id :
                Posting.objects.filter(id=posting_id).update(title=title, content=content)

                return JsonResponse({'message' : 'update posting'}, status=201)

            Posting.objects.create(title=title, content=content)

            return JsonResponse({'message' : 'create new posting'}, status=201)

        except AttributeError as e :
            return JsonResponse({'message': 'AttributeError'}, status=400)
        
        except TypeError :
            return JsonResponse({'message': 'TypeError'}, status=400)

        except KeyError : 
            return JsonResponse({'message': 'KeyError'}, status=400)
