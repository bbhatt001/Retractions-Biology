import pandas as pd
import json

with open ('query-university.json','r') as read_f:
    instt_dict= json.load(read_f)

university_df=pd.DataFrame(instt_dict)
university=university_df[['universityLabel','countryLabel']]
# print(len(university))

with open ('query-engg-college.json','r') as read_col:
    college_dict= json.load(read_col)
college_df=pd.DataFrame(college_dict)
college=college_df[['collegeLabel','countryLabel']]
college=college.rename(columns={'collegeLabel':'universityLabel', 'countryLabel':'countryLabel'})
# print(len(college))

with open ('query-university-system.json','r') as read_sys:
    univsystem_dict= json.load(read_sys)
univ_system_df=pd.DataFrame(univsystem_dict)
univ_system=univ_system_df[['universityLabel','countryLabel']]
# print(len(univ_system))
# print(univ_system)

with open ('query-deemeduniversity.json','r') as read_deem:
    deemeduniv_dict= json.load(read_deem)
deemed_univ_df=pd.DataFrame(deemeduniv_dict)
deemed_univ=deemed_univ_df[['universityLabel','countryLabel']]
# print(len(deemed_univ))
# print(deemed_univ)

with open ('query-research-instt.json','r') as read_research:
    research_instt_dict= json.load(read_research)
research_instt_df=pd.DataFrame(research_instt_dict)
research_instt=research_instt_df[['instituteLabel','countryLabel']]

research_instt=research_instt.rename(columns={'instituteLabel':'universityLabel', 'countryLabel':'countryLabel'})
# print(len(research_instt))

with open ('query-academyofsciences.json','r') as read_aca:
    academy_dict= json.load(read_aca)
academy_df=pd.DataFrame(academy_dict)
academy=academy_df[['academyLabel','countryLabel']]
academy=academy.rename(columns={'academyLabel':'universityLabel', 'countryLabel':'countryLabel'})
# print(len(academy))

with open ('query-instt.json','r') as read_instt:
    instt_dict= json.load(read_instt)
instt_df=pd.DataFrame(instt_dict)
instt=instt_df[['instituteLabel','countryLabel']]
instt=instt.rename(columns={'instituteLabel':'universityLabel', 'countryLabel':'countryLabel'})
# print(len(instt))

with open ('research-center.json','r') as read_center:
    center_dict= json.load(read_center)
center_df=pd.DataFrame(center_dict)
center=center_df[['centerLabel','countryLabel']]
center=center.rename(columns={'centerLabel':'universityLabel', 'countryLabel':'countryLabel'})
# print(len(center))

with open ('query-intntlorganisation.json','r') as read_org:
    int_org_dict= json.load(read_org)
int_org_df=pd.DataFrame(int_org_dict)
int_org=int_org_df[['organisationLabel','countryLabel']]
int_org=int_org.rename(columns={'organisationLabel':'universityLabel', 'countryLabel':'countryLabel'})
# print(len(int_org))

with open ('business.json','r') as read_business:
    business_dict= json.load(read_business)
business_df=pd.DataFrame(business_dict)
business=business_df[['businessLabel','countryLabel']]
business=business.rename(columns={'businessLabel':'universityLabel', 'countryLabel':'countryLabel'})
# print('business',len(business))
# print(business.head())

with open ('hospitals.json','r') as read_hospitals:
    hospitals_dict= json.load(read_hospitals)
hospitals_df=pd.DataFrame(hospitals_dict)
hospitals=hospitals_df[['hospitalLabel','countryLabel']]
hospitals=hospitals.rename(columns={'hospitalLabel':'universityLabel', 'countryLabel':'countryLabel'})
#print('###########')
#print(len(hospitals))
#print(hospitals.head())

universe=pd.concat([university,college,univ_system,deemed_univ,research_instt,academy,instt,center,int_org,business,hospitals])
#print(universe.shape)
universe.to_csv('universities2.csv')
#print('#######')
uni=pd.read_csv('universities2.csv')
print(uni.head(100))
#print(uni[uni['universityLabel']=='University of Navarra'])
print(uni.shape)