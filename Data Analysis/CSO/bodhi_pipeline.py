#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/25-PI-GLO-1 - Clean Dataset (CSO).xlsx')

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    
    country = bd.Indicator(df, "Country", 0, ['country'], i_cal=None, i_type='count', description='Country', period='endline', target = None, visual = False)
    country.add_var_order(["Sierra Leone",
                           "Ghana",
                           "Liberia",
                           "Mali",
                           "Kenya",
                           "Uganda",
                           "Ethiopia",
                           "Lebanon",
                           "Jordan",
                           "Netherlands",
                           "Switzerland",
                           "MENA",
                           "Pan-African",
                           "Global"])
    indicators.append(country)
    
    region = bd.Indicator(df, "Region", 0, ['region_group'], i_cal=None, i_type='count', description='Region distribution', period='endline', target = None)
    region.add_var_order(['East Africa', 'West Africa', 'MENA'])
    indicators.append(region)
    
    gender = bd.Indicator(df, "Gender", 0, ['a2'], i_cal=None, i_type='count', description='Gender distribution', period='endline', target = None)
    gender.add_var_order(['Female', 'Male', 'Prefer not to say', 'Other (please specify)'])
    indicators.append(gender)
    
    age = bd.Indicator(df, "Age group", 0, ['a3'], i_cal=None, i_type='count', description='Age Group distribution', period='endline', target = None)
    age.add_var_order(['Under 18', '18-25', '25-35', '35-45', '45-55'])
    indicators.append(age)
    
    disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability distribution', period='endline', target = None)
    disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(disability)
    
    role_cso = bd.Indicator(df, "Role_CSO", 0, ['a6'], i_cal=None, i_type='count', description='What is your main role in your organisation?', period='endline', target = None, visual= False)
    role_cso.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    role_cso.add_var_order(['Director or senior leadership',
                            'Programme manager or coordinator',
                            'Advocacy or policy staff',
                            'Monitoring, Evaluation, and Learning (MEL) staff',
                            'Communications or media staff',
                            'Finance or operations staff',
                            'Other (please specify)'])
    indicators.append(role_cso)
    
    duration = bd.Indicator(df, "CSO_duration", 0, ['a7'], i_cal=None, i_type='count', description='Which of the following best describes the duration of your work on the She Leads programme?', period='endline', target = None)
    duration.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    duration.add_var_order(["Less than 6 months",
                            "6 months to 1 year",
                            "1–2 years",
                            "3–4 years",
                            "5 years or more"])
    indicators.append(duration)
    
    group_1 = bd.Indicator(df, "CSO_type", 0, ['a8'], i_cal=None, i_type='count', description='Type of organization', period='endline', target = None)
    group_1.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    group_1.add_var_order(["NGO",
                           "CBO",
                           "Network",
                           "Media",
                           "Research",
                           "Other (please specify)"])
    indicators.append(group_1)
    
    group_2 = bd.Indicator(df, "CSO_Size", 0, ['a9'], i_cal=None, i_type='count', description='Size of organisation (in staff numbers)', period='endline', target = None)
    group_2.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    group_2.add_var_order(["0 to 5",
                           "6 to 10",
                           "11 to 20",
                           "21 to 30",
                           "More than 30"])
    indicators.append(group_2)
    
    group_3 = bd.Indicator(df, "CSO_focus", 0, ['a10_1', 'a10_2', 'a10_3', 'a10_4', 'a10_5'], i_cal=None, i_type='count', description='Main focus areas (Select up to 2)', period='endline', target = None)
    group_3.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    group_3.add_var_change({1: "Yes", 0: "No"})
    group_3.add_var_order([1, 0])
    group_3.add_label(["Advocacy",
                       "Gender equality",
                       "Other (please specify)",
                       "SRHR",
                       "Youth participation"])
    indicators.append(group_3)
    
    group_4 = bd.Indicator(df, "CSO_Target", 0, ['a11'], i_cal=None, i_type='count', description='Main target group', period='endline', target = None)
    group_4.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    group_4.add_var_order(["Girls & young women",
                           "Youth (general)",
                           "Women",
                           "Marginalised communities",
                           "Other (please specify)"])
    indicators.append(group_4)
    
    group_5 = bd.Indicator(df, "CSO_budget", 0, ['a12'], i_cal=None, i_type='count', description='Approximate % of 2024 budget from She Leads', period='endline', target = None)
    group_5.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    group_5.add_var_order(["< 10%",
                           "10 - 25 %",
                           "25-50%",
                           ">50%"])
    indicators.append(group_5)
    
    # Indicator Analysis
    outcome2_2 = bd.Indicator(df, "Outcome2.2", 0, ['Outcome2.2'], i_cal=None, i_type='count', description='Outcome2.2', period='endline', target = None)
    outcome2_2.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    outcome2_2.add_var_order(['Applicable','Not applicable'])
    indicators.append(outcome2_2)    
    
    wrge22 = bd.Indicator(df, "WRGE2.2", 0, ['WRGE2.2'], i_cal=None, i_type='count', description='WRGE2.2', period='endline', target = None)
    wrge22.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    wrge22.add_var_order(['Applicable','Not applicable'])
    indicators.append(wrge22)   
    
    ca2 = bd.Indicator(df, "CA.2", 0, ['CA.2'], i_cal=None, i_type='count', description='CA.2', period='endline', target = None)
    ca2.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    ca2.add_var_order(['Applicable','Not applicable'])
    indicators.append(ca2)   
    
    
    pd1 = bd.Indicator(df, "PD.1", 0, ['PD.1'], i_cal=None, i_type='count', description='PD.1', period='endline', target = None)
    pd1.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    pd1.add_var_order(['Applicable','Not applicable'])
    indicators.append(pd1)
    
    lo2 = bd.Indicator(df, "LO.2", 0, ['LO.2'], i_cal=None, i_type='count', description='LO.2', period='endline', target = None)
    lo2.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    lo2.add_var_order(['Applicable','Not applicable'])
    indicators.append(lo2)
    
    wrge5_1 = bd.Indicator(df, "WRGE5.1", 0, ['WRGE5.1'], i_cal=None, i_type='count', description='WRGE5.1', period='endline', target = None)
    wrge5_1.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    wrge5_1.add_var_order(['Applicable','Not applicable'])
    indicators.append(wrge5_1)
    
    scs7 = bd.Indicator(df, "SCS7", 0, ['SCS7'], i_cal=None, i_type='count', description='SCS7', period='endline', target = None)
    scs7.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    scs7.add_var_order(['Applicable','Not applicable'])
    indicators.append(scs7)
    
    # Evaluation Questions 
    e182_1 = bd.Indicator(df, "Eval_182_1", 0, ['f7'], i_cal=None, i_type='count', description='Were there internal or external factors that affected your ability to achieve results?', period='endline', target = None)
    e182_1.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e182_1.add_var_order(['Yes','No', 'Not sure'])
    indicators.append(e182_1)
    
    e211 = bd.Indicator(df, "Eval_211", 0, ['c2_1', 'c2_2', 'c2_3', 'c2_4'], i_cal=None, i_type='count', description='Which levels were targeted by these efforts? (Select all that apply)', period='endline', target = None)
    e211.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e211.add_var_change({1: "Yes", 0: "No"})
    e211.add_var_order([1, 0])
    e211.add_label(["Civil society (e.g., CSO collaboration or capacity)",
                    "Institutional (e.g., policy or governance reform)",
                    "Other (please specify)",
                    "Socio-cultural (e.g., norms change)"])
    indicators.append(e211)
    
    e221_1 = bd.Indicator(df, "Eval_221_1", 0, ['c3'], i_cal=None, i_type='count', description='Has your organisation taken steps to ensure sustainability of its own results?', period='endline', target = None)
    e221_1.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e221_1.add_var_order(['Yes','No', 'Not sure'])
    indicators.append(e221_1)
    
    e221_2 = bd.Indicator(df, "Eval_221_2", 0, ['c4_1', 'c4_2', 'c4_3', 'c4_4', 'c4_5', 'c4_6'], i_cal=None, i_type='count', description='Which of the following measures has your organisation taken? (Select all that apply)', period='endline', target = None)
    e221_2.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e221_2.add_var_change({1: "Yes", 0: "No"})
    e221_2.add_var_order([1, 0])
    e221_2.add_label(["Created or supported local safe spaces",
                      "Formed new partnerships or coalitions",
                      "Influenced institutional mechanisms or policies",
                      "Integrated She Leads approaches into internal practices",
                      "Other (please specify)",
                      "Trained GYW leaders or mentors"])
    indicators.append(e221_2)
    
    e221_3 = bd.Indicator(df, "Eval_221_3", 0, ['c5'], i_cal=None, i_type='count', description='Do you think these sustainability measures were useful?', period='endline', target = None)
    e221_3.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e221_3.add_var_order(["Yes, very useful",
                          "Somewhat useful",
                          "Not useful",
                          "Not sure"])
    indicators.append(e221_3)
    
    e231_1 = bd.Indicator(df, "Eval_231_1", 0, ['c6'], i_cal=None, i_type='count', description='Do you think the changes achieved will last in the short term (next 6–12 months)?', period='endline', target = None)
    e231_1.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e231_1.add_var_order(['Yes','No', 'Not sure'])
    indicators.append(e231_1)
    
    e231_2 = bd.Indicator(df, "Eval_231_2", 0, ['c7'], i_cal=None, i_type='count', description='Do you think the changes will last in the long term (after 1 year)?', period='endline', target = None)
    e231_2.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e231_2.add_var_order(['Yes','No', 'Not sure'])
    indicators.append(e231_2)
    
    e311 = bd.Indicator(df, "Eval_311", 0, ['d6'], i_cal=None, i_type='count', description='In your view, how well did She Leads interventions align across different partners in your network?', period='endline', target = None)
    e311.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e311.add_var_order(["Very well",
                        "Somewhat well",
                        "Not very well",
                        "Not at all",
                        "Not sure"])
    indicators.append(e311)
    
    e331 = bd.Indicator(df, "Eval_331", 0, ['d9'], i_cal=None, i_type='count', description='How well did She Leads interventions align with those of other key actors in your country (e.g., government, donors, INGOs)?', period='endline', target = None)
    e331.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e331.add_var_order(["Very well",
                        "Somewhat well",
                        "Not very well",
                        "Not at all",
                        "Not sure"])
    indicators.append(e331)
    
    e411 = bd.Indicator(df, "Eval_411_1", 0, ['f3'], i_cal=None, i_type='count', description='In your experience, how are final decisions made in the She Leads consortium?', period='endline', target = None)
    e411.add_breakdown({'region_group':'Region', 'country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e411.add_var_order(["Mostly by international or lead partners",
                        "Jointly between all partners",
                        "Mostly by local or regional partners",
                        "Not sure"])
    indicators.append(e411)
    
    e411_2 = bd.Indicator(df, "Eval_411_2", 0, ['f4'], i_cal=None, i_type='count', description='Do you feel your organisation had an equal voice in final decision-making within She Leads?', period='endline', target = None)
    e411_2.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e411_2.add_var_order(["Yes – always",
                          "Yes – sometimes",
                          "Rarely",
                          "No"])
    indicators.append(e411_2)
    
    e412_1 = bd.Indicator(df, "Eval_412_1", 0, ['f1_1', 'f1_2', 'f1_3', 'f1_4'], i_cal=None, i_type='count', description='Did your organisation have decision-making power in the design of She Leads?', period='endline', target = None)
    e412_1.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e412_1.add_var_change({1: "Yes", 0: "No"})
    e412_1.add_var_order([1, 0])
    e412_1.add_label(["Global level",
                      "Network level",
                      "No involvement",
                      "Regional level"])
    indicators.append(e412_1)
    
    e412_2 = bd.Indicator(df, "Eval_412_2", 0, ['f2_1', 'f2_2', 'f2_3'], i_cal=None, i_type='count', description='Did your organisation have decision-making power during implementation of She Leads?', period='endline', target = None)
    e412_2.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e412_2.add_var_change({1: "Yes", 0: "No"})
    e412_2.add_var_order([1, 0])
    e412_2.add_label(["Global level",
                      "Network level",
                      "Regional level"])
    indicators.append(e412_2)
    
    e413 = bd.Indicator(df, "Eval_413", 0, ['f6'], i_cal=None, i_type='count', description='Did the programme take your organisation’s advice into account when implementing activities?', period='endline', target = None)
    e413.add_breakdown({'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e413.add_var_order(["Yes – always",
                        "Yes – sometimes",
                        "Rarely",
                        "No"])
    indicators.append(e413)
        
    return indicators
    
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    
    o22 = bd.Indicator(df, "Outcome2.2", 0, ['Outcome2.2'], i_cal=None, i_type='count', description='Chi2 Test - Outcome 2.2', s_test = 'chi', s_group = {'region_group':'Region','country':'Country','a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    indicators.append(o22)
    
    return indicators



# Create the PMF class ('Project Title', 'Evaluation')
sweetgum = pmf.PerformanceManagementFramework('Sweetgum', 'Evaluation')

"""
df_eth = df[df['country'] == 'Ethiopia']

indicators = []
indicators = statistics(df_eth, indicators)
indicators = statistical_indicators(df_eth, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_ETH.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_ETH.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Ethiopia/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF

df_ken = df[df['country'] == 'Kenya']

indicators = []
indicators = statistics(df_ken, indicators)
indicators = statistical_indicators(df_ken, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_KEN.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_KEN.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Kenya/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF

df_ug = df[df['country'] == 'Uganda']

indicators = []
indicators = statistics(df_ug, indicators)
indicators = statistical_indicators(df_ug, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_UG.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_UG.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Uganda/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF

df_jd = df[df['country'] == 'Jordan']

indicators = []
indicators = statistics(df_jd, indicators)
indicators = statistical_indicators(df_jd, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_jd.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_jd.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Jordan/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF


df_lb = df[df['country'] == 'Lebanon']

indicators = []
indicators = statistics(df_lb, indicators)
indicators = statistical_indicators(df_lb, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_lb.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_lb.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Lebanon/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF

df_liberia = df[df['country'] == 'Liberia']

indicators = []
indicators = statistics(df_liberia, indicators)
indicators = statistical_indicators(df_liberia, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_liberia.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_liberia.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Liberia/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF


df_sl = df[df['country'] == 'Sierra Leone']

indicators = []
indicators = statistics(df_sl, indicators)
indicators = statistical_indicators(df_sl, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_sl.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_sl.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Sierra Leone/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF

df_mali = df[df['country'] == 'Mali']

indicators = []
indicators = statistics(df_mali, indicators)
indicators = statistical_indicators(df_mali, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_mali.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_mali.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Mali/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF

df_ghana = df[df['country'] == 'Ghana']

indicators = []
indicators = statistics(df_ghana, indicators)
indicators = statistical_indicators(df_ghana, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_ghana.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_ghana.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Ghana/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF
"""
# Overall
indicators = []
indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Overall/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF