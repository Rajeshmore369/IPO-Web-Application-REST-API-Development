from django.db import models

# Create your models here.

class UpcomingIPO(models.Model):
    company_name=models.CharField(max_length=100,unique=True)
    Price_band=models.IntegerField()
    open_date=models.DateTimeField()
    close_date=models.DateTimeField()
    issue_size=models.IntegerField()
    issue_type=models.CharField(max_length=100)
    listing_date=models.DateTimeField()
    status=models.CharField(max_length=100)
action=models.IntegerField()
    
    
    