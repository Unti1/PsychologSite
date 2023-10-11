from django.db import models
from django import forms
from django.conf import settings

# Create your models here.
class Author(models.Model):
    author_title = models.CharField(max_length=256, default='Иван Иванов')
    phone = models.CharField(max_length=20, default='79999999999')
    validate_number = models.BooleanField(default=False)
    description = models.TextField(max_length=5000, null=True)
    stage = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    profession = models.CharField(max_length=300, null=True)
    amount_reception = models.IntegerField(default=0, null=True)

    def validate_phone_number(self):
        import phonenumbers
        try:
            parsed_number = phonenumbers.parse(self.phone, None)
            if phonenumbers.is_valid_number(parsed_number):
                self.validate_number = True
            else:
                self.validate_number = False
        except phonenumbers.phonenumberutil.NumberParseException:
            self.validate_number = False
    

    def save(self, *args, **kwargs):
        self.validate_phone_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Данные на сайте'

class Order(models.Model):
    phone = models.CharField(max_length=20, default='79999999999', null=True)
    email = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=400, null=True)

    def validate_phone_number(self):
        import phonenumbers
        try:
            parsed_number = phonenumbers.parse(self.phone, None)
            if phonenumbers.is_valid_number(parsed_number):
                self.validate_number = True
            else:
                self.validate_number = False
        except phonenumbers.phonenumberutil.NumberParseException:
            self.validate_number = False

    def email_validate(self): # Допишешь обработку формы
        pass

    def save(self, *args, **kwargs):
        self.validate_phone_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Данные на сайте'

