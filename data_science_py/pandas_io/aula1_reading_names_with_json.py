#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:41:38 2021

@author: ricardo
"""

import pandas as pd, numpy as np, html5lib, seaborn as sns

from sqlalchemy import create_engine, MetaData, Table

"""in colab could be necessary install !pip3 install html5lib, !pip3 install lxml
!pip install sqlalchemy"""

table_f = pd.read_json('https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=f')

table_m = pd.read_json('https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=m')

#join to tables of names only and convert it into DataFrame

names = pd.concat([table_f, table_m])['nome'].to_frame()

# including student ID in random way, NOT REPEATED!!!

SEED = 132 

total_students = len(names)

# Adding new feature 'student_id'

names['student_id'] = np.random.permutation(total_students) + 1

# Creating two e-mail domains

email_domains = ['@dominiodoemail.com.br', '@servicodoemail.com']

# Random choose to each student

names['domain'] = np.random.choice(email_domains, total_students)

# Create an e-mail name based on previus random choice

names['email'] = names.nome.str.cat(names.domain).str.lower()
""" transform into string to concat both values, names.name and names.domain, then
convert to lowercase"""

# Creating a courses table
""" We can search a already done table!"""

table_courses_address = 'http://tabela-cursos.herokuapp.com/index.html'
#need first import html5lib 

table_courses = pd.read_html(table_courses_address)

#convert the list into a DataFrame

table_courses = table_courses[0]

# avoid spaces between names in columns

table_courses.rename(columns = {'Nome do curso': 'course_name'}, inplace=True)

# create courses id

table_courses['id'] = table_courses.index + 1 #starting at one

# setting id as new index

table_courses.set_index('id', inplace=True)

""" We want to know how many courses each student is taking. So let's record the
number of enrollments per student"""

# We expect few registrations per students, so let's use exponential distribution

names['registration'] = np.random.exponential(size=total_students).astype(int)

# But we don't want students with no registration, so we use np.ceil

names['registration'] = np.ceil(np.random.exponential(size=total_students) * 1.5).astype(int)

# Let's take a look of short statistics

print(names['registration'].describe())

# And take a look in distribution

sns.distplot(names.registration)

# how many students taking number of courses

names.registration.value_counts()

""" But we don't know each student is registred in each course, let's create 
in random manner, link ID to course. We need number of registration per student"""

all_registrations = []

# We have 20 courses

n_courses = len(table_courses)

# each course have a random probability to be chosen

x = np.random.rand(n_courses)

# relative probability of each course be chosen to the rest

prob_x = x /sum(x)

"""iterrows return, in a loop, row by iteration;
loop to iterate over each student id and choose courses according to the 
number of courses enrolled"""

for index, row in names.iterrows():

    #take the student id and number of enrollments
    
    id = row.student_id

    registrations = row.registration
    
    """ Then apply to each student, registration in different courses based on
    random way based in random probabilities"""
    
    for i in range(registrations):

        reg = [id, np.random.choice(table_courses.index, p = prob_x)]
        
        #adding to our list
        
        all_registrations.append(reg)
        
# link id_student to course_id
        
registrations = pd.DataFrame(all_registrations, columns = ['student_id', 'course_id'])

# We'll know how many studens are enrolled in each course

registrations.groupby('course_id').count().join(table_courses).rename(columns={'student_id':'Number of students','course_id': "ID's Course"})

registration_per_course = registrations.groupby('course_id').count().join(table_courses).rename(columns={'student_id':'number_of_students','course_id': "ID's Course"})

# Diferents formats exports

## to csv

registration_per_course.to_csv('registration_per_course.csv', index=False )

## to json

registration_per_course.to_json()

## to html, returns a html table

registration_per_course.to_html()

""" We need to save our data in a Local Database. 
First Let's create our engine, the path where the Database is.

Note Pandas already works with SQL"""

engine = create_engine("sqlite:///:memory:") #memory is the local memory where our database is

# transform our DataFrame registration_per_course into SQL

registration_per_course.to_sql('registrations', engine)

#print names of the tables that are inside

print(engine.table_names())

# Make a query in our SQL database

query = 'select * from registrations where number_of_students < 20'

print(pd.read_sql(query, engine))

## Print entire table with parameters in our desired order

print(pd.read_sql_table('registrations', engine, columns = ['course_name', 'number_of_students']))

# We can make query in pandas itself

many_enrollments = pd.read_sql_table('registrations', engine, columns = ['course_name', 'number_of_students'])

many_enrollments.query('number_of_students > 69')

# Writing in our database

## Another tables was added to it

many_enrollments.to_sql('many_enrollments', con = engine)

print(engine.table_names())

"""Now let's create another class with new students. We must create a worksheet with
course and students list of it to building concierge can know it"""

# Remember

registration_per_course

# Our course will be Estatística básica, course_id = 16, but who are the students?

registrations

course_id = 16

next_class = registrations.query("course_id == {}".format(course_id))

# But we want the names of students

next_class.set_index('student_id').join(names.set_index('student_id'))['nome']

# and export it to a DataFrame

next_class = next_class.set_index('student_id').join(names.set_index('student_id'))['nome'].to_frame()

""" Let's rename DataFrame column to interested course"""

course_name = table_courses.loc[course_id]

course_name[0]

next_class.rename(columns={'nome': f"Alunos do curso de {course_name[0]}"}, inplace=True)

# Let's export it to Excel

next_class.to_excel('next_class.xlsx', index=False)