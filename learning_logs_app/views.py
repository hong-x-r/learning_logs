from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm, EntryAnyForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#def index( request ):
#    """The homepage for learning_logs_app"""
#    return render( request, 'learning_logs_app/index.html' )

def index( request ):
    return render ( request, 'learning_logs_app/index.html' )

@login_required
def topics( request ):
    """List all the topics so far"""
    #topics = Topic.objects.order_by( 'date_added' )
    topics = Topic.objects.all().order_by( '-date_added' )
    context = { 'topics' : topics }
    return render( request, 'learning_logs_app/topics.html', context )

@login_required
def topic( request, topic_id ):
    """List of all entries under topic with the ID"""
    topic = Topic.objects.get( id = topic_id )
    entries = topic.entry_set.order_by( '-date_added' )
    context = { 'topic' : topic, 'entries' : entries }
    return render( request, 'learning_logs_app/topic.html', context )

@login_required
def new_topic( request ):
    """Let user setup a topic"""
    if request.method != 'POST': #No data submitted - a blank form
        form = TopicForm()
    else: #data submitted - to process data
        form = TopicForm( data = request.POST )
        if form.is_valid():
            form.save()
            return redirect( 'learning_logs_app:topics' )

    context = { 'form' : form }
    return render( request, 'learning_logs_app/new_topic.html', context )

@login_required
def new_entry( request, topic_id ):
    """Let user add an entry of specific topic"""
    topic = Topic.objects.get( id = topic_id )

    if request.method != 'POST': #No data to submit -> a blank form
        form = EntryForm()
    else: #Data found in POST mode
        form = EntryForm( data = request.POST )
        if form.is_valid():
            new_entry = form.save( commit = False )
            new_entry.topic = topic
            new_entry.save()
            return redirect( 'learning_logs_app:topic', topic_id = topic_id )

    context = { 'form' : form, 'topic': topic }
    return render( request, 'learning_logs_app/new_entry.html', context )

@login_required
def new_entry_any( request ):
    """Let user an entry of any topic"""
    if request.method != 'POST': #No data yet to submit -> a blank form
        form = EntryAnyForm()
    else: #Date in POST mode
        form = EntryAnyForm( data = request.POST )
        if form.is_valid():
#            topic = form.get_topic()
            form.save()
            return redirect( 'learning_logs_app:topics' )#, topic_id = topic )

    context = { 'form' : form }
    return render( request, 'learning_logs_app/new_entry_any.html', context )

@login_required
def edit_entry( request, entry_id ):
    """Let user edit an entry"""
    entry = Entry.objects.get( id = entry_id )
    topic = entry.topic

    if request.method != 'POST': #initial request filling the form
#        form = EntryForm( instance = entry )
        form = EntryAnyForm( instance = entry )
    else: #post submitted data for update
#        form = EntryForm( instance = entry, data = request.POST )
        form = EntryAnyForm( instance = entry, data = request.POST )
        if form.is_valid():
            form.save()
            return redirect( 'learning_logs_app:topic', topic_id = topic.id )

    context = { 'form' : form, 'topic' : topic, 'entry' : entry }
    return render( request, 'learning_logs_app/edit_entry.html', context )


