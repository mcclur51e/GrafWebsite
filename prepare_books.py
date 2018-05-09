#!/usr/bin/env python

######
## python prepare_books.py data.csv
###### 

import pandas as pd
import sys
pd.options.mode.chained_assignment = None  # default='warn' This code removes warning about changing a DataFrame in place

log_df = pd.read_csv(sys.argv[1]) # read in data.csv file

dicAge = {"A":"Adult","J":"Juvenile","H":"Hatchling","C":"Cocoon","B":"Blood","W":"Water","R":"Rock","G":"Reagents","M":"Mock"} # define dictionary for replacing age shorthand

#Sample Book 
sample_book_long = log_df.loc[log_df['Status'].isin(['Original','Embed'])] # keep only rows whose 'Status' value == 'Original' or 'Embed'
sample_book_trim = sample_book_long[sample_book_long.Storage_Box != 'Missing']
sample_book = sample_book_trim[['Project_Name','Subproject','AnimalSource','JGL_EventID','Source_ID','JGL_SampleID','EmilyID','Sample_Alt_Name','Sample_Type','JGL_NucleicAcidsID','Storage_Location','Storage_Box','Sample_Collector','Fee','Grant_ID','Date_Billed','Fee_Collected','Date_Collected','Empty','JGL_Notes','Record_Date','Record_Creator','Problem']] # choose columns to keep
sample_book.rename(columns={'AnimalSource': 'Site_ID','JGL_EventID':'Event_ID','JGL_SampleID': 'Sample_ID', 'EmilyID':'Historic_Sample_ID','JGL_NucleicAcidsID':'Nucleic_Acids_ID','JGL_Notes': 'Notes'}, inplace=True) # rename (and order) columns to match website csv format
sample_book.to_csv('Book_Sample.csv',index=False) # print csv file ready for upload

#Nucleic Acids Book
nucleic_book_long = log_df.loc[log_df['Status'].isin(['DNA','RNA'])] # keep only rows whose 'Status' value == 'DNA' or 'RNA'
nucleic_book_trim = nucleic_book_long[nucleic_book_long.Storage_Box != 'Missing']
nucleic_book = nucleic_book_trim[['Project_Name','Subproject','JGL_SampleID','Source_ID','Strain_ID','Plasmid_ID','JGL_NucleicAcidsID','NucleicAcids_ID','A260','A280','Ratio','nDrop','Qubit','Quantification_Method','DNA_extractor','DateDNAExtract','Storage_Location','Storage_Box','Kit_Name','Lot_Number','Kit_Name_2','Lot_Number_2','What_is_this?','Empty','JGL_Notes','Record_Date','Record_Creator','Problem']] # choose columns to keep
nucleic_book.rename(columns={'JGL_SampleID':'Sample_ID','JGL_NucleicAcidsID':'Nucleic_Acids_ID','NuceicAcids_ID':'Historic_Nucleic_Acids_ID','DNA_extractor': 'Extractor', 'DateDNAExtract': 'Date_Extracted','JGL_Notes': 'Notes'}, inplace=True) # rename (and order) columns to match website csv format
nucleic_book.to_csv('Book_NucleicAcid.csv',index=False) # print csv file ready for upload

#Source Book (Animal Book)
source_book_long = log_df.loc[log_df['Status'].isin(['Original','Embed'])] # keep only rows whose 'Status' value == 'Original' or 'Embed'
source_book = source_book_long[['Project_Name','Subproject','AnimalSource','Source_ID','AnimalCollector','Type_of_Source','JGL_EventID','Taxonomic_ID','Weight','Height','Length','Age','Health_Status','Symptoms','ParentLot','MealLot1','DaH','Empty','JGL_Notes','Record_Date','Record_Creator','Problem']] # choose columns to keep
source_book.replace({"Age":dicAge}, inplace=True) # insert extended version of age shorthand
source_book.rename(columns={'AnimalSource':'Site_ID','AnimalCollector':'Source_Collector','JGL_EventID':'Event_ID','ParentLot':'Variable_1','MealLot1':'Variable_2','DaH':'Variable_3','JGL_Notes': 'Notes'}, inplace=True) # rename (and order) columns to match website csv format
source_book.to_csv('Book_Source.csv',index=False) # print csv file ready for upload

#Subproject Book
subproject_book_long = log_df.loc[log_df['Status'].isin(['Original','Embed'])] # keep only rows whose 'Status' value == 'Original' or 'Embed'
subproject_book = log_df[['Project_Name','Subproject','Project_Status','Variables','SubprojectDesc','ProjParticipants','JGL_Notes','Record_Date','Record_Creator','Problem']] # choose columns to keep
subproject_book.rename(columns={'SubprojectDesc':'Description', 'ProjParticipants':'Participants','JGL_Notes': 'Notes'}, inplace=True) # rename (and order) columns to match website csv format
subproject_book.drop_duplicates(subset={'Subproject'},keep='first',inplace=True) # Remove duplicate rows so there is only one record per 'Subproject'
subproject_book.to_csv('Book_Subproject.csv',index=False) # print csv file ready for upload

