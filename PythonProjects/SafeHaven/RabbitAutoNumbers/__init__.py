from selenium.webdriver import Chrome
# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
import time
import datetime
import os
import csv
from PythonProjects.SafeHaven.AutoNumbers.user_info import username, password

'''
options = FirefoxOptions()
options.set_preference("browser.download.useDownloadDir", True)
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", "path/to/download/directory")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

opts = Options()
opts.headless = False

opts.set_preference("browser.download.manager.showWhenStarting", False)
opts.set_preference("browser.download.folderList", 0)
opts.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

driver = Firefox(options=options)
'''

chrome_options = Options()
chrome_options.headless = False
# params = {'behavior': 'allow', 'downloadPath': './downloads'}

driver = Chrome(options=chrome_options)
# driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

providence = "#matchTextMC_0 >option:nth-child(107)"
boston = "#matchTextMC_0 > option:nth-child(17)"


def main():

    login_to_quickbase()

    print("Providence Leads:\n")
    download_rep_route(providence)
    scrape_csv("Joseph O'Neill 47661")
    scrape_csv('Ralph Cistoldi 62492')
    scrape_csv('Ian Sauvageau 39668')
    scrape_csv('Michael Bottasso 48362')
    scrape_csv('Edward Hurlburt 49826')
    scrape_csv('Wilson Delaleu 66073')
    scrape_csv('Quintin Botelho 64588')
    scrape_csv('Ian McKinnon 65063')
    scrape_csv('Avery Bouchard 39819')
    scrape_csv('Ruben Martins 66073')
    scrape_csv('Brennan Rosa 69081')

    print("Boston Leads:\n")
    download_rep_route(boston)
    scrape_csv("Joseph O'Neill 47661")
    scrape_csv('Ralph Cistoldi 62492')
    scrape_csv('Ian Sauvageau 39668')
    scrape_csv('Michael Bottasso 48362')
    scrape_csv('Edward Hurlburt 49826')
    scrape_csv('Wilson Delaleu 66073')
    scrape_csv('Quintin Botelho 64588')
    scrape_csv('Ian McKinnon 65063')
    scrape_csv('Avery Bouchard 39819')
    scrape_csv('Ruben Martins 66073')
    scrape_csv('Brennan Rosa 69081')


def login_to_quickbase():
    driver.get('https://davidyost-7821.quickbase.com/db/main?a=signin')

    username_field = driver.find_element(By.NAME, "loginid")
    password_field = driver.find_element(By.NAME, "password")

    #  input username and password
    username_field.send_keys(username)
    password_field.send_keys(password + Keys.ENTER)

    time.sleep(2)


def login_to_sales_rabbit():
    driver.get('https://signin.salesrabbit.com/u/login?state=hKFo2SBZMVJuTVFzMnRzSlYxcW9MWl9JNmhjV0pYMnNkQUpwNKFur3VuaX'
               'ZlcnNhbC1sb2dpbqN0aWTZIG1PODVEdXp1bnlfVlNJQXJxVFVCXzZYbHJjY0d3VVp0o2NpZNkgME9PVDF2SWN4NTdmWkN3cjdQM1RXZ'
               'DkxMjFCQ1o2Ulc')

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)
    driver.find_element(By.NAME, "action").send_keys(Keys.ENTER)


def download_rep_route(office):
    #  navigate to leads page
    driver.get("https://davidyost-7821.quickbase.com/db/bjvssf62r?a=q&qid=214")

    #  Choose office from the dropdown menu
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[13]/table[2]/tbody/tr/td[3]/"
                                                                           "form/table/tbody/tr[2]/td/table/tbody/tr/"
                                                                           "td/table/tbody/tr[1]/td/table/tbody/tr/"
                                                                           "td[7]/table/tbody/tr/td[3]/"
                                                                           "select"))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, office))).click()

    if datetime.date.today().weekday() == 0:
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "how2_1"))).click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[13]/table[2]/tbody/tr/"
                                                                               "td[3]/form/table/tbody/tr[2]/td/table/"
                                                                               "tbody/tr/td/table/tbody/tr[2]/td/table/"
                                                                               "tbody/tr/td[6]/table/tbody/tr/td[3]/"
                                                                               "select/option[3]"))).click()
        driver.find_element(By.NAME, "relDateQuant_1").send_keys(Keys.BACKSPACE + "2")
    else:
        drop_down_date_menu = Select(driver.find_element(By.NAME, "how2_1"))
        drop_down_date_menu.select_by_visible_text("yesterday")

    submit_link = driver.find_element(By.NAME, "display")
    submit_link.click()
    time.sleep(2)
    driver.find_element(By.ID, "download").click()
    time.sleep(5)


