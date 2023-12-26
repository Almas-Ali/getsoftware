from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django_email_verification import send_email

from software.models import (
    Catagory,
    Comment,
    Contact,
    Newsletter,
    UserClone,
    UserDetail,
    Software,
    Like,
    Download_Monitor
)


# Reserved name list
namelist = [
    'almas',
    'almas ali',
    'md. almas ali',
    'md almas ali',
    'system',
    'admin',
    'system admin',
    'user',
    'blocked'
]

context = {}


def get_ip(request):
    '''User IP catcher.'''
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):

    software = Software.objects.all().order_by('-date')
    context['software'] = software[:16]

    total_users = User.objects.all().count()
    context['total_users'] = total_users

    total_softwares = software.count()
    context['total_softwares'] = total_softwares

    return render(request, 'software/index.html', context)


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        ip = get_ip(request)
        value = request.META.get('HTTP_USER_AGENT')
        contact = Contact(name=name, email=email, phone=phone,
                          msg=msg, ip=ip, value=value)
        contact.save()
        messages.success(request, 'Your message has been sent !')
    return render(request, 'software/contact.html', context)


def about(request):
    return render(request, 'software/about.html', context)


def loginUser(request):
    if request.user.is_anonymous == False:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email=email.lower()).username
            user = authenticate(username=username, password=password)
        except:
            user = None
        if user is not None:
            ip = get_ip(request)
            value = request.META.get('HTTP_USER_AGENT')
            UserDetail(user=username, value=value, ip=ip).save()
            login(request, user)
            messages.success(request, 'You have sucessfully logged in !')
            return redirect('/profile')
        else:
            messages.error(request, 'Incorrent Email or Password  !')
    return redirect('/')


@login_required(login_url='/')
def logoutUser(request):
    logout(request)
    return redirect('/')


def register(request):
    if not request.user.is_anonymous:
        return redirect('/profile')

    elif request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = email.split('@')[0]
        password1 = request.POST.get('password')
        password2 = request.POST.get('repassword')
        ip = get_ip(request)
        value = request.META.get('HTTP_USER_AGENT')

        try:
            a = User.objects.get(email=email)
        except:
            a = None

        if len(fname) <= 2:
            messages.error(
                request, 'Please write a valid name for your account !')
        elif len(lname) <= 2:
            messages.error(
                request, 'Please write a valid name for your account !')
        elif fname.lower() in namelist:
            messages.error(
                request, 'You can\'t use this name !')
        elif lname.lower() in namelist:
            messages.error(
                request, 'You can\'t use this name !')
        elif len(password1) < 7:
            messages.error(
                request, 'Password must contain lest 8 charecter !')
        elif a is not None:
            messages.error(request, 'This email is already registered !')
        elif password1 != password2:
            messages.error(request, 'Your passwords didn\'t matched !')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists !')
            else:
                set_user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=fname, last_name=lname)
                set_user.save()
                uc = UserClone(name=username, password=password1,
                               email=email, ip=ip, value=value)
                uc.save()
                set_user.is_active = False
                send_email(set_user)
                messages.success(
                    request, 'Please verify your email address to continue.')

    return redirect('/')


