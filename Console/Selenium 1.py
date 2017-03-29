from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://inventwithpython.com')
head = browser.find_element_by_id('headerimage')
linkr = head.get_attribute('alt')
print(linkr)
#browser.close()
