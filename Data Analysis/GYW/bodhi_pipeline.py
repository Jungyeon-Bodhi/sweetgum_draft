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
df = pd.read_excel('data/25-PI-GLO-1 - Clean Dataset.xlsx')

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    gender = bd.Indicator(df, "Gender", 0, ['a2'], i_cal=None, i_type='count', description='Gender distribution', period='endline', target = None)
    gender.add_var_order(['Female', 'Male', 'Prefer not to say', 'Other (please specify)'])
    indicators.append(gender)
    
    region = bd.Indicator(df, "Region", 0, ['region_group'], i_cal=None, i_type='count', description='Region distribution', period='endline', target = None)
    region.add_var_order(['East Africa', 'West Africa', 'MENA'])
    indicators.append(region)
    
    age = bd.Indicator(df, "Age group", 0, ['a3'], i_cal=None, i_type='count', description='Age Group distribution', period='endline', target = None)
    age.add_var_order(['Under 18', '18-25', '25-35'])
    indicators.append(age)
    
    disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability distribution', period='endline', target = None)
    disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(disability)
    
    role_gyw = bd.Indicator(df, "Role_GYW", 0, ['a5'], i_cal=None, i_type='count', description='What is your role or position in your GYW group?', period='endline', target = None)
    role_gyw.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    role_gyw.add_var_order(['I am a regular member',
                            'I help organise activities and events',
                            'I am part of the leadership team',
                            'I founded to co-founded the group',
                            'I support with communication, outreach and advocacy',
                            'Other (please specify)'])
    indicators.append(role_gyw)
    
    group_1 = bd.Indicator(df, "GYW_group1", 0, ['a7'], i_cal=None, i_type='count', description='Is your group formally registered?', period='endline', target = None)
    group_1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    group_1.add_var_order(['Yes',
                           'No'])
    indicators.append(group_1)
    
    group_2 = bd.Indicator(df, "GYW_group2", 0, ['a8'], i_cal=None, i_type='count', description='Where is your group mainly active?', period='endline', target = None)
    group_2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    group_2.add_var_order(['Rural',
                           'Semi-urban',
                           'Urban'])
    indicators.append(group_2)
    
    group_3 = bd.Indicator(df, "GYW_group3", 0, ['a9'], i_cal=None, i_type='count', description='How many active members does your group have?', period='endline', target = None)
    group_3.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    group_3.add_var_order(['Less than 10',
                           '11 to 20',
                           '21 to 30',
                           'More than 30'])
    indicators.append(group_3)
    
    # Indicator Analysis
    outcome1_2 = bd.Indicator(df, "Outcome 1.2", 0, ['Outcome 1.2'], i_cal=None, i_type='count', description='Outcome 1.2', period='endline', target = None)
    outcome1_2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    outcome1_2.add_var_order(['Applicable','Not applicable'])
    indicators.append(outcome1_2)    
    
    ca1 = bd.Indicator(df, "CA.1", 0, ['CA.1'], i_cal=None, i_type='count', description='CA.1', period='endline', target = None)
    ca1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    ca1.add_var_order(['Applicable','Not applicable'])
    indicators.append(ca1)   
    
    sa2 = bd.Indicator(df, "SA.2", 0, ['SA.2'], i_cal=None, i_type='count', description='SA.2', period='endline', target = None)
    sa2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    sa2.add_var_order(['Applicable','Not applicable'])
    indicators.append(sa2)   
    
    in1 = bd.Indicator(df, "IN.1", 0, ['IN.1'], i_cal=None, i_type='count', description='IN.1', period='endline', target = None)
    in1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    in1.add_var_order(['Applicable','Not applicable'])
    indicators.append(in1) 
    
    in1_2 = bd.Indicator(df, "IN.1_2", 0, ['c4'], i_cal=None, i_type='count', description='Our group includes girls and young women from different age groups.', period='endline', target = None, visual = False)
    in1_2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    in1_2.add_var_order(['1 - Not at all',
                         '2 - Slightly',
                         '3 - Moderately',
                         '4 - A lot',
                         '5 - Extremely'])
    indicators.append(in1_2) 
    
    in1_3 = bd.Indicator(df, "IN.1_3", 0, ['c5'], i_cal=None, i_type='count', description='Our group includes members from different ethnic backgrounds.', period='endline', target = None, visual = False)
    in1_3.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    in1_3.add_var_order(['1 - Not at all',
                         '2 - Slightly',
                         '3 - Moderately',
                         '4 - A lot',
                         '5 - Extremely'])
    indicators.append(in1_3) 
    
    in1_4 = bd.Indicator(df, "IN.1_4", 0, ['c6'], i_cal=None, i_type='count', description='Our group includes members from different religions.', period='endline', target = None, visual = False)
    in1_4.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    in1_4.add_var_order(['1 - Not at all',
                         '2 - Slightly',
                         '3 - Moderately',
                         '4 - A lot',
                         '5 - Extremely'])
    indicators.append(in1_4) 
    
    in1_5 = bd.Indicator(df, "IN.1_5", 0, ['c9'], i_cal=None, i_type='count', description='Our group includes girls and young women of different sexual identities.', period='endline', target = None, visual = False)
    in1_5.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    in1_5.add_var_order(['1 - Not at all',
                         '2 - Slightly',
                         '3 - Moderately',
                         '4 - A lot',
                         '5 - Extremely'])
    indicators.append(in1_5) 
    
    in1_6 = bd.Indicator(df, "IN.1_6", 0, ['c10'], i_cal=None, i_type='count', description='Our group includes girls and young women with disabilities.', period='endline', target = None, visual = False)
    in1_6.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    in1_6.add_var_order(['1 - Not at all',
                         '2 - Slightly',
                         '3 - Moderately',
                         '4 - A lot',
                         '5 - Extremely'])
    indicators.append(in1_6) 
    
    pd1 = bd.Indicator(df, "PD.1", 0, ['PD.1'], i_cal=None, i_type='count', description='PD.1', period='endline', target = None)
    pd1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    pd1.add_var_order(['Applicable','Not applicable'])
    indicators.append(pd1)
    
    lo2_1 = bd.Indicator(df, "LO.2_1", 0, ['c14'], i_cal=None, i_type='count', description='Has the program supported any social media campaigns for your GYW group or network?', period='endline', target = None)
    lo2_1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    lo2_1.add_var_order(['Yes','No'])
    indicators.append(lo2_1)
    
    lo2_2 = bd.Indicator(df, "LO.2_2", 0, ['c15'], i_cal=None, i_type='count', description='If yes, how many?', period='endline', target = None)
    lo2_2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    lo2_2.add_var_order(['1','2', '3', '4', '5+'])
    indicators.append(lo2_2) 
    
    
    # Evaluation Questions 
    e182_1 = bd.Indicator(df, "Eval_182_1", 0, ['i1_1', 'i1_2', 'i1_3', 'i1_4', 'i1_5', 'i1_6', 'i1_7'], i_cal=None, i_type='count', description='Have any outside issues made it harder for your group to do its work?', period='endline', target = None)
    e182_1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e182_1.add_var_change({1: "Yes", 0: "No"})
    e182_1.add_var_order([1, 0])
    e182_1.add_label([ 'COVID-19',
                    'Community opposition',
                    'Conflict or violence',
                    'Lack of funding',
                    'None',
                    'Online harassment',
                    'Other (please specify)'])
    indicators.append(e182_1)
    
    e182_2 = bd.Indicator(df, "Eval_182_2", 0, ['i2'], i_cal=None, i_type='count', description='Have any internal issues within your group made things difficult?', period='endline', target = None)
    e182_2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e182_2.add_var_order(['Yes','No', 'Not sure'])
    indicators.append(e182_2)
    
    e221_1 = bd.Indicator(df, "Eval_221_1", 0, ['b2'], i_cal=None, i_type='count', description='The training sessions I attended through She Leads were high quality and useful', period='endline', target = None)
    e221_1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e221_1.add_var_order(['1 - Not at all',
                          '2 - Slightly',
                          '3 - Moderately',
                          '4 - A lot',
                          '5 - Extremely'])
    indicators.append(e221_1)
    
    e221_2 = bd.Indicator(df, "Eval_221_2", 0, ['e1'], i_cal=None, i_type='count', description='Has your group taken any actions to keep the work going after She Leads ends?', period='endline', target = None)
    e221_2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e221_2.add_var_order(['Yes','No', 'Not sure'])
    indicators.append(e221_2)
    
    e221_3 = bd.Indicator(df, "Eval_231_3", 0, ['e2_1', 'e2_2', 'e2_3', 'e2_4', 'e2_5', 'e2_6'], i_cal=None, i_type='count', description='What kind of actions were taken?', period='endline', target = None)
    e221_3.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e221_3.add_var_change({1: "Yes", 0: "No"})
    e221_3.add_var_order([1, 0])
    e221_3.add_label([ 'Applied for funding',
                      'Built partnerships with other groups',
                      'Created a long-term plan',
                      'None',
                      'Other (please specify)',
                      'Trained new leaders',])
    indicators.append(e221_3)
    
    e231_1 = bd.Indicator(df, "Eval_231_1", 0, ['e3'], i_cal=None, i_type='count', description='Do you think the changes from She Leads will continue in the short-term (next 6–12 months)?', period='endline', target = None)
    e231_1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e231_1.add_var_order(['Yes','No', 'Not sure'])
    indicators.append(e231_1) 
    
    e231_2 = bd.Indicator(df, "Eval_231_2", 0, ['e4'], i_cal=None, i_type='count', description='Do you think the changes will continue in the long-term (beyond 1 year)?', period='endline', target = None)
    e231_2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e231_2.add_var_order(['Yes','No', 'Not sure'])
    indicators.append(e231_2) 
    
    e422_1 = bd.Indicator(df, "Eval_422_1", 0, ['h1'], i_cal=None, i_type='count', description='In the She Leads program, how often were you informed about decisions made?', period='endline', target = None)
    e422_1.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e422_1.add_var_order(['Never','Sometimes', 'Often', 'Always'])
    indicators.append(e422_1)
    
    e422_2 = bd.Indicator(df, "Eval_422_2", 0, ['h2'], i_cal=None, i_type='count', description='How often were you asked for your opinion before a decision was made?', period='endline', target = None)
    e422_2.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e422_2.add_var_order(['Never','Sometimes', 'Often', 'Always'])
    indicators.append(e422_2) 
    
    e422_3 = bd.Indicator(df, "Eval_422_3", 0, ['h3'], i_cal=None, i_type='count', description='How often did you take part in making decisions?', period='endline', target = None)
    e422_3.add_breakdown({'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    e422_3.add_var_order(['Never','Sometimes', 'Often', 'Always'])
    indicators.append(e422_3) 
    
    return indicators
    
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    
    o12 = bd.Indicator(df, "Outcome 1.2", 0, ['Outcome 1.2'], i_cal=None, i_type='count', description='Chi2 Test - Outcome 1.2', s_test = 'chi', s_group = {'region_group':'Region', 'a2':'Gender', 'a3':'Age Group', 'Disability' : 'Disability'})
    indicators.append(o12)
    
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
"""
df_ken = df[df['country'] == 'Kenya']

indicators = []
indicators = statistics(df_ken, indicators)
indicators = statistical_indicators(df_ken, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics_KEN.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results_KEN.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Kenya/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF
"""
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

#Overall
indicators = []
indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
sweetgum.add_indicators(indicators)

file_path1 = 'data/Sweetgum Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Sweetgum Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/Overall/' # File path for saving visuals

sweetgum.PMF_generation(file_path1, file_path2, folder) # Run the PMF

"""
