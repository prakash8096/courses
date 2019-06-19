from django.views.generic.edit import CreateView
from .models import Contact

# Create your views here.
class Contactuss(CreateView):
    model=Contact
    template_name='contactus.html'
    fields = '__all__'