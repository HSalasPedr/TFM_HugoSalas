#%% Conseguir las entradas de 'locus_tag' y 'old_locus_tag'
from Bio import SeqIO

in_file = 'Modelos/P meg DSM319/genome_assemblies_genome_gb/ncbi-genomes-2023-01-26/GCF_000025805.1_ASM2580v1_genomic.gbff'

a = SeqIO.read(in_file, 'gb').features
aux = a[1:] #El primer elemento sobra, es la secuencia completa del genoma

# Creamos dos listas para almacenar los nombres de los locus tag viejos y nuevos
locus_tags = [None]*len(aux)
old_locus_tags = [None]*len(aux)

# Recorremos la lista y almacenamos los nombres de los genes
for element in range(len(aux)):
    try:
        locus_tags[element] = aux[element].qualifiers['locus_tag'][0]
        old_locus_tags[element] = aux[element].qualifiers['old_locus_tag'][0]
    except:
        locus_tags[element], old_locus_tags[element] = None, None

#Quitamos las instancias de None que hayan quedado
locus_tags_final = [i for i in locus_tags if i is not None]
old_locus_tags_final = [i for i in old_locus_tags if i is not None]

#%% Construir el diccionario tal que las claves sean locus_tag y los valores
# los old_locus_tag, eso se le pasa a Cobra y los renombra en el modelo
cobra_dict = dict(zip(old_locus_tags_final, locus_tags_final))

#%% Ahora renombramos los genes en el modelo y sacamos un nuevo excel
import cobra as cb
from cobra.io import read_sbml_model, write_sbml_model

model = read_sbml_model('Modelos/P meg DSM319/DSM319.xml')

#Cambiamos los ids de los genes del modelo
cb.manipulation.modify.rename_genes(model, cobra_dict)

#%% Guardamos el modelo en un xlsx, que es de más fácil interpretación que el xml

import importExcelModel
importExcelModel.cobrapy_to_excel(model, "Modelos/P meg DSM319/DSM319_fixedIDs.xlsx")

#También en xml para usarlo más adelante
write_sbml_model(model,'Modelos/P meg DSM319/DSM319_fixedIDs.xml')