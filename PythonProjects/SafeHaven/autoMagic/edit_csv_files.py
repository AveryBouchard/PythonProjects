import datetime
import csv


def edit_csv_file(read_file, write_file, state="RI"):
    header = ['Last Name','QB Prospect ID','State','First Name','Address','City','Zip','Property Value','Closing Date',
        'Visit Rep','# 0f Visits','Last Visit','Visit Date','LVS','Appointment Date & TIme','Notes','Notes','Unix Code',
        'Date Created','Market','Visit - Property Owner 1','Visit - Property Owner 2','Lead Source']

    read = open(read_file, "r", encoding='ISO-8859-1')
    write = open(write_file, "w", encoding='ISO-8859-1')

    csv_read = csv.reader(read)
    csv_write = csv.writer(write)

    next(csv_read)

    today = datetime.datetime.today()
    two_weeks = datetime.timedelta(days=14)
    one_month = datetime.timedelta(days=30)
    too_new = datetime.timedelta(days=5)

    csv_write.writerow(header)

    for row in csv_read:
        if row[10] != 'NHE' and row[10] != 'VAC':
            row[2] = state
            csv_write.writerow(row)

        else:
            split_date = str(row[11].split('-'))
            split_year = split_date[14:18]
            split_month = split_date[2:4]
            split_day = split_date[8:10]

            split_closing_date = str(row[8].split('-'))
            split_closing_year = split_closing_date[14:18]
            split_closing_month = split_closing_date[2:4]
            split_closing_day = split_closing_date[8:10]

            closing_date = str(split_closing_year + ' ' + split_closing_month + ' ' + split_closing_day)
            closing_date = datetime.datetime.strptime(closing_date, "%Y %m %d")
            visit_date = str(split_year + ' ' + split_month + ' ' + split_day)
            visit_date = datetime.datetime.strptime(visit_date, "%Y %m %d")

            if row[10] == "NHE" and visit_date > today - two_weeks or \
                    row[10] == "VAC" and visit_date > today - one_month or \
                    closing_date > today - too_new:
                row.clear()

            else:
                csv_write.writerow(row)
