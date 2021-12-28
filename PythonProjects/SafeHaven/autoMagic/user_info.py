import datetime

username = "ABouchard@mysafehaven.com"
password = "Duarte1986!"

month = str(datetime.date.today()).split('-')[1]
day = str(datetime.date.today()).split('-')[2]

reps_dict = {
    "avery": {"rep": "avery", "zips": "02901 02903 02905 02907 02909 02910", "lead_owner": "Avery Bouchard 39819",
              "file_name": f"Avery PVD {month}-{day}", "state": "RI"},
    "mike": {"rep": "mike", "zips": "02908 02904 02911 02919 02864 02865", "lead_owner": "Michael Bottasso 48362",
             "file_name": f"Mike Prov {month}-{day}", "state": "RI"},
    "ian": {"rep": "ian", "zips": "02860 02861 02863 02906 02914 02915 02916", "lead_owner": "Ian Sauvageau 39668",
            "file_name": f"Ian Paw {month}-{day}", "state": "RI"},
    "quintin": {"rep": "quintin", "zips": "02740 02744 02745 02746 02743 02719 02738 02739", "lead_owner":
        "Quintin Botelho 64588", "file_name": f"Q NB {month}-{day}", "state": "MA"},
    "wilson": {"rep": "wilson", "zips": "02302 02301", "lead_owner": "Wilson Delaleu 66073", "file_name":
        f"Wilson Brock {month}-{day}", "state": "MA"},
    "ian m": {"rep": "ian m", "zips": "02720 02721 02723 02724 02725 02726 02791 02790", "lead_owner":
        "Ian McKinnon 65063", "file_name": f"IanM FR {month}-{day}", "state": "MA"}
}