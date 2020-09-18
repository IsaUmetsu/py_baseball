import time
import re
import json
from collections import OrderedDict
import pprint
import datetime
import os
import argparse

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from selector import getSelector
from config import getConfig, getTeamInitial
from driver import getChromeDriver, getFirefoxDriver
from util import Util

parser = argparse.ArgumentParser(prog="blowser", add_help=True)
parser.add_argument('-ss', '--season-start', type=str, default=datetime.datetime.now().strftime("%m%d"))
parser.add_argument('-se', '--season-end', type=str, default=(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%m%d"))
parser.add_argument('-s', '--specify', nargs='+', type=int)
parser.add_argument('-e', '--exclude', nargs='+', type=int)
args = parser.parse_args()

def commonWait():
    time.sleep(2)

# driver生成
driver = getFirefoxDriver()
# シーズン開始日設定
targetDate = datetime.datetime.strptime("2020" + args.season_start, "%Y%m%d")
dateEnd = datetime.datetime.strptime("2020" + args.season_end, "%Y%m%d")

print("----- current time: {0} -----".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

while targetDate <= dateEnd:
    util = Util(driver)
    # 指定日の[日程・結果]画面へ遷移
    driver.get(getConfig("scheduleUrl").replace("[date]", targetDate.strftime("%Y-%m-%d")))
    commonWait()

    gameElems = util.getElems("gameCards")

    for gameCnt in range(len(gameElems)):
        gameElem = gameElems[gameCnt]

        # 日付ディレクトリ作成
        pathDate = targetDate.strftime("%Y%m%d")
        fullPathDate = "/".join([getConfig("pathBaseStarter"), pathDate])
        if not os.path.exists(fullPathDate):
            os.mkdir(fullPathDate)

        # 特定試合 指定時
        if args.specify:
            if (gameCnt + 1) not in args.specify:
                continue

        # 特定試合 除外時
        if args.exclude:
            if (gameCnt + 1) in args.exclude:
                continue

        # ゲーム番号生成
        gameNo = "0" + str(gameCnt + 1)

        # 指定試合の[トップ]画面へ遷移
        driver.get(getConfig("gameTopUrl").replace("[dateGameNo]", targetDate.strftime("%Y%m%d") + gameNo))
        commonWait()

        away = "away"
        home = "home"

        try:
            util = Util(driver.find_element_by_css_selector("#gm_recen"))
            away = getTeamInitial(util.getText("awayTeam"))
            home = getTeamInitial(util.getText("homeTeam"))
        except NoSuchElementException as e:
            util = Util(driver.find_element_by_css_selector("#ing_brd"))
            away = getTeamInitial(util.getText("awayTeamPast"))
            home = getTeamInitial(util.getText("homeTeamPast"))

        try:
            util = Util(driver.find_element_by_css_selector("#strt_pit"))
            awayStartPitcher = util.getText("awayStartPitcher")
            homeStartPitcher = util.getText("homeStartPitcher")

            awayInfo = { "team": away, "pitcher": awayStartPitcher }
            homeInfo = { "team": home, "pitcher": homeStartPitcher }

            data = { "away": awayInfo, "home": homeInfo }
            # save as json
            with open("{0}/{1}.json".format(fullPathDate, gameNo), 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print("----- [done] date: {0}, gameNo: {1}, {2} vs {3} -----".format(pathDate, gameNo, away, home))
        except NoSuchElementException as e:
            print("----- [Started or Not announced yet] date: {0}, gameNo: {1}, {2} vs {3}  -----".format(pathDate, gameNo, away, home))

    targetDate = targetDate + datetime.timedelta(days=1)

driver.close()
driver.quit()
print("----- finished time: {0} -----\n\n".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
