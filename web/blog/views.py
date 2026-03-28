from django.shortcuts import render
from django .shortcuts import get_object_or_404
from django.db.models import  Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
from .models import Myblog


def ListBlog ( request): 
    obj = Myblog.objects.all()
    paginator = Paginator(obj,3)
    page = request.GET.get('page')
    print(page)
    try:
        page = obj=paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
    print(obj)
    return render (request, "list.html" , {"list":obj,'page':page})



def DetailBlog (request, slug):
    obj= get_object_or_404(Myblog,slug=slug)
    return render (request, "detail.html" , {"detail" :obj})



def search(request):
    query=None
    result=[]
    if request.method=="GET":
        query=request.GET.get("search")
        result=Myblog.objects.filter(Q(title__icontains=query) | Q(des__icontains=query)  ) 
    return render(request, 'search.html', {'query':query, 'results':result}) 
    
