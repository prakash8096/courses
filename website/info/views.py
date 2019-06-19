from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from .models import Ganesh

class Prakash(TemplateView):
    template_name='home.html'

class Ajay(TemplateView):
    template_name='rating.html'

class Maths(TemplateView):
    template_name='mpc.html'
class Image(TemplateView):
    template_name='image.html'
class Gaanesh(TemplateView):
    template_name='ajayhtml.html'
class Engineering(TemplateView):
    template_name='engg.html'
class Bsc(TemplateView):
    template_name='bsc.html'
class Navy(TemplateView):
    template_name='navy.html'
class Architecture(TemplateView):
    template_name='arch.html'
class Law(TemplateView):
    template_name='law.html'
# Create your views here.
class Data(ListView):
    model=Ganesh
    template_name='rev.html'
class Create(CreateView):
    model=Ganesh
    template_name='create.html'
    fields='__all__'

class Detail(DetailView):
    model=Ganesh
    template_name='detail.html'
    context_object_name='batman'
class Updateview(UpdateView):
    model=Ganesh
    template_name='update.html'
    fields='__all__'
