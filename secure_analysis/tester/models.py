from django.db import models

# Create your models here.
class DTReport(models.Model):
    url= models.URLField()
    is_vulnerable = models.BooleanField(default = False)

class XXEReport (models.Model):
    url= models.URLField()
    is_vulnerable= models.BooleanField(default = False)

class SMisReport (models.Model):
    url= models.URLField()
    is_vulnerable= models.BooleanField(default = False)    
    

class SQLIReport (models.Model):
    url= models.URLField()
    is_vulnerable= models.BooleanField(default = False)     

class    XSSReport (models.Model):
    url= models.URLField()
    is_vulnerable= models.BooleanField(default = False)     
    location = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

class CSRFReport(models.Model):
    url = models.URLField()
    is_vulnerable= models.BooleanField(default = False)
    
class SessionFixReport(models.Model):
    url = models.URLField()
    is_vulnerable= models.BooleanField(default = False)    

class LFIReport(models.Model):
    url = models.URLField()
    is_vulnerable= models.BooleanField(default = False)        
    
    def __str__(self):
        return f"{self.url} - Vulnerable: {self.is_vulnerable}"                 