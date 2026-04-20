'''
Parse raw Tobii files
The tvs/csv files extracted from 40-45 minutes experiment is around 1GB and reading/writing and processing a big data frame takes longer.
This script splits them into small csv files per subject and per news item. 
'''
import argparse 
import os, sys
import glob
import numpy as np
import pandas as pd

def main(args):

    # The raw data will be under $root_folder/data/raw/
    # create a directory for processed files ($root_folder/data/processed/)
    root_folder = args.root_folder
    section = args.section
    if not os.path.exists('%s/data/processed/section_%d'%(root_folder, section)):
        os.makedirs('%s/data/processed/section_%d'%(root_folder, section))

    # Iterate for all participants to get data question-by-question and the original order/version
    for participant_num in range(1, 28):
        
        print('Processing raw files (P%02d)'%(participant_num))

        tobii_file = glob.glob('%s/data/raw/%02d/*.tsv'%(root_folder,participant_num))[0]
        metadata_file = glob.glob('%s/data/raw/%02d/version_*/section_1/metadata.csv'%(root_folder,participant_num))[0]

        df = pd.read_csv(tobii_file, sep='\t', low_memory=False)
        metadata = pd.read_csv(metadata_file)

        key_values = ['Instruction 1']
        save_paths = ['%s/data/processed/P%02d_instructions.csv'%(root_folder, participant_num)]
        for index in range(0, metadata.shape[0]): #  question: 1,2,3,...,60
            # get Stimulus n (1-60)
            if section==1:
                key_values.append('Stimulus%d'%(index+1))
            elif section==2:
                key_values.append('Stimulus%d_2'%(index+1))

            # Note: There is an issue in Stimuli-27 (All users saw fake version, with Bayern. "03_07_02-Osten.html")
            question = metadata.iloc[index]['order']
            version = metadata.iloc[index]['version']
            version = 'fake' if question==27 else version
            filename = 'P%02d_Q%02d_%s'%(participant_num, question, version)
            save_paths.append('%s/data/processed/section_%s/%s.csv'%(root_folder, section, filename))
        
        for index in range(0, len(key_values)):
            key_value, save_path  = key_values[index], save_paths[index]

            # filter the related part of data frame
            if section==1:
                df_stimulus = df[df['Presented Stimulus name']==key_value].reset_index(drop=True)
            elif section==2:
                idx_min = np.min(np.argwhere(df['Presented Stimulus name'].to_numpy()==key_value).squeeze())
                idx_max = np.max(np.argwhere(df['Presented Stimulus name'].to_numpy()==key_value).squeeze())
                df_stimulus = df.iloc[idx_min:idx_max].reset_index(drop=True)

            # rename and save it with the name in the original order and version (fake/true)
            df_stimulus.to_csv(save_path, index=False)


if __name__ == '__main__':
    
    root_folder = os.getcwd()
    parser = argparse.ArgumentParser(description='Split Raw Tobii Files into Blocks (per subject, per news item)')
    parser.add_argument("--root-folder",    default=root_folder,    type=str,  help="root folder")
    parser.add_argument("--section",        default=1,              type=int,  help="section 1 or 2")
    args = parser.parse_args()
    main(args)