from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def java_page_view(request):
    return render(request,'testapp/javaexams.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form = SignUpForm()
    return render(request, 'testapp/signup.html', {'form': form})

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form.save()
    return render(request,'testapp/signup.html',{'form':form})