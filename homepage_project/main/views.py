from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/index.html', {})

def exrave(request):
    return render(request, 'main/exrave.html', {})
