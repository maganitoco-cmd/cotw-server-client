# E2E Timing Report — Gold Safety Net + Quest Items Economy

**Date**: 2026-07-05 17:57:18

**Total calls**: 209  

**Total time**: 52767ms (52.8s)  

**Average**: 252ms/call  


## Gold Safety Net Tracking

| Metric | Value |
|---|---|
| Gold safety net (putGold) | 100,000 |
| Gold actually spent | 600 |
| Gold first used at TH level | 1 |
| Items obtained from quests | 0 |
| Items consumed (speedUpItems) | 0 |
| Items net | 0 |

## Slowest Calls (Top 10)

| # | Phase | Endpoint | ms |
|---|---|---|---|
| 1 | 1-Reset | USER?action=reset | 1613 |
| 2 | 4-Attack | WORLDMAP?action=monster&x=694&y=650&Troops=Infantry.1.1 | 804 |
| 3 | 8-Map | WORLDMAP?action=gather&x=700&y=654&Troops=Infantry.1.1 | 771 |
| 4 | 4-Gather | WORLDMAP?action=gather&x=697&y=648&Troops=Infantry.1.1 | 763 |
| 5 | 4-Gather | WORLDMAP?action=gather&x=699&y=650&Troops=Infantry.1.1 | 750 |
| 6 | 4-Gather | WORLDMAP?action=gather&x=693&y=652&Troops=Infantry.1.1 | 744 |
| 7 | 4-Gather | WORLDMAP?action=gather&x=696&y=653&Troops=Infantry.1.1 | 742 |
| 8 | 4-Attack | WORLDMAP?action=monster&x=697&y=651&Troops=Infantry.1.1 | 740 |
| 9 | 4-Gather | WORLDMAP?action=gather&x=694&y=651&Troops=Infantry.1.1 | 739 |
| 10 | 4-Attack | WORLDMAP?action=monster&x=698&y=649&Troops=Infantry.1.1 | 736 |

## Summary by Phase

| Phase | Calls | Total ms | Avg ms |
|---|---|---|---|
| 1-Reset | 1 | 1613 | 1613 |
| 1-Login | 1 | 203 | 203 |
| 1-Init | 6 | 1369 | 228 |
| 1-Gold | 1 | 150 | 150 |
| 2-Collect | 4 | 840 | 210 |
| 2-Refresh | 1 | 203 | 203 |
| 2-Build | 17 | 4477 | 263 |
| 2-Refresh2 | 1 | 204 | 204 |
| 2-Collect2 | 5 | 1076 | 215 |
| 2-PostBuild | 5 | 1113 | 222 |
| 3-Refresh | 2 | 408 | 204 |
| 3-TH | 15 | 2950 | 196 |
| 3-Townhall | 3 | 1245 | 415 |
| 3-PostTH | 5 | 1021 | 204 |
| 4-Monsters | 1 | 67 | 67 |
| 4-Resources | 1 | 61 | 61 |
| 4-Map | 5 | 260 | 52 |
| 4-Attack | 5 | 3352 | 670 |
| 4-Gather | 5 | 3738 | 747 |
| 4-PostMap | 5 | 956 | 191 |
| 5-Refresh | 1 | 203 | 203 |
| 5-TrainBuild | 16 | 4529 | 283 |
| 5-PreTrain | 5 | 957 | 191 |
| 5-Train | 16 | 4200 | 262 |
| 5-PostTrain | 5 | 989 | 197 |
| 6-Refresh | 1 | 202 | 202 |
| 6-PreResearch | 5 | 1078 | 215 |
| 6-Research | 5 | 1118 | 223 |
| 6-PostResearch | 5 | 1012 | 202 |
| 7-PreHero | 5 | 958 | 191 |
| 7-Hero | 5 | 825 | 165 |
| 7-PostHero | 5 | 1077 | 215 |
| 8-Map | 7 | 2507 | 358 |
| 8-PostMap | 5 | 971 | 194 |
| 9-QuestLoop | 33 | 6597 | 199 |
| 10-Final | 1 | 238 | 238 |

## Per-Call Timing

