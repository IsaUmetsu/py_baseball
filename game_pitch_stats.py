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
from config import getConfig, getTeamInitial, getTeamInitialByFullName
from driver import getChromeDriver, getFirefoxDriver
from util import Util

parser = argparse.ArgumentParser(prog="blowser", add_help=True)
parser.add_argument('-ss', '--season-start', type=str, default=datetime.datetime.now().strftime("%m%d"))
parser.add_argument('-se', '--season-end', type=str, default=datetime.datetime.now().strftime("%m%d"))
parser.add_argument('-s', '--specify', nargs='+', type=str)
parser.add_argument('-e', '--exclude', nargs='+', type=str)
args = parser.parse_args()

def commonWait():
    time.sleep(2)

def createPitchStatsDetail(rows):
    # 試合終了後
    if len(rows) == 14:
        return {
            "result": rows[0].text,
            "name": rows[1].text,
            "era": rows[2].text, # earned run average
            "ip": rows[3].text, # innings pitched
            "np": rows[4].text, # numbers of pitches
            "bf": rows[5].text, # batters faced 
            "ha": rows[6].text, # hits allowed
            "hra": rows[7].text, # homerun allowed
            "so": rows[8].text, # strike out
            "bb": rows[9].text, # bases on balls
            "hbp": rows[10].text, # hit by pitch
            "balk": rows[11].text,
            "ra": rows[12].text, # runs allowed
            "er": rows[13].text # earned runs
        }
    # 試合中
    else:
        return {
            "result": "",
            "name": rows[0].text,
            "era": rows[1].text, # earned run average
            "ip": rows[2].text, # innings pitched
            "np": rows[3].text, # numbers of pitches
            "bf": rows[4].text, # batters faced 
            "ha": rows[5].text, # hits allowed
            "hra": rows[6].text, # homerun allowed
            "so": rows[7].text, # strike out
            "bb": rows[8].text, # bases on balls
            "hbp": rows[9].text, # hit by pitch
            "balk": rows[10].text,
            "ra": rows[11].text, # runs allowed
            "er": rows[12].text # earned runs
        }

def createPitchStats(pitchStatusElem):
    pitchStats = []
    for pitchStat in pitchStatusElem:
        rows = pitchStat.find_elements_by_css_selector("tr td")
        pitchStats.append(createPitchStatsDetail(rows))
    return pitchStats

# driver生成
driver = getFirefoxDriver()
# シーズン開始日設定
targetDate = datetime.datetime.strptime("2020" + args.season_start, "%Y%m%d")
dateEnd = datetime.datetime.strptime("2020" + args.season_end, "%Y%m%d")

print("----- current time: {0} -----".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

try:
    while targetDate <= dateEnd:
        util = Util(driver)
        # 指定日の[日程・結果]画面へ遷移
        driver.get(getConfig("scheduleUrl").replace("[date]", targetDate.strftime("%Y-%m-%d")))
        commonWait()

        for gameCard in util.getElems("gameCards"):
            startTime = time.time()
            # 日付ディレクトリ作成
            pathDate = targetDate.strftime("%Y%m%d")
            fullPathDate = "/".join([getConfig("pathPitcherStats"), pathDate])
            if not os.path.exists(fullPathDate):
                os.mkdir(fullPathDate)

            # 試合番号生成
            gameNo = util.getGameNo(gameCard, pathDate)
            # 特定試合 指定時
            if args.specify:
                if gameNo not in args.specify:
                    continue
            # 特定試合 除外時
            if args.exclude:
                if gameNo in args.exclude:
                    continue
            # ゲーム番号生成
            gameNo = '0' + gameNo

            # 指定試合の[トップ]画面へ遷移
            driver.get(getConfig("gameTopUrl").replace("[dateGameNo]", targetDate.strftime("%Y%m%d") + gameNo))
            commonWait()

            gameState = driver.find_element_by_css_selector(getSelector("gameState")).text
            isFinished = gameState in ["試合終了", "試合中止", "ノーゲーム"]

            # 指定試合の[出場成績]画面へ遷移
            driver.get(getConfig("gameStatsUrl").replace("[dateGameNo]", targetDate.strftime("%Y%m%d") + gameNo))
            commonWait()

            contentMain = driver.find_element_by_css_selector("#gm_stats")
            util = Util(contentMain)

            awayTeam = getTeamInitialByFullName(util.getText("awayTeamFullName"))
            homeTeam = getTeamInitialByFullName(util.getText("homeTeamFullName"))
            awayPitchStats = createPitchStats(util.getElems("awayPitchStats"))
            homePitchStats = createPitchStats(util.getElems("homePitchStats"))

            awayInfo = { "team": awayTeam, "stats": awayPitchStats }
            homeInfo = { "team": homeTeam, "stats": homePitchStats }

            data = { "away": awayInfo, "home": homeInfo, "isFinished": isFinished }
            # save as json
            with open("{0}/{1}.json".format(fullPathDate, gameNo), 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print("----- [done] "\
                "date: {0}, "
                "gameNo: {1}, "\
                "{2} vs {3}, "\
                "{4:3.1f}[sec]"\
                " -----".format(
                    pathDate,
                    gameNo,
                    awayTeam,
                    homeTeam,
                    time.time() - startTime
                )
            )

        targetDate = targetDate + datetime.timedelta(days=1)

    driver.close()
    driver.quit()
    print("----- finished time: {0} -----\n\n".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

except:
    driver.close()
    driver.quit()

    import traceback
    traceback.print_exc()
