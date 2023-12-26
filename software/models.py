from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=100)
    email = models.CharField(default='', max_length=100)
    phone = models.CharField(default='', max_length=30)
    msg = models.TextField(default='', max_length=5000)
    date = models.DateTimeField(default=now)
    ip = models.CharField(default='', max_length=20)
    value = models.TextField(default='', max_length=200)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.date}'


class UserDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100, default='')
    ip = models.CharField(default='', max_length=20)
    value = models.TextField(default='', max_length=200)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.user}'


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Catagory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=30)
    slug = models.CharField(default='', max_length=100)
    # short_dsc = models.CharField(default='', max_length=500)
    short_dsc = RichTextField(default='', max_length=500)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=now)
    name = models.CharField(default='', max_length=100)
    img = models.ImageField(default='', upload_to='img/')
    short_dsc = RichTextField(default='', max_length=500)

    def __str__(self):
        return self.name


class Software(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=100)
    slug = models.CharField(default='', max_length=100)
    short_dsc = RichTextField(default='', max_length=500)
    dsc = RichTextField(default='', max_length=10000)
    d_link = models.CharField(default='', max_length=200)
    img = models.ImageField(default='', upload_to='software_img/')
    date = models.DateTimeField(default=now)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, default=None, blank=True)

    @property
    def total_likes(self):
        return self.likes.all().count()

    def __str__(self):
        return self.name


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Software, on_delete=models.CASCADE)
    ip = models.CharField(default='', max_length=20)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=12)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.post)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    cmt = models.TextField(default='', max_length=5000)
    post = models.ForeignKey(Software, on_delete=models.CASCADE, default='')
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE, default=None)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=now)
    ip = models.CharField(default='', max_length=20)
    value = models.CharField(default='', max_length=200)
    likes = models.ManyToManyField(
        User, related_name='comment_like', default=None, blank=True)

    @property
    def total_like(self):
        return self.likes.all().count()

    def __str__(self):
        return str(self.post.id)


class Newsletter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=30)
    email = models.CharField(default='', max_length=100)
    ip = models.CharField(default='', max_length=20)
    value = models.TextField(default='', max_length=200)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.name} {self.email}'


class Download_Monitor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Software, on_delete=models.CASCADE)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    user = models.CharField(default='', max_length=30)
    ip = models.CharField(default='', max_length=20)
    value = models.TextField(default='', max_length=200)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.name)


class UserClone(models.Model):
    id = models.AutoField(primary_key=True)
    name = CharField(default='', max_length=50)
    email = CharField(default='', max_length=100)
    password = CharField(default='', max_length=100)
    date = DateTimeField(default=now)
    ip = models.CharField(default='', max_length=20)
    value = models.TextField(default='', max_length=200)

    def __str__(self):
        return self.name