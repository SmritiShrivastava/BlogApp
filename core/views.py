from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# registeration View
def homeView(request):
    querySet = BlogModel.objects.all()[::-1]
    context = {
        'models': querySet
    }
    return render(request, "home.html", context)

def signUpView(request):
    if request.method == "POST":
        username = request.POST["username"]
        if userProfiles.objects.filter(username = username).exists():
            messages.warning(request, "username already exists")
            return redirect("signup")
        email = request.POST["email"]
        if userProfiles.objects.filter(email = email).exists():
            messages.warning(request, "email already exists")
            return redirect("signup")
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        contact_number = request.POST["contact_number"]
        gender = request.POST["gender"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            object = userProfiles()
            object.username = username
            object.email = email
            object.set_password(password)
            object.firstName = first_name
            object.lastName = last_name
            object.contactNumber = contact_number
            object.gender = gender
            object.save()
            message_string = "Thankyou "+ username
            messages.success(request, message_string)
            return redirect("login")
        else:
            messages.warning(request, "password doesn,t matched")
            return redirect("signup")
    else:
        form = signUpForm()
        context = {
            'form': form
        }
        return render(request, "signUp.html", context)


def logInView(request):
    if request.method == "POST":
        form = logInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if userProfiles.objects.filter(username = username).exists():
                user = authenticate(request, username =  username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    messages.info(request,"username and password doesn't match")
                    return redirect("login")
            else:
                messages.info(request,"username doesn't exists")
                return redirect("signup")
        else:
            messages.warning(request,"something went wrong")
            return redirect("login")
    else:
        form = logInForm()
        context = {
            'form':form
        }
        return render(request,"login.html",context)

#logout view
def logoutView(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect("home")
	else:
		return redirect("login")


#writeBlog view
def writeBlog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = blogForm(request.POST, request.FILES)
            if form.is_valid():
                blogTitle = form.cleaned_data.get('blogTitle')
                blogDescription = form.cleaned_data.get('blogDescription')
                blogImage = form.cleaned_data.get('blogImage')
                location = form.cleaned_data.get('location')
                blogContent = form.cleaned_data.get('blogContent')
                object = BlogModel.objects.create(
                    blogTitle = blogTitle,
                    blogDescription = blogDescription,
                    blogImage = blogImage,
                    location = location,
                    blogContent = blogContent,
                    user = userProfiles.objects.get(username = request.user)
                )
                object.save()
                messages.success(request, "Congratulations! Your blog is created successfully")
                return redirect("home")
            else:
                messages.info(request, "something went wrong, Please try again")
                return redirect("write")
        else:
            form = blogForm()
            context = {
                'form': form,
                'user': request.user
            }
            return render(request, "writeBlog.html", context)
    else:
        messages.info(request, "please login")
        return redirect("login")


def profilePage(request):
    if request.user.is_authenticated:
        userquery = userProfiles.objects.get(username = request.user)
        blogquery = BlogModel.objects.filter(user = userquery)
        sum1 = 0
        for i in blogquery:
            sum1+=1
        context = {
            'usermodel': userquery,
            'blogmodel': blogquery
        }
        return render(request, "profile.html", context)
    else:
        messages.warning(request, "Please Login")
        return redirect("login")

def detailView(request,id):
    try:
        form = commentForm()
        blogQuery = BlogModel.objects.get(id = id)
        authorQuery = userProfiles.objects.get(username = blogQuery.user)
        likes = likeModel.objects.filter(blog = blogQuery)
        comments = commentsModel.objects.filter(blog = blogQuery)
        no_of_likes = 0
        for i in likes:
            no_of_likes+=1
        no_of_comments = 0
        for i in comments:
            no_of_comments+=1
        context = {
            'blogmodel': blogQuery,
            'author': authorQuery,
            'likes': no_of_likes,
            'comments': comments,
            'no_of_comments': no_of_comments,
        }
        if request.method == "POST":
            comment = request.POST['comment']
            if request.user.is_authenticated:
                model = commentsModel()
                model.comment = comment
                model.blog = blogQuery
                model.user = userProfiles.objects.get(username = request.user)
                model.save()
                return redirect(detailView,id)
            else:
                messages.warning(request,"Please Login First")
                return redirect("login")
        context['form'] = form
        return render(request,"detailedBlog.html", context)
    except Exception as e:
        print(e)
        messages.warning(request, "something went wrong")
        return redirect("home")

def searchView(request):
    if request.method == "POST":
        search = request.POST['search']
        queryset = {}
        if search == " ":
            pass
        else:
            queryset = BlogModel.objects.filter(blogTitle__iexact = search)
        context = {
        	'models' : queryset
        }
        return render(request,"home.html",context)
    else:
        form = Search()
        return redirect("/")


def likeView(request,id):
    try:
        if request.user.is_authenticated:
            userQuery = userProfiles.objects.get(username = request.user)
            blogQuery = BlogModel.objects.get(id = id)
            if likeModel.objects.filter(user = userQuery).exists():
                pass
            else:
                model = likeModel()
                model.user = userQuery
                model.blog = blogQuery
                model.like = 1
                model.save()
            return redirect(detailView, id)
        else:
            messages.info(request, "please login first")
            return redirect("login")
    except Exception as e:
        print(e)
        return redirect(detailView,id)
