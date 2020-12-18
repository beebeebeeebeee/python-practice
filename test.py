from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

def eta(route, ro, stop, leng):
    try:
        rotate = False
        if ro == "1":
            rotate = True
        options = Options()
        options.add_argument("--disable-notifications")

        chrome = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities={'browserName': 'chrome'})
        #chrome = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
        chrome.get("http://search.kmb.hk/KMBWebSite/index.aspx?lang={}".format(leng))

        chrome.find_element_by_id("imgRouteSearchIcon").click()
        chrome.execute_script("document.getElementById('txtRoute').value='{}'".format(route))
        chrome.execute_script("document.getElementById('routeSearchButton').click()")

        time.sleep(0.2)
        if rotate:
            chrome.execute_script("exchangeRouteSearch()")
            
        time.sleep(5)
        soup = BeautifulSoup(chrome.page_source, 'html.parser')
        tdStop = soup.find(id= "tdStop{}".format(stop))
        chrome.execute_script(tdStop.find_parent().find_all('td')[2]['onclick'])
        
        time.sleep(5)
        newSoup = BeautifulSoup(chrome.page_source, 'html.parser')
        contentPane = newSoup.find("div", {"class": "contentPane"})
        etime = contentPane.findChildren("table")[0].findChildren("table")[0].find_all('tr')[1:]

        direction = "{} > {}".format(newSoup.find(id = "busDetailsOrigin").text, newSoup.find(id = "busDetailsDest").text)
        station = tdStop.find_parent().find_all('td')[2].findChildren('span')[0].text

        eta = []
        for each in etime:
            eta.append(each.text)

        print({'Route': route, 'Direction': direction, 'station': station, 'eta': eta})
    finally:
        chrome.quit()



eta(86, 0, 3, "tc")
#eta(86, True, 9)
