from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import AccountVerificationForm, LoginForm, ProfileEditForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm  # Assume you have a form to handle user changes


def home(request):
    return render(request, 'home/index.html')


def generate_verification_code():
    return get_random_string(length=6)  # Generate a 6-character random string


def account_register(request):
    if request.method == 'POST':
        form = AccountVerificationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            verification_code = generate_verification_code()

            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                verification_code=verification_code,
            )

            send_mail(
                'Your Verification Code',
                f'Your verification code is: {verification_code}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            request.session['email'] = email
            request.session['username'] = username

            messages.success(request, "A verification code has been sent to your email. Please verify your account.")
            return redirect('account_verify')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AccountVerificationForm()

    return render(request, 'home/account_register.html', {'form': form})


def account_verify(request):
    if request.method == 'POST':
        email = request.session.get('email')
        verification_code = request.POST.get('verification_code')

        if email:
            try:
                user = CustomUser.objects.get(email=email)

                if user.verification_code == verification_code and not user.is_verified:
                    user.is_verified = True
                    user.verification_code = ''
                    user.save()

                    login(request, user)
                    messages.success(request, "Your account has been verified successfully!")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid code.")
            except CustomUser.DoesNotExist:
                messages.error(request, "No account found for this email.")
        else:
            messages.error(request, "Session expired or invalid.")

    return render(request, 'home/account_verify.html')


def reset_verification(request):
    email = request.session.get('email')

    if email:
        try:
            user = get_object_or_404(CustomUser, email=email)
            if user.is_verified:
                messages.info(request, "Your account is already verified.")
                return redirect('account_login')

            user.verification_code = generate_verification_code()
            user.is_verified = False
            user.save()

            send_mail(
                'New Verification Code',
                f'Your new verification code is: {user.verification_code}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(request, "A new verification code has been sent to your email.")
            return redirect('account_verify')
        except CustomUser.DoesNotExist:
            messages.error(request, "No account found for this email.")
            return redirect('account_register')
    else:
        messages.error(request, "Session expired or invalid.")
        return redirect('account_login')


def account_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = CustomUser.objects.get(email=email)
                if user.is_verified:
                    user = authenticate(request, username=user.username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, "Login successful!")
                        return redirect('home')
                    else:
                        messages.error(request, "Invalid email or password.")
                else:
                    messages.error(request, "Account not verified.")
            except CustomUser.DoesNotExist:
                messages.error(request, "No account found for this email.")
    else:
        form = LoginForm()

    return render(request, 'home/account_login.html', {'form': form})


@login_required
def account_profile(request):
    user = request.user
    return render(request, 'home/account_profile.html', {'user': user, 'MEDIA_URL': settings.MEDIA_URL})


@login_required
def account_profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_profile')  # Redirect to profile page after editing
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'home/account_profile_edit.html', {'form': form})
