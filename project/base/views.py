from django.shortcuts import render

def main_page(req):
    return render(req, 'main.html')