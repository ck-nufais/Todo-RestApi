from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    text = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todos")
    def __str__(self):
        return self.text