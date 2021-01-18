# from selenium import webdriver


# myEmail = 'suhashareesh09'
# myPassword = 'Suhas@0905'

# driver = webdriver.Chrome()

# def login(url,usernameId, username, passwordId, password, submit_buttonId):
#    driver.get(url)
#    driver.find_element_by_id(usernameId).send_keys(username)
#    driver.find_element_by_id(passwordId).send_keys(password)
#    driver.find_element_by_id(submit_buttonId).click()

# login("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin", "email", myEmail, "pass", myPassword, "loginbutton")

# import requests

# r = requests.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# print (r.text)

import webbrowser

webbrowser.open("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# webbrowser.register('chrome', webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'),1)
# c=webbrowser.get('chrome')
# c.open("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
