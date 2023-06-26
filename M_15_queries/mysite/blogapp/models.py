from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=False, blank=True)
    
    
class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=40)
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    
    def __str__(self):
        return f"#{self.name}"


class Article(models.Model):
    title = models.CharField(null=False, blank=True, max_length=200)
    content = models.TextField(null=False, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="articles")
    
    def __str__(self):
        return f"Article №{self.pk}"
    