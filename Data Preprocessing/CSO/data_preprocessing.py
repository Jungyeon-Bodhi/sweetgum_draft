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

file_path = "Data/25-PI-GLO-1 - Raw Dataset (CSO)"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/25-PI-GLO-1 - Open-End (CSO).xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

respondent_name = 'a1'
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = [respondent_name, 'start', 'formhub-uuid']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers
dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['SubmissionDate', 'formhub-uuid', 'start', 'end', 'today', 'deviceid', 'intro', 'country', 'region', 'district',
 'cso', 'SectionA-sect1_intro',
 'a1', 'a2', 'a2_oth', 'a3', 'a4', 'a5_oth', 'a6', 'a6_oth', 'a7', 'a8', 'a8_oth', 'a9', 'a10_oth',
 'a11', 'a11_oth', 'a12', 'SectionB-sectc_intro', 'b1', 'b1_exp', 'b2_oth', 'b4_oth', 'b5_oth', 'b5_exp', 'b7',
 'b8_oth', 'b8_exp', 'b11', 'b12_intro', 'b12a', 'b12b', 'b13_intro', 'b13a', 'b13b', 'b13c', 'b13d', 'b13e',
 'b14_intro', 'b14a', 'b14b', 'b14c', 'b14d', 'SectionC-sectc_intro_001',
 'c1', 'c2_oth', 'c3', 'c4_oth', 'c5', 'c6', 'c7', 'c8', 'c8_exp', 'c9', 'c9_exp',
 'SectionD-sectd_intro', 'd1', 'd2', 'd3_oth', 'd4_oth', 'd5_oth', 'd6', 'd7', 'd8', 'd9',
 'SectionE-secte_intro', 'e1', 'e2', 'e2_oth', 'e3', 'e4', 'e5_intro', 'e5a', 'e5b', 'e5c', 'e5d', 'e5e', 'e5f',
 'SectionF-sectf_intro', 'f3', 'f4', 'f5', 'f5_exp', 'f6', 'f7', 'f7_exp', 'f8', 'f8_exp',
 'f9', 'f10', 'f10_exp', 'closeout',
 '__version__', 'meta-instanceID', 'KEY', 'isValidated', 'start_dt', 'end_dt', 'start_date', 'end_date', 'duration_min',
 'a5_1', 'a5_2', 'a5_3', 'a5_4', 'a5_5', 'a5_6', 'a10_1', 'a10_2', 'a10_3', 'a10_4', 'a10_5',
 'b2_1', 'b2_2', 'b2_3', 'b2_4', 'b2_5', 'b2_6', 'b3_1', 'b3_2', 'b3_3', 'b3_4', 'b3_5',
 'b4_1', 'b4_2', 'b4_3', 'b4_4', 'b4_5', 'b4_6', 'b5_1', 'b5_2', 'b5_3', 'b5_4', 'b5_5', 'b6_1', 'b6_2', 'b6_3', 'b6_4',
 'b8_1', 'b8_2', 'b8_3', 'b8_4', 'b8_5', 'b8_6', 'b9_1', 'b9_2', 'b9_3', 'b9_4', 'b9_5', 'b10_1', 'b10_2', 'b10_3', 'b10_4', 'b10_5',
 'c2_1', 'c2_2', 'c2_6', 'c2_3', 'c2_4', 'c2_5', 'c4_1', 'c4_2', 'c4_3', 'c4_4', 'c4_5', 'c4_6', 'c4_7',
 'd3_1', 'd3_2', 'd3_3', 'd3_4', 'd3_5', 'd3_6', 'd4_1', 'd4_2', 'd4_3', 'd4_4', 'd4_5', 'd4_6', 'd4_7', 'd4_8', 'd4_9',
 'd5_1', 'd5_2', 'd5_3', 'd5_4', 'd5_5', 'd5_6', 'd5_7', 'd5_8', 'f1_1', 'f1_2', 'f1_3', 'f1_4', 'f2_1', 'f2_2', 'f2_4', 'f2_3']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['SubmissionDate', 'formhub-uuid', 'start', 'end', 'today', 'deviceid', 'intro','SectionA-sect1_intro',
                'SectionB-sectc_intro','b12_intro','b13_intro','b14_intro','SectionC-sectc_intro_001','SectionD-sectd_intro',
                'SectionE-secte_intro', 'e5_intro', 'SectionF-sectf_intro', '__version__', 'meta-instanceID', 'KEY', 'isValidated', 'start_dt', 'end_dt', 'start_date', 'end_date', 'duration_min']
