from django import forms
from .models import Topic, Entry

class TopicForm( forms.ModelForm ):
    """For a form to setup a topic by user"""
    class Meta:
        model = Topic
        fields = [ 'topic_cate', 'text' ]
        labels = { 'topic_cate' : 'Topic category', 'text' : 'Text' }

class EntryForm( forms.ModelForm ):
    """For a form to insert an entry by user"""
    class Meta:
        model = Entry
        fields = [ 'text' ]
        labels = { 'text' : 'Entry:' }
        widgets = { 'text' : forms.Textarea( attrs = { 'cols' : 80 } ) }

class EntryAnyForm( forms.ModelForm ):
    """For a form to insert an entry of any topic by user"""
    class Meta:
        model = Entry
        fields = [ 'topic', 'text' ]
        labels = { 'topic' : 'Topic:', 'text' : 'Entry:' }
        widgets = { 'text' : forms.Textarea( attrs = { 'cols' : 80 } ) }
