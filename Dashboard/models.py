from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelBase
import random , string

def generate_string(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField(null=False)
    file_id = models.TextField()

    def create(self, user,name):
        self.user =  user
        self.name = name
        self.file_id = generate_string(32) + ".html"
        self.save()
