from django.db import models




class Dcat(models.Model):
    option_template_name = 'django/forms/widgets/select_option.html'
    alcohol = 'Alcohol'
    beers = 'Beers'
    wines = 'Wines'
    spirits = 'Spirits'
    sin = 'Sin'
    none_alcohol = 'None Alcohol'
    pop = 'Pop'
    mixers ='Mixers'
    cartons = 'Cartons'
    water = 'Water'
    cordial = 'Cordial'
    tea = 'Tea'
    coffee ='Coffee'
    malted = 'Malted'
    DRINK_CHOICES = (
    ('Alcohol', (
            ('beers', 'Beers'),
            ('wines', 'Wines'),
            ('spirits', 'Spirits'),
            ('sin', 'Sin'),
        )
    ), 
    ('None_Alcohol', (
            ('pop', 'Pop'),
            ('mixers', 'Mixers'),
            ('cartons', 'Cartons'),
            ('water', 'Water'),
            ('cordial', 'Cordial'),
            ('tea', 'Tea'),
            ('coffee', 'Coffee'),
            ('malted', 'Malted'),
        )
    )
    )
    drink_choice = models.CharField(max_length=100,choices=DRINK_CHOICES,default=alcohol,null=True)
    

    def drink_category(self):
        return self.drink_choice in (self.DRINK_CHOICES)

    def __str__(self):
        return self.drink_choice


class Ditem(models.Model):
    title = models.CharField(max_length=100,null=True)
    slug = models.SlugField(null=True)
    thumb = models.ImageField(default='default.png', null=True)
    body = models.TextField(null=True)
    drink_cat = models.ForeignKey(Dcat, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:20] + '...'