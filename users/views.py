from django.shortcuts import render, redirect
from .forms import UserOurRegistration
from django.contrib import messages

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
