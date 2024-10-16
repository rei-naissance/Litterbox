from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddCoverImage, AddProfileImage, ProfileForm, AddBio
from .models import Profile
from PIL import Image

# Create your views here.
def profile_view(request, user_id):
    profile = get_object_or_404(Profile, id=user_id)
    
    cover_form = AddCoverImage()
    profile_img_form = AddProfileImage()
    profile_form = ProfileForm(instance=profile)
    about_form  = AddBio()
    

    if request.method == "POST":
        if 'profile_change' in request.POST:
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                cover_image = profile_form.cleaned_data.get('cover_image')
                if 'cover_image-clear' in request.POST:  
                    cover_image = None
                if cover_image:  
                    img = Image.open(cover_image)
                    width, height = img.size
                    if width >= 400 and height >= 200:
                        profile.cover_image = cover_image 

                profile_image = profile_form.cleaned_data.get('profile_image')
                if 'profile_image-clear' in request.POST:  
                    profile_image = None
                if profile_image:  
                    img = Image.open(profile_image)
                    width, height = img.size
                    if width >= 200 and height >= 200:
                        profile.profile_image = profile_image 
                
                profile.bio = profile_form.cleaned_data.get('bio')
                profile.title = profile_form.cleaned_data.get('title')
                profile.social_links = profile_form.cleaned_data.get('social_links')
                profile.save()
                return redirect('profile_view', user_id=user_id)

                    
        if 'cover-submit' in request.POST:
            cover_form = AddCoverImage(request.POST, request.FILES)
            if cover_form.is_valid():
                cover_image = cover_form.cleaned_data['cover_image']
                img = Image.open(cover_image)
                width, height = img.size

                if width >= 400 and height >= 200:
                    profile.cover_image = cover_image
                    profile.save()
                    return redirect('profile_view', user_id=user_id)

        if 'profile-img-submit' in request.POST:
            profile_img_form = AddProfileImage(request.POST, request.FILES)
            if profile_img_form.is_valid():
                profile.profile_image = profile_img_form.cleaned_data['profile_image']
                profile.save()
                return redirect('profile_view', user_id=user_id)
            
        if 'about-submit' in request.POST:
            about_form = AddBio(request.POST)
            if about_form.is_valid():
                profile.bio = about_form.cleaned_data['bio']
                profile.save()
                return redirect('profile_view', user_id=user_id)

    return render(request, 'profile.html', {
        'cover_form': cover_form,
        'profile_img_form': profile_img_form,
        'profile_form': profile_form,
        'about_form': about_form,
        'profile': profile,
    })


    
