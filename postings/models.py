from django.db   import models

from core.models import TimesStampModel

class Posting(TimesStampModel) :
    title = models.CharField(max_length=20)
    content = models.TextField()

    class Meta :
        db_table = 'postings'