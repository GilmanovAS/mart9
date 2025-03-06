from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main_page/main.html')


def question1(request):
    return render(request, 'templates1/quest1.html')


def question2(request):
    return render(request, 'templates2/quest2.html')


def question3(request):
    return render(request, 'templates3/quest3.html')


def question4(request):
    return render(request, 'templates4/quest4.html')


def question5(request):
    return render(request, 'templates5/quest5.html')


def question6(request):
    return render(request, 'templates6/quest6.html')
