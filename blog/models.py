from django.db import models
from organizer.models import Tag, Startup
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, unique_for_month='publication_date',
    help_text='A label for URL config.')
    text = models.TextField()
    publication_date = models.DateField(verbose_name='publication date',
    auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    def __str__(self):
        return "{} on {}".format(self.title,self.publication_date.strftime('%Y-%m-%d'))

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-publication_date','title']
        get_latest_by = 'publication_date'
