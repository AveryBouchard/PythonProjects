from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PythonProjects.SafeHaven.autoMagic.edit_csv_files import edit_csv_file
import os
from PythonProjects.SafeHaven.AutoNumbers.user_info import username, password
from PythonProjects.SafeHaven.autoMagic.user_info import reps_dict

driver = Chrome()
Chrome(executable_path='C:/Users/avery/.local/bin/chromedriver.exe')


def main():

    login_to_sales_rabbit()

    login_to_quickbase()

    rep_name_input = " "

    while rep_name_input != "":

        rep_name_input = input("What rep are you making the list for? (avery, mike, ian, quintin, wilson, ian m) ")\
            .lower()

        input_zips(rep_name_input)

        edit_csv_file(find_newest_file(), save_file_name(rep_name_input), get_state(rep_name_input))

        upload_to_sales_rabbit(rep_name_input)


def login_to_quickbase():
    driver.get('https://davidyost-7821.quickbase.com/db/main?a=signin')

    username_field = driver.find_element(By.NAME, "loginid")
    password_field = driver.find_element(By.NAME, "password")

    #  input username and password
    username_field.send_keys(username)
    password_field.send_keys(password + Keys.ENTER)


def input_zips(rep_name):

    office = "Providence"

    #  navigate to leads page
    driver.get("https://davidyost-7821.quickbase.com/db/bjvssf6xf?from=myqb")
    leads_link = driver.find_element(By.XPATH, "/html/body/div[9]/div[12]/ul[1]/li[1]/a")
    leads_link.send_keys(Keys.ENTER)

    #  Choose office from the dropdown menu
    time.sleep(1)
    drop_down_menu = Select(driver.find_element(By.CSS_SELECTOR, "#matchTextMC_0"))
    drop_down_menu.select_by_visible_text(office)
    submit_link = driver.find_element(By.ID, "tableHomePageSearch")
    submit_link.click()

    #  navigate to 2018 Multi Zip
    driver.get("https://davidyost-7821.quickbase.com/db/bjvssf6xv?a=q&qid=906")

    number_of_reps = 1

    text_field_number, reps = 0, 0

    #  gives the option to input zip codes for multiple reps
    while reps < number_of_reps:

        zip_code_input = get_zips(rep_name)

        #  loops through all input zip codes
        for zip_code in zip_code_input:

            #  adds the number of the text field to the end of the element name
            zip_input_field = driver.find_element(By.NAME, "matchText_" + str(text_field_number))

            zip_input_field.send_keys(zip_code)

            #  increment the text field number to go down to the next field
            text_field_number += 1

        reps += 1

        display_report_button = driver.find_element(By.ID, "saveButton")

        display_report_button.send_keys(Keys.ENTER)

        time.sleep(2)

        download_button = driver.find_element(By.ID, "download")

        download_button.send_keys(Keys.ENTER)  # download the CSV file

        time.sleep(1)


def get_zips(rep):

    zip_codes = user_info.reps_dict.get(rep)["zips"].split()

    return zip_codes


def get_state(rep):
    state = user_info.reps_dict.get(rep)["state"]

    return state


def save_file_name(rep):
    saved_file_name = user_info.reps_dict.get(rep)["file_name"]
    saved_file_name = saved_file_name + ".csv"

    return saved_file_name


def find_newest_file():
    folder_path = r'C:/Users/avery/Downloads'
    os.chdir(folder_path)
    newest_file = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)[-1]
    return newest_file


def login_to_sales_rabbit():
    driver.get('https://signin.salesrabbit.com/u/login?state=hKFo2SBZMVJuTVFzMnRzSlYxcW9MWl9JNmhjV0pYMnNkQUpwNKFur3VuaX'
               'ZlcnNhbC1sb2dpbqN0aWTZIG1PODVEdXp1bnlfVlNJQXJxVFVCXzZYbHJjY0d3VVp0o2NpZNkgME9PVDF2SWN4NTdmWkN3cjdQM1RXZ'
               'DkxMjFCQ1o2Ulc')

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)
    driver.find_element(By.NAME, "action").send_keys(Keys.ENTER)


def upload_to_sales_rabbit(rep):

    driver.get("https://app.salesrabbit.com/recruiting/import.php")

    upload_file = find_newest_file()
    choose_file_button = driver.find_element(By.NAME, "csv")
    file_folder = "C:/Users/avery/Downloads"
    choose_file_button.send_keys(file_folder + upload_file)

    drop_down_menu = Select(driver.find_element(By.NAME, "importType"))
    drop_down_menu.select_by_visible_text("Leads")

    driver.find_element(By.NAME, "forward").send_keys(Keys.ENTER)

    driver.find_element(By.NAME, "forward").send_keys(Keys.ENTER)

    lead_owner_drop_down = Select(driver.find_element(By.ID, '1'))
    lead_owner_drop_down.select_by_visible_text(user_info.reps_dict.get(rep)["lead_owner"])

    lead_status_drop_down = Select(driver.find_element(By.ID, '2'))
    lead_status_drop_down.select_by_visible_text("Dispatched")

    driver.find_element(By.NAME, "forward").send_keys(Keys.ENTER)

    driver.find_element(By.NAME, "forward").send_keys(Keys.ENTER)


# rep_name_input = "wilson"
main()
# login_to_sales_rabbit()
# upload_to_sales_rabbit(rep_name_input)
# edit_csv_file("/home/avery/Downloads/Leads (1).csv", save_file_name(rep_name_input), "MA")
# print(user_info.reps_dict.get(user)["zips"])

driver.close()
