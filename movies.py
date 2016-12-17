# Movie-Recommendation


import pandas as pd    
import numpy as np
with open('/Users/sbhushan/Downloads/ml-1m/users.dat','r') as f:
    next(f) # skip first row
    users_df = pd.DataFrame(l.rstrip().split() for l in f)
    
with open('/Users/sbhushan/Downloads/ml-1m/ratings.dat','r') as f:
    next(f) # skip first row
    ratings_df = pd.DataFrame(l.rstrip().split() for l in f)
    
with open('/Users/sbhushan/Downloads/ml-1m/movies.dat','r') as f:
    next(f) # skip first row
    movies_df = pd.DataFrame(l.rstrip().split("\n") for l in f)

ratings_df['User_ID'] = 0
ratings_df['Movie_ID'] = 0
ratings_df['Rating'] = 0
ratings_df['Timestamp'] = 0

ratings_np = np.array(ratings_df)

for i in range(0,len(ratings_np)):
    temp_var = ratings_np[i][0].split("::")
    ratings_np[i][1] = temp_var[0] 
    ratings_np[i][2] = temp_var[1] 
    ratings_np[i][3]= temp_var[2]
    ratings_np[i][4] = temp_var[3]
    
ratings_df = pd.DataFrame(data=ratings_np,columns=['Data','User_ID','Movie_ID','Rating','Timestamp'])
del ratings_df['Data']

users_df['User_ID'] = 0
users_df['Gender_ID'] = 0
users_df['Age_ID'] = 0
users_df['Occupation_ID'] = 0
users_df['ZipCode'] = 0

users_np = np.array(users_df)
for i in range(0,len(users_np)):
    temp_var = users_np[i][0].split("::")
    users_np[i][1] = temp_var[0] 
    users_np[i][2] = temp_var[1] 
    users_np[i][3]= temp_var[2]
    users_np[i][4] = temp_var[3]
    users_np[i][5] = temp_var[4]


users_df = pd.DataFrame(data=users_np,columns=['Data','User_ID','Gender_ID','Age_ID','Occupation_ID','ZipCode'])
del users_df['Data']

users_df

movies_df['Movie_ID'] = 0
movies_df['Title'] = ""
movies_df['Genres'] = ""

movies_np = np.array(movies_df)
for i in range(0,len(movies_np)):
    temp_var = movies_np[i][0].split("::")
    movies_np[i][1] = temp_var[0] 
    movies_np[i][2] = temp_var[1] 
    movies_np[i][3]= temp_var[2]
   
movies_df = pd.DataFrame(data=movies_np,columns=['Data','Movie_ID','Title','Genres'])
del movies_df['Data']

users_df['Age_ID'].unique()

users_ratings_df = ratings_df.merge(users_df,on='User_ID',how="left")

users_ratings_movies_df = users_ratings_df.merge(movies_df,on='Movie_ID',how="left")

encoded_occupation = users_ratings_movies_df['Occupation_ID'].unique()
encoded_age = users_ratings_movies_df['Age_ID'].unique()


