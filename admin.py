from django.contrib import admin
from .models import ProjetFME,Demande,Categorie
from django.shortcuts import render
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy
from .templates import *
from django.http import HttpResponse
from .models import Demande,ProjetFME

from django.contrib import admin
from django.urls import path,include
import sys
sys.path.append(r"C:\Program Files\FME\fmeobjects\python37")
import fmeobjects

admin.site.site_header="FME"
# initiate FMEWorkspaceRunner Class
#runner = fmeobjects.FMEWorkspaceRunner()
dialog= fmeobjects.FMEDialog()
log=fmeobjects.FMELogFile()


#from .templates.admin import change_form


class ProjetFMEAdmin(admin.ModelAdmin):
    list_display = ('Nom','FichierFmw','Description','Propriétaire')
    list_filter=('Catégorie','DernièreModification','Propriétaire')
    search_fields=('Nom','ProjetFMEAdmin')

admin.site.register(ProjetFME,ProjetFMEAdmin)
#admin.site.register(Parametres)
admin.site.unregister(Group)



#admin.site.register(InformationsFichierFME)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('Nom','Description','Couleur')
    search_fields=('Nom',)

admin.site.register(Categorie,CategorieAdmin)

class DemandeAdmin(admin.ModelAdmin):
    #list_display=('ProjetFME','DateDeLaDemande') 
    """
    change_form_template="change_form.html"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(r'my_view/', self.my_view,name="custom_view")
        ]
        urls = my_urls + urls
        return urls
        

    

    def my_view(self, request):
        if foo:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            return HttpResponse('<h1>Page was found</h1>')
        

        
    """
            
            
admin.site.register(Demande)
        
        

