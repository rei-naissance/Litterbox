from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
from datetime import datetime
from .forms import PostForm, CommentForm, ReportForm
from .models import Post, Comment, Report, Like
from django.http import JsonResponse
from django.db.models import Prefetch
import json

def admin_check(user):
    return user.is_authenticated and user.is_admin

def toggle_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    like, created = Like.objects.get_or_create(author=user, post=post)
    if created:
        like.liked_on = datetime.now()
        like.save()
    else:
        like.delete()
    return JsonResponse({
        'like_count': post.likes.count(),
        'liked': created
    })

@user_passes_test(admin_check)
def delete_reported_post(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    if request.method == 'POST':
        post = report.post
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
    comments_queryset = Comment.objects.filter(is_deleted=False)
    posts = (
        Post.objects.filter(is_deleted=False)
        .prefetch_related(Prefetch('comments', queryset=comments_queryset))
        .order_by('-date_posted')
    )
    user_likes = set(request.user.likes.values_list('post_id', flat=True)) if request.user.is_authenticated else set()
    
    post_count = posts.filter(author=user).count()
    comment_count = comments_queryset.filter(author=user).count()
    
    return render(request, 'dashboard.html', {
        'user': user,
        'post_count': post_count,
        'comment_count': comment_count,
        'posts': posts,
        'user_likes': user_likes
    })


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
    user_liked = post.likes.filter(author=request.user).exists() if request.user.is_authenticated else False
    # TOD0: returns a render of post details with current active user
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
                post=post,
                author=request.user,
                content=content
            )
            return JsonResponse({'success': True, 'comment_id': comment.id, 'content': comment.content})
        else:
            return JsonResponse({'success': False, 'error': 'Comment content cannot be empty'}, status=400)
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
        return JsonResponse({'success': False, 'error': 'Content cannot be empty'}, status=400)
        
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