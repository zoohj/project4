from django.db import models
from users.models import User

# Create your models here.

class Post(models.Model):
    # type= 신고 or 신청

    title = models.CharField(max_length= 20)
    content = models.TextField(max_length=300, default='')
    image= models.ImageField(upload_to="post", null= True)
    
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add= True, blank= True)

    likes = models.ManyToManyField(User,related_name = "like_post")
    
    def get_likes(self):
        return self.likes.all().count()