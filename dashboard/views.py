from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PostForm, CommentForm, ReportForm
from .models import Post, Comment, Report
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