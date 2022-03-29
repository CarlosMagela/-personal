from django.views.generic import TemplateView

from .forms import ContatoForm

def contato(request):
    form = ContatoForm()
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

class IndexView(TemplateView):
    template_name = 'index.html'

class ContatoView(TemplateView):
    template_name = 'contato.html'