users_ratings_movies_df['Is_Male'] = 0
users_ratings_movies_df['Is_Female'] = 0
users_ratings_movies_df['Is_Gender_Unkown'] = 0
users_ratings_movies_df['Is_56'] = 0
users_ratings_movies_df['Is_25'] = 0
users_ratings_movies_df['Is_45'] = 0
users_ratings_movies_df['Is_50'] = 0
users_ratings_movies_df['Is_35'] = 0
users_ratings_movies_df['Is_18'] = 0
users_ratings_movies_df['Is_1'] = 0
users_ratings_movies_df['Is_nan'] = 0
users_ratings_movies_df['Is_same_zip'] = 0
users_ratings_movies_df['Is_Occupation_0'] = 0
users_ratings_movies_df['Is_Occupation_1'] = 0
users_ratings_movies_df['Is_Occupation_2'] = 0
users_ratings_movies_df['Is_Occupation_3'] = 0
users_ratings_movies_df['Is_Occupation_4'] = 0
users_ratings_movies_df['Is_Occupation_5'] = 0
users_ratings_movies_df['Is_Occupation_6'] = 0
users_ratings_movies_df['Is_Occupation_7'] = 0
users_ratings_movies_df['Is_Occupation_8'] = 0
users_ratings_movies_df['Is_Occupation_9'] = 0
users_ratings_movies_df['Is_Occupation_10'] = 0
users_ratings_movies_df['Is_Occupation_11'] = 0
users_ratings_movies_df['Is_Occupation_12'] = 0
users_ratings_movies_df['Is_Occupation_13'] = 0
users_ratings_movies_df['Is_Occupation_14'] = 0
users_ratings_movies_df['Is_Occupation_15'] = 0
users_ratings_movies_df['Is_Occupation_16'] = 0
users_ratings_movies_df['Is_Occupation_17'] = 0
users_ratings_movies_df['Is_Occupation_18'] = 0
users_ratings_movies_df['Is_Occupation_19'] = 0
users_ratings_movies_df['Is_Occupation_20'] = 0
users_ratings_movies_df['Is_Occupation_21'] = 0
col_no = 34
l2 = []
#for i in range(0,len(users_ratings_movies_df['ZipCode'].unique())):
    #l2.append(col_no)
    #users_ratings_movies_df[str(col_no)] = 0
    #col_no+=1
users_ratings_movies_np = np.array(users_ratings_movies_df)

ly=[]
print 'here'
for i in range(0,len(users_ratings_movies_np)):
    if users_ratings_movies_np[i][4] == 'M':
       users_ratings_movies_np[i][10] = 1
    if users_ratings_movies_np[i][4] == 'F':
       users_ratings_movies_np[i][11] = 1
    if (users_ratings_movies_np[i][4] != 'M' and users_ratings_movies_np[i][4] != 'F'):
       users_ratings_movies_np[i][12] = 1
    count = 0
    for j in encoded_occupation:
        if users_ratings_movies_np[i][6] == j:
            users_ratings_movies_np[i][22+count] = 1
            break
        count +=1
    count =0
    for j in encoded_age:
        if users_ratings_movies_np[i][5] == j:
            users_ratings_movies_np[i][3+count] = 1
            break
        count +=1
    
    
    #for j in users_ratings_movies_df['ZipCode'].unique():
        
        #if users_ratings_movies_np[i][7] == j:
            #users_ratings_movies_np[i][count] = 1
            #break
        #count = count + 1
    
  users_ratings_movies_df = pd.DataFrame(data=users_ratings_movies_np)
  
  users_ratings_movies_df[7] = pd.to_numeric(users_ratings_movies_df[7], errors='coerce')
  
  input_df = pd.DataFrame(users_ratings_movies_df[:62])
  
  np1 = np.array(users_ratings_movies_df)
  
  
 index = []
differences = []
zip_same = []
def recommender_sri(input_df):
    np2 = np.array(input_df)
    
    for i in range(0,len(np1)):
        index.append(i)
        if np2[58][7] == np1[i][7]:
            zip_same.append(1)
        else:
            zip_same.append(0)
        sum_diff=0
        for j in range(10,42):
            sum_diff += abs(np2[58][j]-np1[i][j])
        differences.append(sum_diff)
    #Run loop over the train data set and calculate the distance between the inpurt data and train data
    #then gather all user_ids with similar features
    #if multiple users ids with same distance, sort by prioritizing features
    # How to know which feature is better ? -- tr
    
    
    recommender_sri(input_df)
    
    
    
    final_df = pd.DataFrame(columns=['Index_Value','Difference','Same_Zip'])
    
    
final_df['Index_Value'] = index
final_df['Difference'] = differences
final_df['Same_Zip'] = zip_same
    
    
matched_index = final_df[final_df['Same_Zip']==1]['Index_Value']


recommended_movies = []
for i in matched_index:
    recommended_movies.append(np1[i][8])
    
 
 
recommended_movies
    
    
    
