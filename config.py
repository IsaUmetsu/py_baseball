def getConfig(key):
    config = {
        "seasonStart": "2020/06/20",
        "scheduleUrl": "https://baseball.yahoo.co.jp/npb/schedule/?date=[date]",
        "gameScoreUrl": "https://baseball.yahoo.co.jp/npb/game/[dateGameNo]/score",
        "pathBase": "/Users/IsamuUmetsu/dev/py_baseball/output",
    }
    return config[key]
