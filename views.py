#from .models import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
#from .templates import*
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.views import View



import sys

sys.path.append(r"C:\Program Files\FME\fmeobjects\python37")
import fmeobjects 
#mport FMEWorkspaceRunner
#from .templates import *
#class fme(admin.ModelAdmin):
    #change_list_template = "path/to/change_form.html"
    
@csrf_exempt
def Run(request):
    parameters = {}
    parameters['_X'] =r"2.3522219"
    parameters['_Y']=r"48.856614"
    parameters['DestDataset_SHAPEFILE'] = r"E:\tmp"
    
    try:
        parameters={}
        workspace=r"C:\Users\r.khamassi\Desktop\projet\Projet\none2shapefile.fmw"
        runner=fmeobjects.FMEWorkspaceRunner()
        print('before run')
        tup=runner.getPublishedParamNames(workspace)
        print(tup)    
        #for i in tup:
            #parameters[i]=input("saisir le paramètre ")
            
        #runner.run(workspace)
        runner.runWithParameters(workspace, parameters)
 
        print('after run')
        return HttpResponse(f"The Workspace: {workspace} ...ran successfully ")
    
    except fmeobjects.FMEException as ex:
    
        return HttpResponse(ex.message)

    runner = None

    
    
    
    
    
    
    
        




               
        #except fmeobjects.FMEException as ex:
            
            #a=ex.message
        
    
    
    #return HttpResponse(runner.run( r"C:\Users\r.khamassi\Desktop\projet\Projet\none2shapefile.fmw"))
    #return render(request,"change_form.html")
        
    