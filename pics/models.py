from django.db import models

# Application Models 
class Location(models.Model):
    name = models.CharField(max_length = 30)

    '''
    the __str__ function defines how our class instances gonna appear on our backend .
    '''
    def __str__(self):
        return self.name

    @classmethod
    def fetch_locations(cls):
        locations = cls.objects.all()
        return locations

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


    @classmethod
    def fetch_categories(cls):
        cats = cls.objects.all()
        return cats


class Image(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    image_url = models.ImageField(upload_to = 'images/' ,blank = True)

    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()

    @classmethod
    def fetch_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_by_category(cls , cat):
        images = cls.objects.filter(category__name__startswith = cat)
        return images

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(description__icontains = search_term)
        # also = cls.objects.filter(category__name__startswith = search_term)
        return images
    
    @classmethod
    def  get_image(cls,id):
        image = cls.objects.filter(id=id)
        return image
    

    @classmethod
    def get_by_location(cls , location):
        images = cls.objects.filter(location__name__startswith= location)
        return images
    
    @classmethod
    def update_image(cls , name , location , category):
        image = cls.objects.filter(name = name).update(location = location,category = category)
        return image

