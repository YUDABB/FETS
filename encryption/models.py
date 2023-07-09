from django.db import models
from django.contrib.auth.models import User

class enfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    send_user = models.CharField(null=True, max_length=20)
    file_date = models.DateTimeField(auto_now=True)
    file_text = models.TextField(null=True, max_length=100)
    file_content = models.FileField(null=True)

    def __str__(self):
        return self.file_content
