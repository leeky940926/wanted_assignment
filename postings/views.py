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

    def get(self, request) :
        try :
            offset = int(request.GET.get('offset', 0))
            limit  = int(request.GET.get('limit', 10))

            if limit > 15 :
                return JsonResponse({'message' : 'too much list'}, status=400)
            
            postings = Posting.objects.all()[offset:offset+limit]

            posting_list = [
                {
                    'posting_id' : posting.id,
                    'title'      : posting.title,
                    'content'    : posting.content 
                }
            for posting in postings]

            return JsonResponse({'message' : posting_list}, status=200)

        except AttributeError :
            return JsonResponse({'message': 'AttributeError'}, status=400)
        
        except TypeError :
            return JsonResponse({'message': 'TypeError'}, status=400)
