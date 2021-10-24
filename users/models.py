from django.db   import models

from core.models import TimesStampModel

class User(TimesStampModel) :
    email        = models.EmailField(max_length=30, unique=True)
    password     = models.CharField(max_length=500)

    class Meta :
        db_table = 'users'