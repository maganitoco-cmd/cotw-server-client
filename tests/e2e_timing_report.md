# E2E Timing Report — Quest Economy

**Date**: 2026-07-05 16:39:19

**Total calls**: 158  

**Total time**: 38543ms (38.5s)  

**Average**: 244ms/call  


## Slowest Calls (Top 10)

| # | Phase | Endpoint | ms |
|---|---|---|---|
| 1 | 1-Reset | USER?action=reset | 1586 |
| 2 | 7-Map | WORLDMAP?action=gather&x=685&y=639&Troops=Infantry.1.1 | 753 |
| 3 | 7-Map | WORLDMAP?action=monster&x=692&y=646&Troops=Infantry.1.1 | 747 |
| 4 | 7-Map | WORLDMAP?action=gather&x=700&y=654&Troops=Infantry.1.1 | 731 |
| 5 | 2-Build | BUILDINGS?action=construct&idBuilding=2003&Node=5 | 632 |
| 6 | 4-TrainBuild | BUILDINGS?action=construct&idBuilding=2012&Node=12 | 594 |
| 7 | 4-Train | BUILDINGS?action=train&idBuilding=2014&Level=1&Quantity=5 | 581 |
| 8 | 4-TrainBuild | BUILDINGS?action=construct&idBuilding=2014&Node=10 | 580 |
| 9 | 3-Townhall | BUILDINGS?action=levelUpB&Node=3 | 570 |
| 10 | 4-Train | BUILDINGS?action=train&idBuilding=2012&Level=1&Quantity=3 | 545 |

## Summary by Phase

| Phase | Calls | Total ms | Avg ms |
|---|---|---|---|
| 1-Reset | 1 | 1586 | 1586 |
| 1-Login | 1 | 201 | 201 |
| 1-Init | 6 | 1175 | 195 |
| 2-Collect | 4 | 835 | 208 |
| 2-Refresh | 1 | 207 | 207 |
| 2-Build | 18 | 4662 | 259 |
| 2-Refresh2 | 1 | 251 | 251 |
| 2-Collect2 | 5 | 1220 | 244 |
| 2-PostBuild | 5 | 1036 | 207 |
| 3-Refresh | 2 | 402 | 201 |
| 3-TH | 15 | 2990 | 199 |
| 3-Townhall | 4 | 1412 | 353 |
| 3-PostTH | 5 | 1038 | 207 |
| 4-Refresh | 1 | 203 | 203 |
| 4-TrainBuild | 18 | 4832 | 268 |
| 4-PreTrain | 5 | 1016 | 203 |
| 4-Train | 16 | 4121 | 257 |
| 4-PostTrain | 5 | 950 | 190 |
| 5-Refresh | 1 | 218 | 218 |
| 5-PreResearch | 5 | 981 | 196 |
| 5-Research | 5 | 1044 | 208 |
| 5-PostResearch | 5 | 1022 | 204 |
| 6-PreHero | 5 | 958 | 191 |
| 6-Hero | 5 | 839 | 167 |
| 6-PostHero | 5 | 1000 | 200 |
| 7-Map | 8 | 3160 | 395 |
| 7-PostMap | 5 | 983 | 196 |
| 8-Final | 1 | 201 | 201 |

## Per-Call Timing

