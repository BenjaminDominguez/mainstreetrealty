from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages
from django.template import loader
from django.utils.html import strip_tags
from .models import Property
from .forms import CMAForm, IndexForm
import os
# Create your views here.

def index(request):
    active_properties = Property.objects.filter(status__name="Active")
    first_two_properties = active_properties[0:2]
    after_two_properties = active_properties[2:]

    if request.method == "POST":
        form = IndexForm(request.POST)
        if form.is_valid():
            mail_subject = 'New lead for FHA from website!'
            lead = form.cleaned_data['email']
            html_body = loader.render_to_string('properties/lead.html', {
            'lead': lead,
            'type':
            'FHA/Lending',
            'cma': False,
            'offer': 'free appraisal upon working with them'})
            mail_body = strip_tags(html_body)
            mail_recipient = ['info@mainstreetrealtyandassociates.com', 'bendominguez011@gmail.com']
            mail_sender = 'fhanewlead@gmail.com'
            send_mail(mail_subject, mail_body,\
            mail_sender, mail_recipient, html_message=html_body, fail_silently=False)
            return HttpResponseRedirect(reverse('properties:index'))
    else:
        form = IndexForm()
    context = {
    'first_two_properties': first_two_properties,
    'after_two_properties': after_two_properties,
    'form': form
    }

    return render(request, 'properties/index.html', context)

def cma(request):
    if request.method == "POST":
        form = CMAForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lead = form.cleaned_data['email']
            mail_subject = 'New lead for main st. realty from website!'
            html_body = loader.render_to_string('properties/lead.html', {
            'lead': lead,
            'type': 'real estate/comparative market analysis',
            'cma': True,
            'name': name,
            'offer': 'comparative market analysis'
            })
            mail_body = strip_tags(html_body)
            mail_recipient = ['info@mainstreetrealtyandassociates.com', 'bendominguez011@gmail.com']
            mail_sender = 'fhanewlead@gmail.com'
            send_mail(mail_subject, mail_body,\
            mail_sender, mail_recipient, html_message=html_body, fail_silently=False)
            new_user = form.save()
            messages.success(request, 'Thank you for filling out the form! We will get back to you in 1-2 business days.')
            return HttpResponseRedirect(reverse('properties:cma'))
    else:
        form = CMAForm()
    context = {
    'form': form,
    'title': 'Main Street Realty | Form'
    }
    return render(request, 'properties/cma.html', context)
