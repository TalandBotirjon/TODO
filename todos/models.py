from django.db import models
import  datetime
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    tekshirish = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    do_success = models.BooleanField(default=False)

    def __str__(self):
        return self.title


