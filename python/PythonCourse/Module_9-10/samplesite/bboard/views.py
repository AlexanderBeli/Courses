from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Bb
from .models import Rubric
from .forms import BbForm


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'by_rubric.html', context)

def index(request):
    bbs = Bb.objects.all()  # 6й заход
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'index.html', context)


    # bbs = Bb.objects.all()                                  #5й заход
    # return render(request, 'index.html', {'bbs': bbs})

    # bbs = Bb.objects.order_by('-published')                 #4й заход
    # return render(request, 'index.html', {'bbs': bbs})

    # template = loader.get_template('index.html')            #3й заход
    # bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    # return HttpResponse(template.render(context, request))

    # return HttpResponse("Здесь будет выведен список объявлений.") #1й заход

    # s = 'Список объявлений\r\n\r\n\r\n'                           #2й заход
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain: charset=utf-8')