| # | Phase | Action | Endpoint | HTTP | ms | Result |
|---|---|---|---|---|---|---|
| 1 | 1-Reset | reset | USER?action=reset | 200 | 1586 | 1 |
| 2 | 1-Login | refresh | USER?action=loginJustUser | 200 | 201 | 1 |
| 3 | 1-Init | dailyReward | USER?action=dailyReward | 200 | 161 | -1 |
| 4 | 1-Init | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 251 | -1 |
| 5 | 1-Init | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 209 | -1 |
| 6 | 1-Init | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 7 | 1-Init | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 8 | 1-Init | login_resource_check | USER?action=loginJustUser | 200 | 202 | 1 |
| 9 | 2-Collect | collect | BUILDINGS?action=collect&Node=3 | 200 | 223 | 1 |
| 10 | 2-Collect | collect | BUILDINGS?action=collect&Node=1 | 200 | 207 | 1 |
| 11 | 2-Collect | collect | BUILDINGS?action=collect&Node=2 | 200 | 202 | 1 |
| 12 | 2-Collect | collect | BUILDINGS?action=collect&Node=8 | 200 | 203 | 1 |
| 13 | 2-Refresh | refresh | USER?action=loginJustUser | 200 | 207 | 1 |
| 14 | 2-Build | construct_Academy | BUILDINGS?action=construct&idBuilding=2002&Node=4 | 200 | 246 | 0 |
| 15 | 2-Build | construct_Academy | BUILDINGS?action=construct&idBuilding=2002&Node=14 | 200 | 245 | 0 |
| 16 | 2-Build | construct_Hospital | BUILDINGS?action=construct&idBuilding=2003&Node=5 | 200 | 632 | 1 |
| 17 | 2-Build | remainingTime_Hospital | CONSTRUCT?action=remainingTime&idConstruct=6a4a888e6097dc21ed21a73a | 200 | 309 | 1 |
| 18 | 2-Build | speedUpGold_Hospital | CONSTRUCT?action=speedUpGold&idConstruct=6a4a888e6097dc21ed21a73a | 200 | 245 | 0 |
| 19 | 2-Build | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | -1 |
| 20 | 2-Build | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 198 | -1 |
| 21 | 2-Build | dailyReward | USER?action=dailyReward | 200 | 147 | -1 |
| 22 | 2-Build | login_items_check | USER?action=loginJustUser | 200 | 239 | 1 |
| 23 | 2-Build | login_resource_check | USER?action=loginJustUser | 200 | 215 | 1 |
| 24 | 2-Build | construct_Forge | BUILDINGS?action=construct&idBuilding=2007&Node=6 | 200 | 246 | 0 |
| 25 | 2-Build | construct_Forge | BUILDINGS?action=construct&idBuilding=2007&Node=16 | 200 | 258 | 0 |
| 26 | 2-Build | construct_Embassy | BUILDINGS?action=construct&idBuilding=2006&Node=9 | 200 | 246 | 0 |
| 27 | 2-Build | construct_Embassy | BUILDINGS?action=construct&idBuilding=2006&Node=19 | 200 | 245 | 0 |
| 28 | 2-Build | construct_Pit | BUILDINGS?action=construct&idBuilding=2008&Node=7 | 200 | 244 | 0 |
| 29 | 2-Build | construct_Pit | BUILDINGS?action=construct&idBuilding=2008&Node=17 | 200 | 247 | 0 |
| 30 | 2-Build | construct_Wishing Well | BUILDINGS?action=construct&idBuilding=2009&Node=18 | 200 | 247 | 0 |
| 31 | 2-Build | construct_Wishing Well | BUILDINGS?action=construct&idBuilding=2009&Node=20 | 200 | 253 | 0 |
| 32 | 2-Refresh2 | refresh | USER?action=loginJustUser | 200 | 251 | 1 |
| 33 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=3 | 200 | 204 | 1 |
| 34 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=1 | 200 | 209 | 1 |
| 35 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=2 | 200 | 255 | 1 |
| 36 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=8 | 200 | 284 | 1 |
| 37 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=5 | 200 | 268 | 1 |
| 38 | 2-PostBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 209 | -1 |
| 39 | 2-PostBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 221 | -1 |
| 40 | 2-PostBuild | dailyReward | USER?action=dailyReward | 200 | 173 | -1 |
| 41 | 2-PostBuild | login_items_check | USER?action=loginJustUser | 200 | 229 | 1 |
| 42 | 2-PostBuild | login_resource_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 43 | 3-Refresh | refresh | USER?action=loginJustUser | 200 | 202 | 1 |
| 44 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 204 | -1 |
| 45 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 199 | -1 |
| 46 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 147 | -1 |
| 47 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 200 | 1 |
| 48 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 208 | 1 |
| 49 | 3-Townhall | levelUp_1 | BUILDINGS?action=levelUpB&Node=3 | 200 | 570 | 1 |
| 50 | 3-Townhall | remainingTime_TH Lvl 1 | CONSTRUCT?action=remainingTime&idConstruct=6a4a88976097dc21ed21a794 | 200 | 340 | 1 |
| 51 | 3-Townhall | speedUpGold_TH Lvl 1 | CONSTRUCT?action=speedUpGold&idConstruct=6a4a88976097dc21ed21a794 | 200 | 244 | 0 |
| 52 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 199 | -1 |
| 53 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 251 | -1 |
| 54 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 183 | -1 |
| 55 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 220 | 1 |
| 56 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 199 | 1 |
| 57 | 3-Refresh | refresh | USER?action=loginJustUser | 200 | 200 | 1 |
| 58 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 204 | -1 |
| 59 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 198 | -1 |
| 60 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 149 | -1 |
| 61 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 200 | 1 |
| 62 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 229 | 1 |
| 63 | 3-Townhall | levelUp_2 | BUILDINGS?action=levelUpB&Node=3 | 200 | 258 | 0 |
| 64 | 3-PostTH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 198 | -1 |
| 65 | 3-PostTH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 198 | -1 |
| 66 | 3-PostTH | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 67 | 3-PostTH | login_items_check | USER?action=loginJustUser | 200 | 220 | 1 |
| 68 | 3-PostTH | login_resource_check | USER?action=loginJustUser | 200 | 274 | 1 |
| 69 | 4-Refresh | refresh | USER?action=loginJustUser | 200 | 203 | 1 |
| 70 | 4-TrainBuild | construct_Barracks(Infantry) | BUILDINGS?action=construct&idBuilding=2014&Node=10 | 200 | 580 | 1 |
| 71 | 4-TrainBuild | remainingTime_Barracks (Infantry) | CONSTRUCT?action=remainingTime&idConstruct=6a4a889e6097dc21ed21a7cb | 200 | 294 | 1 |
| 72 | 4-TrainBuild | speedUpGold_Barracks (Infantry) | CONSTRUCT?action=speedUpGold&idConstruct=6a4a889e6097dc21ed21a7cb | 200 | 257 | 0 |
| 73 | 4-TrainBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 231 | -1 |
| 74 | 4-TrainBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 204 | -1 |
| 75 | 4-TrainBuild | dailyReward | USER?action=dailyReward | 200 | 147 | -1 |
| 76 | 4-TrainBuild | login_items_check | USER?action=loginJustUser | 200 | 208 | 1 |
| 77 | 4-TrainBuild | login_resource_check | USER?action=loginJustUser | 200 | 201 | 1 |
| 78 | 4-TrainBuild | construct_ArcherRange | BUILDINGS?action=construct&idBuilding=2012&Node=12 | 200 | 594 | 1 |
| 79 | 4-TrainBuild | remainingTime_Archer Range | CONSTRUCT?action=remainingTime&idConstruct=6a4a88a16097dc21ed21a7e3 | 200 | 338 | 1 |
| 80 | 4-TrainBuild | speedUpGold_Archer Range | CONSTRUCT?action=speedUpGold&idConstruct=6a4a88a16097dc21ed21a7e3 | 200 | 246 | 0 |
| 81 | 4-TrainBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 199 | -1 |
| 82 | 4-TrainBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 211 | -1 |
| 83 | 4-TrainBuild | dailyReward | USER?action=dailyReward | 200 | 150 | -1 |
| 84 | 4-TrainBuild | login_items_check | USER?action=loginJustUser | 200 | 201 | 1 |
| 85 | 4-TrainBuild | login_resource_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 86 | 4-TrainBuild | construct_Stable(Cavalry) | BUILDINGS?action=construct&idBuilding=2013&Node=11 | 200 | 316 | 0 |
| 87 | 4-TrainBuild | construct_SiegeWorkshop | BUILDINGS?action=construct&idBuilding=2015&Node=13 | 200 | 250 | 0 |
| 88 | 4-PreTrain | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 198 | -1 |
| 89 | 4-PreTrain | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 201 | -1 |
| 90 | 4-PreTrain | dailyReward | USER?action=dailyReward | 200 | 181 | -1 |
| 91 | 4-PreTrain | login_items_check | USER?action=loginJustUser | 200 | 235 | 1 |
| 92 | 4-PreTrain | login_resource_check | USER?action=loginJustUser | 200 | 201 | 1 |
| 93 | 4-Train | train_Infantry | BUILDINGS?action=train&idBuilding=2014&Level=1&Quantity=5 | 200 | 581 | 1 |
| 94 | 4-Train | remainingTime_Infantry | CONSTRUCT?action=remainingTime&idConstruct=6a4a88a66097dc21ed21a80c | 200 | 244 | 0 |
| 95 | 4-Train | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 248 | -1 |
| 96 | 4-Train | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 243 | -1 |
| 97 | 4-Train | dailyReward | USER?action=dailyReward | 200 | 155 | -1 |
| 98 | 4-Train | login_items_check | USER?action=loginJustUser | 200 | 200 | 1 |
| 99 | 4-Train | login_resource_check | USER?action=loginJustUser | 200 | 212 | 1 |
| 100 | 4-Train | train_Archer | BUILDINGS?action=train&idBuilding=2012&Level=1&Quantity=3 | 200 | 545 | 1 |
| 101 | 4-Train | remainingTime_Archer | CONSTRUCT?action=remainingTime&idConstruct=6a4a88a96097dc21ed21a821 | 200 | 258 | 0 |
| 102 | 4-Train | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 269 | -1 |
| 103 | 4-Train | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 218 | -1 |
| 104 | 4-Train | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 105 | 4-Train | login_items_check | USER?action=loginJustUser | 200 | 200 | 1 |
| 106 | 4-Train | login_resource_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 107 | 4-Train | train_Cavalry | BUILDINGS?action=train&idBuilding=2013&Level=1&Quantity=2 | 200 | 198 | 0 |
| 108 | 4-Train | train_Siege | BUILDINGS?action=train&idBuilding=2015&Level=1&Quantity=1 | 200 | 198 | 0 |
| 109 | 4-PostTrain | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 197 | -1 |
| 110 | 4-PostTrain | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 198 | -1 |
| 111 | 4-PostTrain | dailyReward | USER?action=dailyReward | 200 | 146 | -1 |
| 112 | 4-PostTrain | login_items_check | USER?action=loginJustUser | 200 | 207 | 1 |
| 113 | 4-PostTrain | login_resource_check | USER?action=loginJustUser | 200 | 202 | 1 |
| 114 | 5-Refresh | refresh | USER?action=loginJustUser | 200 | 218 | 1 |
| 115 | 5-PreResearch | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 220 | -1 |
| 116 | 5-PreResearch | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 216 | -1 |
| 117 | 5-PreResearch | dailyReward | USER?action=dailyReward | 200 | 147 | -1 |
| 118 | 5-PreResearch | login_items_check | USER?action=loginJustUser | 200 | 199 | 1 |
| 119 | 5-PreResearch | login_resource_check | USER?action=loginJustUser | 200 | 199 | 1 |
| 120 | 5-Research | research_1 | BUILDINGS?action=research&idResearch=1 | 200 | 197 | 0 |
| 121 | 5-Research | research_2 | BUILDINGS?action=research&idResearch=2 | 200 | 196 | 0 |
| 122 | 5-Research | research_3 | BUILDINGS?action=research&idResearch=3 | 200 | 198 | 0 |
| 123 | 5-Research | research_4 | BUILDINGS?action=research&idResearch=4 | 200 | 202 | 0 |
| 124 | 5-Research | research_5 | BUILDINGS?action=research&idResearch=5 | 200 | 251 | 0 |
| 125 | 5-PostResearch | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 230 | -1 |
| 126 | 5-PostResearch | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 199 | -1 |
| 127 | 5-PostResearch | dailyReward | USER?action=dailyReward | 200 | 147 | -1 |
| 128 | 5-PostResearch | login_items_check | USER?action=loginJustUser | 200 | 233 | 1 |
| 129 | 5-PostResearch | login_resource_check | USER?action=loginJustUser | 200 | 213 | 1 |
| 130 | 6-PreHero | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 212 | -1 |
| 131 | 6-PreHero | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 198 | -1 |
| 132 | 6-PreHero | dailyReward | USER?action=dailyReward | 200 | 147 | -1 |
| 133 | 6-PreHero | login_items_check | USER?action=loginJustUser | 200 | 200 | 1 |
| 134 | 6-PreHero | login_resource_check | USER?action=loginJustUser | 200 | 201 | 1 |
| 135 | 6-Hero | status | HERO?action=status | 200 | 98 | 1 |
| 136 | 6-Hero | levelUpH | HERO?action=levelUpH | 200 | 198 | 0 |
| 137 | 6-Hero | activateSkill | HERO?action=activateSkill | 200 | 209 | -1 |
| 138 | 6-Hero | prisonFeed | HERO?action=prisonFeed | 200 | 189 | 1 |
| 139 | 6-Hero | pitFeed | HERO?action=pitFeed | 200 | 145 | 0 |
| 140 | 6-PostHero | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 198 | -1 |
| 141 | 6-PostHero | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 206 | -1 |
| 142 | 6-PostHero | dailyReward | USER?action=dailyReward | 200 | 181 | -1 |
| 143 | 6-PostHero | login_items_check | USER?action=loginJustUser | 200 | 213 | 1 |
| 144 | 6-PostHero | login_resource_check | USER?action=loginJustUser | 200 | 202 | 1 |
| 145 | 7-Map | getQuadrant | WORLDMAP?action=getQuadrant&idKingdom=1&x=675&y=629 | 200 | 241 | -1 |
| 146 | 7-Map | scout | WORLDMAP?action=scout&x=705&y=659 | 200 | 51 | None |
| 147 | 7-Map | scout | WORLDMAP?action=scout&x=715&y=669 | 200 | 50 | None |
| 148 | 7-Map | scout | WORLDMAP?action=scout&x=690&y=644 | 200 | 51 | None |
| 149 | 7-Map | gather | WORLDMAP?action=gather&x=700&y=654&Troops=Infantry.1.1 | 200 | 731 | 2 |
| 150 | 7-Map | gather | WORLDMAP?action=gather&x=710&y=664&Troops=Infantry.1.1 | 200 | 536 | 0 |
| 151 | 7-Map | gather | WORLDMAP?action=gather&x=685&y=639&Troops=Infantry.1.1 | 200 | 753 | 2 |
| 152 | 7-Map | monster | WORLDMAP?action=monster&x=692&y=646&Troops=Infantry.1.1 | 200 | 747 | 2 |
| 153 | 7-PostMap | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | -1 |
| 154 | 7-PostMap | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 217 | -1 |
| 155 | 7-PostMap | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 156 | 7-PostMap | login_items_check | USER?action=loginJustUser | 200 | 216 | 1 |
| 157 | 7-PostMap | login_resource_check | USER?action=loginJustUser | 200 | 202 | 1 |
| 158 | 8-Final | refresh | USER?action=loginJustUser | 200 | 201 | 1 |

---
_Generated by E2E test on 2026-07-05 16:39:19_