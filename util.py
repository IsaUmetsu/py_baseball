import re
import datetime
import argparse
from selenium.common.exceptions import NoSuchElementException

from selector import getSelector
from config import getConfig

class Util:
    def __init__(self, driver):
        self.driver = driver

    def getText(self, selector):
        try:
            return self.driver.find_element_by_css_selector(getSelector(selector)).text
        except NoSuchElementException:
            return ""
    
    def getElems(self, selector):
        try:
            return self.driver.find_elements_by_css_selector(getSelector(selector))
        except NoSuchElementException:
            return []

    def getSpecifyText(self, elem, selector):
        try:
            return elem.find_element_by_css_selector(selector).text
        except NoSuchElementException:
            return ""

    def getSpecifyClass(self, elem, selector):
        try:
            return elem.find_element_by_css_selector(selector).get_attribute("class")
        except NoSuchElementException:
            return ""

    def getSpecifyElems(self, elem, selector):
        try:
            return elem.find_elements_by_css_selector(selector)
        except NoSuchElementException:
            return []

    def getTeamText(self, homeAway, selector):
        try:
            fullSelector = getSelector(homeAway) + " " + getSelector(selector)
            return self.driver.find_element_by_css_selector(fullSelector).text
        except NoSuchElementException:
            return ""

    def getTeamElems(self, homeAway, selector):
        try:
            fullSelector = getSelector(homeAway) + " " + getSelector(selector)
            return self.driver.find_elements_by_css_selector(fullSelector)
        except NoSuchElementException:
            return []

    def getGameNo(self, gameCard, pathDate):
        indexUrlRegex = getConfig('gameIndexUrl').replace('[dateGameNo]', pathDate + '0(\d)')
        searchResult = re.findall(indexUrlRegex, gameCard.get_attribute('href'))
        return searchResult[0] if len(searchResult) > 0 else ''

    def parseArgs(self):
        parser = argparse.ArgumentParser(prog="blowser", add_help=True)
        parser.add_argument('-ss', '--season-start', type=str, default=datetime.datetime.now().strftime("%m%d"))
        parser.add_argument('-se', '--season-end', type=str, default=datetime.datetime.now().strftime("%m%d"))
        parser.add_argument('-s', '--specify', nargs='+', type=str)
        parser.add_argument('-e', '--exclude', nargs='+', type=str)
        parser.add_argument('-gk', '--game-kind', nargs='+', type=str, default='1,2')
        return parser.parse_args()

    def getDateInfo(self, args):
        thisyear = datetime.date.today().strftime("%Y")
        targetDate = datetime.datetime.strptime(thisyear + args.season_start, "%Y%m%d")
        dateEnd = datetime.datetime.strptime(thisyear + args.season_end, "%Y%m%d")
        return targetDate, dateEnd
    
    def getGameKindIds(self, argsGameKind): # argsGameKind が配列型になるのでif文の条件式も配列で比較
        if argsGameKind == ['open']: # オープン戦
            return '5'
        elif argsGameKind == ['interleague']: # 交流戦
            return '26'
        elif argsGameKind == ['allstar']: # オールスター
            return '4'
        elif argsGameKind == ['cs']: # CS
            return '35,36,37,38'
        elif argsGameKind == ['js']: # 日本シリーズ
            return '3'
        else:
            return argsGameKind
        # elif argsGameKind == 'all': # 全て
        #     return '1,2,26,4,35,36,37,38,3,5,57,159,160'
