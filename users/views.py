import json
import re
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View

from users.models import User

class UserSignUpView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']

            email_validation    = re.compile("^[a-zA-Z0-9+-_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
            password_validation = re.compile("^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%*^&+=]).*$")

            if not email_validation.match(email) :
                return JsonResponse({'message' : 'EMAIL VALIDATION ERROR'}, status=400)

            if User.objects.filter(email = email).exists() :
                return JsonResponse({'message' : 'EMAIL ALREADY EXISTS'}, status=400)
            
            if not password_validation.match(password) :
                return JsonResponse({'message' : 'PASSWORD VALIDATION ERROR'}, status=400)

            hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decoded_password = hashed_password.decode('utf-8')

            User.objects.create(
                email    = email,
                password = decoded_password
            )

            return JsonResponse({'message' : 'Success'}, status=201)

        except KeyError :
            return JsonResponse({'message' : 'KEY ERROR'}, status=400)

        except User.DoesNotExist :
            return JsonResponse({'message' : 'USER MATCHING QUERY DOES NOT EXIST'}, status=400)