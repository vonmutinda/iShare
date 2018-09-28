from django.db import models

# Create your models here.
class Mutinda(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 15 , blank = True)

    def __str__(self):
        return self.name


    '''
    Method for saving a new editor to the database
    '''
    def save_mutinda(self):
        self.save()
    

    '''
    Class method for deleting an editor
    '''
    def delete_mutinda(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    user = models.ForeignKey(Mutinda)
    image = models.ImageField(upload_to = 'articles/')




    @classmethod
    def search_by_title(cls,search_term):
        articles = cls.objects.filter(title__icontains = search_term)
        return articles