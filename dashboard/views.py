from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.serializers import serialize
from .forms import PostForm, CommentForm, ReportForm, EventForm
from .models import Post, Comment, Report, Event, Follow
from django.http import JsonResponse

# Create your views here.

def fetch_posts():
    pass

def admin_check(user):
    return user.is_authenticated and user.is_admin

@login_required
def dashboard_home(request):
    user = request.user
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'dashboard.html', {'user': user, 'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    user_liked = post.likes.filter(author=request.user).exists() if request.user.is_authenticated else False
    # TOD0: returns a render of post details with current active user
    return render(request, 'dashboard.html', {
        'post': post,
        'comments': comments,
        'user_liked': user_liked
    })


@login_required
def post_create(request):
    posts = Post.objects.all().order_by('-date_posted')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard_home')
    else:
        form = PostForm()
    return render(request, 'dashboard.html', {'form': form, 'posts': posts})

@login_required
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=request.POST.get('post_id'))
            comment.author = request.user
            comment.save()
            return redirect('dashboard_home')
        
@user_passes_test(admin_check)
def admin_dashboard(request):
    reports = Report.objects.all().order_by('-reported_on')
    return render(request, 'admin_dashboard.html', {'reports': reports})

# test view function for sending reports to admin dashboard
@login_required
def send_report(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.post = post
            report.save()
            return redirect('dashboard_home')
    else: 
        form = ReportForm()
    return render(request, 'dashboard.html', {'form': form, 'post': post})


def calendar_view(request):
    user = request.user
    
    # Events created by the user
    created_events = Event.objects.filter(user=user)

    # Events the user is following
    followed_events = Event.objects.filter(followers__user=user)

    # Combine the two sets of events
    events = created_events | followed_events

    return render(request, 'calendar.html', {'events': events, 'user': user})

# Create or update an event 
def save_event(request):
    if request.method == 'POST':
        event_id = request.POST.get('id', None)
        
        print("Received POST data:", request.POST)

        if event_id:  
            event = get_object_or_404(Event, pk=event_id)
            form = EventForm(request.POST, instance=event)
        else: 
            form = EventForm(request.POST)

        if not form.is_valid():
            print("Form errors:", form.errors)
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        
        event = form.save(commit=False)
        event.user = request.user 

        try:
            event.save()
        except Exception as e:
            return JsonResponse({'success': False, 'errors': str(e)}, status=500)

        return JsonResponse({'success': True, 'event': {
            'id': event.id,
            'title': event.title,
            'start_date': event.start_date.strftime('%Y-%m-%d'),
            'end_date': event.end_date.strftime('%Y-%m-%d'),
            'start_time': event.start_time.strftime('%H:%M'),
            'end_time': event.end_time.strftime('%H:%M'),
            'location': event.location,
            'description': event.description,
        }})
    return JsonResponse({'success': False, 'errors': 'Invalid request'}, status=400)


# Delete an event 
def delete_event(request, event_id):
    if request.method == 'POST':
        try:
            event = get_object_or_404(Event, id=event_id)
            event.delete()
            
            return JsonResponse({'success': True})
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'An error occurred: {str(e)}'}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


@login_required
def get_events(request):
    user_events = Event.objects.filter(user=request.user)

    followed_events = Follow.objects.filter(user=request.user).values_list('event', flat=True)
    followed_events_data = Event.objects.filter(id__in=followed_events)

    # Serialize both user-created events and followed events
    user_events_data = [
        {
            'id': event.id,
            'title': event.title,
            'start': f"{event.start_date.isoformat()}T{event.start_time.isoformat()}", 
            'end': f"{event.end_date.isoformat()}T{event.end_time.isoformat()}", 
            'description': event.description,
            'extendedProps': {
                'user_id': event.user.id,
                'organizer_id': event.organizer.id if event.organizer else None,  
            }
        }
        for event in user_events
    ]

    followed_events_data_list = [
        {
            'id': event.id,
            'title': event.title,
            'start': f"{event.start_date.isoformat()}T{event.start_time.isoformat()}", 
            'end': f"{event.end_date.isoformat()}T{event.end_time.isoformat()}", 
            'description': event.description,
            'extendedProps': {
                'user_id': event.user.id,
                'organizer_id': event.organizer.id if event.organizer else None,  
            }
        }
        for event in followed_events_data
    ]

    # Combine both lists into one list of events
    combined_events_data = user_events_data + followed_events_data_list

    # Return combined list as JSON
    return JsonResponse(combined_events_data, safe=False)



@login_required
def user_events(request):
    # Ensure the user is only seeing their own events
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Not authenticated"}, status=401)

    events = Event.objects.filter(user=request.user)
    serialized_events = serialize('json', events, fields=('title', 'start_date', 'end_date', 'start_time', 'end_time', 'location', 'description'))

    return JsonResponse({'events': serialized_events}, safe=False)


@login_required
def follow_event(request, event_id):
    event = Event.objects.get(id=event_id)
    follow, created = Follow.objects.get_or_create(user=request.user, event=event)
    
    if created:
        return JsonResponse({'message': 'Event followed successfully'})
    else:
        return JsonResponse({'message': 'Already following this event'})

@login_required
def unfollow_event(request, event_id):
    event = Event.objects.get(id=event_id)
    follow = Follow.objects.filter(user=request.user, event=event).first()
    
    if follow:
        follow.delete()
        return JsonResponse({'message': 'Unfollowed successfully'})
    else:
        return JsonResponse({'message': 'You are not following this event'})
    
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = EventForm(instance=event)
    return render(request, "event_detail.html", {"event": event, "form": form})

