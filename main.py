import pandas as pd
import numpy as np
import time

if __name__ == '__main__':

    prob_df = pd.read_csv('CRISPR_gene_dependency 3.06.36 PM.csv').reset_index()
    label_df = pd.read_csv('sample_info.csv').reset_index()
    label_df = label_df[['DepMap_ID', 'stripped_cell_line_name',
                         'sex', 'sample_collection_site', "primary_or_metastasis",
                         "primary_disease", "Subtype", 'age', 'default_growth_pattern']]

    combined_df = pd.merge(prob_df, label_df, left_on='DepMap_ID', right_on='DepMap_ID')

    cancer_bool = combined_df['primary_disease'] == 'Non-Cancerous'

    combined_df['is_cancer'] = cancer_bool.replace({False:1, True:0})




