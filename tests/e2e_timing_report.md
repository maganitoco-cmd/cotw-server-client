# E2E Timing Report — Gold Safety Net + Quest Items Economy

**Date**: 2026-07-05 17:16:39

**Total calls**: 221  

**Total time**: 56922ms (56.9s)  

**Average**: 258ms/call  


## Gold Safety Net Tracking

| Metric | Value |
|---|---|
| Gold safety net (putGold) | 100,000 |
| Gold actually spent | 0 |
| Gold first used at TH level | Never used |
| Items obtained from quests | 0 |
| Items consumed (speedUpItems) | 0 |
| Items net | 0 |

## Slowest Calls (Top 10)

| # | Phase | Endpoint | ms |
|---|---|---|---|
| 1 | 1-Reset | USER?action=reset | 2258 |
| 2 | 1-Init | QUEST?action=rewards&idQuest=0 | 871 |
| 3 | 4-Gather | WORLDMAP?action=gather&x=694&y=651&Troops=Infantry.1.1 | 786 |
| 4 | 4-Attack | WORLDMAP?action=monster&x=698&y=649&Troops=Infantry.1.1 | 785 |
| 5 | 8-Map | WORLDMAP?action=gather&x=700&y=654&Troops=Infantry.1.1 | 755 |
| 6 | 4-Gather | WORLDMAP?action=gather&x=693&y=652&Troops=Infantry.1.1 | 744 |
| 7 | 4-Attack | WORLDMAP?action=monster&x=697&y=651&Troops=Infantry.1.1 | 743 |
| 8 | 4-Gather | WORLDMAP?action=gather&x=697&y=648&Troops=Infantry.1.1 | 742 |
| 9 | 4-Gather | WORLDMAP?action=gather&x=699&y=650&Troops=Infantry.1.1 | 742 |
| 10 | 8-Map | WORLDMAP?action=gather&x=685&y=639&Troops=Infantry.1.1 | 742 |

## Summary by Phase

| Phase | Calls | Total ms | Avg ms |
|---|---|---|---|
| 1-Reset | 1 | 2258 | 2258 |
| 1-Login | 1 | 243 | 243 |
| 1-Init | 6 | 1819 | 303 |
| 1-Gold | 1 | 155 | 155 |
| 2-Collect | 4 | 855 | 213 |
| 2-Refresh | 1 | 205 | 205 |
| 2-Build | 20 | 5326 | 266 |
| 2-Refresh2 | 1 | 205 | 205 |
| 2-Collect2 | 5 | 1237 | 247 |
| 2-PostBuild | 5 | 1039 | 207 |
| 3-Refresh | 2 | 430 | 215 |
| 3-TH | 15 | 3135 | 209 |
| 3-Townhall | 6 | 1812 | 302 |
| 3-PostTH | 5 | 1020 | 204 |
| 4-Monsters | 1 | 53 | 53 |
| 4-Resources | 1 | 53 | 53 |
| 4-Map | 5 | 262 | 52 |
| 4-Attack | 5 | 3343 | 668 |
| 4-Gather | 5 | 3753 | 750 |
| 4-PostMap | 5 | 968 | 193 |
| 5-Refresh | 1 | 204 | 204 |
| 5-TrainBuild | 22 | 5936 | 269 |
| 5-PreTrain | 5 | 992 | 198 |
| 5-Train | 16 | 4102 | 256 |
| 5-PostTrain | 5 | 1071 | 214 |
| 6-Refresh | 1 | 215 | 215 |
| 6-PreResearch | 5 | 1043 | 208 |
| 6-Research | 5 | 1002 | 200 |
| 6-PostResearch | 5 | 955 | 191 |
| 7-PreHero | 5 | 1018 | 203 |
| 7-Hero | 5 | 936 | 187 |
| 7-PostHero | 5 | 954 | 190 |
| 8-Map | 7 | 2528 | 361 |
| 8-PostMap | 5 | 1048 | 209 |
| 9-QuestLoop | 33 | 6539 | 198 |
| 10-Final | 1 | 208 | 208 |

## Per-Call Timing

