from selenium import webdriver
from selenium.webdriver.common.keys import Keys


result_text = "'ФУТБОЛКИ'"
browser = webdriver.Chrome("/Users/nikitasakun/Desktop/Проекты Pycharm/Lab6NikitaSakun/chromedriver")
browser.implicitly_wait(10)
browser.get("https://www.farfetch.com/ua/shopping/women/items.aspx")

browser.find_element_by_css_selector('[type="search"]').send_keys("Футболки")
browser.find_element_by_css_selector('[type="search"]').send_keys(Keys.RETURN)
   
actual_result = browser.find_element_by_css_selector('[class="css-jcxr20-Display e5enhw40"]').text

assert result_text == actual_result
