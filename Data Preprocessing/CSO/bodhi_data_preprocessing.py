#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:07:52 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please download following Python Libraries:
1. Pandas
2. Numpy
3. uuid
4. openpyxl
"""

import pandas as pd
import numpy as np
import uuid
from openpyxl import load_workbook

class Preprocessing:
    
    def __init__(self, name, file_path, file_path_others, list_del_cols, dates, miss_col, anon_col, identifiers, opened_cols, cols_new, new_cols_order, 
                 age_col = None, diss_cols = None, del_type = 0, file_type='xlsx'):
        """
        - Initialise the Performance Management Framework class

        name: str, Name of the project
        file_path: str, Directory of the raw dataset
        file_path_others: str, Directory of the opened-end questions' answers
        list_del_cols: list, Columns list for deleting
        dates: list, Dates on which the pilot test was conducted from the data
        miss_col: list, 
        anon_col: str, Column for anonymisation (Respondent Name)
        anon_col2: str, Column for anonymisation (Enumerator Name)
        identifiers: list, Columns for checking duplicates 
        opened_cols: list, Opened-end question columns
        cols_new: list, New names for the columns (for data analysis purpose)
        age_col: str, Column of age infromation (for age-grouping purpose)
        diss_cols: list, Column of WG-SS questions in the dataset (for disability-grouping purpose)
        del_type: int, [0 or 1]
        -> 0: Remove all missing values from the columns where missing values are detected
        -> 1: First, remove columns where missing values make up 10% or more of the total data points
              Then, remove all remaining missing values from the columns where they are detected
        file_type: str, filetype of the raw dataset
        """
        self.name = name
        self.file_path = file_path
        self.file_path_others = file_path_others
        self.file_type = file_type
        self.list_del_cols = list_del_cols
        self.dates = dates
        self.miss_col = miss_col
        self.anon_col = anon_col
        self.identifiers = identifiers
        self.opened_cols = opened_cols
        self.new_order = new_cols_order
        self.cols_new = cols_new
        self.age_col = age_col
        self.diss_cols = diss_cols
        self.del_type = del_type
        self.df = None
    
    def data_load(self):
        """
        - To load a dataset
        """
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df = pd.read_excel(f"{file_path}.{file_type}")
            self.df = df
            return True
        elif file_type == 'csv':
            df = pd.read_csv(f"{file_path}.{file_type}")
            self.df = df
            return True
        else:
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        
    def delete_columns(self):
        """
        - To drop unnecessary columns
        """
        df = self.df
        list_cols = self.list_del_cols
        df = df.drop(columns = list_cols)
        print(f'Number of columns: {len(df.columns)} | After removing the columns that are not needed for the analysis')
        self.df = df
        return True

    def date_filter(self):
        """
        - To remove dates on which the pilot test was conducted from the dataset
        """
        df = self.df 
        dates = self.dates
        for date in dates:
            df = df[df['today'] != date]
        self.df = df
        return True
        
    def missing_value_clean(self):
        """
        - To detect and remove missing values
        """
        miss_col = self.miss_col
        df = self.df
        del_type = self.del_type
        initial_data_points = len(df)
        num_missing_cols = {}
        print("")
        for col in miss_col:
            missing_count = df[col].isnull().sum()
            num_missing_cols[col] = missing_count
            print(f'Column {col} has {missing_count} missing values')
    
        if del_type == 0: # Remove all missing values from the columns where missing values are detected
            df_cleaned = df.dropna(subset=miss_col)

        # First, remove columns where missing values make up 10% or more of the total data points
        # Then, remove all remaining missing values from the columns where they are detected
        elif del_type == 1:
            threshold = 0.1 * initial_data_points
            cols_to_drop = [col for col, missing_count in num_missing_cols.items() if missing_count > threshold]
            df_cleaned = df.drop(columns=cols_to_drop)
            print("")
            print(f'Number of columns: {len(df.columns)} | After removing the columns that contained missing values more than 10% of data points')
            print(f'Dropped columns = {cols_to_drop}')
            df_cleaned = df_cleaned.dropna(subset=miss_col)
        
        remaind_data_points = len(df_cleaned)
        print("")
        print(f'Number of deleted missing values: {initial_data_points - remaind_data_points}')
        print(f"Number of data points after missing value handling: {remaind_data_points}")
        print("")
        self.df = df_cleaned
        return True
    
    def save_data(self):
        """
        - To save the new dataframe
        """
        df = self.df
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        if file_type == 'xlsx':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx' or 'csv' file")
            return False
        
    def data_anonymisation(self):
        """
        - To implement a dataframe anonymisation
        """
        df = self.df
        col1 = self.anon_col
        file_path = self.file_path
    
        def generate_unique_strings(prefix, series):
            unique_values = series.unique()
            key_mapping = {value: f"{prefix}{uuid.uuid4()}" for value in unique_values}
            return series.map(key_mapping), key_mapping
    
        df[col1], respondent_mapping = generate_unique_strings('respondent_', df[col1])
        original = self.file_path
        self.file_path = f'{file_path}_anonymised'
        self.save_data()
        self.file_path = original
        self.df = df
        print("The respondent name has been anonymised")
        return True
    
    def duplicates(self):
        """
        - To detect and remove duplicates
        """
        df = self.df
        col = self.identifiers
        duplicates = df[df.duplicated(subset=col, keep=False)]
        print("")
        print(f"Number of duplicate based on '{col}': {len(duplicates)}")

        if not duplicates.empty:
            print("Duplicate rows:")
            print(duplicates)
    
        df_cleaned = df.drop_duplicates(subset=col, keep='first')
    
        print(f"Number of data points: {len(df_cleaned)} | After removing duplicates")
        print("")
        self.df = df_cleaned
        return True

    def open_ended_cols(self):
        """
        - To save opened-ended columns and remove these from the dataset
        """
        df = self.df
        cols = self.opened_cols
        file_path = self.file_path_others
        empty_df = pd.DataFrame()
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df.to_excel(writer, sheet_name='basic', index=False)
        
            max_length = 0
            unique_data = {}

            for col in cols:
                unique_values = df[col].dropna().unique()
                unique_data[col] = unique_values
                max_length = max(max_length, len(unique_values))
        
            combined_df = pd.DataFrame({col: pd.Series(unique_data[col]) for col in cols})
            combined_df.to_excel(writer, sheet_name='open_ended', index=False)
        
        print(f"Open-ended columns have been saved to '{file_path}': {cols} ")
        df = df.drop(columns=cols)
        print(f'Number of columns: {len(df.columns)} | After removing the open-ended columns')
        self.df = df
        return True

    def columns_redefine(self):
        """
        - To change column names for smoother data analysis
        """
        df = self.df
        new_cols = self.cols_new
        file_path = f'{self.file_path}_columns_book.xlsx'
        original_cols = list(df.columns)
        df.columns = new_cols
    
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df = pd.DataFrame()
            empty_df.to_excel(writer, sheet_name='basic', index=False)

            columns_df = pd.DataFrame({'Column Names': new_cols,'Original Names': original_cols})
        
            columns_df.to_excel(writer, sheet_name='Column_Info', index=False)

            workbook = writer.book
            worksheet = workbook['Column_Info']
        
            for col in worksheet.columns:
                max_length = max(len(str(cell.value)) for cell in col)
                adjusted_width = max(max_length, 12)
                worksheet.column_dimensions[col[0].column_letter].width = adjusted_width

        print(f"Column information has been saved: {file_path}")
        self.df = df
        return True
    
    def re_order(self):
        """
        - Reorder the columns of self.df according to self.new_order
        """
        df = self.df
        new_order = self.new_order
    
        cols_to_use = [col for col in new_order if col in df.columns]
        df = df[cols_to_use]
    
        self.df = df
        print(f"Columns have been reordered according to new_order: {cols_to_use}")
        return True

    def age_group(self):
        """
        - To create new age group variable
        """
        df = self.df
        col = self.age_col
        bins = [0, 17, 24, 34, 44, 54, 64, float('inf')]
        labels = ['Below 18','18 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years']
        df[col] = df[col].astype(int)
        df['Age Group'] = pd.cut(df[col], bins=bins, labels=labels, right=True)
        print('New age group variable (Age Group) has been created in this dataset')
        self.df = df
        return True
    
    def disability(self):
        """
        - Simplified disability variable creation
        - If any of a4_1 ~ a4_6 is 1, mark as 'Disability'
        - If a4_7 is 1, mark as 'No Disability'
        - Default is 'No Disability'
        """
        df = self.df
        cols = ['a5_1', 'a5_2', 'a5_3', 'a5_4', 'a5_5', 'a5_6']
    
        try:
            df['Disability'] = 'No Disability'
    
            df.loc[df['a5_5'] == 1, 'Disability'] = 'No Disability'
    
            df.loc[df[cols[:4]].eq(1).any(axis=1), 'Disability'] = 'Disability'
    
            self.df = df
            print('New disability variable (Disability) has been created')
            return True
    
        except Exception as e:
            print('New disability variable has not been created:', e)
            return False
        
        
    def region_group(self):
        """
        - To create new age group variable
        """
        df = self.df

        west_africa = ['Sierra Leone', 'Ghana', 'Liberia', 'Mali']
        east_africa = ['Kenya', 'Uganda', 'Ethiopia']
        mena = ['Lebanon', 'Jordan']
    
        df['region_group'] = df['country'].apply(
            lambda x: 'West Africa' if x in west_africa else
                      'East Africa' if x in east_africa else
                      'MENA' if x in mena else
                      None
        )

        print('New region group variable (Age Group) has been created in this dataset')
        self.df = df
        return True
        
    def indicator_calculation(self):

        df = self.df
        score_map = {'1 - Not at all': 1,'2 - Slightly': 2,'3 - Moderately': 3,'4 - A Lot': 4,'5 - Extremely': 5}
        
        cso_mapping = {

    'DCI': 'Defence for Children International Ghana',
    'Defence for Children International-Ghana': 'Defence for Children International Ghana',
    'Defence for Children International, Ghana': 'Defence for Children International Ghana',
    
    'Rights and Responsibilities Initiative Ghana': 'Rights and Responsibilities Initiatives Ghana',
    
    'CARD GHANA': 'Community Aid for Rural Development',
    
    'TdH': 'Terre des Hommes Netherlands',
    'TDH': 'Terre des Hommes Netherlands',
    'Terre des Hommes NL': 'Terre des Hommes Netherlands',

    'KAFA (enough) Violence & Exploitation': 'KAFA (Enough) Violence & Exploitation',
    
    'Community Safety Initiative CSI': 'Community Healthcare Initiative',
    
    'Defence for children International Liberia': 'Defence for Children International Liberia',
    'DCI-Liberia': 'Defence for Children International Liberia',
    'DCI-LIBERIA': 'Defence for Children International Liberia',
    'Defense for Children International- Liberia (DCI-Liberia)': 'Defence for Children International Liberia',
    
    "United Funding and Development for Underage Mother's (UFDUM) Inc": 
    'United Funding and Development for Underage Mothers (UFDUM), Inc.',
    
    'Defence for Children International -Sierra Leone': 'Defence for Children International Sierra Leone',
    'Defence for Children International, Sierra Leone': 'Defence for Children International Sierra Leone',
    
    'YADNET UGANDA': 'Youth Advocacy and Development Network (YADNET)',
    'Yadnet': 'Youth Advocacy and Development Network (YADNET)',
    
    'GIRL UP INITIATIVE UGANDA': 'Girl Up Initiative Uganda',
    
    'GLOBAL LEARNING FOR SUSTAINABILITY': 'Global Learning for Sustainability (GLS)',
    'Global Learning for Sustainability(GLS)': 'Global Learning for Sustainability (GLS)'}


        df['cso'] = df['cso'].replace(cso_mapping)
        
        # Outcome 2.2
        df['Outcome2.2'] = df.apply(lambda row: 'Applicable' if row['b9_1'] == 1 or row['b9_3'] == 1 else 'Not applicable',axis=1)
        
        # WRGE 2.2
        df['WRGE2.2'] = df.apply(lambda row: 'Not applicable' if row['b6_2'] == 1 else 'Applicable',axis=1)
        
        # CA.2
        for col in ['b13a', 'b13b', 'b13c', 'b13d', 'b13e']:
            df[col + '_score'] = df[col].map(score_map)
        
        df['CA.2'] = df[['b13a_score', 'b13b_score', 'b13c_score', 'b13d_score', 'b13e_score']].apply(
            lambda x: 'Applicable' if  all(x >= 3) else 'Not applicable', axis=1)
        df.drop(columns = ['b13a_score', 'b13b_score', 'b13c_score', 'b13d_score', 'b13e_score'], inplace = True)
        
        # PD.1
        df['PD.1'] = df.apply(lambda row: 'Applicable' if row['f4'] == "Yes – always" or row['f4'] == "Yes – sometimes" else 'Not applicable',axis=1)

        # LO.2
        df['LO.2'] = df.apply(lambda row: 'Not applicable' if row['b8_1'] == 1 else 'Applicable',axis=1)

        # WRGE5.1
        for col in ['b14a', 'b14b', 'b14c']:
            df[col + '_score'] = df[col].map(score_map)
        
        df['WRGE5.1'] = df[['b14a_score', 'b14b_score', 'b14c_score']].apply(
            lambda x: 'Applicable' if  all(x >= 3) else 'Not applicable', axis=1)
        df.drop(columns = ['b14a_score', 'b14b_score', 'b14c_score'], inplace = True)
        
        # SCS7
        df['SCS7'] = df.apply(lambda row: 'Not applicable' if row['b10_4'] == 1 else 'Applicable',axis=1)
        
            #lambda x: 'Applicable' if x.sum() >= 21 else 'Not applicable', axis=1)
        
        self.df = df
        print('All relevant indicators have been measured')        

        
    def processing(self):
        """
        - To conduct data pre-processing
        1. Load the raw dataset
        2. Re-define variable names
        3. Handle duplicates
        4. Anonymise data (Respondents' names)
        5. Remove pilot test data points
        6. Drop unnecessary columns
        7. Handle missing values
        8. Extract answers from open-ended questions
        9. Create age and disability groups
        10. Save the cleaned dataset
        """
        self.data_load()
        self.columns_redefine()
        self.re_order()
        print(f'Initial data points: {len(self.df)}')
        self.duplicates()
        self.data_anonymisation()
        if len(self.dates) != 0:
            self.date_filter()
        print(f'Initial number of columns: {len(self.df.columns)}')
        self.delete_columns()
        self.missing_value_clean()
        self.region_group()
        self.open_ended_cols()
        if self.age_col != None:
            self.age_group()
        if self.diss_cols != None:
            self.disability()
        self.indicator_calculation()
        original = self.file_path
        self.file_path = f'{self.file_path}_cleaned'
        self.save_data()
        self.file_path = original
        print("")
        print(f'Final number of data points: {len(self.df)}')
        print(f"Cleaned dataframe has been saved: {self.file_path}_cleaned.{self.file_type}")
        return True