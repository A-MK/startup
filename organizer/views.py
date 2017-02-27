from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http.response import HttpResponse, Http404
from .models import Tag, Startup
from django.template import loader, RequestContext

def tag_list(request):
    #the function without django shortcuts:
    # tag_list = Tag.objects.all()
    # template = loader.get_template('organizer/tag_list.html',using='django')
    # context = RequestContext(request,{'tag_list':tag_list})
    # output = template.render(context)
    # return HttpResponse(output)
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list':Tag.objects.all()}
        )

def tag_detail(request,slug):
    #the function without django shortcuts:
    # try:
    #     tag = Tag.objects.get(slug__iexact=slug)
    # except Tag.DoesNotExist:
    #     raise Http404
    # else:
    #     template = loader.get_template('organizer/tag_detail.html')
    #     context = RequestContext(request,{'tag':tag})
    #     output = template.render(context)
    #     return HttpResponse(output)
    tag = get_object_or_404(Tag,slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag':tag}
        )

def startup_list(request):
    return render(
                request,
                'organizer/startup_list.html',
                {'startup_list':Startup.objects.all()})

#def 
