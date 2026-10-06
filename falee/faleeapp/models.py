from django.db import models
from django.contrib import admin
class service_DB(models.Model):
    Seriel_No=models.CharField(primary_key=True)
    Name=models.CharField(max_length=10)
    DoB=models.DateField()
    Address=models.TextField()
    Mobile=models.IntegerField()
    Vechicle=models.CharField()
    Received_Date=models.DateField()
class service_DBAdmin(admin.ModelAdmin):    
    list_display=["Seriel_No","Name", "DoB","Address","Mobile","Vechicle","Received_Date"]
