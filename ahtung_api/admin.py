from django.contrib import admin

from ahtung_api.models import Person, Group, Signal, EnabledSignal
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Signal)
admin.site.register(EnabledSignal)

# Register your models here.
