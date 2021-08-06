import pandas as pd

def disp():
  MD = pd.read_excel(r'motions.xlsx')
  print('There are ' , len(MD), ' motions in the database.')


MD = pd.read_excel(r'motions.xlsx')
THW_DB = MD.loc[MD['Motions'].str.contains('THW|This House Would', na = False , case=False)]
THS_DB = MD.loc[MD['Motions'].str.contains('THS|This house supports', na = False , case=False)]
THR_DB = MD.loc[MD['Motions'].str.contains('THR|This House Regrets', na = False , case=False)]
THas_DB = MD.loc[MD['Motions'].str.contains('TH as|This House as|TH, as|This house, as', na = False , case=False)]
THP_DB = MD.loc[MD['Motions'].str.contains('THP|This House prefers', na = False , case=False)]
THBT_DB = MD.loc[MD['Motions'].str.contains('THBT|This House believes that', na = False , case=False)]
THO_DB = MD.loc[MD['Motions'].str.contains('THO|This House Opposes', na = False , case=True)]

Motions_list = [THW_DB, THR_DB, THO_DB, THP_DB, THas_DB, THBT_DB, THS_DB]

def disp_InfoMotions():
  sum_IS = 0
  sum_total = 0
  for df, name  in zip(Motions_list,  ['THW_DB', 'THR_DB', 'THO_DB', 'THP_DB', 'THas_DB', 'THBT_DB', 'THS_DB'] ) :
    info_df = df.loc[df["Infoslide"].notna()]
    sum_IS += len(info_df)
    sum_total += len(df)
    print (name , " has ", len(info_df), " motions with infoslides.")
    print (name , " has ", len(df), " motions.")
    print(df.loc[df["Infoslide"].notna()].head())
    print ('--------------------------------------')

def getMotion(motion_type = 'default'): 
  raw_motion = []
  
  if motion_type == 'THW':
    raw_motion = (THW_DB.sample().reset_index())

  if motion_type == 'Actor':
    raw_motion = (THas_DB.sample().reset_index())

  if motion_type == 'THP':
    raw_motion = (THP_DB.sample().reset_index())

  if motion_type == 'THR':
    raw_motion = (THR_DB.sample().reset_index())

  if motion_type == 'THS':
    raw_motion = (THS_DB.sample().reset_index())

  if motion_type == 'THBT':
    raw_motion = (THBT_DB.sample().reset_index())  

  if motion_type == 'THO':
    raw_motion = (THO_DB.sample().reset_index())  
  
  motion = raw_motion['Motions'].item()
  Infoslide = raw_motion['Infoslide'].item()  
  
  return [motion, Infoslide]
