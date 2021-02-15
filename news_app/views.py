from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, User, UserProfileInfo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import CommentForm, UserForm, UserProfileInfoForm, EditProfileForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'news_app/post_list.html', {'posts': posts})

def post_list_category(request, category):
    posts = Post.objects.filter(categories=category, published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'news_app/post_list.html', {'posts': posts})

def post_item(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,'news_app/post_item.html', {'post': post})


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    current_user = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            comment.post = post
            comment.save()
            return redirect('post_item', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'news_app/comment_form.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_item', pk=post_pk)


@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('post_list'))

@login_required
def profile_page(request, username):
    user = User.objects.get(username=username)
    comments = Comment.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'news_app/user_account.html', {'profile_user': user, 'comments': comments})

def viewed_profile(request, comment_author):
    profile_user = User.objects.get(username=comment_author)
    print(profile_user)
    return render(request, 'news_app/viewed_user.html', {'profile_user': profile_user})

def register(request):
    registered = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        #portfolio = request.POST.get('portfolio_site')

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('user_login'))
        else:
            messages.error(request,'Invalid credentials!')
            #print("They used: {} {} {} {}".format(email, username, password, portfolio))
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'news_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    errors = ['Invalid credentials! Please try again.']
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('post_list'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request,'Username or password not correct')
            return redirect('user_login')
    else:
        return render(request, 'news_app/login.html', {})



@login_required
def edit_profile(request):
    comments = Comment.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    print(comments)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        user_profile, created = UserProfileInfo.objects.get_or_create(user=request.user)

        update_profile_form = UserProfileInfoForm(data=request.POST, instance=user_profile)
        print(update_profile_form)
        print('\n')
        print(update_profile_form.is_valid())

        if update_profile_form.is_valid():
            print('valid')
            #user = update_user_form.save()
            profile = update_profile_form.save(commit=False)
            #profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
                print(profile.profile_pic.url)

            profile.save()
        else:
            print('invalid')
            print(update_profile_form.errors)

        if form.is_valid():
            form.save()
            return redirect('edit_profile')

        args = {'form': form, 'update_profile_form': update_profile_form, 'comments': comments}
        return render(request, 'news_app/user_account.html', args)
    return render(request, 'news_app/user_account.html', {'comments': comments})


@login_required
def delete_profile_image(request):
    user_profile = UserProfileInfo.objects.get(user=request.user)
    user_profile.profile_pic.delete()
    return HttpResponseRedirect(reverse('edit_profile'))
