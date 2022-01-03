import merger
# Escherichia coli
merger.eggnog_mapper('files/Ecoli_emapper_genepred.fasta', 'files/Ecoli_emapper_annotation.tsv', 'Escherichia_coli')
merger.operon_mapper('files/Ecoli_omapper_ORFs.txt', 'files/Ecoli_omapper_COGs.txt', 'Escherichia_coli')
merger.prokka('files/Ecoli_prokka.gff', 'files/Ecoli_prokka.tsv', 'Escherichia_coli')
merger.CD_Search('files/Ecoli_prokka.gff', 'files/Ecoli_CD_COGs.txt', 'Escherichia_coli')

# Clostridium beijerinckii
merger.eggnog_mapper('files/Clostridium_bei_emapper_genepred.fasta', 'files/Clostridium_bei_emapper_annotation.tsv',
                     'Clostridium_beijerinckii')
merger.operon_mapper('files/Clostridium_bei_omapper_ORFs.txt', 'files/Clostridium_bei_omapper_COGs.txt',
                     'Clostridium_beijerinckii')
merger.prokka('files/Clostridium_bei_prokka.gff', 'files/Clostridium_bei_prokka.tsv', 'Clostridium_beijerinckii')
merger.CD_Search('files/Clostridium_bei_prokka.gff', 'files/Clostridium_bei_CD_COGs.txt', 'Clostridium_beijerinckii')

# Clostridium diolis
merger.eggnog_mapper('files/Clostridium_dio_emapper_genepred.fasta', 'files/Clostridium_dio_emapper_annotations.tsv',
                     'Clostridium_diolis')
merger.operon_mapper('files/Clostridium_dio_omapper_ORFs.txt', 'files/Clostridium_dio_omapper_COGs.txt',
                     'Clostridium_diolis')
merger.prokka('files/Clostridium_dio_prokka.gff', 'files/Clostridium_dio_prokka.tsv', 'Clostridium_diolis')
merger.CD_Search('files/Clostridium_dio_prokka.gff', 'files/Clostridium_dio_CD_COGs.txt', 'Clostridium_diolis')

# Schlegelella thermodepolymerans
merger.eggnog_mapper('files/Schlegelella_emapper_genepred.fasta', 'files/Schlegelella_emapper_annotation.tsv',
                     'Schlegelella_thermodepolymerans')
merger.operon_mapper('files/Schlegelella_omapper_ORFs.txt', 'files/Schlegelella_omapper_COGs.txt',
                     'Schlegelella_thermodepolymerans')
merger.prokka('files/Schlegelella_prokka.gff', 'files/Schlegelella_prokka.tsv', 'Schlegelella_thermodepolymerans')
merger.CD_Search('files/Schlegelella_prokka.gff', 'files/Schlegelella_CD_COGs.txt',
                 'Schlegelella_thermodepolymerans')

# Rhodospirillum rubrum
merger.eggnog_mapper('files/Rrubrum_emapper_genepred.fasta', 'files/Rrubrum_emapper_annotation.tsv',
                     'Rhodospirillum_rubrum')
merger.operon_mapper('files/Rrubrum_omapper_ORFs.txt', 'files/Rrubrum_omapper_COGs.txt',
                     'Rhodospirillum_rubrum')
merger.prokka('files/Rrubrum_prokka.gff', 'files/Rrubrum_prokka.tsv', 'Rhodospirillum_rubrum')
merger.CD_Search('files/Rrubrum_prokka.gff', 'files/Rrubrum_CD_COGs.txt','Rhodospirillum_rubrum')

# Tepidimonas_taiwanensis
merger.eggnog_mapper('files/Tepidimonas_emapper_genepred.fasta','files/Tepidimonas_emapper_annotation.tsv',
                     'Tepidimonas_taiwanensis')
merger.operon_mapper('files/Tepidimonas_omapper_ORFs.txt','files/Tepidimonas_omapper_COGs.txt',
                     'Tepidimonas_taiwanensis')
merger.prokka('files/Tepidimonas_prokka.gff', 'files/Tepidimonas_prokka.tsv', 'Tepidimonas_taiwanensis')
merger.CD_Search('files/Tepidimonas_prokka.gff', 'files/Tepidimonas_CD_COGs.txt','Tepidimonas_taiwanensis')

# Aneurinibacillus thermoaerophilus
merger.eggnog_mapper('files/Aneurinibacillus_emapper_genepred.fasta','files/Aneurinibacillus_emapper_annotation.tsv',
                     'Aneurinibacillus_thermoaerophilus')
merger.operon_mapper('files/Aneurinibacillus_omapper_ORFs.txt','files/Aneurinibacillus_omapper_COGs.txt',
                     'Aneurinibacillus_thermoaerophilus')
merger.prokka('files/Aneurinibacilus_prokka.gff', 'files/Aneurinibacilus_prokka.tsv',
              'Aneurinibacillus_thermoaerophilus')
merger.CD_Search('files/Aneurinibacilus_prokka.gff', 'files/Aneurinibacilus_CD_COGs.txt',
                 'Aneurinibacillus_thermoaerophilus')

