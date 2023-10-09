from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'card/main_list.html', {})

def record(request):
    return render(request, 'card/record.html', {})