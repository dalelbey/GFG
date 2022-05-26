"""
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def redirect(request):
    return HttpResponseRedirect('home')

def index(request):
    if request.user.is_authenticated:
        return render(request , 'index.html')
    else:
        return  HttpResponseRedirect('dashborad/login')

def login(request):
    if request.user.is_authenticated:
         return HttpResponseRedirect('/dashborad')
    else:
        return render(request , 'user/login.html')  
"""   
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render, redirect
from dashboard.models import Order
from django.core import serializers
import pandas as pd 
from ftplib import all_errors
from os import link
import time
from selenium import webdriver
import csv

"""
def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {}) #fonction qui dirige un utilisateur vers les modèles spécifiques définis dans le dashboard/templates

def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False) #méthode auxiliaire qui envoie la réponse avec les données au tableau croisé dynamique sur le front-end de l'application.
"""
def index(request):

    data = pd.read_csv("C:\\Users\\ACER\\scraping_playstore.csv")
    return render(request, 'dashboard/index.html')

def charts(request):
    return render(request, 'dashboard/charts.html')


def widgets(request):
    return render(request, 'dashboard/widgets.html')




def tables(request):
    return render(request, "dashboard/tables.html")




def grid(request):
    return render(request, "dashboard/grid.html")




def form_basic(request):
    return render(request, "dashboard/form_basic.html")




def form_wizard(request):
    return render(request, "dashboard/form_wizard.html")




def buttons(request):
    return render(request, "dashboard/buttons.html")




def icon_material(request):
    return render(request, "dashboard/icon-material.html")




def icon_fontawesome(request):
    return render(request, "dashboard/icon-fontawesome.html")




def elements(request):
    return render(request, "dashboard/elements.html")




def gallery(request):
    return render(request, "dashboard/gallery.html")





def invoice(request):
    return render(request, "dashboard/invoice.html")



def chat(request):
    return render(request, "dashboard/chat.html")

def search(request):
    search = request.GET['search']
    driver = webdriver.Chrome()
    url='https://play.google.com/store/apps/'
    query = "&showAllReviews=true"
    driver.get(url +search + query )
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
       elem.click()
       time.sleep(1)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    list_all_elements = []
    for i in len(elems): 
       app_name = driver.find_element_by_tag_name("h1").text
       nbretoiles = driver.find_element_by_class_name("BHMmbe").text
       others = driver.find_elements_by_class_name("htlgb")
       list_others = []
       for x in range (len(others)):
          if x % 2 == 0:
             list_others.append(others[x].text)
    titles = driver.find_elements_by_class_name("BgcNfc")
    nbrreview = driver.find_element_by_class_name("EymY4b").text
    list_elements = [app_name, float(nbretoiles.replace(",",".")), nbrreview ]#.split()[0]
    for x in range (len(titles)):
      if titles[x].text == "Installations":
          list_elements.append(list_others[x])
      if titles[x].text == "Taille":
                list_elements.append(list_others[x])
      if titles[x].text == "Développeur":
            for y in list_others[x].split("\n"):
                if "@" in y:
                    list_elements.append(y)
                    break 

    list_all_elements.append(list_elements)
    context = {
        'list_all_elements' : list_all_elements

    }
    

   


   #df = pd.DataFrame(list_all_elements,columns=['Name', 'nbretoiles', 'nbrreview', 'Taille', 'Installs', 'Email Address'])
   # df.to_csv('scraping_playstore.csv', header = True, index=False)       
   
    
    return render(request, 'search.html', context)

