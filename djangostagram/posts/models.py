from django.db import models
from djangostagram.users import models as user_model

# Create your models here.

# This class is used in other models as an inheritance.
# An often-used pattern 
class TimeStamedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # An option that makes this model to not show up directly on the database
    class Meta:
        abstract = True


class Posts(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null = True,
                on_delete = models.CASCADE,
                related_name = "post_author"
            )
    caption = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name='post_image_likes')


class Comments(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null = True,
                on_delete = models.CASCADE,
                related_name = "comment_author"
            )
    posts = models.ForeignKey(
                Posts,
                null = True,
                on_delete = models.CASCADE,
                related_name = "comment_post"
    )
    contents = models.TextField(blank=True)
