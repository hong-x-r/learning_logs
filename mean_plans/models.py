from django.db import models

# Create your models here.
class Meal( models.Model ):
    """A meal"""
    BREAKFAST = 'BF'
    LUNCH = 'LC'
    SUPPER = 'SP'

    CATE_CHOICES = [
        ( BREAKFAST, 'Breakfast' ),
        ( LUNCH, 'Lunch' ),
        ( SUPPER, 'Supper' ),
    ]

    cate = models.CharField(
        max_length = 2,
        choices = CATE_CHOICES,
        default = BREAKFAST
    )

    #size = models.IntegerField( label = _('for'), min_value = 0, required = True, initial = 0 )
    size = models.IntegerField()
    cuisine = models.CharField( max_length = 40 )

    def __str__( self ):
        """A string representation of the Mean"""
        return f" { self.cuisine } { self.get_cate_display() } for { self.size } "

