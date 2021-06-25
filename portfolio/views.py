
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Contact
from.forms import ContactForm


def home(request):
    projects = Project.objects.all().order_by('-created')
    paginator = Paginator(projects, 2)  # 3 posts in each page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # process form data
            obj = Contact()  # gets new object
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            obj.subject = form.cleaned_data['subject']
            obj.message = form.cleaned_data['message']
            # finally save the object in db
            obj.save()
            return HttpResponseRedirect('/')
        else:
            form = ContactForm()
    return render(request, 'portfolio/home.html', {'projects': projects, 'posts': posts, 'page': page, 'form': form})


def ContactView(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # process form data
            obj = Contact()  # gets new object
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            obj.subject = form.cleaned_data['subject']
            obj.message = form.cleaned_data['message']
            # finally save the object in db
            obj.save()
            return HttpResponseRedirect('/')
        else:
            form = ContactForm()

    return render(request, 'portfolio/email.html', {'form': form})


def portfolio_detail(request, pk):
    projects = Project.objects.get(pk=pk)
    return render(request, 'portfolio/portfolio_details.html', {"projects": projects})


def contact(request):
    return render(request, "portfolio/contactme.html")
