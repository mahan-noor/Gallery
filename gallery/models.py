from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Editor(models.Model):
    editor_name = models.CharField(max_length =30)
    email = models.EmailField()


    def __str__(self):
        return self.editor_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['editor_name']

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    img = CloudinaryField("photo")
    img_name = models.CharField(max_length= 30)
    img_description = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search):
        images = Image.objects.filter(category__name__icontains=search)
        return images

    @classmethod
    def search_by_location(cls,search):
        images = Image.objects.filter(location__name__icontains=search)
        return images



