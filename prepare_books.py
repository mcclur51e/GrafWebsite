#!/usr/bin/env python

######
## python prepare_books.py data.csv
###### 

import pandas as pd
import sys

print(sys.argv[1])

log_df = pd.read_csv(sys.argv[1])

#Sample Book 
sample_book_long = log_df.loc[log_df['Status'].isin(['Original','Embed'])] # keep only rows whose 'Status' value == 'Original' or 'Embed'
sample_book = sample_book_long[['Project_Name','Subproject','AnimalSource','Event_ID','Source_ID','Website_SampleID','Sample_ID','Sample_Type','Website_NucleicAcidsID','Storage_Location','Storage_Box','Sample_Collector','Fee','Grant_ID','Date_Billed','Fee_Collected','Date_Collected','Empty','Website_Notes']] # choose columns to keep
sample_book.rename(columns={'AnimalSource': 'Site_ID','Website_SampleID': 'Sample_ID','Website_NucleicAcidsID':'Nucleic_Acids_ID','Sample_ID':'Sample_Alt_Name','Website_Notes': 'Notes'}, inplace=True) # rename (and order) columns to match website csv format
sample_book.to_csv('Book_Sample.csv',index=False) # print csv file to upload

#Nucleic Acids Book
nucleic_book_long = log_df.loc[log_df['Status'].isin(['DNA','RNA'])] # keep only rows whose 'Status' value == 'DNA' or 'RNA'
nucleic_book = nucleic_book_long[['Project_Name','Subproject','Website_SampleID','Source_ID','Strain_ID','Plasmid_ID','Website_NucleicAcidsID','A260','A280','Ratio','nDrop','Qubit','Quantification_Method','DNA_extractor','DateDNAExtract','Storage_Location','Storage_Box','Kit_Name','Lot_Number','Kit_Name_2','Lot_Number_2','What_is_this?','Empty','Notes']]
nucleic_book.rename(columns={'Website_SampleID': 'Sample_ID','Website_NucleicAcidsID':'Nucleic_Acids_ID','DNA_extractor': 'Extractor', 'DateDNAExtract': 'Date_Extracted'}, inplace=True)
nucleic_book.to_csv('Book_NucleicAcid.csv',index=False)

#Source Book (Animal Book)
source_book_long = log_df.loc[log_df['Status'].isin(['Original','Embed'])] # keep only rows whose 'Status' value == 'Original' or 'Embed'
source_book = source_book_long[['Project_Name','Subproject','AnimalSource','Source_ID','Sample_Collector','Sample_Type','Event_ID','Taxonomic_ID','Weight','Height','Length','Age','Health_Status','Symptoms','Variable_1','Variable_2','Variable_3','Empty','Notes']]
source_book.rename(columns={'Sample_Collector':'Source_Collector','Sample_Type':'Type_of_Source','AnimalSource':'Site_ID'}, inplace=True)
source_book.to_csv('Book_Source.csv',index=False)

#Event Book
#event_book = log_df[['Project_Name','Subproject','Event_ID','Day','Site_ID','Date','Variable_1','Variable_2','Variable_3','Notes']]
#event_book.to_csv('/Users/emily/Desktop/Website/python_2017_1110/EventBook.csv',index=False)

#Illumina Run Book
#illuminarun_book = log_df[['Project_Name','Subproject','Run_ID','Run_Alt_ID','Who_Did_Run','Run_Date','Sequencer','KFS1','KFS2','Date_Ownership_Transferred','Reagent_ID','Flow_Cell_ID']]
#illuminarun_book.to_csv('/Users/emily/Desktop/Website/python_2017_1110/IlluminaRunBook.csv',index=False)

#Illumina Sample Book
#illuminasample_book = log_df[['Project_Name','Subproject','Source_ID','Illumina_Sample_ID','EmilyID','Sample_Plate','Sample_Well','PCR_Date','i7_Index_ID','i7_Seq','i5_Index_ID','i5_Seq','Nucleic_Acids_ID','Illumina_Sample_ID','Gene_Name','Amplicon_Size','PostPCRDNA_ng_uL','Run2_ID','PCR_Experimenter','MiSeq_Run','Run_ID','Run_Status','Taq_Name','Taq_Lot','Description','Notes']]
#illuminasample_book.rename(columns={'PostPCRDNA_ng_uL': 'Library_Concentration', 'MiSeq_Run': 'Run_ID', 'PCR_Experimenter': 'Library_Preparer', 'EmilyID': 'Sample_Name', 'PCR_Date': 'Date_Prepared', 'i7_Seq': 'Index', 'i5_Seq': 'Index2'}, inplace=True)
#illuminasample_book.to_csv('/Users/emily/Desktop/Website/python_2017_1110/IlluminaSampleBook.csv',index=False)

#sample_book_long.drop_duplicates(subset={'Website_SampleID'},keep='first',inplace=True)
