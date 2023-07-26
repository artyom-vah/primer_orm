from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserOurRegistration, UserUpdateForm, ProfileImage
from app_primer.models import User


# Create your views here.
def register(request):
    '''Регистрация пользователей'''
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('app_primer:all_posts')
    else:
        form = UserOurRegistration()
    context = {
        'form': form,
    }
    return render(request, 'users/registration.html', context)


# def profile(request):
#     return render(request,'users/profile.html',)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts_author = author.posts.all()
    context = {
        'author': author,
        'posts_author': posts_author
    }
    return render(request, 'users/profile.html', context)

# @login_required()
# def profile(request):
#     '''Профиль пользователя'''
#     if request.method == 'POST':
#         img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
#         update_user = UserUpdateForm(request.POST, instance=request.user)
#
#         if update_user.is_valid() and img_profile.is_valid():
#             update_user.save()
#             img_profile.save()
#             messages.success(request, f'Ваш аккаунт был успешно обновлен')
#             return redirect('profile')
#     else:
#         img_profile = ProfileImage(instance=request.user.profile)
#         update_user = UserUpdateForm(instance=request.user)
#
#         context = {
#             'img_profile': img_profile,
#             'update_user': update_user
#         }
#     return render(request, 'users/profile.html', context)

