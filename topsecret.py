import csv

videos = []
with open('Canvas Word and Excel Lists.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        videos.append(row)
del videos[0]

students = []
with open('Student List.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        students.append(row)
del students[0]

reports = []
with open('AL Report 8.28.17 - 10.16.17.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        reports.append(row)
del reports[0]

counts = {}
vidCount = 0
prev = videos[0]
for video in videos:
    if video[1]!=prev[1]:
        counts[prev[1]]=vidCount
        vidCount=1
        prev = video
    elif video == videos[-1]:
        vidCount+=1
        counts[video[1]]=vidCount
    else:
        prev = video
        vidCount+=1
print(counts)
#stuCount = []
#vidCount =0
#for student in students:
 #  for report in reports:
  #      if report[0]!=name:

   #     elif report==reports[-1]:

    #    else:

#ans = []
#for stu in stuCount:
