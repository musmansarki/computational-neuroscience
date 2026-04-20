'''
Extracts features from raw Tobii files (each file read here belongs to viewing single news item)
'''
import argparse 
import os, sys
import glob
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

def main(args):

    root_folder = args.root_folder
    print('participant,question,version,viewingTimeSec,fixationCount,saccadeCount,meanFixationDuration,meanSaccadeDuration,meanPupilDiamater,meanPupilDiamaterFixation,minFixationDuration,maxFixationDuration,minSaccadeDuration,maxSaccadeDuration')
    for participant_num in range(1, 28):

        # Before reading the fake news data first read instruction screen and calculate pupil baseline
        df_baseline = pd.read_csv('%s/data/processed/P%02d_instructions.csv'%(root_folder, participant_num), low_memory=False)
        valid_indices = (df_baseline['Sensor'].to_numpy()=='Eye Tracker') & (df_baseline['Validity left'].to_numpy()=='Valid') & (df_baseline['Validity right'].to_numpy()=='Valid')
        df_baseline = df_baseline.iloc[valid_indices].reset_index(drop=True)

        time_msec = [ df_baseline.iloc[i]['Recording timestamp']- df_baseline.iloc[i-1]['Recording timestamp']   for i in range(1, df_baseline['Recording timestamp'].shape[0])]
        time_msec = [0] + time_msec

        pupil_d_left_baseline = np.array([str(i).replace(',','.') for i in df_baseline['Pupil diameter left'].to_list()]).astype(np.float)
        pupil_d_right_baseline = np.array([str(i).replace(',','.') for i in df_baseline['Pupil diameter right'].to_list()]).astype(np.float)

        pupil_baseline = 0.5 * (pupil_d_left_baseline + pupil_d_right_baseline)
        pupil_baseline = np.median(pupil_baseline[0:10])


        # Now read all fake news data belong to the participant_num
        file_names = sorted(glob.glob('%s/data/processed/section_1/P%02d_Q*.csv'%(root_folder, participant_num)))

        for file_index in range(60):

            # read data frame
            df = pd.read_csv(file_names[file_index], low_memory=False)

            # Eye tracker Success ratio
            conditions_section1_total = (df['Sensor'].to_numpy()=='Eye Tracker')
            conditions_section1_valid = (df['Sensor'].to_numpy()=='Eye Tracker') & (df['Validity left'].to_numpy()=='Valid') & (df['Validity right'].to_numpy()=='Valid')
            successRatio =  np.sum(conditions_section1_valid) / np.sum(conditions_section1_total)     
            #print('successRatio=%2.2f  (%d / %d)'%(successRatio,  np.sum(conditions_section1_valid), np.sum(conditions_section1_total)))

            if successRatio>=0.80:

                # First. let's filter and normalize pupil diameters
                time_sec = (df['Recording timestamp'] - df['Recording timestamp'].min())  / 1e3
                pupil_d_left_raw = np.array([str(i).replace(',','.') for i in df['Pupil diameter left'].to_list()]).astype(np.float)
                pupil_d_right_raw = np.array([str(i).replace(',','.') for i in df['Pupil diameter right'].to_list()]).astype(np.float)

                # Applying SavGol filter directly causes SVD error in optimization when there are nan values
                idx_not_nan = np.argwhere(~np.isnan(pupil_d_left_raw)).squeeze()
                pupil_d_left_filtered = np.copy(pupil_d_left_raw)
                pupil_d_left_filtered[idx_not_nan] = savgol_filter(pupil_d_left_raw[idx_not_nan], window_length=15, polyorder=2)

                idx_not_nan = np.argwhere(~np.isnan(pupil_d_right_raw)).squeeze()
                pupil_d_right_filtered = np.copy(pupil_d_right_raw)
                pupil_d_right_filtered[idx_not_nan] = savgol_filter(pupil_d_right_raw[idx_not_nan], window_length=15, polyorder=2)
                
                pupil_diameter_filtered = 0.5 * (pupil_d_left_filtered + pupil_d_right_filtered)
                df['Pupil diameter processed'] = pupil_diameter_filtered / pupil_baseline

                # get question and version
                question_number, version = int(os.path.basename(file_names[file_index]).replace('.csv','').split('_')[1].replace('Q','')), os.path.basename(file_names[file_index]).replace('.csv','').split('_')[2]

                # Total duration
                viewingTimeSec = (df['Recording timestamp'].max() - df['Recording timestamp'].min()) / 1e6
                #print('viewingTimeSec=',viewingTimeSec)

                # Get valid data points
                df = df[conditions_section1_valid].reset_index(drop=True)

                # Get fixation and saccade counts and durations
                movement_index = df.iloc[0]['Eye movement type index']  # 'Eye movement type'
                indices = [0]
                batches = []

                for i in range(1, df.shape[0]):
                    if df.iloc[i]['Eye movement type index']==movement_index:
                        indices.append(i)
                    else:
                        batches.append({'event':df.iloc[i-1]['Eye movement type'] , 'indices':indices})
                        movement_index = df.iloc[i]['Eye movement type index']
                        indices = [i]

                valid_groups = [batch for batch in batches if batch['event']=='Fixation' or batch['event']=='Saccade']
                # Remove the first event (it is merged with transition)
                valid_groups = valid_groups[1:]

                batch_data = []
                saccadeIdx = 1
                fixationIdx = 1 

                for batch in valid_groups:

                    # Event Type
                    eventType = batch['event']
                    indices = batch['indices']
                    df_batch = df.iloc[indices].reset_index(drop=True)
                    df_batch = df_batch[['Recording timestamp', 'Gaze event duration', 'Eye movement type', 'Fixation point X', 'Fixation point Y', 
                                        'Pupil diameter processed', 'Gaze point left X','Gaze point left Y','Gaze point right X', 'Gaze point right Y', 'Eye movement type index']]
                    # Note: 'Pupil diameter left', 'Pupil diameter right' were changed with 'Pupil diameter processed'

                    # eventIdx
                    if eventType=='Fixation':
                        eventIdx = fixationIdx
                        fixationIdx += 1
                    elif eventType=='Saccade':
                        eventIdx = saccadeIdx
                        saccadeIdx += 1

                    # Start Time
                    startTime = df_batch.iloc[0]['Recording timestamp']

                    # gazeEventDuration
                    if df_batch['Gaze event duration'].unique().size==1:
                        gazeEventDuration = df_batch['Gaze event duration'][0]  
                    else:
                        gazeEventDuration = (df_batch.iloc[-1]['Recording timestamp'] - df_batch.iloc[0]['Recording timestamp']) / 1e3

                    # Mean Pupil Diameter
                    #pupil_diameter_left = np.array([str(i).replace(',','.') for i in df_batch['Pupil diameter left'].to_list()]).astype(np.float)
                    #pupil_diameter_right = np.array([str(i).replace(',','.') for i in df_batch['Pupil diameter right'].to_list()]).astype(np.float)
                    #meanPupilDiameter = '%3.5f'%np.mean(0.5 * (pupil_diameter_left + pupil_diameter_right))
                    meanPupilDiameter = '%3.5f'%np.mean(df_batch['Pupil diameter processed'])

                    # Fixation or Saccade
                    meanX, meanY = 'NaN', 'NaN'
                    startSaccadeX, startSaccadeY, endSaccadeX, endSaccadeY = 'NaN', 'NaN','NaN', 'NaN'

                    if eventType=='Fixation':
                        meanX, meanY = '%2.2f'%df_batch['Fixation point X'].mean(), '%2.2f'%df_batch['Fixation point Y'].mean()
                    elif eventType=='Saccade':
                        startSaccadeX = '%2.2f'%round(0.5 * (df_batch.iloc[0]['Gaze point left X'] + df_batch.iloc[0]['Gaze point right X']))
                        startSaccadeY = '%2.2f'%round(0.5 * (df_batch.iloc[0]['Gaze point left Y'] + df_batch.iloc[0]['Gaze point right Y']))
                        endSaccadeX = '%2.2f'%round(0.5 * (df_batch.iloc[-1]['Gaze point left X'] + df_batch.iloc[-1]['Gaze point right X']))
                        endSaccadeY = '%2.2f'%round(0.5 * (df_batch.iloc[-1]['Gaze point left Y'] + df_batch.iloc[-1]['Gaze point right Y']))
                    else:
                        raise Exception('Event type must be Fixation or Saccade!') 

                    batch_data.append([startTime, gazeEventDuration, eventType, eventIdx, meanPupilDiameter, meanX, meanY, startSaccadeX, startSaccadeY, endSaccadeX, endSaccadeY])

                batch_data = pd.DataFrame(batch_data, columns=['starttime', 'duration', 'eventType', 'eventIdx', 'meanPupilDiameter', 'meanX', 'meanY', 'startSaccadeX', 'startSaccadeY', 'endSaccadeX', 'endSaccadeY'])

                # Save batch_data 
                # Later, rund this script and save each "batch_data" data frame seperately to share in the dataset.
                save_filename = '%s/data/final/P%02d_S%02d_%s.csv'%(root_folder, participant_num, question_number, version)
                batch_data.to_csv(save_filename, index=False)

                # Extract Features
                # Total viewing duration
                #viewingTimeSec

                # Count of Fixation and Saccades
                fixationCount = np.sum(batch_data['eventType']=='Fixation')
                saccadeCount = np.sum(batch_data['eventType']=='Saccade')

                # Mean Event Duration
                meanFixationDuration = batch_data[batch_data['eventType']=='Fixation']['duration'].mean()
                meanSaccadeDuration = batch_data[batch_data['eventType']=='Saccade']['duration'].mean()

                # Additional entries to see the min/max of fixation and saccade durations (maybe later we filter them by a threshold)
                minFixationDuration = batch_data[batch_data['eventType']=='Fixation']['duration'].min()
                maxFixationDuration = batch_data[batch_data['eventType']=='Fixation']['duration'].max()
                minSaccadeDuration = batch_data[batch_data['eventType']=='Saccade']['duration'].min()
                maxSaccadeDuration = batch_data[batch_data['eventType']=='Saccade']['duration'].max()

                # Pupil Diameter during Fixation
                meanPupilDiameterFixation = np.sum(np.multiply(batch_data[batch_data['eventType']=='Fixation']['meanPupilDiameter'].to_numpy().astype(np.float32),
                                                            batch_data[batch_data['eventType']=='Fixation']['duration'].to_numpy())) / batch_data[batch_data['eventType']=='Fixation']['duration'].sum()

                meanPupilDiameter = np.sum(np.multiply(batch_data['meanPupilDiameter'].to_numpy().astype(np.float32), batch_data['duration'].to_numpy())) / batch_data['duration'].sum()

                # print features per subject adn per news item
                print('%02d,%02d,%s,%2.3f,%d,%d,%2.3f,%2.3f,%2.3f,%2.3f,%2.3f,%2.3f,%2.3f,%2.3f'%(participant_num, question_number, version,
                                            viewingTimeSec, 
                                            fixationCount, saccadeCount, 
                                            meanFixationDuration, meanSaccadeDuration, 
                                            meanPupilDiameter, meanPupilDiameterFixation,
                                            minFixationDuration, maxFixationDuration,
                                            minSaccadeDuration, maxSaccadeDuration))


if __name__ == '__main__':
    
    root_folder = os.getcwd()
    parser = argparse.ArgumentParser(description='Extract features')
    parser.add_argument("--root-folder",    default='./',           type=str,  help="root folder")
    args = parser.parse_args()
    main(args)