def download_dispos():
    driver.get("https://app.salesrabbit.com/recruiting/leads.php")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#leadsTable_wrapper > div.sr-toolbar"
                                                                                  " > div > button"))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#headingDateStatusModified > h4 > "
                                                                                  "a"))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[3]/div/div[5]/div/div/"
                                                                           "div[2]/div/div[3]/div[2]/div/div/span/"
                                                                           "text()"))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.daterangepicker."
                                                                                  "dropdown-menu.opensright."
                                                                                  "show-calendar > div.ranges > ul > "
                                                                                  "li:nth-child(2)"))).click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "leadApplyFilters"))).click()


# converts the date from today into a string and adds an equation for yesterday's date
def format_date():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    month = str(yesterday).split('-')[1]
    day = str(yesterday).split('-')[2]
    year = str(yesterday).split('-')[0]
    formatted_date = f"{month}-{day}-{year}"

    return formatted_date


def scrape_csv(sales_rep):
    # opens newest file in the Downloads folder
    read_file = get_newest_file()
    read = open(read_file, 'r', encoding='ISO-8859-1')
    csv_read = csv.reader(read)
    # skip the first line of the csv file (header)
    next(csv_read)
    # today = datetime.date.today()
    # dictionary = {}

    # initialize a dictionary for the rep object
    rep = {"Doors Knocked": 0, "Contacts": 0, "Start Time": 0, "End Time": 0, "Sales": 0}

    # read through each line of the csv file
    for row in csv_read:
        dictionary = {"Rep": row[1], "Lead Status": row[2], "Visit Time": row[6].split()[1], "Visits": 0, "Contacts": 0,
                      "Start Time": 0, "End Time": 0, "Sales": 0}
        # the following block of code adjusts the visit hour to Eastern Standard Time
        rep_visit_time = dictionary.get("Visit Time").split()[0]
        adj_visit_hour = str(int(rep_visit_time[1]) + 1)
        est_rep_visit_time = str(rep_visit_time[0] + adj_visit_hour + rep_visit_time[2:])

        # check if line contains the rep we are looking for, and if it does...
        if dictionary.get("Rep") == sales_rep:

            # add a knocked door for every line which contains that rep
            rep["Doors Knocked"] += 1

            # gets the first door knocked time and makes that the start time (+1 for EST)
            if rep["Start Time"] == 0:
                rep["Start Time"] = est_rep_visit_time

            # check if lead status insinuates rep spoke to somebody at the door and considers that a contact
            if dictionary.get("Lead Status") == "NID" or dictionary.get("Lead Status") == "NIP" or \
                    dictionary.get("Lead Status") == "GB" or dictionary.get("Lead Status") == "APPT" or \
                    dictionary.get("Lead Status") == "Sold":
                rep["Contacts"] += 1

            # looks for a sold account
            if dictionary.get("Lead Status") == "Sold":
                rep["Sales"] += 1

            # takes the last time with the reps name on it and makes that the end time
            rep["End Time"] = est_rep_visit_time

    # prints the rep dictionary to the console as long as there were doors knocked
    if rep["Doors Knocked"] != 0:
        print(sales_rep + ': \nDoors Knocked: ' + str(rep["Doors Knocked"]) + "\nContacts: " +
                              str(rep["Contacts"]) + "\nStart Time: " + str(rep["Start Time"]) + "\nEnd Time: " +
                              str(rep["End Time"]) + "\nSales: " + str(rep["Sales"]) + "\n\n")


def get_newest_file():
    folder_path = r'C:/Users/avery/Downloads'
    os.chdir(folder_path)
    newest_file = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)[-1]
    return newest_file


main()
