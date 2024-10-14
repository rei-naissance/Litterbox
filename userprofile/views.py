from django.shortcuts import render, redirect
from .forms import AddCoverImage, AddProfileImage
from .models import profile
from PIL import Image

# Create your views here.
def profile_view(request):
    first_profile = profile.objects.first()
    cover_form = AddCoverImage()
    profile_form = AddProfileImage()
    

    if request.method == "POST":
        if 'cover-submit' in request.POST:
            cover_form = AddCoverImage(request.POST, request.FILES)
            if cover_form.is_valid():
                
                cover_image = cover_form.cleaned_data['cover_image']
                img = Image.open(cover_image)
                width, height = img.size

                if width >= 400 and height >= 200:

                    first_profile.cover_image = cover_image
                    first_profile.save()
                    return redirect('profile_view')
        
        if 'profile-img-submit' in request.POST:
            profile_form = AddProfileImage(request.POST, request.FILES)
            if profile_form.is_valid():

                first_profile.profile_image = profile_form.cleaned_data['profile_image']
                first_profile.save()

                return redirect('profile_view')

    return render(request, 'profile.html', {
        'cover_form': cover_form,
        'profile_form': profile_form,
        'profile': first_profile,
    })

    
