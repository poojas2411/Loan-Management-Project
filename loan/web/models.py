from django.db import models
from django_enumfield import enum
# Create your models here.
class status_enum(enum.Enum):
    rejected=0
    Inprogress=1
    Checked=2
    
class userinfo(models.Model):
    loan_type=models.CharField(max_length=50,null=True)
    Bank_name=models.CharField(max_length=50,null=True)
    Account_number=models.BigIntegerField(null=True)
    Bank_ifsc=models.CharField(max_length=50,null=True)
    Aadhaar_no=models.CharField(max_length=50,null=True)
    pancard_number=models.CharField(max_length=50,null=True)
    Address=models.TextField(max_length=100,null=True)
    phone_no=models.IntegerField(null=True)
    Email=models.EmailField(null=True)
    status=enum.EnumField(status_enum,default=status_enum.Inprogress)
    money=models.IntegerField(null=True)
    Aadhaar_card=models.ImageField(upload_to='pics')
    #pan_card=models.ImageField(upload_to='pics')

class Home_loan(models.Model):
    loan_type=models.CharField(max_length=50,null=True)
    Bank_name=models.CharField(max_length=50,null=True)
    Account_number=models.BigIntegerField(null=True)
    Bank_ifsc=models.CharField(max_length=50,null=True)
    Aadhaar_no=models.CharField(max_length=50,null=True)
    pancard_number=models.CharField(max_length=50,null=True)
    Address=models.TextField(max_length=100,null=True)
    phone_no=models.IntegerField(null=True)
    Email=models.EmailField(null=True)
    status=enum.EnumField(status_enum,default=status_enum.Inprogress)
    money=models.IntegerField(null=True)
    Aadhaar_card=models.ImageField(upload_to='pics',null=True,blank=True)
    pan_card=models.ImageField(upload_to='pics',null=True,blank=True)
    def __str__(self):
        return f"{self.loan_type}"

class Car_loan(models.Model):
    loan_type=models.CharField(max_length=50,null=True)
    Bank_name=models.CharField(max_length=50,null=True)
    Account_number=models.BigIntegerField(null=True)
    Bank_ifsc=models.CharField(max_length=50,null=True)
    Aadhaar_no=models.CharField(max_length=50,null=True)
    pancard_number=models.CharField(max_length=50,null=True)
    Address=models.TextField(max_length=100,null=True)
    phone_no=models.IntegerField(null=True)
    Email=models.EmailField(null=True)
    status=enum.EnumField(status_enum,default=status_enum.Inprogress)
    money=models.IntegerField(null=True)
    #Aadhaar_card=models.ImageField(upload_to='pics')
    #pan_card=models.ImageField(upload_to='pics')



class Contact(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    message=models.TextField(null=True)
    def __str__(self):
        return f"{self.name},{self.email}"
class Usefull_links(models.Model):
    link_name=models.CharField(max_length=200,null=True,blank=True)
    link=models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return f"{self.link_name}"
    
class What_we_offer(models.Model):
    Heading=models.CharField(max_length=50,null=True)
    sub_heading=models.TextField(null=True)
    def __str__(self):
        return f"{self.Heading}"