from time import localtime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post, Comment, Report, Like, Save, Announcement
from .forms import PostForm, CommentForm, ReportForm, AnnouncementForm
from django.db.models import Prefetch
from django.core.serializers import serialize
from .forms import PostForm, CommentForm, ReportForm, EventForm
from .models import Post, Comment, Report, Event, Follow
from django.http import JsonResponse
from datetime import datetime
from django.utils.timezone import localtime
import json

def admin_check(user):                                                          # decorator to check if user is admin.
    return user.is_authenticated and user.is_admin

@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    like, created = Like.objects.get_or_create(author=user, post=post)          # get_or_create returns a tuple contaning like object and boolean.
    if created:                                                                 # boolean used to check if like object was created (post was unliked beforehand).
        like.liked_on = datetime.now()
        like.save()
    else:
        like.delete()
    return JsonResponse({                                                       # returns line count and status to reflect on frontend.
        'like_count': post.likes.count(),
        'liked': created
    })

@login_required
def toggle_save(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    save, created = Save.objects.get_or_create(author=user, post=post)          # similar logic to post likes except number of saves is not saved.
    if created:
        save.saved_on = datetime.now()
        save.save()
    else:
        save.delete()
    return JsonResponse({
        'saved': created
    })

@user_passes_test(admin_check)
def delete_reported_post(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    if request.method == 'POST':                                                
        post = report.post                                                      # grabs post from report.
        post.is_deleted = True
        post.save()
        report.is_resolved = True
        report.save()
    return redirect('admin_dashboard')

@user_passes_test(admin_check)
def disregard_reported_post(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    if request.method == 'POST':
        report.is_resolved = True
        report.save()
    return redirect('admin_dashboard')
        
@login_required
def dashboard_home(request):
    user = request.user
    comments_queryset = Comment.objects.filter(is_deleted=False)                # grabs all comments.
    posts = (
        Post.objects.filter(is_deleted=False)
        .prefetch_related(Prefetch('comments', queryset=comments_queryset))
        .order_by('-date_posted')
    )

    if request.user.is_authenticated:                                           # renders the user's likes and saves for dashboard frontend.
        user_likes = set(request.user.likes.values_list('post_id', flat=True))
        user_saves = set(request.user.saves.values_list('post_id', flat=True))
    else:
        user_likes = set()
        user_saves = set()
    
    # changed for readability.
    # user_likes = set(request.user.likes.values_list('post_id', flat=True)) if request.user.is_authenticated else set()
    # user_saves = set(request.user.saves.values_list('post_id', flat=True)) if request.user.is_authenticated else set()
    
    post_count = posts.filter(author=user).count()
    comment_count = comments_queryset.filter(author=user).count()
    
    return render(request, 'dashboard.html', {
        'user': user,
        'post_count': post_count,
        'comment_count': comment_count,
        'posts': posts,
        'user_likes': user_likes,
        'user_saves': user_saves
    })


@login_required
def event_home(request):
    # user = request.user
    # comments_queryset = Comment.objects.filter(is_deleted=False)
    # posts = (
    #     Post.objects.filter(is_deleted=False)
    #     .prefetch_related(Prefetch('comments', queryset=comments_queryset))
    #     .order_by('-date_posted')
    # )
    # user_likes = set(request.user.likes.values_list('post_id', flat=True)) if request.user.is_authenticated else set()
    
    # post_count = posts.filter(author=user).count()
    # comment_count = comments_queryset.filter(author=user).count()
    
    return render(request, 'dashboard.html', {
        # 'user': user,
        # 'post_count': post_count,
        # 'comment_count': comment_count,
        # 'posts': posts,
        # 'user_likes': user_likes
    })

@login_required
def announcement_home(request):
    # Fetch and order announcements
    announcements = Announcement.objects.filter(is_archived=False).order_by('-created_at')

    # Group announcements by "Month Year"
    grouped_announcements = {}
    for announcement in announcements:
        # Safely format datetime into "Month Year" string
        month_year = localtime(announcement.created_at).strftime("%B %Y")
        grouped_announcements.setdefault(month_year, []).append(announcement)

    # Pass grouped announcements to the template
    return render(request, 'dashboard.html', {'grouped_announcements': grouped_announcements})

@login_required
def announcement_create(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            form.save()
            return redirect('announcements')  # Redirect to announcements list
    else:
        form = AnnouncementForm()
    return render(request, 'dashboard.html', {'form': form})

def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, pk=announcement_id)

    return render(request, 'dashboard.html', {
        'announcement': announcement
    })

@login_required
def saved_posts(request):
    user = request.user
    saved_posts = (
        Post.objects.filter(is_deleted=False, saves__author=user)                # gets all saved posts.
        .distinct()                                                              # removes duplicates.
        .order_by('-date_posted')
    )

    if request.user.is_authenticated:                                           
        user_saves = set(request.user.saves.values_list('post_id', flat=True))
    else:
        user_saves = set()

    return render(request, 'saved_posts.html', {'saved_posts': saved_posts, 'user_saves': user_saves})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard_home')  # Redirect to dashboard home after posting
    else:
        form = PostForm()
    return render(request, 'dashboard.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(is_deleted=False).order_by('-date_posted')


    if request.user.is_authenticated:
        user_liked = post.likes.filter(author=request.user).exists()
    else:
        user_liked = False

    # user_liked = post.likes.filter(author=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'dashboard.html', {
        'post': post,
        'comments': comments,
        'user_liked': user_liked
    })

@login_required
def comment_create(request, post_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content', '').strip()
        
        if content:
            post = get_object_or_404(Post, pk=post_id)
            comment = Comment.objects.create(
                post = post,
                author = request.user,
                content = content
            )
            return JsonResponse({'success': True, 'comment_id': comment.id, 'content': comment.content})
        else:
            # 400 Bad Request
            return JsonResponse({'success': False, 'error': 'Comment content cannot be empty'}, status=400)
    # 405 Method Not Allowed
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
        
@login_required
@require_http_methods(["DELETE"])
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    comment.is_deleted = True
    comment.save()
    return JsonResponse({'success': True})

@login_required
@require_http_methods(["PATCH"])
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    data = json.loads(request.body)
    new_content = data.get('content', '').strip()

    if new_content:
        comment.content = new_content
        comment.save()
        return JsonResponse({'success': True, 'content': new_content})
    else:
        # 400 Bad Request
        return JsonResponse({'success': False, 'error': 'Content cannot be empty'}, status=400)
        
@login_required
@user_passes_test(admin_check)
def admin_dashboard(request):
    reports = Report.objects.filter(is_resolved=False).order_by('-reported_on')
    return render(request, 'admin_dashboard.html', {'reports': reports})

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

