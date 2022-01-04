# This script was created for the purpose of comparing four tools (eggNOG-mapper, Operon-mapper, Prokka, Batch CD-Search)
# in my bachelor thesis (Functional annotation of non-model bacteria based on sequential homology). These functions merge 
# the files of each tool into the table that contains id, start, end and OG assignment for each CDS.

# Author: Petra Polakovičová

# These tools are available at:
# eggNOG-mapper: https://github.com/eggnogdb/eggnog-mapper
# Operon-mapper: https://biocomputo.ibt.unam.mx/operon_mapper/
# Prokka: https://github.com/tseemann/prokka
# Batch CD-Search: https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi

import csv
from Bio import SeqIO

def eggnog_mapper(gene_prediction_file, annotation_file, organism_name):
    with open('tables/eggNOG_mapper_' + organism_name + '.csv', "w", newline='') as eggnog_file:
        csv_writer = csv.writer(eggnog_file)
        fieldnames = ['id', 'start', 'end', 'OG']
        csv_writer.writerow(fieldnames)

        for seq_record in SeqIO.parse(gene_prediction_file, "fasta"):
            description = seq_record.description.split(' # ')
            id_seq = description[0]
            with open(annotation_file) as cog_file:
                for cog_row in cog_file:
                    id_cog = (cog_row.split('\t'))[0]
                    if id_cog == id_seq:
                        cog = cog_row.split('\t')[4]
                        cog = cog.split('@')
                        csv_writer.writerow([id_seq, description[1], description[2], cog[0]])


def operon_mapper(ORF_file, COG_file, organism_name):
    with open ('tables/operon_mapper_'+ organism_name + '.csv',"w",newline='') as operon_file:
        csv_writer = csv.writer(operon_file)
        fieldnames = ['id', 'start', 'end', 'OG']
        csv_writer.writerow(fieldnames)

        with open(ORF_file,'r') as ORFfile:
            for row_orf in ORFfile:
                IDorf = (row_orf.split('\t'))[8][3:17]

                with open(COG_file) as COGfile:
                    for row_cog in COGfile:
                        IDcog = (row_cog.split('\t'))[0]

                        if IDorf == IDcog:
                            row_orf = row_orf.split('\t')
                            csv_writer.writerow([IDorf,row_orf[3],row_orf[4],(row_cog.split('\t'))[1]])


def prokka(genes_file, COG_file, organism_name):
    with open('tables/prokka_' + organism_name+'.csv',"w",newline='') as prokka_file:
        csv_writer = csv.writer(prokka_file)
        fieldnames = ['id', 'start', 'end', 'OG']
        csv_writer.writerow(fieldnames)
        with open(genes_file,'r') as GeneFile:
            for gene_row in GeneFile:
                IDgene = (gene_row.split('\t'))[8][3:17]

                with open(COG_file) as cog_file:
                    for cog_row in cog_file:
                        IDcog = (cog_row.split('\t'))[0]
                        if IDgene == IDcog:
                            gene_row = gene_row.split('\t')
                            if (cog_row.split('\t'))[5][0:3] == 'COG':
                                csv_writer.writerow([IDgene,gene_row[3],gene_row[4],(cog_row.split('\t'))[5]])


def CD_Search(genes_file, COG_file, organism_name):
    with open('tables/cdd_'+organism_name+'.csv', "w", newline='') as cdd_file:
        csv_writer = csv.writer(cdd_file)
        fieldnames = ['id', 'start', 'end', 'OG']
        csv_writer.writerow(fieldnames)
        with open(genes_file, 'r') as gene_file:
            for gene_row in gene_file:
                IDgene = (gene_row.split('\t'))[8][3:17]
                with open(COG_file) as cog_file:
                    for row in cog_file:
                        IDcog = (row.split('>'))[1][0:14]
                        if IDgene == IDcog:
                            start = (gene_row.split('\t'))[3]
                            end = (gene_row.split('\t'))[4]
                            try:
                                index = row.index('COG')
                                cog = row[index:index + 7]
                                csv_writer.writerow([IDgene, start, end, cog])
                            except:
                                pass

