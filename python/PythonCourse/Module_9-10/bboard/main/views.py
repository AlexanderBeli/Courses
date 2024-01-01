from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def profile(request):
    return render(request, 'main/profile.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.method = POST['pswd']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect()#User to the dashboard!)
        else:
            message.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
class BBLoginView(LoginView):
    template_name = 'main/login.html'

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

def index(request):
    return render(request, 'main/index.html')