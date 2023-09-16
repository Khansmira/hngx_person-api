from django.db import models

class person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.email + ' ' + self.gender + ' ' + self.address
