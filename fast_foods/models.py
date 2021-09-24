from django.db import models


class Fastfood(models.Model):
    id = models.IntegerField(db_column='index', primary_key=True)
    address = models.CharField(db_column='address', max_length=255, blank=False, default='')
    categories = models.CharField(db_column='categories', max_length=50, blank=False, default='')
    city = models.CharField(db_column='city', max_length=30, blank=False, default='')
    country = models.CharField(db_column='country', max_length=2, blank=False, default='')
    name = models.CharField(db_column='name', max_length=255, blank=False, default='')
    postalCode = models.CharField(db_column='postalCode', max_length=9, blank=False, default='')
    province = models.CharField(db_column='province', max_length=2, blank=False, default='')
    websites = models.CharField(db_column='websites', max_length=255, blank=False, default='')
    latitude = models.FloatField(db_column='latitude', )
    longitude = models.FloatField(db_column='longitude')

    class Meta:
        managed = False
        db_table = 'fast-food'
