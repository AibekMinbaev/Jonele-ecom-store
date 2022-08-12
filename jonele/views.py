from curses.ascii import HT
from django.shortcuts import render
from django.shortcuts import HttpResponse 

def homepage(request): 
    return render(request, 'jonele/homepage.html')  


def allproducts(request): 
    return render(request, 'jonele/allproducts.html')


def checkout(request): 
    return render(request, 'jonele/checkout.html') 


def cart(request): 
    return render(request, 'jonele/cart.html') 
    









