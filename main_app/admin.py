from django.contrib import admin
from .models import Cat, Feeding, Toy

# Register your models here.
admin.site.register(Cat) # to see the model in admin site
admin.site.register(Feeding)
admin.site.register(Toy)