| # | Phase | Action | Endpoint | HTTP | ms | Result |
|---|---|---|---|---|---|---|
| 1 | 1-Reset | reset | USER?action=reset | 200 | 1613 | 1 |
| 2 | 1-Login | refresh | USER?action=loginJustUser | 200 | 203 | 1 |
| 3 | 1-Init | dailyReward | USER?action=dailyReward | 200 | 149 | 0 |
| 4 | 1-Init | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 5 | 1-Init | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 213 | 0 |
| 6 | 1-Init | dailyReward | USER?action=dailyReward | 200 | 170 | 0 |
| 7 | 1-Init | login_items_check | USER?action=loginJustUser | 200 | 432 | 1 |
| 8 | 1-Init | login_resource_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 9 | 1-Gold | putGold | DEMO?action=putGold&deviceId=test050726 | 200 | 150 | 1 |
| 10 | 2-Collect | collect | BUILDINGS?action=collect&Node=3 | 200 | 229 | 1 |
| 11 | 2-Collect | collect | BUILDINGS?action=collect&Node=1 | 200 | 205 | 1 |
| 12 | 2-Collect | collect | BUILDINGS?action=collect&Node=2 | 200 | 203 | 1 |
| 13 | 2-Collect | collect | BUILDINGS?action=collect&Node=8 | 200 | 203 | 1 |
| 14 | 2-Refresh | refresh | USER?action=loginJustUser | 200 | 203 | 1 |
| 15 | 2-Build | construct_Academy | BUILDINGS?action=construct&idBuilding=2002&Node=4 | 200 | 256 | 0 |
| 16 | 2-Build | construct_Academy | BUILDINGS?action=construct&idBuilding=2002&Node=14 | 200 | 250 | 0 |
| 17 | 2-Build | construct_Hospital | BUILDINGS?action=construct&idBuilding=2003&Node=5 | 200 | 585 | 1 |
| 18 | 2-Build | speedUpGold_Hospital | CONSTRUCT?action=speedUpGold&idConstruct=6a4a9acb6097dcdc6759c33b | 200 | 299 | 1 |
| 19 | 2-Build | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 20 | 2-Build | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 212 | 0 |
| 21 | 2-Build | dailyReward | USER?action=dailyReward | 200 | 167 | 0 |
| 22 | 2-Build | login_items_check | USER?action=loginJustUser | 200 | 239 | 1 |
| 23 | 2-Build | login_resource_check | USER?action=loginJustUser | 200 | 225 | 1 |
| 24 | 2-Build | construct_Forge | BUILDINGS?action=construct&idBuilding=2007&Node=6 | 200 | 246 | 0 |
| 25 | 2-Build | construct_Forge | BUILDINGS?action=construct&idBuilding=2007&Node=16 | 200 | 248 | 0 |
| 26 | 2-Build | construct_Embassy | BUILDINGS?action=construct&idBuilding=2006&Node=9 | 200 | 249 | 0 |
| 27 | 2-Build | construct_Embassy | BUILDINGS?action=construct&idBuilding=2006&Node=19 | 200 | 290 | 0 |
| 28 | 2-Build | construct_Pit | BUILDINGS?action=construct&idBuilding=2008&Node=7 | 200 | 251 | 0 |
| 29 | 2-Build | construct_Pit | BUILDINGS?action=construct&idBuilding=2008&Node=17 | 200 | 250 | 0 |
| 30 | 2-Build | construct_Wishing Well | BUILDINGS?action=construct&idBuilding=2009&Node=18 | 200 | 249 | 0 |
| 31 | 2-Build | construct_Wishing Well | BUILDINGS?action=construct&idBuilding=2009&Node=20 | 200 | 260 | 0 |
| 32 | 2-Refresh2 | refresh | USER?action=loginJustUser | 200 | 204 | 1 |
| 33 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=3 | 200 | 258 | 1 |
| 34 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=1 | 200 | 203 | 1 |
| 35 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=2 | 200 | 206 | 1 |
| 36 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=8 | 200 | 203 | 1 |
| 37 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=5 | 200 | 206 | 1 |
| 38 | 2-PostBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 199 | 0 |
| 39 | 2-PostBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 213 | 0 |
| 40 | 2-PostBuild | dailyReward | USER?action=dailyReward | 200 | 192 | 0 |
| 41 | 2-PostBuild | login_items_check | USER?action=loginJustUser | 200 | 288 | 1 |
| 42 | 2-PostBuild | login_resource_check | USER?action=loginJustUser | 200 | 221 | 1 |
| 43 | 3-Refresh | refresh | USER?action=loginJustUser | 200 | 204 | 1 |
| 44 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 45 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 227 | 0 |
| 46 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 163 | 0 |
| 47 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 212 | 1 |
| 48 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 202 | 1 |
| 49 | 3-Townhall | levelUp_1 | BUILDINGS?action=levelUpB&Node=3 | 200 | 565 | 1 |
| 50 | 3-Townhall | speedUpGold_TH Lvl 1 | CONSTRUCT?action=speedUpGold&idConstruct=6a4a9ad36097dcdc6759c38e | 200 | 344 | 1 |
| 51 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 52 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 200 | 0 |
| 53 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 149 | 0 |
| 54 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 209 | 1 |
| 55 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 56 | 3-Refresh | refresh | USER?action=loginJustUser | 200 | 204 | 1 |
| 57 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 202 | 0 |
| 58 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 199 | 0 |
| 59 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 149 | 0 |
| 60 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 218 | 1 |
| 61 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 214 | 1 |
| 62 | 3-Townhall | levelUp_2 | BUILDINGS?action=levelUpB&Node=3 | 200 | 336 | 0 |
| 63 | 3-PostTH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 209 | 0 |
| 64 | 3-PostTH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 202 | 0 |
| 65 | 3-PostTH | dailyReward | USER?action=dailyReward | 200 | 149 | 0 |
| 66 | 3-PostTH | login_items_check | USER?action=loginJustUser | 200 | 216 | 1 |
| 67 | 3-PostTH | login_resource_check | USER?action=loginJustUser | 200 | 245 | 1 |
| 68 | 4-Monsters | spawnMonsters | DEMO?action=spawnMonsters&deviceId=test050726 | 200 | 67 | None |
| 69 | 4-Resources | spawnResources | DEMO?action=spawnResources&deviceId=test050726 | 200 | 61 | None |
| 70 | 4-Map | scout | WORLDMAP?action=scout&x=693&y=647 | 200 | 52 | None |
| 71 | 4-Map | scout | WORLDMAP?action=scout&x=697&y=651 | 200 | 53 | None |
| 72 | 4-Map | scout | WORLDMAP?action=scout&x=695&y=653 | 200 | 52 | None |
| 73 | 4-Map | scout | WORLDMAP?action=scout&x=699&y=649 | 200 | 52 | None |
| 74 | 4-Map | scout | WORLDMAP?action=scout&x=692&y=650 | 200 | 51 | None |
| 75 | 4-Attack | monster_696_650 | WORLDMAP?action=monster&x=696&y=650&Troops=Infantry.1.1 | 200 | 537 | 0 |
| 76 | 4-Attack | monster_697_651 | WORLDMAP?action=monster&x=697&y=651&Troops=Infantry.1.1 | 200 | 740 | 2 |
| 77 | 4-Attack | monster_694_650 | WORLDMAP?action=monster&x=694&y=650&Troops=Infantry.1.1 | 200 | 804 | 2 |
| 78 | 4-Attack | monster_698_649 | WORLDMAP?action=monster&x=698&y=649&Troops=Infantry.1.1 | 200 | 736 | 2 |
| 79 | 4-Attack | monster_695_652 | WORLDMAP?action=monster&x=695&y=652&Troops=Infantry.1.1 | 200 | 535 | 0 |
| 80 | 4-Gather | gather_694_651 | WORLDMAP?action=gather&x=694&y=651&Troops=Infantry.1.1 | 200 | 739 | 2 |
| 81 | 4-Gather | gather_697_648 | WORLDMAP?action=gather&x=697&y=648&Troops=Infantry.1.1 | 200 | 763 | 2 |
| 82 | 4-Gather | gather_699_650 | WORLDMAP?action=gather&x=699&y=650&Troops=Infantry.1.1 | 200 | 750 | 2 |
| 83 | 4-Gather | gather_696_653 | WORLDMAP?action=gather&x=696&y=653&Troops=Infantry.1.1 | 200 | 742 | 2 |
| 84 | 4-Gather | gather_693_652 | WORLDMAP?action=gather&x=693&y=652&Troops=Infantry.1.1 | 200 | 744 | 2 |
| 85 | 4-PostMap | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 86 | 4-PostMap | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 201 | 0 |
| 87 | 4-PostMap | dailyReward | USER?action=dailyReward | 200 | 148 | 0 |
| 88 | 4-PostMap | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 89 | 4-PostMap | login_resource_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 90 | 5-Refresh | refresh | USER?action=loginJustUser | 200 | 203 | 1 |
| 91 | 5-TrainBuild | construct_Barracks(Infantry) | BUILDINGS?action=construct&idBuilding=2014&Node=10 | 200 | 609 | 1 |
| 92 | 5-TrainBuild | speedUpGold_Barracks (Infantry) | CONSTRUCT?action=speedUpGold&idConstruct=6a4a9ae16097dcdc6759c3fe | 200 | 355 | 1 |
| 93 | 5-TrainBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 235 | 0 |
| 94 | 5-TrainBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 203 | 0 |
| 95 | 5-TrainBuild | dailyReward | USER?action=dailyReward | 200 | 149 | 0 |
| 96 | 5-TrainBuild | login_items_check | USER?action=loginJustUser | 200 | 216 | 1 |
| 97 | 5-TrainBuild | login_resource_check | USER?action=loginJustUser | 200 | 235 | 1 |
| 98 | 5-TrainBuild | construct_ArcherRange | BUILDINGS?action=construct&idBuilding=2012&Node=12 | 200 | 627 | 1 |
| 99 | 5-TrainBuild | speedUpGold_Archer Range | CONSTRUCT?action=speedUpGold&idConstruct=6a4a9ae36097dcdc6759c40f | 200 | 297 | 1 |
| 100 | 5-TrainBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 217 | 0 |
| 101 | 5-TrainBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 260 | 0 |
| 102 | 5-TrainBuild | dailyReward | USER?action=dailyReward | 200 | 148 | 0 |
| 103 | 5-TrainBuild | login_items_check | USER?action=loginJustUser | 200 | 215 | 1 |
| 104 | 5-TrainBuild | login_resource_check | USER?action=loginJustUser | 200 | 217 | 1 |
| 105 | 5-TrainBuild | construct_Stable(Cavalry) | BUILDINGS?action=construct&idBuilding=2013&Node=11 | 200 | 297 | 0 |
| 106 | 5-TrainBuild | construct_SiegeWorkshop | BUILDINGS?action=construct&idBuilding=2015&Node=13 | 200 | 249 | 0 |
| 107 | 5-PreTrain | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 202 | 0 |
| 108 | 5-PreTrain | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 199 | 0 |
| 109 | 5-PreTrain | dailyReward | USER?action=dailyReward | 200 | 149 | 0 |
| 110 | 5-PreTrain | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 111 | 5-PreTrain | login_resource_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 112 | 5-Train | train_Infantry | BUILDINGS?action=train&idBuilding=2014&Level=1&Quantity=5 | 200 | 559 | 1 |
| 113 | 5-Train | speedUpGold_Infantry | CONSTRUCT?action=speedUpGold&idConstruct=6a4a9ae76097dcdc6759c432 | 200 | 388 | 1 |
| 114 | 5-Train | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 210 | 0 |
| 115 | 5-Train | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 201 | 0 |
| 116 | 5-Train | dailyReward | USER?action=dailyReward | 200 | 148 | 0 |
| 117 | 5-Train | login_items_check | USER?action=loginJustUser | 200 | 207 | 1 |
| 118 | 5-Train | login_resource_check | USER?action=loginJustUser | 200 | 251 | 1 |
| 119 | 5-Train | train_Archer | BUILDINGS?action=train&idBuilding=2012&Level=1&Quantity=3 | 200 | 549 | 1 |
| 120 | 5-Train | speedUpGold_Archer | CONSTRUCT?action=speedUpGold&idConstruct=6a4a9ae96097dcdc6759c443 | 200 | 304 | 1 |
| 121 | 5-Train | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 202 | 0 |
| 122 | 5-Train | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 211 | 0 |
| 123 | 5-Train | dailyReward | USER?action=dailyReward | 200 | 148 | 0 |
| 124 | 5-Train | login_items_check | USER?action=loginJustUser | 200 | 214 | 1 |
| 125 | 5-Train | login_resource_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 126 | 5-Train | train_Cavalry | BUILDINGS?action=train&idBuilding=2013&Level=1&Quantity=2 | 200 | 203 | 0 |
| 127 | 5-Train | train_Siege | BUILDINGS?action=train&idBuilding=2015&Level=1&Quantity=1 | 200 | 201 | 0 |
| 128 | 5-PostTrain | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 212 | 0 |
| 129 | 5-PostTrain | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 200 | 0 |
| 130 | 5-PostTrain | dailyReward | USER?action=dailyReward | 200 | 160 | 0 |
| 131 | 5-PostTrain | login_items_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 132 | 5-PostTrain | login_resource_check | USER?action=loginJustUser | 200 | 214 | 1 |
| 133 | 6-Refresh | refresh | USER?action=loginJustUser | 200 | 202 | 1 |
| 134 | 6-PreResearch | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 135 | 6-PreResearch | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 212 | 0 |
| 136 | 6-PreResearch | dailyReward | USER?action=dailyReward | 200 | 190 | 0 |
| 137 | 6-PreResearch | login_items_check | USER?action=loginJustUser | 200 | 263 | 1 |
| 138 | 6-PreResearch | login_resource_check | USER?action=loginJustUser | 200 | 213 | 1 |
| 139 | 6-Research | research_1 | BUILDINGS?action=research&idResearch=1 | 200 | 200 | 0 |
| 140 | 6-Research | research_2 | BUILDINGS?action=research&idResearch=2 | 200 | 212 | 0 |
| 141 | 6-Research | research_3 | BUILDINGS?action=research&idResearch=3 | 200 | 221 | 0 |
| 142 | 6-Research | research_4 | BUILDINGS?action=research&idResearch=4 | 200 | 269 | 0 |
| 143 | 6-Research | research_5 | BUILDINGS?action=research&idResearch=5 | 200 | 216 | 0 |
| 144 | 6-PostResearch | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 145 | 6-PostResearch | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 253 | 0 |
| 146 | 6-PostResearch | dailyReward | USER?action=dailyReward | 200 | 150 | 0 |
| 147 | 6-PostResearch | login_items_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 148 | 6-PostResearch | login_resource_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 149 | 7-PreHero | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 202 | 0 |
| 150 | 7-PreHero | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 201 | 0 |
| 151 | 7-PreHero | dailyReward | USER?action=dailyReward | 200 | 146 | 0 |
| 152 | 7-PreHero | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 153 | 7-PreHero | login_resource_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 154 | 7-Hero | status | HERO?action=status | 200 | 127 | 1 |
| 155 | 7-Hero | levelUpH | HERO?action=levelUpH | 200 | 202 | 0 |
| 156 | 7-Hero | activateSkill | HERO?action=activateSkill | 200 | 200 | 0 |
| 157 | 7-Hero | prisonFeed | HERO?action=prisonFeed | 200 | 147 | 1 |
| 158 | 7-Hero | pitFeed | HERO?action=pitFeed | 200 | 149 | 0 |
| 159 | 7-PostHero | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 202 | 0 |
| 160 | 7-PostHero | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 200 | 0 |
| 161 | 7-PostHero | dailyReward | USER?action=dailyReward | 200 | 159 | 0 |
| 162 | 7-PostHero | login_items_check | USER?action=loginJustUser | 200 | 219 | 1 |
| 163 | 7-PostHero | login_resource_check | USER?action=loginJustUser | 200 | 297 | 1 |
| 164 | 8-Map | getQuadrant | WORLDMAP?action=getQuadrant&idKingdom=1&x=675&y=629 | 200 | 281 | -1 |
| 165 | 8-Map | scout | WORLDMAP?action=scout&x=705&y=659 | 200 | 54 | None |
| 166 | 8-Map | scout | WORLDMAP?action=scout&x=715&y=669 | 200 | 52 | None |
| 167 | 8-Map | scout | WORLDMAP?action=scout&x=690&y=644 | 200 | 52 | None |
| 168 | 8-Map | gather | WORLDMAP?action=gather&x=700&y=654&Troops=Infantry.1.1 | 200 | 771 | 2 |
| 169 | 8-Map | gather | WORLDMAP?action=gather&x=710&y=664&Troops=Infantry.1.1 | 200 | 561 | 0 |
| 170 | 8-Map | gather | WORLDMAP?action=gather&x=685&y=639&Troops=Infantry.1.1 | 200 | 736 | 2 |
| 171 | 8-PostMap | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 213 | 0 |
| 172 | 8-PostMap | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 203 | 0 |
| 173 | 8-PostMap | dailyReward | USER?action=dailyReward | 200 | 147 | 0 |
| 174 | 8-PostMap | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 175 | 8-PostMap | login_resource_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 176 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 177 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 202 | 0 |
| 178 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 160 | 0 |
| 179 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 180 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 181 | 9-QuestLoop | chestQuests | DEMO?action=chestQuests&deviceId=test050726 | 200 | 150 | 1 |
| 182 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 183 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 209 | 0 |
| 184 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 186 | 0 |
| 185 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 263 | 1 |
| 186 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 223 | 1 |
| 187 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 252 | 0 |
| 188 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 282 | 0 |
| 189 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 164 | 0 |
| 190 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 191 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 192 | 9-QuestLoop | chestQuests | DEMO?action=chestQuests&deviceId=test050726 | 200 | 148 | 1 |
| 193 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 205 | 0 |
| 194 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 199 | 0 |
| 195 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 148 | 0 |
| 196 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 197 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 215 | 1 |
| 198 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 199 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 201 | 0 |
| 200 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 148 | 0 |
| 201 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 202 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 203 | 9-QuestLoop | chestQuests | DEMO?action=chestQuests&deviceId=test050726 | 200 | 146 | 1 |
| 204 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 205 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 232 | 0 |
| 206 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 176 | 0 |
| 207 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 234 | 1 |
| 208 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 225 | 1 |
| 209 | 10-Final | refresh | USER?action=loginJustUser | 200 | 238 | 1 |

---
_Generated by E2E test on 2026-07-05 17:57:18_