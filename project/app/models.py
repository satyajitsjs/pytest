from django.db import models

# Create your models here.


class user(models.Model):
    userid = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
class post(models.Model):
    postid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return self.title

class like(models.Model):
    LIKE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )

    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    choice = models.CharField(max_length=7, choices=LIKE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.choice} - {self.post.title}"
