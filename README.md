
# Assignment 2 - DSP301x_1.1-A

🔥 **README** 🔥
This is my work of Assignment 2 in DSP301x_1.1-A class (Introduce about Data Science). I'm trying to use English so it'll have some 
grammar error, vocab,... But I hope you can understand it :)

In Assignment 2, with description is we need to code a program that it can read a answer file per class, filter data, calculate score of student in that class, statistical with data score of student and write to a file. After all, we need use pandas and numpy to redo tasks before. This problem can be devied to 5 task:
    - Task 1: Open & Check file
    - Task 2: Data progessing¶
    - Task 3: Calculate mark of student
    - Task 4: Save data to file
    - Task 5: Use pandas & numpy and redo 4 above tab 
    
### 0. Enviroment
- Python 3.9
- Anaconda 3

### 1. Library

I'm using some libraries: **Pandas** & **Numpy** to handle task about data

### 2. Variable

```
    filename - Name of the file (except for tail '.txt)
    
    markOfStudents - Data answers of Students when open file
    
    valid_mark - List answers valid
    
    total_valdid_data - Total valid data
    
    total_invalid_data -  Total invalid data
    
    mark_table - List answers of Students when split (',')
    
    scores - List score when calculate

    answer_key - key of answer
    
    wrong_answer - list total which student wrong answer
    
    omitted_answer - list total which student wrong answer

    total_highest_score - total number of score students >80 
    
    mean - mean of list score
    
    median -  median of list score
    
    score_table - score table when fill 0 in NaN value
    
```

### User manual
#### 1. Run Program:
- If you use Anaconda or Colab to run, you must run all of function in file code. In my file code, I name it is **"lastname_firstname_grade_the_exams.ipynb**. I sorted all function to head of file and you can run continuous with '''Shift + Enter''' when meet Main program.

- If you use another code editor: just run :))

#### 2. Input name of file:
- I code automatic add tail of file '.txt' so you only input name of file. E.g: file name you want to open is class1.txt, you just input class1 :)

#### 3. Program show result:
- My program will progress and show you result of calculates: Total student of high scores, Mean, Max,..
- If you use Anaconda or Colab to run, you need only run sequence the blocks of code that I have extracted.

#### 4. Save file:
- Similar as open file, I code automatic add tail of file '_grade.txt'
- You need only enter a name class which you want to save.

### Acknowledgments 
Thank Funix for opening a useful course, thank you Cousera, Khanhblog for providing me with the knowledge to apply to this exercise.
Thank Hahnna Hien when push the deadline for me :) This is the first step and also 1/5, I know the next courses will be more difficult but I will try my best.

