from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic( models.Model ):
    """A topic the user is learning about"""
    LITERATURE = 'LI'
    SPORTS = 'SP'
    EDUCATION = 'ED'
    CHILDEDU = 'CED'
    ADULTEDU = 'AED'
    MISCELLANEOUS = 'MI'

    TOPIC_CATE_CHOICES = [
        ( LITERATURE, 'Literature' ),
        ( SPORTS, 'Sports' ),
        ( EDUCATION, (
                ( CHILDEDU, 'Children Education' ),
                ( ADULTEDU, 'Adult Education' ),
            ),
        ),
        ( MISCELLANEOUS, 'Miscellaneous'),
    ]

    topic_cate = models.CharField( 
        max_length = 3,
        choices = TOPIC_CATE_CHOICES,
        default = LITERATURE
    )

    owner = models.ForeignKey( User, on_delete = models.CASCADE )
    text = models.CharField( max_length = 200 )
    date_added = models.DateTimeField( auto_now_add = True )

    def __str__( self ):
        """Return a string representation of the model"""
        return f"{ self.text } - { self.get_topic_cate_display() }"


class Entry( models.Model ):
    """More details on the topic"""
    topic = models.ForeignKey( Topic, on_delete = models.CASCADE )
    text = models.TextField()
    date_added = models.DateTimeField( auto_now_add = True )


    class Meta:
        verbose_name_plural = 'entries'

    def __str__( self ):
        """A string representation"""
        rslt = self.text[ : 50 ] + '...' if len( self.text ) > 50 else self.text
        return rslt

