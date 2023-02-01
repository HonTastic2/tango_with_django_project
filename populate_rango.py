import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    
    python_pages = [
    {'title': 'Official Python Tutorial',
    'url':'http://docs.python.org/3/tutorial/'},
    {'title':'How to Think like a Computer Scientist',
    'url':'http://www.greenteapress.com/thinkpython/'},
    {'title':'Learn Python in 10 Minutes',
    'url':'http://www.korokithakis.net/tutorials/python/'} ]

    django_pages = [
    {'title':'Official Django Tutorial',
    'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
    {'title':'Django Rocks',
    'url':'http://www.djangorocks.com/'},
    {'title':'How to Tango with Django',
    'url':'http://www.tangowithdjango.com/'} ]
    
    other_pages = [
    {'title':'Bottle',
    'url':'http://bottlepy.org/docs/dev/'},
    {'title':'Flask',
    'url':'http://flask.pocoo.org'} ]
    
    cats = {'Python': {'pages': python_pages},'Django': {'pages': django_pages}, 'Other Frameworks': {'pages': other_pages} }
    
    for cat, cat_data in cats.items():
        if (cat=='Python'):
            c = add_cat(cat, 128, 64)
        elif (cat=='Django'):
            c = add_cat(cat, 64, 32)
        elif (cat =='Other Frameworks'):
            c = add_cat(cat, 32, 16)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], random.randint(1,500))
          
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')
            
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
    
def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes=likes
    c.views=views
    c.save()
    return c
    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()