| # | Phase | Action | Endpoint | HTTP | ms | Result |
|---|---|---|---|---|---|---|
| 1 | 1-Reset | reset | USER?action=reset | 200 | 2258 | 1 |
| 2 | 1-Login | refresh | USER?action=loginJustUser | 200 | 243 | 1 |
| 3 | 1-Init | dailyReward | USER?action=dailyReward | 200 | 150 | -1 |
| 4 | 1-Init | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 871 | 0 |
| 5 | 1-Init | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 215 | 0 |
| 6 | 1-Init | dailyReward | USER?action=dailyReward | 200 | 153 | -1 |
| 7 | 1-Init | login_items_check | USER?action=loginJustUser | 200 | 225 | 1 |
| 8 | 1-Init | login_resource_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 9 | 1-Gold | putGold | DEMO?action=putGold&deviceId=test050726 | 200 | 155 | 1 |
| 10 | 2-Collect | collect | BUILDINGS?action=collect&Node=3 | 200 | 233 | 1 |
| 11 | 2-Collect | collect | BUILDINGS?action=collect&Node=1 | 200 | 208 | 1 |
| 12 | 2-Collect | collect | BUILDINGS?action=collect&Node=2 | 200 | 207 | 1 |
| 13 | 2-Collect | collect | BUILDINGS?action=collect&Node=8 | 200 | 207 | 1 |
| 14 | 2-Refresh | refresh | USER?action=loginJustUser | 200 | 205 | 1 |
| 15 | 2-Build | construct_Academy | BUILDINGS?action=construct&idBuilding=2002&Node=4 | 200 | 249 | 0 |
| 16 | 2-Build | construct_Academy | BUILDINGS?action=construct&idBuilding=2002&Node=14 | 200 | 271 | 0 |
| 17 | 2-Build | construct_Hospital | BUILDINGS?action=construct&idBuilding=2003&Node=5 | 200 | 680 | 1 |
| 18 | 2-Build | remainingTime_Hospital | CONSTRUCT?action=remainingTime&idConstruct=6a4a91306097dcdc67e33b4d | 200 | 310 | 1 |
| 19 | 2-Build | timeItems | ITEMS?action=timeItems | 200 | 100 | 1 |
| 20 | 2-Build | speedUpGold_Hospital | CONSTRUCT?action=speedUpGold&idConstruct=6a4a91306097dcdc67e33b4d | 200 | 248 | 0 |
| 21 | 2-Build | remainingTime2_Hospital | CONSTRUCT?action=remainingTime&idConstruct=6a4a91306097dcdc67e33b4d | 200 | 437 | 0 |
| 22 | 2-Build | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 223 | 0 |
| 23 | 2-Build | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 202 | 0 |
| 24 | 2-Build | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 25 | 2-Build | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 26 | 2-Build | login_resource_check | USER?action=loginJustUser | 200 | 229 | 1 |
| 27 | 2-Build | construct_Forge | BUILDINGS?action=construct&idBuilding=2007&Node=6 | 200 | 267 | 0 |
| 28 | 2-Build | construct_Forge | BUILDINGS?action=construct&idBuilding=2007&Node=16 | 200 | 247 | 0 |
| 29 | 2-Build | construct_Embassy | BUILDINGS?action=construct&idBuilding=2006&Node=9 | 200 | 257 | 0 |
| 30 | 2-Build | construct_Embassy | BUILDINGS?action=construct&idBuilding=2006&Node=19 | 200 | 248 | 0 |
| 31 | 2-Build | construct_Pit | BUILDINGS?action=construct&idBuilding=2008&Node=7 | 200 | 263 | 0 |
| 32 | 2-Build | construct_Pit | BUILDINGS?action=construct&idBuilding=2008&Node=17 | 200 | 247 | 0 |
| 33 | 2-Build | construct_Wishing Well | BUILDINGS?action=construct&idBuilding=2009&Node=18 | 200 | 248 | 0 |
| 34 | 2-Build | construct_Wishing Well | BUILDINGS?action=construct&idBuilding=2009&Node=20 | 200 | 248 | 0 |
| 35 | 2-Refresh2 | refresh | USER?action=loginJustUser | 200 | 205 | 1 |
| 36 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=3 | 200 | 231 | 1 |
| 37 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=1 | 200 | 214 | 1 |
| 38 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=2 | 200 | 226 | 1 |
| 39 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=8 | 200 | 275 | 1 |
| 40 | 2-Collect2 | collect | BUILDINGS?action=collect&Node=5 | 200 | 291 | 1 |
| 41 | 2-PostBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 216 | 0 |
| 42 | 2-PostBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 208 | 0 |
| 43 | 2-PostBuild | dailyReward | USER?action=dailyReward | 200 | 152 | -1 |
| 44 | 2-PostBuild | login_items_check | USER?action=loginJustUser | 200 | 227 | 1 |
| 45 | 2-PostBuild | login_resource_check | USER?action=loginJustUser | 200 | 236 | 1 |
| 46 | 3-Refresh | refresh | USER?action=loginJustUser | 200 | 227 | 1 |
| 47 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 212 | 0 |
| 48 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 217 | 0 |
| 49 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 167 | -1 |
| 50 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 51 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 52 | 3-Townhall | levelUp_1 | BUILDINGS?action=levelUpB&Node=3 | 200 | 565 | 1 |
| 53 | 3-Townhall | remainingTime_TH Lvl 1 | CONSTRUCT?action=remainingTime&idConstruct=6a4a913d6097dcdc67e33bb5 | 200 | 346 | 1 |
| 54 | 3-Townhall | timeItems | ITEMS?action=timeItems | 200 | 145 | 1 |
| 55 | 3-Townhall | speedUpGold_TH Lvl 1 | CONSTRUCT?action=speedUpGold&idConstruct=6a4a913d6097dcdc67e33bb5 | 200 | 247 | 0 |
| 56 | 3-Townhall | remainingTime2_TH Lvl 1 | CONSTRUCT?action=remainingTime&idConstruct=6a4a913d6097dcdc67e33bb5 | 200 | 252 | 0 |
| 57 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 199 | 0 |
| 58 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 198 | 0 |
| 59 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 60 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 223 | 1 |
| 61 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 219 | 1 |
| 62 | 3-Refresh | refresh | USER?action=loginJustUser | 200 | 203 | 1 |
| 63 | 3-TH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 206 | 0 |
| 64 | 3-TH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 205 | 0 |
| 65 | 3-TH | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 66 | 3-TH | login_items_check | USER?action=loginJustUser | 200 | 275 | 1 |
| 67 | 3-TH | login_resource_check | USER?action=loginJustUser | 200 | 312 | 1 |
| 68 | 3-Townhall | levelUp_2 | BUILDINGS?action=levelUpB&Node=3 | 200 | 257 | 0 |
| 69 | 3-PostTH | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 70 | 3-PostTH | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 205 | 0 |
| 71 | 3-PostTH | dailyReward | USER?action=dailyReward | 200 | 161 | -1 |
| 72 | 3-PostTH | login_items_check | USER?action=loginJustUser | 200 | 243 | 1 |
| 73 | 3-PostTH | login_resource_check | USER?action=loginJustUser | 200 | 211 | 1 |
| 74 | 4-Monsters | spawnMonsters | DEMO?action=spawnMonsters&deviceId=test050726 | 200 | 53 | None |
| 75 | 4-Resources | spawnResources | DEMO?action=spawnResources&deviceId=test050726 | 200 | 53 | None |
| 76 | 4-Map | scout | WORLDMAP?action=scout&x=693&y=647 | 200 | 54 | None |
| 77 | 4-Map | scout | WORLDMAP?action=scout&x=697&y=651 | 200 | 52 | None |
| 78 | 4-Map | scout | WORLDMAP?action=scout&x=695&y=653 | 200 | 52 | None |
| 79 | 4-Map | scout | WORLDMAP?action=scout&x=699&y=649 | 200 | 52 | None |
| 80 | 4-Map | scout | WORLDMAP?action=scout&x=692&y=650 | 200 | 52 | None |
| 81 | 4-Attack | monster_696_650 | WORLDMAP?action=monster&x=696&y=650&Troops=Infantry.1.1 | 200 | 530 | 0 |
| 82 | 4-Attack | monster_697_651 | WORLDMAP?action=monster&x=697&y=651&Troops=Infantry.1.1 | 200 | 743 | 2 |
| 83 | 4-Attack | monster_694_650 | WORLDMAP?action=monster&x=694&y=650&Troops=Infantry.1.1 | 200 | 732 | 2 |
| 84 | 4-Attack | monster_698_649 | WORLDMAP?action=monster&x=698&y=649&Troops=Infantry.1.1 | 200 | 785 | 2 |
| 85 | 4-Attack | monster_695_652 | WORLDMAP?action=monster&x=695&y=652&Troops=Infantry.1.1 | 200 | 553 | 0 |
| 86 | 4-Gather | gather_694_651 | WORLDMAP?action=gather&x=694&y=651&Troops=Infantry.1.1 | 200 | 786 | 2 |
| 87 | 4-Gather | gather_697_648 | WORLDMAP?action=gather&x=697&y=648&Troops=Infantry.1.1 | 200 | 742 | 2 |
| 88 | 4-Gather | gather_699_650 | WORLDMAP?action=gather&x=699&y=650&Troops=Infantry.1.1 | 200 | 742 | 2 |
| 89 | 4-Gather | gather_696_653 | WORLDMAP?action=gather&x=696&y=653&Troops=Infantry.1.1 | 200 | 739 | 2 |
| 90 | 4-Gather | gather_693_652 | WORLDMAP?action=gather&x=693&y=652&Troops=Infantry.1.1 | 200 | 744 | 2 |
| 91 | 4-PostMap | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 206 | 0 |
| 92 | 4-PostMap | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 201 | 0 |
| 93 | 4-PostMap | dailyReward | USER?action=dailyReward | 200 | 152 | -1 |
| 94 | 4-PostMap | login_items_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 95 | 4-PostMap | login_resource_check | USER?action=loginJustUser | 200 | 206 | 1 |
| 96 | 5-Refresh | refresh | USER?action=loginJustUser | 200 | 204 | 1 |
| 97 | 5-TrainBuild | construct_Barracks(Infantry) | BUILDINGS?action=construct&idBuilding=2014&Node=10 | 200 | 697 | 1 |
| 98 | 5-TrainBuild | remainingTime_Barracks (Infantry) | CONSTRUCT?action=remainingTime&idConstruct=6a4a91506097dcdc67e33c39 | 200 | 335 | 1 |
| 99 | 5-TrainBuild | timeItems | ITEMS?action=timeItems | 200 | 113 | 1 |
| 100 | 5-TrainBuild | speedUpGold_Barracks (Infantry) | CONSTRUCT?action=speedUpGold&idConstruct=6a4a91506097dcdc67e33c39 | 200 | 252 | 0 |
| 101 | 5-TrainBuild | remainingTime2_Barracks (Infantry) | CONSTRUCT?action=remainingTime&idConstruct=6a4a91506097dcdc67e33c39 | 200 | 340 | 0 |
| 102 | 5-TrainBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 238 | 0 |
| 103 | 5-TrainBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 212 | 0 |
| 104 | 5-TrainBuild | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 105 | 5-TrainBuild | login_items_check | USER?action=loginJustUser | 200 | 208 | 1 |
| 106 | 5-TrainBuild | login_resource_check | USER?action=loginJustUser | 200 | 202 | 1 |
| 107 | 5-TrainBuild | construct_ArcherRange | BUILDINGS?action=construct&idBuilding=2012&Node=12 | 200 | 685 | 1 |
| 108 | 5-TrainBuild | remainingTime_Archer Range | CONSTRUCT?action=remainingTime&idConstruct=6a4a91576097dcdc67e33c5f | 200 | 312 | 1 |
| 109 | 5-TrainBuild | timeItems | ITEMS?action=timeItems | 200 | 99 | 1 |
| 110 | 5-TrainBuild | speedUpGold_Archer Range | CONSTRUCT?action=speedUpGold&idConstruct=6a4a91576097dcdc67e33c5f | 200 | 246 | 0 |
| 111 | 5-TrainBuild | remainingTime2_Archer Range | CONSTRUCT?action=remainingTime&idConstruct=6a4a91576097dcdc67e33c5f | 200 | 260 | 0 |
| 112 | 5-TrainBuild | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 262 | 0 |
| 113 | 5-TrainBuild | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 217 | 0 |
| 114 | 5-TrainBuild | dailyReward | USER?action=dailyReward | 200 | 149 | -1 |
| 115 | 5-TrainBuild | login_items_check | USER?action=loginJustUser | 200 | 219 | 1 |
| 116 | 5-TrainBuild | login_resource_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 117 | 5-TrainBuild | construct_Stable(Cavalry) | BUILDINGS?action=construct&idBuilding=2013&Node=11 | 200 | 293 | 0 |
| 118 | 5-TrainBuild | construct_SiegeWorkshop | BUILDINGS?action=construct&idBuilding=2015&Node=13 | 200 | 246 | 0 |
| 119 | 5-PreTrain | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 198 | 0 |
| 120 | 5-PreTrain | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 202 | 0 |
| 121 | 5-PreTrain | dailyReward | USER?action=dailyReward | 200 | 182 | -1 |
| 122 | 5-PreTrain | login_items_check | USER?action=loginJustUser | 200 | 206 | 1 |
| 123 | 5-PreTrain | login_resource_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 124 | 5-Train | train_Infantry | BUILDINGS?action=train&idBuilding=2014&Level=1&Quantity=5 | 200 | 575 | 1 |
| 125 | 5-Train | remainingTime_Infantry | CONSTRUCT?action=remainingTime&idConstruct=6a4a915f6097dcdc67e33c96 | 200 | 331 | 0 |
| 126 | 5-Train | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 127 | 5-Train | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 201 | 0 |
| 128 | 5-Train | dailyReward | USER?action=dailyReward | 200 | 149 | -1 |
| 129 | 5-Train | login_items_check | USER?action=loginJustUser | 200 | 207 | 1 |
| 130 | 5-Train | login_resource_check | USER?action=loginJustUser | 200 | 222 | 1 |
| 131 | 5-Train | train_Archer | BUILDINGS?action=train&idBuilding=2012&Level=1&Quantity=3 | 200 | 578 | 1 |
| 132 | 5-Train | remainingTime_Archer | CONSTRUCT?action=remainingTime&idConstruct=6a4a91626097dcdc67e33cab | 200 | 247 | 0 |
| 133 | 5-Train | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 203 | 0 |
| 134 | 5-Train | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 210 | 0 |
| 135 | 5-Train | dailyReward | USER?action=dailyReward | 200 | 149 | -1 |
| 136 | 5-Train | login_items_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 137 | 5-Train | login_resource_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 138 | 5-Train | train_Cavalry | BUILDINGS?action=train&idBuilding=2013&Level=1&Quantity=2 | 200 | 199 | 0 |
| 139 | 5-Train | train_Siege | BUILDINGS?action=train&idBuilding=2015&Level=1&Quantity=1 | 200 | 223 | 0 |
| 140 | 5-PostTrain | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 233 | 0 |
| 141 | 5-PostTrain | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 200 | 0 |
| 142 | 5-PostTrain | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 143 | 5-PostTrain | login_items_check | USER?action=loginJustUser | 200 | 277 | 1 |
| 144 | 5-PostTrain | login_resource_check | USER?action=loginJustUser | 200 | 213 | 1 |
| 145 | 6-Refresh | refresh | USER?action=loginJustUser | 200 | 215 | 1 |
| 146 | 6-PreResearch | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 147 | 6-PreResearch | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 200 | 0 |
| 148 | 6-PreResearch | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 149 | 6-PreResearch | login_items_check | USER?action=loginJustUser | 200 | 219 | 1 |
| 150 | 6-PreResearch | login_resource_check | USER?action=loginJustUser | 200 | 275 | 1 |
| 151 | 6-Research | research_1 | BUILDINGS?action=research&idResearch=1 | 200 | 204 | 0 |
| 152 | 6-Research | research_2 | BUILDINGS?action=research&idResearch=2 | 200 | 199 | 0 |
| 153 | 6-Research | research_3 | BUILDINGS?action=research&idResearch=3 | 200 | 201 | 0 |
| 154 | 6-Research | research_4 | BUILDINGS?action=research&idResearch=4 | 200 | 198 | 0 |
| 155 | 6-Research | research_5 | BUILDINGS?action=research&idResearch=5 | 200 | 200 | 0 |
| 156 | 6-PostResearch | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 202 | 0 |
| 157 | 6-PostResearch | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 198 | 0 |
| 158 | 6-PostResearch | dailyReward | USER?action=dailyReward | 200 | 149 | -1 |
| 159 | 6-PostResearch | login_items_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 160 | 6-PostResearch | login_resource_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 161 | 7-PreHero | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 162 | 7-PreHero | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 200 | 0 |
| 163 | 7-PreHero | dailyReward | USER?action=dailyReward | 200 | 149 | -1 |
| 164 | 7-PreHero | login_items_check | USER?action=loginJustUser | 200 | 202 | 1 |
| 165 | 7-PreHero | login_resource_check | USER?action=loginJustUser | 200 | 266 | 1 |
| 166 | 7-Hero | status | HERO?action=status | 200 | 130 | 1 |
| 167 | 7-Hero | levelUpH | HERO?action=levelUpH | 200 | 215 | 0 |
| 168 | 7-Hero | activateSkill | HERO?action=activateSkill | 200 | 249 | 0 |
| 169 | 7-Hero | prisonFeed | HERO?action=prisonFeed | 200 | 162 | 1 |
| 170 | 7-Hero | pitFeed | HERO?action=pitFeed | 200 | 180 | 0 |
| 171 | 7-PostHero | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 172 | 7-PostHero | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 201 | 0 |
| 173 | 7-PostHero | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 174 | 7-PostHero | login_items_check | USER?action=loginJustUser | 200 | 204 | 1 |
| 175 | 7-PostHero | login_resource_check | USER?action=loginJustUser | 200 | 201 | 1 |
| 176 | 8-Map | getQuadrant | WORLDMAP?action=getQuadrant&idKingdom=1&x=675&y=629 | 200 | 274 | -1 |
| 177 | 8-Map | scout | WORLDMAP?action=scout&x=705&y=659 | 200 | 83 | None |
| 178 | 8-Map | scout | WORLDMAP?action=scout&x=715&y=669 | 200 | 70 | None |
| 179 | 8-Map | scout | WORLDMAP?action=scout&x=690&y=644 | 200 | 67 | None |
| 180 | 8-Map | gather | WORLDMAP?action=gather&x=700&y=654&Troops=Infantry.1.1 | 200 | 755 | 2 |
| 181 | 8-Map | gather | WORLDMAP?action=gather&x=710&y=664&Troops=Infantry.1.1 | 200 | 537 | 0 |
| 182 | 8-Map | gather | WORLDMAP?action=gather&x=685&y=639&Troops=Infantry.1.1 | 200 | 742 | 2 |
| 183 | 8-PostMap | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 200 | 0 |
| 184 | 8-PostMap | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 200 | 0 |
| 185 | 8-PostMap | dailyReward | USER?action=dailyReward | 200 | 148 | -1 |
| 186 | 8-PostMap | login_items_check | USER?action=loginJustUser | 200 | 218 | 1 |
| 187 | 8-PostMap | login_resource_check | USER?action=loginJustUser | 200 | 282 | 1 |
| 188 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 189 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 199 | 0 |
| 190 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 187 | -1 |
| 191 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 269 | 1 |
| 192 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 193 | 9-QuestLoop | chestQuests | DEMO?action=chestQuests&deviceId=test050726 | 200 | 150 | 1 |
| 194 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 195 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 202 | 0 |
| 196 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 151 | -1 |
| 197 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 227 | 1 |
| 198 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 248 | 1 |
| 199 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 199 | 0 |
| 200 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 199 | 0 |
| 201 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 149 | -1 |
| 202 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 203 | 1 |
| 203 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 201 | 1 |
| 204 | 9-QuestLoop | chestQuests | DEMO?action=chestQuests&deviceId=test050726 | 200 | 148 | 1 |
| 205 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 206 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 199 | 0 |
| 207 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 147 | -1 |
| 208 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 205 | 1 |
| 209 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 217 | 1 |
| 210 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 247 | 0 |
| 211 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 222 | 0 |
| 212 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 165 | -1 |
| 213 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 229 | 1 |
| 214 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 212 | 1 |
| 215 | 9-QuestLoop | chestQuests | DEMO?action=chestQuests&deviceId=test050726 | 200 | 147 | 1 |
| 216 | 9-QuestLoop | quest_rewards | QUEST?action=rewards&idQuest=0 | 200 | 201 | 0 |
| 217 | 9-QuestLoop | quest_rewardsD | QUEST?action=rewardsD&idQuest=0 | 200 | 200 | 0 |
| 218 | 9-QuestLoop | dailyReward | USER?action=dailyReward | 200 | 149 | -1 |
| 219 | 9-QuestLoop | login_items_check | USER?action=loginJustUser | 200 | 202 | 1 |
| 220 | 9-QuestLoop | login_resource_check | USER?action=loginJustUser | 200 | 257 | 1 |
| 221 | 10-Final | refresh | USER?action=loginJustUser | 200 | 208 | 1 |

---
_Generated by E2E test on 2026-07-05 17:16:39_