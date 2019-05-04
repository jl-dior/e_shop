from django.db import models

# Create your models here.
from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
	videos_url = models.URLField()

from oscar.apps.catalogue.models import *