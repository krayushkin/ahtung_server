from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View
from django.http import HttpResponse
from django.core import serializers
from ahtung_api.models import Person, Group, Signal, EnabledSignal
from ahtung_api.populate_db import populate

class AhtungApi:
    COMMAND_GET_USERS = "get_users"
    COMMAND_JOIN_GROUP = "join_group"
    COMMAND_LEAVE_GROUP = "leave_group"
    COMMAND_CREATE_GROUP = "create_group" # registration_id, name, enabled_signals
    COMMAND_SEND_SIGNAL = "send_signal"

class PopulateView(View):
    def get(self, request, *args, **kwargs):
        populate()
        return HttpResponse("populated")

class ApiView(View):
    template_name = "test.js"

    func_name = "UNSUPPORTED"
    func_args = {}
    r = None
   

    def get(self, request, *args, **kwargs):
        params = request.GET
        action = params['action']

        data = "Nichego net vashpe -((((("
    
        if action == AhtungApi.COMMAND_GET_USERS:
            group_id = params['group_id']
            users = Person.objects.filter(group__group_id__exact = group_id)
            data = serializers.serialize("json", users, indent=2)

        elif action == AhtungApi.COMMAND_JOIN_GROUP:
            group_id = params['group_id']
            registration_id = params['registration_id']
            name = params['name']
            group = Group.objects.get(group_id__exact=group_id)
            person = Person(group=group, name=name, registration_id=registration_id)
            person.save()
            data = "Person {0} added".format(person.pk)
        elif action == AhtungApi.COMMAND_LEAVE_GROUP:
            registration_id = params['registration_id']
            person = Person.objects.get(registration_id__exact=registration_id)
            person_pk = person.pk
            person.delete()
            data = "Person {0} deleted".format(person_pk)

        elif action == AhtungApi.COMMAND_CREATE_GROUP:
            Group()

        return HttpResponse(data, content_type="text/json")

    def get_context_data(self, **kwargs):
        context = super(ApiView, self).get_context_data(**kwargs)
        context['test'] = self.r
        return context
