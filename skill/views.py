from multiprocessing import context
from turtle import title
from django.shortcuts import render
from .models import Myskill, Contact


def homepage(request):

    item = Myskill.objects.all()

    title = 'Welcome To my Website.'
    desc = 'Looking for Graphic Design Services? Browse Fiverr Freelancers by skills, reviews, and price. Select the right Freelancer to meet your needs and budget.'

    context = {
        'title': title,
        'desc': desc,
        'data': item,
    }
    return render(request, 'index.html', context)


def aboutpage(request):

    title = ' About Page for Skill App'
    desc = 'Regardless of whether youre looking for a new logo or some stunning flyers, our creators can make it happen. There no restriction to what you can get designed. From individual design services and little one-time projects as far as possible up to global graphic design projects requiring many professional designers working exclusively on contract to your company.Regardless of whether youre looking for a new logo or some stunning flyers, our creators can make it happen. There no restriction to what you can get designed. From individual design services and little one-time projects as far as possible up to global graphic design projects requiring many professional designers working exclusively on contract to your company'

    context = {
        'title': title,
        'aboutdesc': desc,
    }

    return render(request, 'about.html', context)


def contactpage(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('comments')

        # mydata =Contact( cname = name, cemail = email, cquery = query)
        mydata = Contact()
        mydata.cname = name
        mydata.cemail = email
        mydata.cquery = query

        mydata.save()

    return render(request, 'contact.html')


def mobile(request):
    return render(request, 'mobile.html')


def laptop(request):
    return render(request, 'laptop.html')


def computer(request):
    return render(request, 'computer.html')


def accessories(request):
    return render(request, 'accessories.html')
