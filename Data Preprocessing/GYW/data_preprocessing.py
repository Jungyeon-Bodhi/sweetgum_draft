#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "Final Term Evaluation of She Leads"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/25-PI-GLO-1 - Raw Dataset"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/25-PI-GLO-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

enumerator_name = 'enum_id'
respondent_name = 'a1'
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = [enumerator_name, respondent_name, 'start', 'metaID']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['SubmissionDate', 'formhub-uuid', 'start', 'end', 'today', 'deviceid', 'enum_name', 'enum_id',
 'country', 'region', 'district', 'gyw_group', 'intro', 'consent', 'consent2', 'SectionA-sectA_intro', 
 'a1', 'a2', 'a2_o', 'a3', 'a5', 'a5_o', 'SectionA-sectA_groupinfo', 'a7', 'a8', 'a9',
 'SectionB-sectB_satifact', 'b1', 'b2', 'b3', 'b4', 'b5', 'SectionB-sectB_safeguard', 'b6', 'b7', 'b8',
 'SectionB-sectB_skills', 'b9', 'b10', 'b11', 'b12', 'b13', 'b14',
 'SectionB-sectB_leadership', 'b15', 'b15b', 'b16', 'b16b', 'SectionC-sectC_voice',
 'c1', 'c2', 'c3', 'SectionC-sectC_diversity', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10',
 'SectionC-sectC_partication', 'c11', 'c12', 'c13', 'SectionC-sectC_socials', 'c14', 'c15',
 'SectionD-sectD_intro', 'd1_oth', 'd3_oth', 'd4_oth', 'e1', 'e2_oth', 'e3', 'e4',
 'SectionF-sectF_partners', 'f1', 'f2', 'SectionF-sectF_decisions', 'f3', 'f4', 'f5', 'f6',
 'SectionG-sectG_orgchange', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
 'h1', 'h2', 'h3', 'i1_oth', 'i2', 'i2b', 'i3',
 'version', 'metaID', 'KEY', 'isValidated',
 'a4_1', 'a4_2', 'a4_3', 'a4_4', 'a4_5', 'a4_6', 'a4_7', 'a4_8', 'a4_nan',
 'd1_1', 'd1_2', 'd1_3', 'd1_4', 'd1_5', 'd1_nan',
 'd2_1', 'd2_2', 'd2_3', 'd2_4', 'd2_5', 'd2_6', 'd2_nan',
 'd3_1', 'd3_2', "d3_3", "d3_4", 'd3_5', 'd3_6', 'd3_7', 'd3_nan',
 'd4_1', 'd4_2', 'd4_3', 'd4_4', 'd4_5', 'd4_6', 'd4_7', 'd4_8', 'd4_9', 'd4_nan',
 'e2_1', 'e2_2', 'e2_3', 'e2_4', 'e2_5', 'e2_6', 'e2_nan',
 'g9_1', 'g9_2', 'g9_3', 'g9_4', 'g9_5', 'g9_nan',
 'i1_1', 'i1_2', 'i1_3', 'i1_4', 'i1_5', 'i1_6', 'i1_7', 'i1_nan']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['SubmissionDate', 'formhub-uuid', 'start', 'end', 'today', 'deviceid', 'enum_name', 'enum_id',
                'intro', 'consent', 'consent2', 'SectionA-sectA_intro', 'SectionA-sectA_groupinfo', 'SectionB-sectB_satifact',
                'SectionB-sectB_safeguard','SectionB-sectB_skills','SectionB-sectB_leadership', 'SectionC-sectC_voice',
                'SectionC-sectC_partication', 'SectionC-sectC_socials',  'SectionD-sectD_intro', 'SectionF-sectF_partners',
                'SectionF-sectF_decisions', 'SectionG-sectG_orgchange','version', 'metaID', 'KEY', 'isValidated', 'SectionC-sectC_diversity']
# Specify the columns to be excluded from the data analysis

miss_col = ['a2', 'a3', 'a5', 'a7', 'a8', 'a9']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['a2_o', 'a5_o', 'b15b', 'b16b', 'd1_oth', 'd3_oth', 'd4_oth', 'e2_oth','i1_oth', 'i2b', 'i3']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = None
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['a4_1', 'a4_2', 'a4_3', 'a4_4', 'a4_5', 'a4_6', 'a4_7', 'a4_8', 'a4_nan']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])

new_cols_order = ['SubmissionDate', 'formhub-uuid', 'start', 'end', 'today', 'deviceid', 'enum_name', 'enum_id',
 'country', 'region', 'district', 'gyw_group', 'intro', 'consent', 'consent2', 'SectionA-sectA_intro', 
 'a1', 'a2', 'a2_o', 'a3', 'a4_1', 'a4_2', 'a4_3', 'a4_4', 'a4_5', 'a4_6', 'a4_7', 'a4_8', 'a4_nan',
'a5', 'a5_o', 'SectionA-sectA_groupinfo', 'a7', 'a8', 'a9',
 'SectionB-sectB_satifact', 'b1', 'b2', 'b3', 'b4', 'b5', 'SectionB-sectB_safeguard', 'b6', 'b7', 'b8',
 'SectionB-sectB_skills', 'b9', 'b10', 'b11', 'b12', 'b13', 'b14',
 'SectionB-sectB_leadership', 'b15', 'b15b', 'b16', 'b16b', 'SectionC-sectC_voice',
 'c1', 'c2', 'c3', 'SectionC-sectC_diversity', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10',
 'SectionC-sectC_partication', 'c11', 'c12', 'c13', 'SectionC-sectC_socials', 'c14', 'c15',
 'SectionD-sectD_intro', 'd1_1', 'd1_2', 'd1_3', 'd1_4', 'd1_5', 'd1_nan', 'd1_oth', 
 'd2_1', 'd2_2', 'd2_3', 'd2_4', 'd2_5', 'd2_6', 'd2_nan',
 'd3_1', 'd3_2', "d3_3", "d3_4", 'd3_5', 'd3_6', 'd3_7', 'd3_nan', 'd3_oth', 
  'd4_1', 'd4_2', 'd4_3', 'd4_4', 'd4_5', 'd4_6', 'd4_7', 'd4_8', 'd4_9', 'd4_nan', 'd4_oth', 
   'e1', 'e2_1', 'e2_2', 'e2_3', 'e2_4', 'e2_5', 'e2_6', 'e2_nan','e2_oth', 'e3', 'e4',
 'SectionF-sectF_partners', 'f1', 'f2', 'SectionF-sectF_decisions', 'f3', 'f4', 'f5', 'f6',
 'SectionG-sectG_orgchange', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
 'g9_1', 'g9_2', 'g9_3', 'g9_4', 'g9_5', 'g9_nan','h1', 'h2', 'h3', 
 'i1_1', 'i1_2', 'i1_3', 'i1_4', 'i1_5', 'i1_6', 'i1_7', 'i1_nan', 'i1_oth', 'i2', 'i2b', 'i3',
 'version', 'metaID', 'KEY', 'isValidated']


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

sweetgum = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, enumerator_name, identifiers, open_cols, cols_new, new_cols_order, age_col, diss_cols, del_type = 0, file_type=file_type)
sweetgum.processing()