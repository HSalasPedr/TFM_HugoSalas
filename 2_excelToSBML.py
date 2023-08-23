#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cobra as cb
from importExcelModel import *

def excel_to_sbml(model2, modelName):
    model=import_excel_model(model2)
    
    for i in model.metabolites:
        i = i.id
        formula=model.metabolites.get_by_id(i).formula
        try:
            model.metabolites.get_by_id(i).formula = str(formula)
        except ValueError:
            print("Error en estos metabolitos al poner su formula en str: ", i,"\n")

        carga=model.metabolites.get_by_id(i).charge
        try:
            model.metabolites.get_by_id(i).charge = int(carga)
        except ValueError:
            print("Error en estos metabolitos al poner su carga en str: ", i,"\n")
    for i in model.reactions:
        i = i.id
        nombre=model.reactions.get_by_id(i).name
        try:
            model.reactions.get_by_id(i).name = str(nombre)
        except ValueError:
            print("Error al poner el nombre de estas reacciones en str: ", i,"\n")
    
    cb.io.write_sbml_model(model, modelName+".xml")
    
    return ("SBML file ", modelName+".xml", " created")

