from django.db import connections
from django.db import models

class InsertData(models.Model):
    url=models.CharField(max_length=200)
    result=models.CharField(max_length=5000)
    context=models.CharField(max_length=5000)
    class Meta:
        db_table="stat"