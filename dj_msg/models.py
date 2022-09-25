
from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email_address = models.EmailField()
    message = models.TextField()
    
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = "Contact"
        # fields = ("first_name","last_name","email","messasge")