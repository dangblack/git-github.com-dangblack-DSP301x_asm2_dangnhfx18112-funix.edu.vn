#!/usr/bin/env python
# coding: utf-8

# # Assignment 2 - Test Grade Caculator

# ## Task 1: Open & Check file

# *Define Input - Output:*
# 
# |      INPUT        |          OUTPUT         |
# |:-----------------:|:-----------------------:|
# |a name of the file | result of checking file |
# 

# In[3]:


# Create a function input a file name

def input_filename():
    while 1:
        filename = input('Enter a name of file: ')
        if filename == "":
            print("File name can not empty. Please enter again!")
        else:
            return filename


# In[4]:


# Create a function open file

def open_file(filename):
    try:
            # add tail of file 'txt'
            filePath = filename.strip()+'.txt'
            
            # open file
            with open(filePath, 'r') as file:
                print("Successfully opened ", filename)
                mark_table = file.read()
                return mark_table
    except:
            print("File cannot be found.")


# ## Task 2: Data progessing

# *Define Input - Output:*
# 
# |      INPUT        |          OUTPUT         |
# |:-----------------:|:-----------------------:|
# | Data of file      | Valid data & Invalid data |
# 
# 

# In[5]:


def check_value_data():
    valid_mark = []
    total_valdid_data = 0
    total_invalid_data = 0
    mark_table = []
    # Split data whenerver look at '\n' in row
    mark_table = markOfStudents.split('\n')

    for line in mark_table:
        x = line.strip().split(",")

        # Check data per row:
        # Valid data will have len = 26, first character = N and after is digrit, student code has 9 characters
        if len(x) == 26:
            if x[0][0:1] == 'N' and x[0][1:].isnumeric() == True and len(x[0])==9:
                total_valdid_data +=1
                valid_mark.append(line)
            else:
                total_invalid_data +=1
                print(f'Invalid student code: \n {line} \n')
        else:
            total_invalid_data +=1
            print(f'Data in row does not have correct character or wrong student code: \n {line}\n')
    return valid_mark, total_valdid_data, total_invalid_data, mark_table


# ## Task 3: Calculate mark of student

# *Define Input - Output:*
# 
# |      INPUT        |          OUTPUT         |
# |:-----------------:|:-----------------------:|
# | Valid Mark        | List Scrore, List wrong answer, List ommited answer  |
# | List Scrore, List wrong answer, List ommited answer      | Statistical: Count score of Student > 80, mean, max, min,| 
# | List Scrore, List wrong answer, List ommited answer      | value domain, median, list question skipped, list question wrong |
# 
# 

# In[16]:


def cal_mark(valid_mark):
    # Create list scrore
    scores = []
    # Calculate mark
    for line in valid_mark:
        x = line.strip().split(',')
        score = 0
        for i in range(len(x)-1):
            if x[i+1] == answer_key[i]:
                score += 4
            elif x[i+1] == '':
                score += 0
                omitted_answer[i] = omitted_answer[i] + 1
            else:
                score = score - 1
                wrong_answer[i] = wrong_answer[i] + 1
        scores.append(score)
    return scores, omitted_answer, wrong_answer


# In[17]:


def find_median_score(scores):
    if len(scores)/2 != 0:
        a = int(len(scores)/2) + 1
        median = sorted(scores)[a]
    else:
        a = int(len(scores)/2)
        b = int(len(scores)/2) + 1
        median = (sorted(scores[a]) + sorted(scores[b]))/2
    return median


# In[18]:


'''
    Statistical:
    - Total student of high scores: score > 80
    - Mean (average) score: Mean = Total marks / count valid mark
    - Max
    - Min
    - Value domain = Max - Min
    - Median = 
    - Question that most people skip:
    - Question that most people answer incorrectly:
    
    Question that most people skip: 3 - 4 - 0.2 , 5 - 4 - 0.2 , 23 - 4 - 0.2

    Question that most people answer incorrectly: 10 - 4 - 0.20, 14 - 4 - 0.20, 16 - 4 - 0.20, 19 - 4 - 0.20, 22 - 4 - 0.20
'''





# In[8]:


# Count score of Student > 80
def count_highest_score(scores):
    total_highest_score = 0
    for i in range(len(scores)):
        if scores[i] > 80:
            total_highest_score += 1
    return total_highest_score


# In[9]:


# Mean (average) score:
def mean_score(scores):
    mean = float(sum(scores)/len(scores))
    return mean
    


# In[10]:


# find most wrong answers
def find_most_wrong_answers(wrong_answer):
    # Find most wrong answers
    i=0
    for i in range(len(wrong_answer)):
        if wrong_answer[i] == max(wrong_answer):
            print('Question that most people skip is Number No :', i+1, '- ', max(wrong_answer), '- ', max(wrong_answer)/25)


# In[35]:


# Find most omitted answers is number no - people skip - % skip
def find_most_omitted_answers(omitted_answer):
    for i in range(len(omitted_answer)):
        if omitted_answer[i] == max(omitted_answer):
            print('Question that most people skip is Number No :', i+1, '- ', max(omitted_answer), '- ', max(omitted_answer)/25)
    


