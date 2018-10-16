from django.shortcuts import render
from Mainsite.models import Article


# Create your views here.
def index(request):
    context = {'articles1': Article.objects.order_by('createdAt')[:3],
               'articles2': Article.objects.order_by('createdAt')[3:]
               }
    return render(request, "index.html", context)


def articleView(request, id):
    obj = Article.objects.get(pk=id)
    context = {'article': obj}
    return render(request, "generic.html", context)
