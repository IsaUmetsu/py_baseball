
selectorList = {
    ### 日程結果
    "gameCards": "#gm_card .bb-score__content",
    "gameCardsAwayTeam": ".bb-score__team p:nth-child(1)",
    "gameCardsHomeTeam": ".bb-score__team p:nth-child(2)",

    ### 一球速報
    ## イニング
    "inningBase": "#ing_brd tbody tr:nth-child({0}) td:nth-child({1})",
    "topOf1": "#ing_brd tbody tr td:nth-child(2)",

    ## 速報詳細
    ## ライブヘッダ
    "inning": "#async-fieldBso .live em",
    "countBall": "#async-fieldBso .score .sbo .b b",
    "countStrike": "#async-fieldBso .score .sbo .s b",
    "countOut": "#async-fieldBso .score .sbo .o b",
    "teamInitialAway": "#async-fieldBso .score table tbody tr:nth-child(1) td:nth-child(1)",
    "currentScoreAway": "#async-fieldBso .score table tbody tr:nth-child(1) td:nth-child(2)",
    "teamInitialHome": "#async-fieldBso .score table tbody tr:nth-child(2) td:nth-child(1)",
    "currentScoreHome": "#async-fieldBso .score table tbody tr:nth-child(2) td:nth-child(2)",

    ## ライブボディ
    "battingResult": "#liveBody #result span",
    "pitchingResult": "#liveBody #result em",
    "onbaseInfo": "#dakyu div",
    "nextBatter": "#liveBody .bottom #nxt_batt .next table tbody tr:nth-child(2)",
    # 現在打者概要
    "currentBatterName": "#liveBody .bottom #batter .nm_box .nm a",
    "currentBatterPlayerNo": "#liveBody .bottom #batter .nm_box .nm span",
    "currentBatterDomainHand": "#liveBody .bottom #batter .dominantHand",
    "currentBatterRate": "#liveBody .bottom #batter .rate",
    "currentBatterPrevResult": "#liveBody .bottom #batter .anda",
    # 登板投手概要
    "currentPitcherName": "#liveBody .bottom #pit .nm_box .nm a",
    "currentPitcherPlayerNo": "#liveBody .bottom #pit .nm_box .nm span",
    "currentPitcherHand": "#liveBody .bottom #pit .dominantHand",
    "currentPitchCount": "#liveBody .bottom #pit .score td:nth-child(1)",
    "currentPitcherVSBatterCount": "#liveBody .bottom #pit .score td:nth-child(2)",
    "currentPitchERA": "#liveBody .bottom #pit .score td:nth-child(3)",
    "inningBatterCnt": "#replay dt",

    ## 投球詳細情報
    "pitchDetail": ".bb-splits__item:nth-child(2) table:nth-child(3) tbody tr",
    "pitchingCourse": ".bb-splits__item:nth-child(2) table:nth-child(1) tbody tr td div span.bb-icon__ballCircle",
    # 対戦相手
    "gameResultLeftTitle": "#gm_rslt thead tr th:nth-child(1)",
    "gameResultLeftName": "#gm_rslt tbody tr td:nth-child(1)",
    "gameResultLeftDomainHand": "#gm_rslt tbody tr td:nth-child(2)",
    "gameResultRightTitle": "#gm_rslt thead tr th:nth-child(2)",
    "gameResultRightName": "#gm_rslt tbody tr td:nth-child(3)",
    "gameResultRightDomainHand": "#gm_rslt tbody tr td:nth-child(4)",

    ## 各チーム情報
    "homeTeamElemId": "#gm_memh",
    "awayTeamElemId": "#gm_mema",
    # チーム情報
    "teamName": ".bb-head03__title",
    "teamOrder": "table:nth-child(2) tbody tr",
    "teamBattery": "table:nth-child(4) tbody:nth-child(1) tr:nth-child(2) td",
    "teamHomerun": "table:nth-child(4) tbody:nth-child(2) tr:nth-child(2) td",
    "benchPitcherInfo": "table:nth-child(5) tbody:nth-child(2) tr",
    "benchCatcherInfo": "table:nth-child(5) tbody:nth-child(3) tr",
    "benchInfielderInfo": "table:nth-child(5) tbody:nth-child(4) tr",
    "benchOutfielderInfo": "table:nth-child(5) tbody:nth-child(5) tr",
}

def getSelector(selector):    
    return selectorList[selector]
