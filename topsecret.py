import csv

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