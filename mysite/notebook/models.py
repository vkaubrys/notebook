from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Documents'

class User(models.Model):
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Users'

    # def get_absolute_url(self):
    #     return reverse()




    class Meta:
        ordering = ('title',)
        # verbose_name = 'Document'
        # verbose_name_plural = 'Documents'






