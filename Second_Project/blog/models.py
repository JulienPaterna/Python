from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-published_at']
        # on configure la class à notre guise : ici on ordonne par ordre décroissant
        db_table = 'posts'
        # pour créer une table nommée 'posts', et non 'blog_post', par défaut

    def __str__(self):
        return self.title