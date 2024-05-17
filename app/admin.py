from django.contrib import admin

from app.models import Valyuta, Categories, Product

admin.site.register([Valyuta, Categories, Product])
