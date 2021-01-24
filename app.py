from flask import Flask
from flask import request, jsonify, redirect, url_for, render_template
import pandas as pd

app = Flask(__name__)
data = pd.read_csv('FilteredData.csv')

@app.route('/')
def splash():
    return render_template('splash_a.html')

@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        print(request.form['query'])
        return redirect((url_for('results', query=request.form['query'])))
    return redirect((url_for('splash')))

@app.route('/results/')
@app.route('/results/<query>')
def results(query=None):
    if query is not None:


#         jobsInCity = []
# city = "Noida"
# for i in range (len(df)):
#     if city in df.iloc[i]['Location']:
#         jobsInCity.append(df.iloc[i]) 



#         rolesInCity = {}
# for i in range (len(jobsInCity)):
#     if (jobsInCity[i]['Role'] in rolesInCity):
#         rolesInCity[jobsInCity[i]['Role']] += 1
#     else:
#         rolesInCity[jobsInCity[i]['Role']] = 1


# role = "Software Developer"
# jobs = []
# for i in range (len(jobsInCity)):
#     if role in jobsInCity[i]['Role']:
#         jobs.append(jobsInCity[i])


# jobs is all the jobs of the chosen role in the chosen city

#rolesInCity is a list of all the roles in the chosen city


#jobsInCity is a list of all the jobs in the city
        jobsInCity = []
        # breh
        # need to match cities info with our query value
        for i in range (len(data)):
            if query in data.iloc[i]['Location']:
                jobsInCity.append(data.iloc[i])
        # we need to find the most frequent jobs with appropriate city match
        rolesInCity = {}
        for i in range (len(jobsInCity)):
            if (jobsInCity[i]['Role'] in rolesInCity):
                rolesInCity[jobsInCity[i]['Role']] += 1
            else:
                rolesInCity[jobsInCity[i]['Role']] = 1

        # find the top 5 common roles 
        #rolesInCity.sort(reverse = True)

        # print(rolesInCity)

        sortedVals = sorted(rolesInCity.items(), key=lambda i: i[1], reverse=True)
        top5Roles = sortedVals[:5]
        print(top5Roles)

        # find the number of jobs available to each role in the city
        # jobs = []
        # count = 0
        # role = top5Roles[count]

        # for i in range (len(top5Roles)):
        #     if role in jobsInCity[i]['Role']:
        #         count += 1
        #         jobs.append(jobsInCity[i])
        
        # find the average salary for each role in the city
        
        # salaries = []
        # for i in range(len(jobsInCity)):
        
        # result will be of form
        # {"role":____, "num":____, "avg_pay":______ }
            

        results = ["Textiles Manager", "Supply Chain Analyst", "Software Developer"]
        return render_template('results.html', query=query.capitalize(), results=results)
    else:
        return redirect((url_for('splash')))
    
@app.route('/explore/<query>/<focus>')
def explore(query=None, focus=None):
    if query is not None and focus is not None:
        # breh
        
        query_jobs = []
        city = query.capitalize()
        for i in range (len(data)):
            if city in data.iloc[i]['Location'] and focus in data.iloc[i]['Role']:
                job = {"title":data.iloc[i]["Job Title"],
                       "location":city,
                       "pay": data.iloc[i]['Job Salary'],
                       "skills":data.iloc[i]["Key Skills"]}
                query_jobs.append(job)
                if len(query_jobs) > 4:
                    break
        
        materials = ["YT 123","Khan","blah"]
        return render_template('explore.html', 
                               query=query.capitalize(), 
                               focus=focus, 
                               jobs=query_jobs, 
                               materials=materials)
    else:
        return redirect((url_for('results', query=query)))