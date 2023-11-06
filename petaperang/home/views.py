import django.contrib.auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from home import helper
from home.forms import SignUpForm, LoginUserForm, RegEditorForm, \
    AllUpdateForm, EmailConfirmation

from home.models import User
from home.tokens import account_activation_token


# Create your views here.
def show_home_page(request):
    return render(request, 'home.html')


def redirect_to_home_page(request):
    return redirect('/home/')


def page_not_found(request, exception):
    return render(request, 'handler_exceptions.html')


def show_login_form(request):
    form = LoginUserForm(request.POST)
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return redirect('home')
    if any([request.POST.get("username"), request.POST.get("password")]):
        return render(request, 'login.html', {'form': form, 'enter_exception': 1})
    return render(request, 'login.html', {'form': form, 'enter_exception': 0})


def registration(request):
    form = SignUpForm(request.POST)
    exception_text = ''
    if request.user.is_authenticated:
        return redirect('home')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        form.save()
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(request, new_user)
        return redirect('home')

    if any([request.POST.get("username"), request.POST.get("password1"), request.POST.get("password2"),
            request.POST.get("phone_number")]):
        exception_text = "Слишком простой пароль/пароли не совпадают/Телефон уже использовался"
    form = SignUpForm()

    return render(request, 'registration.html', {'form': form, 'exception_text': exception_text})


@login_required(login_url='login')
def getting_editor_rights(request):
    user = request.user
    if not user.email_verified:
        return redirect('email_activating_form')
    exception_text = ''
    if request.user.editor_rights:
        return redirect('profile')
    if request.method == 'POST':
        form = RegEditorForm(request.POST, instance=user)
        #
        # form.fields['editor_rights'] = form.fields['editor_rights'] == 'on'
        if form.is_valid():
            form.save()
            return redirect('/home/')

    if any([request.POST.get("username"), request.POST.get("password1"), request.POST.get("password2"),
            request.POST.get("phone_number")]):
        exception_text = "Слишком простой пароль/пароли не совпадают/Телефон уже использовался"
    form = RegEditorForm(instance=user)

    return render(request, 'registration_editor.html', {'form': form, 'exception_text': exception_text})


@login_required(login_url='login')
def logout(request):
    django.contrib.auth.logout(request)
    return redirect('/home/')


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='login')
def instruments(request):
    if request.user.editor_rights:
        return render(request, 'instruments.html')
    return redirect('getting_editor')


@login_required(login_url='login')
def show_editor_page(request):
    user = request.user
    exception_text = ''
    if request.method == 'POST':
        form = AllUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user_record = User.objects.get(id=user.id)
            if user_record.email != form.cleaned_data.get('email'):
                user_record.phone_number = form.cleaned_data.get('phone_number')
                user_record.first_name = form.cleaned_data.get('first_name')
                user_record.second_name = form.cleaned_data.get('second_name')
                user_record.email = form.cleaned_data.get('email')
                user_record.email_verified = False
                user_record.save()
            else:
                form.save()
            return redirect('/profile/')

    if any([request.POST.get("username"), request.POST.get("password1"), request.POST.get("password2"),
            request.POST.get("phone_number")]):
        exception_text = "Слишком простой пароль/пароли не совпадают/Телефон уже использовался"
    form = AllUpdateForm(instance=user)

    return render(request, 'editor.html', {'form': form, 'exception_text': exception_text})


# активация электронной почты
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.email_verified = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('profile')

    messages.error(request, 'Activation link is invalid!')

    return redirect('home')


@login_required(login_url='login')
def activating_form(request):
    user = request.user
    if user.email_verified:
        return redirect('profile')
    if request.method == 'POST':
        form = EmailConfirmation(request.POST, instance=request.user)
        if form.is_valid():
            helper.send_email(request)
            form.save()
        return redirect('profile')
    form = EmailConfirmation(instance=request.user)
    return render(request, 'email_activating.html', {'form': form})
