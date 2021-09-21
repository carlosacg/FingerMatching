from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render, redirect
from apps.matching.forms import UploadImageForm
from django.urls import reverse_lazy
from apps.matching.fnutils import get_match
from django.contrib import messages


class Matching(View):
    name = 'match_image'
    image = None

    def get(self,request,*args,**kwargs):
        form = UploadImageForm()
        context = {
            'form':form,
        }
        return render(request,'matching_template.html',context)

    def post(self, request, *args, **kwargs):
        form = UploadImageForm(self.request.POST, self.request.FILES)
        image_object = form.save()
        percentage, file = get_match(image_object.image.url[1:len(image_object.image.url)])
        if file:
            message_str = "Se encontro una coincidencia del {} % con el archivo {}".format(percentage,file)
            messages.success(request, message_str)
        else:
            message_str = "No se encontro ninguna coincidencia"
            messages.error(request, message_str)
        return redirect(reverse_lazy("match_image"))