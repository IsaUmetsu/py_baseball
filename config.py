def getConfig(key):
    config = {
        "scheduleUrl": "https://baseball.yahoo.co.jp/npb/schedule/?date=[date]",
        "gameScoreUrl": "https://baseball.yahoo.co.jp/npb/game/[dateGameNo]/score",
        "gameTopUrl": "https://baseball.yahoo.co.jp/npb/game/[dateGameNo]/top",
        "gameStatsUrl": "https://baseball.yahoo.co.jp/npb/game/[dateGameNo]/stats",
        "gameTextUrl": "https://baseball.yahoo.co.jp/npb/game/[dateGameNo]/text",
        "gameIndexUrl": "https://baseball.yahoo.co.jp/npb/game/[dateGameNo]/index",
        "pathBase": "/Users/IsamuUmetsu/dev/py_baseball/output",
        "pathBaseCards": "/Users/IsamuUmetsu/dev/py_baseball/cards",
        "pathBaseStarter": "/Users/IsamuUmetsu/dev/py_baseball/starter",
        "pathPitcherStats": "/Users/IsamuUmetsu/dev/py_baseball/pitcherStats",
        "pathBatterStats": "/Users/IsamuUmetsu/dev/py_baseball/batterStats",
        "pathTextStats": "/Users/IsamuUmetsu/dev/py_baseball/text",
    }
    return config[key]

def getTeamInitial(team):
    teamInitial = {
        "DeNA": "De",
        "阪神": "T",
        "巨人": "G",
        "中日": "D",
        "広島": "C",
        "ヤクルト": "S",
        "楽天": "E",
        "ソフトバンク": "H",
        "西武": "L",
        "オリックス": "B",
        "ロッテ": "M",
        "日本ハム": "F"
    }
    return teamInitial[team]

def getTeamInitialByFullName(team):
    teamInitial = {
        "横浜DeNAベイスターズ": "De",
        "阪神タイガース": "T",
        "読売ジャイアンツ": "G",
        "中日ドラゴンズ": "D",
        "広島東洋カープ": "C",
        "東京ヤクルトスワローズ": "S",
        "東北楽天ゴールデンイーグルス": "E",
        "福岡ソフトバンクホークス": "H",
        "埼玉西武ライオンズ": "L",
        "オリックス・バファローズ": "B",
        "千葉ロッテマリーンズ": "M",
        "北海道日本ハムファイターズ": "F"
    }
    return teamInitial[team]

def getHawksGameInfo():
    return {
        "20200709": 6,
        "20200718": 6,
        "20200719": 6,
        "20200721": 6,
        "20200722": 6,
        "20200723": 6,
        "20200724": 6,
        "20200725": 6,
        "20200726": 6,
        "20200727": -1,
        "20200728": 6,
        "20200729": 6,
        "20200730": 6,
        "20200731": 6,
        "20200801": 6,
        "20200802": 5,
        "20200804": 5,
        "20200805": 5,
        "20200806": 5,
        "20200807": 5,
        "20200808": 5,
        "20200809": 5,
        "20200810": -1,
        "20200811": 5,
        "20200812": 6,
        "20200813": 4,
        "20200814": 6,
        "20200815": 6,
        "20200816": 6,
        "20200818": 5,
        "20200819": 5,
        "20200820": 5,
        "20200821": 5,
        "20200822": 5,
        "20200823": 5,
        "20200824": -1,
        "20200825": 6,
        "20200826": -1,
        "20200827": -1,
        "20200828": -1,
        "20200829": -1,
        "20200830": -1,
        "20200831": -1,
        "20200901": -1,
    }

def getOpen2021(date):
    open2021 = {
        "0302": ["11", "12"],
        "0303": ["13", "14", "15", "16"],
        "0304": ["17", "18"],
        "0305": ["19", "20"],
        "0306": ["21", "22", "23", "24", "25", "26"],
        "0307": ["27", "28", "29", "30", "31", "32"],
        "0309": ["33", "34", "35", "36", "37", "38"],
        "0310": ["39", "40", "41", "42", "43", "44"],
        "0311": ["45"],
        "0312": ["46", "47", "48", "49", "50", "51"],
        "0313": ["52", "53", "54", "55", "56", "57"],
        "0314": ["58", "59", "60", "61", "62", "63"],
        "0316": ["64", "65", "66", "67", "68", "69"],
        "0317": ["70", "71", "72", "73", "74", "75"],
        "0318": ["76"],
        "0319": ["77", "78", "79", "80", "81", "82"],
        "0320": ["83", "84", "85", "86", "87", "88"],
        "0321": ["89", "90", "91", "92", "93", "94"],
    }
    return open2021[date]

def getLeague2021(date):
    league2021 = {
        "0326": ["095", "096", "097", "098", "099", "100"],
        "0327": ["101", "102", "103", "104", "105", "106"],
    }
    return league2021[date]