# Specify the columns to be excluded from the data analysis

miss_col = ['a2', 'a3', 'a4', 'a6', 'a7', 'a8']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['a2_oth','a5_oth','a6_oth','a8_oth','a10_oth','a11_oth','b1_exp','b2_oth', 'b4_oth', 'b5_oth','b5_exp',
            'b8_oth', 'b8_exp','c2_oth','c4_oth','d3_oth', 'd4_oth', 'd5_oth','e2_oth',
             'f5_exp', 'f7_exp', 'f8_exp', 'f10_exp', 'closeout']

age_col = None
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['a5_1', 'a5_2', 'a5_3', 'a5_4', 'a5_5', 'a5_6','a5_oth']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])

new_cols_order = ['SubmissionDate', 'formhub-uuid', 'start', 'end', 'today', 'deviceid', 'intro', 'country', 'region', 'district',
 'cso', 'SectionA-sect1_intro',
 'a1', 'a2', 'a2_oth', 'a3', 'a4', 'a5_1', 'a5_2', 'a5_3', 'a5_4', 'a5_5', 'a5_6','a5_oth', 
 'a6', 'a6_oth', 'a7', 'a8', 'a8_oth', 'a9', 'a10_1', 'a10_2', 'a10_3', 'a10_4', 'a10_5', 'a10_oth',
 'a11', 'a11_oth', 'a12', 'SectionB-sectc_intro', 'b1', 'b1_exp', 'b2_1', 'b2_2', 'b2_3', 'b2_4', 'b2_5', 'b2_6', 'b2_oth',
  'b3_1', 'b3_2', 'b3_3', 'b3_4', 'b3_5', 'b4_1', 'b4_2', 'b4_3', 'b4_4', 'b4_5', 'b4_6', 'b4_oth', 
  'b5_1', 'b5_2', 'b5_3', 'b5_4', 'b5_5','b5_oth', 'b5_exp', 'b6_1', 'b6_2', 'b6_3', 'b6_4','b7',
  'b8_1', 'b8_2', 'b8_3', 'b8_4', 'b8_5', 'b8_6', 'b8_oth', 'b8_exp', 
  'b9_1', 'b9_2', 'b9_3', 'b9_4', 'b9_5', 'b10_1', 'b10_2', 'b10_3', 'b10_4', 'b10_5','b11', 'b12_intro', 
  'b12a', 'b12b', 'b13_intro', 'b13a', 'b13b', 'b13c', 'b13d', 'b13e', 'b14_intro', 'b14a', 'b14b', 'b14c', 'b14d', 'SectionC-sectc_intro_001',
  'c1', 'c2_1', 'c2_2', 'c2_3', 'c2_4', 'c2_5','c2_6', 'c2_oth', 'c3', 'c4_1', 'c4_2', 'c4_3', 'c4_4', 'c4_5', 'c4_6', 'c4_7','c4_oth', 
  'c5', 'c6', 'c7', 'c8', 'c8_exp', 'c9', 'c9_exp','SectionD-sectd_intro', 'd1', 'd2', 
   'd3_1', 'd3_2', 'd3_3', 'd3_4', 'd3_5', 'd3_6','d3_oth', 'd4_1', 'd4_2', 'd4_3', 'd4_4', 'd4_5', 'd4_6', 'd4_7', 'd4_8', 'd4_9','d4_oth', 
    'd5_1', 'd5_2', 'd5_3', 'd5_4', 'd5_5', 'd5_6', 'd5_7', 'd5_8','d5_oth', 'd6', 'd7', 'd8', 'd9',
 'SectionE-secte_intro', 'e1', 'e2', 'e2_oth', 'e3', 'e4', 'e5_intro', 'e5a', 'e5b', 'e5c', 'e5d', 'e5e', 'e5f',
 'SectionF-sectf_intro', 'f1_1', 'f1_2', 'f1_3', 'f1_4','f2_1', 'f2_2', 'f2_3', 'f2_4', 'f3', 'f4', 'f5', 'f5_exp', 'f6', 'f7', 'f7_exp', 
  'f8', 'f8_exp','f9', 'f10', 'f10_exp', 'closeout','__version__', 'meta-instanceID', 'KEY', 'isValidated', 'start_dt', 'end_dt', 'start_date', 'end_date', 'duration_min']


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

sweetgum = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, identifiers, open_cols, cols_new, new_cols_order, age_col, diss_cols, del_type = 0, file_type=file_type)
sweetgum.processing()