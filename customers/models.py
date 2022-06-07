from django.db import models


# Create your models here.

class People(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)
    user_Address = models.ForeignKey("Address", on_delete = models.CASCADE, default = 1)
    user_doc = models.ForeignKey("Doctor", on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.first_name

class Address(models.Model):
    Home_Address = models.CharField(max_length = 500)
    State = models.CharField(max_length = 100, default = 1)
    Country = models.CharField(max_length = 70)
    Telephone = models.CharField(max_length = 70, default = 1)

    def __str__(self):
       return str(self.State)

class Doctor(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)
    office_address = models.CharField(max_length = 100)

    def __str__(self):
       return str(self.first_name)
     

class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    product_maker = models.CharField(max_length = 50)
    product_price = models.CharField(max_length = 50)
    product_country = models.CharField(max_length = 10)

    def __str__(self):
        return self.product_name

class Bio(models.Model):
    user_profile = models.OneToOneField(People, on_delete=models.CASCADE)
    profession = models.CharField(max_length = 50)
    nationality = models.CharField(max_length = 50)
    degree = models.CharField(max_length = 50)
    user_email = models.EmailField(max_length=200)

    def __str__(self):
        return str(self.user_profile)