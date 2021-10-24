import json
import re
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View

from users.models    import User
from wanted.settings import (
    ALGORITHMS,
    SECRET_KEY
)

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

        except AttributeError :
            return JsonResponse({'message' : 'ATTRIBUTE ERROR'}, status=400)

        except User.DoesNotExist :
            return JsonResponse({'message' : 'USER MATCHING QUERY DOES NOT EXIST'}, status=400)

class UserSignInView(View) :
    def post(self, request) :
        try :
            data = json.loads(request.body)

            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email).exists() :
                return JsonResponse({'message':'USER_DOES_NOT_EXIST'}, status=401)

            user = User.objects.get(email=email)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) :
                return JsonResponse({'message' : 'INVALID USER'}, status=401)
            
            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHMS)

            return JsonResponse({'access_token' : access_token}, status=200)

        except KeyError :
            return JsonResponse({'message' : 'KEY ERROR'}, status=400)

        except AttributeError :
            return JsonResponse({'message' : 'ATTRIBUTE ERROR'}, status=400)