#Event Book
event_book_long = log_df.loc[log_df['Status'].isin(['Original','Embed'])] # keep only rows whose 'Status' value == 'Original' or 'Embed'
event_book = log_df[['Project_Name','Subproject','JGL_EventID','Da1F','AnimalSource','Date_Collected','Variable_1','Variable_2','Variable_3','JGL_Notes','Record_Date','Record_Creator','Problem']] # choose columns to keep
event_book.rename(columns={'JGL_EventID':'Event_ID','Da1F':'Day', 'AnimalSource': 'Site_ID','Date_Collected':'Date','JGL_Notes': 'Notes'}, inplace=True) # rename (and order) columns to match website csv format
event_book.drop_duplicates(subset={'Event_ID'},keep='first',inplace=True) # Remove duplicate rows so there is only one record per 'Event_ID'
event_book.to_csv('Book_Event.csv',index=False) # print csv file ready for upload

#Illumina Run Book
#illuminarun_book = log_df[['Project_Name','Subproject','Run_ID','Run_Alt_ID','Who_Did_Run','Run_Date','Sequencer','KFS1','KFS2','Date_Ownership_Transferred','Reagent_ID','Flow_Cell_ID']]
#illuminarun_book.to_csv('/Users/emily/Desktop/Website/python_2017_1110/IlluminaRunBook.csv',index=False)

#Illumina Sample Book
illumina_book_long = log_df.loc[log_df['Status'].isin(['MiSeq'])] # keep only rows whose 'Status' value == 'MiSeq'
illuminasample_book = illumina_book_long[['Project_Name','Subproject','Source_ID','JGL_SampleID','EmilyID','Sample_Plate','Sample_Well','PCR_Date','i7_Index_ID','i7_Seq','i5_Index_ID','i5_Seq','JGL_NucleicAcidsID','JGL_IlluminaID','Illumina_SampleID','Gene_Name','Run2_ID','PCR_Experimenter','MiSeq_Run','Run_Status','Taq_Name','Taq_Lot','Description','JGL_Notes','Record_Date','Record_Creator','Problem']] # choose columns to keep
illuminasample_book.rename(columns={'JGL_SampleID':'Sample_ID','EmilyID': 'Sample_Name','PCR_Date':'Date_Prepared','i7_Seq': 'Index', 'i5_Seq': 'Index2','JGL_NucleicAcidsID':'Nucleic_Acids_ID','JGL_IlluminaID':'Illumina_Sample_ID','Illumina_SampleID':'Historic_Illumina_Sample_ID', 'PCR_Experimenter': 'Library_Preparer','MiSeq_Run': 'Run_ID','JGL_Notes': 'Notes'}, inplace=True) # rename (and order) columns to match website csv format
illuminasample_book.to_csv('Book_IlluminaSample.csv',index=False) # print csv file ready for upload

#sample_book_long.drop_duplicates(subset={'Website_SampleID'},keep='first',inplace=True)

#QIAxcel Book
qiaxcel_book_long = log_df.loc[log_df['Status'].isin(['MiSeq'])] # keep only rows whose 'Status' value == 'MiSeq'
qiaxcel_book = log_df[['Sample_Plate','JGL_IlluminaID','PostPCRDNA_ng_uL','Amplicon_Size','JGL_Notes','Record_Date','Record_Creator','Problem']] # choose columns to keep
qiaxcel_book.rename(columns={'JGL_IlluminaID':'Sample_ID', 'PostPCRDNA_ng_uL':'Library_Concentration','JGL_Notes': 'Notes'}, inplace=True) # rename (and order) columns to match website csv format
qiaxcel_book.to_csv('Book_Qiaxcel.csv',index=False) # print csv file ready for upload

#Read Depth Book
depth_book_long = log_df.loc[log_df['Status'].isin(['MiSeq'])] # keep only rows whose 'Status' value == 'MiSeq'
depth_book = log_df[['MiSeq_Run','JGL_IlluminaID','ReadsCount','JGL_Notes','Record_Date','Record_Creator','Problem']] # choose columns to keep
depth_book.rename(columns={'MiSeq_Run':'Run_ID','JGL_IlluminaID':'Sample_ID','ReadsCount':'Read_Depth'}, inplace=True) # rename (and order) columns to match website csv format
depth_book.to_csv('Book_Depth.csv',index=False) # print csv file ready for upload


