# -*- coding: utf-8 -*-
import os
import weasyprint as wp
import csv
import jinja2 as j2
import progress.bar as pb

try:
    os.mkdir('director_report')
    os.mkdir('teacher_report')
    os.mkdir('progress')
except OSError:
	pass

csv_file = open('new-data-total.csv','r')
data = csv.DictReader(csv_file, delimiter=',')
env = j2.Environment(loader=j2.FileSystemLoader('./'))

director_tmplt = env.get_template('report_director.html')
teacher_tmplt = env.get_template('report_teacher.html')
progress_tmplt = env.get_template('progress.html')


for row in data:
    filename = row['login'] + '.pdf'
    dir_html = director_tmplt.render(row)
    report_director = wp.HTML(string=dir_html)
    report_director.write_pdf(target='director_report/' + filename)

    teach_html = teacher_tmplt.render(row)
    report_teacher = wp.HTML(string=teach_html)
    report_teacher.write_pdf(target='teacher_report/' + filename)

    progress_html = progress_tmplt.render(row)
    report_progress = wp.HTML(string=progress_html)
    report_progress.write_pdf(target='progress/' + filename)

	
    