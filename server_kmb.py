from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from bs4 import BeautifulSoup

waiting = 3

# pip install selenium flask bs4
app = Flask(__name__)

@app.route('/')
def index():
    return "use it with: /api/[route]/[ro]/[stop]/[leng (option)]"


@app.route('/api/<route>/<ro>/<stop>', defaults={'leng': "tc"}, methods=['GET'])
@app.route('/api/<route>/<ro>/<stop>/<leng>', methods=['GET'])
def eta(route, ro, stop, leng):
    try:
        rotate = False
        if ro == "1":
            rotate = True
        options = Options()
        options.add_argument("--disable-notifications")

        #chrome = webdriver.Chrome('chromedriver', options=options)
        #chrome = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)

        CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        chrome = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                  chrome_options=chrome_options
                                  )

        chrome.get(
            "http://search.kmb.hk/KMBWebSite/index.aspx?lang={}".format(leng))

        chrome.find_element_by_id("imgRouteSearchIcon").click()
        chrome.execute_script(
            "document.getElementById('txtRoute').value='{}'".format(route))
        chrome.execute_script(
            "document.getElementById('routeSearchButton').click()")

        time.sleep(0.2)
        if rotate:
            chrome.execute_script("exchangeRouteSearch()")

        time.sleep(waiting)
        soup = BeautifulSoup(chrome.page_source, 'html.parser')
        tdStop = soup.find(id= "tdStop{}".format(stop))
        # chrome.execute_script(tdStop.find_parent().find_all('td')[2]['onclick'])
        chrome.execute_script('getETA("{}", {}, 1, "", {})'.format(route, int(ro)+1, stop))

        time.sleep(waiting)
        soup = BeautifulSoup(chrome.page_source, 'html.parser')
        contentPane = soup.find("div", {"class": "contentPane"})
        etime = contentPane.findChildren("table")[0].findChildren("table")[
            0].find_all('tr')[1:]

        direction = "{} > {}".format(
            soup.find(id="busDetailsOrigin").text, soup.find(id="busDetailsDest").text)
        if stop != "0" and stop != "999":
            station = tdStop.find_parent().find_all(
                'td')[2].findChildren('span')[0].text
        else:
            station = tdStop.find_parent().find_all('td')[2].text

        eta = []
        for each in etime:
            eta.append(each.text)

        return jsonify({'Route': route, 'Direction': direction, 'station': station, 'eta': eta})
    finally:
        chrome.quit()
        pass


if __name__ == '__main__':
    app.run(host="192.168.0.246", debug=False)
    # app.run(debug=True)

# eta("86", "0", "3", "tc")
# eta("86", "1", "9", "tc")
