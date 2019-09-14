from django.db import models
from django.urls import reverse # Used to generatre URLs by reversing the URL patterens
import uuid # require for unique book instances
# Create your models here.
class Genre(models.Model):
    '''Model reperesent a book genre.'''
    name = models.CharField(max_length = 200 ,help_text='Enter a book genere (e.g Science Fiction)')

    def __str__(self):
        '''String for reperesenting the model object '''
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 200)

    objects = models.Manager()
    author = models.ForeignKey('Author',on_delete = models.SET_NULL , null = True)
    summary = models.TextField(max_length=1000 , help_text='13 Charecter')
    genre = models.ManyToManyField(Genre ,help_text = 'Select genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])

    def display_genre(self):
        """Create string for the Genre . This is required to display genre in Admin"""
        return ','.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description ='Genre'

class BookInstance(models.Model):
    """ Model reperesenting a specific copy of a book """

    id = models.UUIDField(primary_key=True, default = uuid.uuid4 , help_text ='Unique ID for this particular book')
    book = models.ForeignKey('Book',on_delete =  models.SET_NULL , null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True , blank = True)

    LOAN_STATUS = (
    ('m','Maintenance'),
    ('o','On loan'),
    ('a','Available'),
    ('r','Reserved'),
    )
    status = models.CharField(
    max_length = 1,
    choices = LOAN_STATUS,
    blank  = True ,
    default = 'm',
    help_text = 'Book availablilty'
    )
    objects = models.Manager()

    class Meta :
        ordering = ['due_back']


    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """ Model reperesent the author"""
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null = True ,blank = True)
    date_of_death = models.DateField('Died',null = True , blank = True)
    objects = models.Manager()
    class Meta:
        ordering = ['last_name' ,'first_name']

    def get_absolute_url(self):
        return reverse('author-detail' , arg = [str(self.id)])

    def __str__(self):
        return f'{self.last_name} , {self.first_name}'
