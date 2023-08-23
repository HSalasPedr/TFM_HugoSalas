#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:18:07 2023

@author: hugo
"""

from Gapfilling import *
import modelseed_gapfilling
import cobra
from cobra.flux_analysis import gapfill

#%% Load necessary files for gapfilling

PmegMOA_mod = read_sbml_model('Modelos/PmegMOA/PmegMOA_ExFixed.xml')
DSM319_mod = read_sbml_model('Modelos/P meg DSM319/DSM319_fixedIDs.xml')
WSH002_mod = read_sbml_model('Modelos/P meg WSH002/PmegWSH002_fixed.xml')
iml1515 = load_model("textbook") # E. coli iML1515 already comes with cobra

#%%
'''
reactions=PmegMOA_mod.reactions
for r in reactions:
    re=r.id
    if re.startswith('Ex'):
        r.bounds=-100,100
    print(re)
'''
#%% Run gapfilling method

out_1 = homology_gapfilling(model = PmegMOA_mod,
                                     templates = [DSM319_mod],
                                     model_obj = True,
                                     template_obj = True,
                                     use_all_templates = True,
                                     integer_threshold = 1e-9,
                                     force_exchange = True,
                                     force_transport = True,
                                     t_all_compounds = True,
                                     t_ignore_h = False,
                                     value_fraction = 0.8)

#%%
out_2 = homology_gapfilling(model = PmegMOA_mod,
                                     templates = [DSM319_mod, WSH002_mod],
                                     model_obj = True,
                                     template_obj = True,
                                     use_all_templates = True,
                                     integer_threshold = 1e-9,
                                     force_exchange = True,
                                     force_transport = True,
                                     t_all_compounds = True,
                                     t_ignore_h = False,
                                     value_fraction = 0.8)
#%%