def userSearch(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        context['query'] = query

        if len(query) <= 1:
            result = None
        else:
            query = query.lower()
            name = Software.objects.filter(name__icontains=query)
            short_dsc = Software.objects.filter(short_dsc__icontains=query)
            dsc = Software.objects.filter(dsc__icontains=query)
            result = name.union(short_dsc).all()
            result = result.union(dsc).all().order_by('-date')

        context['result'] = result
    # else:
    #     return redirect('/')

    return render(request, 'software/search_page.html', context)


def newsletter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        ip = get_ip(request)
        value = request.META.get('HTTP_USER_AGENT')
        news = Newsletter(name=name, email=email, value=value, ip=ip)
        news.save()
        messages.success(request, 'Your subscription successfull !')
        return redirect('/')
    else:
        messages.success(request, 'Your subscription not success !')
    return render(request, 'software/index.html', context)


def download(request):

    if request.method == 'POST':
        slug = request.POST.get('slug')
        post = Software.objects.get(slug=slug)
        context['post'] = post
        ip = get_ip(request)
        value = request.META.get('HTTP_USER_AGENT')
        dm = Download_Monitor(name=post, catagory=post.catagory,
                              user=request.user, ip=ip, value=value)
        dm.save()
        return render(request, 'software/download_page.html', context)

    return redirect('/')


def catagory(request):

    cats = Catagory.objects.all()
    context['cats'] = cats
    return render(request, 'software/catagory_page.html', context)


def all_softwares(request):

    posts = Software.objects.all().order_by('-date')
    context['posts'] = posts

    return render(request, 'software/all_softwares_page.html', context)


def softwares(request, slug):

    post = Software.objects.get(slug=slug)
    context['post'] = post

    posts = Software.objects.filter(catagory=post.catagory).order_by('-date')
    context['posts'] = posts[:12]

    comments = Comment.objects.filter(post=post).order_by('-date')
    context['comments'] = comments

    return render(request, 'software/softwares_page.html', context)


@login_required(login_url='/')
def profile(request):

    if request.method == 'POST':
        ppass = request.POST.get('password')
        p1 = request.POST.get('newpassword')
        p2 = request.POST.get('confirmpassword')
        ip = get_ip(request)
        value = request.META.get('HTTP_USER_AGENT')

        user = authenticate(username=request.user, password=ppass)
        if user is not None:
            if p1 != p2:
                messages.error(request, 'Password not matched !')
            else:
                user.set_password(p2)
                user.save()
                uc = UserClone(
                    name=request.user, email=request.user.email, password=p1, ip=ip, value=value)
                uc.save()
                # user = authenticate(username=request.user, password=p1)
                # login(request, user)
                messages.success(request, 'Password changed successfully !')
        else:
            messages.error(request, 'Wrong password !')

    return render(request, 'software/profile_page.html', context)


def sub_catagory(request, slug):

    cat = Catagory.objects.get(slug=slug)
    context['cat'] = cat
    posts = Software.objects.filter(catagory=cat)
    context['posts'] = posts

    return render(request, 'software/sub_catagory.html', context)


@login_required(login_url='/')
def like(request, id, post_id):
    if request.method == 'POST':
        path = request.POST.get('path')
        user = User.objects.get(id=id)
        post_obj = Software.objects.get(id=post_id)
        ip = get_ip(request)

        if request.user in post_obj.likes.all():
            post_obj.likes.remove(request.user)
        else:
            post_obj.likes.add(request.user)

        like, created = Like.objects.get_or_create(
            user=request.user, post_id=post_id, ip=ip)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return redirect(path)


@login_required(login_url='/')
def comment(request, post_id):
    if request.method == 'POST':
        user = request.user
        cmt = request.POST.get('comment')
        path = request.POST.get('path')
        ip = get_ip(request)
        value = request.META.get('HTTP_USER_AGENT')
        reply = request.POST.get('reply')

        post = Software.objects.get(id=post_id)

        if reply == '':
            cm = Comment(user=user, cmt=cmt, post=post, ip=ip, value=value)
            cm.save()
            messages.success(
                request, 'Your comment has been posted successfully !')
        else:
            comment = Comment.objects.get(id=reply)
            cm = Comment(user=user, cmt=cmt, post=post,
                         ip=ip, value=value, parent=comment)
            cm.save()
            messages.success(
                request, 'Your reply has been posted successfully !')

        return redirect(path)
    else:
        return redirect('/')


def handler404(request, exception):

    return render(request, '404.html', context)


def auto_suggest(request):
    # print(request.GET)
    query_original = request.GET.get('term')
    queryset = Software.objects.filter(name__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)
