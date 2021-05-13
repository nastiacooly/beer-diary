from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

# Beer type model
class BeerType(models.Model):
    """
    Model representing a specific beer type.
    """
    name = models.CharField(max_length=200, help_text='Enter name of a beer type')

    COLOR_TYPES = (
        ('d', 'dark'),
        ('l', 'light')
    )

    color = models.CharField(max_length=1, choices=COLOR_TYPES, help_text='Choose dark or light type of a beer')

    FILTERED = (
        ('y', 'filtered'),
        ('n', 'unfiltered')
    )

    filtered = models.CharField(max_length=1, choices=FILTERED, null=True, blank=True, help_text='Choose filtered or unfiltered')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


    def get_absolute_url(self):
        """
        Returns the url to access a particular beer instance.
        """
        return reverse('beertype-detail', args=[str(self.id)])


# Beer review model
class BeerReview(models.Model):
    """
    Model representing a specific beer review of a specific user.
    """
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.URLField(max_length=2000, help_text='Enter URL for beer image', blank=True, default='')
    name = models.CharField(max_length=200, help_text='Enter beer name')
    beertype = models.ForeignKey(BeerType, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because beer can only have one type, but types of beer can be attributable to multiple beers
    RATINGS = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'average'),
        ('4', 'good'),
        ('5', 'perfect')
    )

    rating = models.CharField(max_length=1, choices=RATINGS, help_text='Choose beer rating')
    comments = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular beer instance.
        """
        return reverse('beer-detail', args=[str(self.id)])