# from django.conf import settings
import os
from django.shortcuts import render, redirect, get_object_or_404

from dashboard.models import Post
from .forms import AddCoverImage, AddProfileImage, ProfileForm, AddBio, AddLinks
from .models import Profile
from authentication.models import Student
from PIL import Image
from django.contrib.auth import authenticate
import json


DEFAULT_COVER_IMAGE = "images/cover_photo.png"
DEFAULT_PROFILE_IMAGE = "images/default_profile_pic.png"

def delete_image(file_path):
    # Ensure file_path is not empty and it's not the default image
    if file_path:
        if file_path != DEFAULT_COVER_IMAGE and file_path != DEFAULT_PROFILE_IMAGE:
            # Proceed with deleting the image if it's not the default image
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"Deleted image: {file_path}")
                except Exception as e:
                    print(f"Error deleting image: {e}")
        else:
            print(f"Skipping deletion of default image: {file_path}")

# Create your views here.
def profile_view(request, user_id):
    user = request.user
    student = get_object_or_404(Student, id=user_id)
    if not hasattr(student, 'profile'):
        Profile.objects.create(student=student)

    profile = get_object_or_404(Profile, student=student)
    posts = Post.objects.filter(author=student).order_by('-date_posted')
    
    cover_form = AddCoverImage()
    profile_img_form = AddProfileImage()
    profile_form = ProfileForm(instance=profile)
    about_form  = AddBio(instance=profile)
    links_form = AddLinks(instance=profile)

    if request.method == "POST":
        
        if 'profile_change' in request.POST:
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

            current_cover_image_path = profile.cover_image.path if profile.cover_image else None
            current_profile_image_path = profile.profile_image.path if profile.profile_image else None
            # print("cci", current_cover_image_path)
            # print("cpi", current_profile_image_path )

            if profile_form.is_valid():
                cover_image = profile_form.cleaned_data.get('cover_image')
                profile_image = profile_form.cleaned_data.get('profile_image')
                # print("ci", cover_image)
                # print("pi", profile_image )

                # Update other profile fields
                profile.bio = profile_form.cleaned_data.get('bio')
                profile.title = profile_form.cleaned_data.get('title')

                # Handle social links
                social_links_json = request.POST.get('social_links_json')
                if social_links_json:
                    profile.social_links = json.loads(social_links_json)

                # Handle cover image clear
                if 'cover_image-clear' in request.POST and current_cover_image_path:
                    delete_image(current_cover_image_path)
                    profile.cover_image = DEFAULT_COVER_IMAGE
                elif cover_image and cover_image != profile.cover_image.name: 
                    if current_cover_image_path:
                        delete_image(current_cover_image_path)
                    try:
                        img = Image.open(cover_image)
                        width, height = img.size
                        if width >= 400 and height >= 200:
                            profile.cover_image = cover_image
                    except Exception as e:
                        print("Error opening cover image:", e)

                # Handle profile image clear
                if 'profile_image-clear' in request.POST and current_profile_image_path:
                    delete_image(current_profile_image_path)
                    profile.profile_image = DEFAULT_PROFILE_IMAGE
                elif profile_image and profile_image != profile.profile_image.name:
                    if current_profile_image_path:
                        delete_image(current_profile_image_path)
                    try:
                        img = Image.open(profile_image)
                        width, height = img.size
                        if width >= 400 and height >= 200:
                            profile.profile_image = profile_image
                    except Exception as e:
                        print("Error opening profile image:", e)

                # Save the profile instance
                profile.save()
                return redirect('profile_view', user_id=user_id)


                    
        if 'cover-submit' in request.POST:
            cover_form = AddCoverImage(request.POST, request.FILES)

            current_cover_image_path = profile.cover_image.path if profile.cover_image else None

            if cover_form.is_valid():
                cover_image = cover_form.cleaned_data['cover_image']


                if 'cover_image-clear' in request.POST:
                    delete_image(current_cover_image_path) 
                    profile.cover_image = DEFAULT_COVER_IMAGE

                # Save the new cover image if provided and valid
                elif cover_image:
                    if current_cover_image_path:
                        delete_image(current_cover_image_path) 
                    try:
                        img = Image.open(cover_image)
                        width, height = img.size
                        if width >= 400 and height >= 200:
                            profile.cover_image = cover_image
                    except Exception as e:
                        print("Error opening cover image:", e)

                profile.save()
                return redirect('profile_view', user_id=user_id)


        if 'profile-img-submit' in request.POST:
            profile_img_form = AddProfileImage(request.POST, request.FILES)

            current_profile_image_path = profile.profile_image.path if profile.profile_image else None

            if profile_img_form.is_valid():
                profile_image = profile_img_form.cleaned_data['profile_image']

                if 'profile_image-clear' in request.POST:
                    delete_image(current_profile_image_path) 
                    profile.profile_image = DEFAULT_PROFILE_IMAGE

                # Save the new cover image if provided and valid
                elif profile_image:
                    if current_profile_image_path:
                        delete_image(current_profile_image_path) 
                    try:
                        img = Image.open(profile_image)
                        width, height = img.size
                        if width >= 400 and height >= 200:
                            profile.profile_image = profile_image
                    except Exception as e:
                        print("Error opening cover image:", e)

                profile.save()
                return redirect('profile_view', user_id=user_id)
            
        if 'about-submit' in request.POST:
            about_form = AddBio(request.POST)
            if about_form.is_valid():
                profile.bio = about_form.cleaned_data['bio']
                profile.save()
                return redirect('profile_view', user_id=user_id)
            
        if 'links_change_v2' in request.POST:
            links_form = AddLinks(request.POST)
            if links_form.is_valid():
                social_links_json = request.POST.get('social_links_json')
                if social_links_json:
                    social_links = json.loads(social_links_json)
                    profile.social_links = social_links
                    profile.save()
                    return redirect('profile_view', user_id=user_id)

    context = {
        'cover_form': cover_form,
        'profile_img_form': profile_img_form,
        'profile_form': profile_form,
        'about_form': about_form,
        'links_form': links_form,
        'profile': profile,
        'posts': posts,
        'user': user
    }

    return render(request, 'profile.html', context)

def account_termination_success(request, action):
    if action == 'terminated':
        message = "We hope to see you back!"
    elif action == 'deactivate':
        message = "Your account is deactivated. You can reactivate it by contacting support."
    else:
        message = "Unexpected action."

    return render(request, 'account_termination_success.html', {'message': message})

def account_termination(request, action):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None and user == request.user:
            if action == 'terminate':
                user.delete()  # Terminate the account
                return render(request, 'account_termination_success.html', {'action': 'terminated'})
            elif action == 'deactivate':
                user.is_active = False  # Deactivate the account
                user.save()
                return render(request, 'account_termination_success.html', {'action': 'deactivate'})
        else:
            return render(request, 'account_termination.html', {'error': 'Invalid credentials'})

    return render(request, 'account_termination.html', {'action': action})

    
