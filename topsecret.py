from datetime import datetime
import time as t
import csv

reports = []
with open('AL Report 8.28.17 - 10.16.17.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')

    i=0
    for row in csvReader:
        if(i>0):

            grade="unknown"
            if(i>1):
                newName=row[0]+" "+row[1]
                if(newName==name):
                    newTime=t.mktime(datetime.strptime(row[4]+","+row[5],"%Y-%m-%d,%I:%M:%S %p").timetuple())
                    
                    videoLength =row[9]
                    minutes=videoLength[0]+videoLength[1]+""
                    minutes=int(minutes)
                    minutes=minutes*60
                    seconds=videoLength[4]+videoLength[5]+""
                    seconds=int(seconds)
                    videoLength=minutes+seconds

                    if((time-newTime)>=(videoLength-5)):
                        grade="pass"
                    else:
                        grade="fail"


            name=row[0]+" "+row[1]
            time=t.mktime(datetime.strptime(row[4]+","+row[5],"%Y-%m-%d,%I:%M:%S %p").timetuple())
            application=row[6]
            series=row[7]
            title=row[8]

            report=(name,series,title,grade,application)
            reports.append(report)

        i=i+1

for i in range(len(reports)-2,-1,-1):
    for j in range(len(reports)-1,i,-1):
        if reports[i][0] == reports[j][0]:
            if reports[i][2] == reports[j][2]:
                if reports[i][3] != "pass" and reports[j][3] == "pass":
                    temp=reports[i]
                    reports[i]=reports[j]
                    reports[j]=temp

                del reports[j]


with open('output1.csv','w',newline='') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['name','series title','video title','grade','application'])
    for report in reports:
        if report[3]=='pass':
            csv_out.writerow(report)

videos = {}
with open('Canvas Word and Excel Lists.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        if row[0] not in videos.keys():
            videos[row[0]]={}
        if row[1] not in videos[row[0]].keys():
            videos[row[0]][row[1]]=[]
        videos[row[0]][row[1]].append(row[2])
del videos['Application']

students = []
with open('Student List.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        students.append(row[0])
del students[0]

reports = {}
with open('output1.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        if row[4] not in reports.keys():
            reports[row[4]]={}
        if row[0] not in reports[row[4]].keys():
            reports[row[4]][row[0]]={}
        if row[1] not in reports[row[4]][row[0]].keys():
            reports[row[4]][row[0]][row[1]]=[]
        reports[row[4]][row[0]][row[1]].append(row[2])
del reports['application']

for application in videos.keys():
    with open("output/"+application+'_output.csv', 'w', newline='') as out:
        title=[]
        title.append("")
        for key in videos[application].keys():
            title.append(key)
        title.append("Total")
        csv_out = csv.writer(out)
        csv_out.writerow(title)

        for student in students:
            if student in reports[application].keys():
                row=[]
                row.append(student)
                total=0
                for series in sorted(videos[application].keys()):
                    if series in reports[application][student].keys():
                        row.append(len(reports[application][student][series]))
                        total+=len(reports[application][student][series])
                    else:
                        row.append(0)
                row.append(total)
                csv_out.writerow(row)

        row=["Videos In Series: "]
        total=0
        for series in sorted(videos[application].keys()):
            row.append(len(videos[application][series]))
            total+=len(videos[application][series])
        row.append(total)
        csv_out.writerow(row)