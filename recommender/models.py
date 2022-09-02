from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Movies(models.Model):
    _id = models.IntegerField(primary_key=True, blank=False)
    genres = models.CharField(max_length=1000, blank=True)
    title = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ['_id']
        db_table = 'Movies'
