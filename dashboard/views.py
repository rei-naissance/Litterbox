from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PostForm, CommentForm, ReportForm
from .models import Post, Comment, Report, Like
from django.http import JsonResponse

# Create your views here.

def fetch_posts():
    pass

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
    posts = Post.objects.filter(is_deleted=False).order_by('-date_posted')
    user_likes = set(request.user.likes.values_list('post_id', flat=True)) if request.user.is_authenticated else set()
    return render(request, 'dashboard.html', {'user' : user, 'posts': posts, 'user_likes': user_likes})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    user_liked = post.likes.filter(author=request.user).exists() if request.user.is_authenticated else False
    # TOD0: returns a render of post details with current active user
    return render(request, 'post_testing.html', {
        'post': post,
        'comments': comments,
        'user_liked': user_liked
    })

@login_required
def post_create(request):
    posts = Post.objects.filter(is_deleted=False).order_by('-date_posted')
    user_likes = set(request.user.likes.values_list('post_id', flat=True)) if request.user.is_authenticated else set()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_create')
        
    else:
        form = PostForm()
    return render(request, 'dashboard.html', {'form': form, 'posts': posts, 'user_likes': user_likes})

@login_required
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=request.POST.get('post_id'))
            comment.author = request.user
            comment.save()
            return redirect('create_post')
        
@user_passes_test(admin_check)
def admin_dashboard(request):
    reports = Report.objects.filter(is_resolved=False).order_by('-reported_on')
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
            return redirect('create_post')
    else: 
        form = ReportForm()
    return render(request, 'report_post.html', {'form': form, 'post': post})