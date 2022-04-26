# in your IDE terminal(without running python) the following items need to be pip installed (as shown) or package instal
# for all of the ones below, assuming you have python3 install by typing the following commands following the  dashes
# and ignore the comments after the dashes, they are only explaining what you are installing
# numpy --- pip install numpy --- a scientific number library needed for pandas to work in some ide's better to have it
# wheel --- pip install wheel --- a key package manager for python environments, especially conda
# pandas --- pip install pandas --- this is the tool that organizes raw data into manageable data sets
# selenium --- pip install selenium --- this is how we are automating our website and getting useful data
# openpyxl --- pip install openpyxl --- this is how we are exporting our dataframes to an xlsx doc
# the other imports shown below can simply be imported as shown since theyre standard python libraries
# even if they look greyed out and say theyre unused imports, just ignore it
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
from datetime import date

                                                   # establish some variables from the outset that we want
today = date.today()                               # todays date being captured in today variable
today = today.strftime("%m %d %Y")                 # today being reformatted without characters
PATH = "C:\Program Files (x86)\chromedriver.exe"   # the actual location of the chrome driver exec file
driver = webdriver.Chrome(PATH)                    #setting its location as a variable so can access

print('''This is a console application, no GUI(Graphic User Interface) is present. When asked for the PMA number, you \n
         have to enter it on your keyboard and hit Return/Enter to have the search begin. This script allows you to \n
         have the pma number you enter automatically search into the FDA's pma database. It will then automate itself\n
         to the original PMA associated with that number, and then scrape certain information from every single\n
         supplement attached to that pma and place it into an excel and csv sheet with the pma number and current date as\n
         the file name. If you enter the PMA incorrectly, nothing we can do at the moment. If further functionality is \n
         desired money and time is required to make this a proper web app or extension. If there are any errors, just \n
         close out the opened browser and the program will terminate. You know who to call
      ''')


userPma = input("Enter PMA Number: ")             # grabs terminal input so we can simulate typing it in later
time.sleep(2)                                     # sleep allows the browser time to load the page before proceeding
driver.get("https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma.cfm")
time.sleep(2)
pmaNumber = driver.find_element_by_id("pmanumber")         # establish variables by assigning html elements to them, in this case the pma search box assinged to the var
pmaNumber.send_keys(userPma)                               # have the input variable taken in the command line be sent keys aka copies that input into our search box
pmaNumber.send_keys(Keys.RETURN)                           # have the browser hit enter and begin the search
firstResult = driver.find_element_by_xpath('//*[@id="user_provided"]/table[2]/tbody/tr/td/table/tbody/tr[3]/td[1]/a')       # store the first result on the list
firstResult.click()                                        # click on the first result of the list
time.sleep(2)
originalPMA = driver.find_element_by_xpath('//*[@id="pma-details"]/table[1]/tbody/tr/td/a')
originalPMA.click()
time.sleep(2)
originalPMAselect = driver.find_element_by_xpath('//*[@id="user_provided"]/table[2]/tbody/tr/td/table/tbody/tr[3]/td[1]/a')
originalPMAselect.click()
time.sleep(2)
current = driver.current_url                            # get the url of the current web page and store it
driver.get(current)                                     # open the current variable
time.sleep(2)
supList = []                                            # create an empty list to store all the supplement links in
elems = driver.find_elements_by_xpath('//a[@href]')     # using a dynamic path to find all html link tags
for elem in elems:
    ref = elem.get_attribute('href')                    # iterating through every single link on the current page
    if "SupplementNumber" in ref:                       # checking to see if this tag is in the link string
        supList.append(ref)                             # adding all supplement link url's to supList
suplDict = {
            "Device ID": [], "Generic Name": [], "Applicant": [], "PMA Number": [], "Supplement Number": [],
            "Date Received": [], "Decision Date": [], "Product Code": [], "Advisory Committee": [],
             "Supplement Type/Clinical Trials": []
            }                                         # rest is standard selenium chrome automation and python
for supl in supList:
    driver.get(supl)
    time.sleep(.75)
    deviceLink = driver.find_element_by_xpath('//*[@id="user_provided"]/table[2]/tbody/tr/td/table/tbody/tr[3]/td[1]')
    deviceLink.click()
    time.sleep(.5)
    deviceID = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[2]/td').text
    genericName = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[3]/td').text
    applicant = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[4]/td').text
    pmaNumberFinal = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[5]/td').text
    supplementNumber = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[6]/td').text
    dateReceived = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[7]/td').text
    decisionDate = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[8]/td').text
    productCode = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[9]/td').text
    advisoryCommittee = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[10]/td').text
    supplementType = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[11]/td').text
    suplDict["Device ID"].append(deviceID)
    suplDict["Generic Name"].append(genericName)
    suplDict["Applicant"].append(applicant)
    suplDict["PMA Number"].append(pmaNumberFinal)
    suplDict["Supplement Number"].append(supplementNumber)
    suplDict["Date Received"].append(dateReceived)
    suplDict["Decision Date"].append(decisionDate)
    suplDict["Product Code"].append(productCode)
    suplDict["Advisory Committee"].append(advisoryCommittee)
    suplDict["Supplement Type/Clinical Trials"].append(supplementType)
supplementInformation = pd.DataFrame(suplDict)  #-----# assign completed dict to a variable and then export to desired path
supplementInformation.to_excel(r'C:\Users\jacob\Desktop\'' + pmaNumberFinal + ' ' + today + '.xlsx', index=False, header=True)
supplementInformation.to_csv(r'C:\Users\jacob\Desktop\'' + pmaNumberFinal + ' ' + today + '.csv', index=False, header=True)
time.sleep(2)
driver.quit() # quits the entire browser, dont wanna keep it open





# Notes, Documentation, Etc. Below because if im not getting paid im not making a markdown for this lmao
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# Code to not delete, look at later because different loops and calls might work in various scenarios
# -----------------------------------------------------------------------------------------------------------------------
# loop 1 ---------------------------------------------------------------------------------------------------------------
# supplementList = driver.find_elements_by_tag_name('A')
# supList = []
# for supplement in supplementList:
#    sup = supplement.get_attribute('href')
#    for supl in sup:
#        if supl.__contains__("SupplementNumber"):
#            supList.append(supl)
# loop 2 ---------------------------------------------------------------------------------------------------------------
# print(supplement.get_attribute("href"))
# supList.append(supplement.get_attribute("href"))
# print(len(supList))
# print(supList# )
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# Below are the supplement dictionary variables that we removed because the last few variables as ommitted
# vary too much from page to page, the dynamic paths on the fda site is hot garbage without a well defined css selector
# so well cut them out for now until we figure out what the crackhead who built their website was thinking
# ----------------------------------------------------------------------------------------------------------------------
# suplDict["Supplement Reason"].append(supplementReason)
    # suplDict["Expedited Review Granted?"].append(expeditedReview)
    # suplDict["Combination Product"].append(combinationProduct)
    # suplDict["Approval Order Statement"].append(approvalOrderStatement)
    # driver.close()  -----dont need this, the get function at the iterable level automaticall forces the new item
    # without needing to close out the focused page, useful for later-----
# supplementReason = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[12]/td').text
    # expeditedReview = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[13]/td').text
    # combinationProduct = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[14]/td').text
    # approvalOrderStatement = driver.find_element_by_xpath('//*[@id="pma-details"]/tbody/tr[15]/td').text
#, "Supplement Reason": [], "Expedited Review Granted?": [],
            # "Combination Product": [], "Approval Order Statement": []









