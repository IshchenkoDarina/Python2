from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values':
                                                      ["Contact by email", "darina.ishchenko17@gmail.com"]})
