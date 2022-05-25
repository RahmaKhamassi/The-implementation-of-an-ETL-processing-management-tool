from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from colorfield.fields import ColorField

import sys

sys.path.append(r"C:\Program Files\FME\fmeobjects\python37")
import fmeobjects 
license=fmeobjects.FMELicenseManager()
session=fmeobjects.FMESession()
runner=fmeobjects.FMEWorkspaceRunner()

class Categorie (models.Model):
    Nom = models.CharField(primary_key=True,max_length=50)
    Description = models.TextField(null=True,blank=True)
    Couleur = ColorField()


class ProjetFME (models.Model):
    Nom = models.CharField(primary_key=True,max_length=50)
    FichierFmw = models.FileField(blank=False,unique=True,upload_to='none2shapefile.fmw')
    Description = models.TextField(null=True,blank=True)
    Propriétaire = models.ForeignKey(User,on_delete=models.CASCADE)
    Catégorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    DernièreModification=models.DateTimeField(null=True,blank=True)  
    TypeLicence=models.CharField(default=license.getLicenseType(),max_length=60)
    VersionFME=models.CharField(max_length=70,default=session.fmeVersion())
    
    def file_name(self):
        return os.path.basename(self.FichierFmw.name)
    def param(self):
        
        Parametres=models.CharField(max_length=70,default=runner.getPublishedParamNames(self.file_name()))
        return Parametres

class Parametres(models.Model):
    Parametres=models.CharField(max_length=70,default=runner.getPublishedParamNames(ProjetFME.file_name()))

    #def run(self):
        #worksapce=self.file_name()
        #runner.run(worksapce)
    
    #def format(self):
        
#x=ProjetFME()
#x.file_name()
#print(x.file_name())
#class Parametres(models.Model):
    
    #format=models.CharField(default=dialog.guessFormat(x.file_name()),max_length=50)
    
#class InformationsFichierFME(models.Model):
    
    #Format= models.CharField(default=dialog.guessFormat(a),max_length=50)
class Demande (models.Model):
    
    ProjetFME =models.ForeignKey (ProjetFME,on_delete=models.CASCADE)
    #FichierFME=models.ForeignKey(FichierFME)
    DateDeLaDemande=models.DateTimeField(null=True,blank=True)


    
   
    




    
    
    