# ## Task 4: Save data to file

# *Define Input - Output:*
# 
# |      INPUT        |          OUTPUT         |
# |:-----------------:|:-----------------------:|
# | List student code, score        | A file saved with data code, score  |
# 

# In[38]:


def create_list_score(valid_mark,scores):
    name_id = []
    for line in valid_mark:
        x = line.strip().split(",")
        name_id.append(x[0])
    score_table = []
    for i in range(len(name_id)):
        score_table.append(name_id[i] + "," + str(scores[i]) + "\n")
    return score_table


# In[44]:


# Save file
def save_file(file_name_save, score_table):
    grade_file = filename + '_grade.txt'
    with open(grade_file, "w") as writefile:
        for line in score_table:
            writefile.write(line)


# ## Main Program

# In[103]:


# Import library
import re
import pandas as pd
import numpy as np

# Define variable name
filename = ''
markOfStudents = []

valid_mark = []
total_valdid_data = 0
total_invalid_data = 0
mark_table = []
scores = []

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(",")
wrong_answer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
omitted_answer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

total_highest_score = 0
mean = 0
median = 0
score_table = []

# -------- Main program --------

# Input a file name
filename = input_filename()

# Open file 
markOfStudents = open_file(filename)
print(markOfStudents)


# In[117]:


# Check value data 
print('--'*10)
valid_mark,total_valdid_data, total_invalid_data, mark_table = check_value_data()
print('--'*10)
print('Total valid data', total_valdid_data)
print('Total invalid data', total_invalid_data)


# In[19]:


# Calculate Mark
scores, omitted_answer, wrong_answer = cal_mark(valid_mark)


# In[20]:


# Count hightest score
total_highest_score = count_highest_score(scores)
print(f'Total student of high scores: {total_highest_score}')


# In[21]:


# Mean
mean = mean_score(scores)
print(f'Mean (average) score: {mean}')


# In[22]:


# Max
print(f'Max: {max(scores)}')


# In[23]:


# Max
print(f'Min: {min(scores)}')


# In[24]:


# Range of Score
print(f'Range of score: {max(scores) - min(scores)}')


# In[25]:


# find median:
find_median_score(scores)


# In[26]:


# find most wrong answers
find_most_wrong_answers(wrong_answer)


# In[29]:


# find most ommited answers
find_most_omitted_answers(omitted_answer)


# In[39]:


# Create list score of student with code:
score_table = create_list_score(valid_mark,scores)
score_table


# In[45]:


# save file score 
save_file(filename, score_table)


# In[58]:


# Test open file save
print(open_file('class1_grade'))


# ## Task 5: Using pandas and numpy to do task 1-4

# ### Main program task 5
# 

# In[258]:


# Import library
import re
import pandas as pd
import numpy as np


# -------- Main program --------
answer_key = ("B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D").split(",")
# Input a file name
filename = input_filename()
filepath = filename + '.txt'
try:
    df = pd.read_csv((filepath), sep = ",", header = None, index_col = 0, on_bad_lines='skip')
    print('Successful open file {}'.format(filepath))
except:
    print('File name invalid')


# In[259]:


df


# In[260]:


# Valid Data
valid_code = df[(df.index.str.len() == 9) & (df.index.str.startswith('N'))]
valid_mark = valid_code[valid_code.index.str.removeprefix("N").str.isdigit()]
valid_mark


# In[261]:


# Invalid Data
invalid_mark = df[~df.index.isin(valid_mark.index)]
invalid_mark


# In[262]:


# fill 0 with empty empty
valid_mark_full = valid_mark.fillna(0)
valid_mark_full


# In[263]:


# cal score per row
for i in range(25): 
    valid_mark_full.loc[:,i + 1][valid_mark_full.loc[:,i+1] == answer_key[i]] = 4
    valid_mark_full.loc[:,i + 1][(valid_mark_full.loc[:,i+1] != 4) & (valid_mark_full.loc[:,i+1] != 0)] = -1
valid_mark_full


# In[264]:


# sum score with column total
valid_mark_full["Total"] = valid_mark_full.loc[:,1:25].sum(axis = 1)
valid_mark_full


# In[265]:


valid_mark_full["Total"].describe()


# In[266]:


# find omited answer
omited_answer_pd = valid_mark_full.apply(lambda x: (x==0).sum(), axis = 'index')
print('question student omited most',omited_answer_pd.idxmax())


# In[267]:


#wrong answer

wrong_answer_pd = valid_mark_full.apply(lambda x: (x==-1).sum(), axis = 'index')

print('question student wrong most',wrong_answer_pd.idxmax())



# In[268]:


valid_mark_full.iloc[:,:26]


# In[269]:


Student_score = valid_mark_full.iloc[:,:25].apply(lambda x: sum(x), axis = 1)
Student_score


# In[270]:


# save file
Student_score.to_csv((filename + '_grade.txt'), sep = ',', header = None)


# In[271]:


# Using numpy
a = np.asarray(Student_score)
a


# In[272]:


a.max()


# In[273]:


a.mean()


# In[274]:


np.median(a)


# In[275]:


np.max(a)

