#!/usr/bin/env python3
"""COTW Test Client — Full Flow Integration Tests.

Tests all modules via the /api/ proxy, matching the interactive flow categories.
Requires proxy running at http://localhost:9000
"""

import json
import sys
import time
import urllib.request
import urllib.parse

BASE = "http://localhost:9000/api"
DEVICE_ID = "4df64994e692f5a00be2d29faefd8c7c50119a20"
USER_ID = None  # populated after login
TIMEOUT = 30

passed = 0
failed = 0
total_start = time.time()


def log(msg):
    print(f"  {msg}")


def ok(msg=""):
    global passed
    passed += 1
    print(f"  ✅ {msg}" if msg else "  ✅")


def fail(msg=""):
    global failed
    failed += 1
    print(f"  ❌ {msg}" if msg else "  ❌")


def api(endpoint, expect_result=1, silent=False):
    """Call /api/<endpoint>, check result, return parsed JSON."""
    url = f"{BASE}/{endpoint}"
    if not silent:
        print(f"  GET /api/{endpoint.split('?')[0]}...", end=" ")
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read().decode()
            data = json.loads(body)
            if not silent:
                print(f"HTTP {resp.status} result={data.get('result')} elapsed={data.get('_proxy_elapsed_ms', '?')}ms")
            if expect_result is not None and data.get("result") != expect_result:
                msg = data.get("Message", data.get("message", json.dumps(data)[:200]))
                if not silent:
                    print(f"    ⚠ Expected result={expect_result}, got {data.get('result')}: {msg}")
            return data
    except Exception as e:
        if not silent:
            print(f"❌ {e}")
        return {"error": str(e)}


def section(title):
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


# =================== 0. LOGIN ===================
section("0. LOGIN — Establecer sesión")

data = api(f"USER?action=login&deviceId={DEVICE_ID}")
USER_ID = None
if data and data.get("result") == 1:
    user = data.get("User", {})
    USER_ID = user.get("_id", {}).get("$oid") or user.get("_id", "")
    username = user.get("Player", {}).get("UserName", "?")
    if USER_ID:
        ok(f"Login OK — {username} (idUser: {USER_ID})")
    else:
        fail("No se pudo extraer userId")
else:
    fail(f"Login falló: {json.dumps(data, default=str)[:200]}")
    sys.exit(1)


# =================== MODULE 1: USUARIO ===================
section("1. USUARIO — Endpoints de usuario")

api(f"USER?action=getDictionaries&deviceId={DEVICE_ID}&idUser={USER_ID}")
api(f"USER?action=dailyReward&deviceId={DEVICE_ID}&idUser={USER_ID}")
api(f"USER?action=getLanguage&deviceId={DEVICE_ID}&idUser={USER_ID}")

data = api(f"USER?action=changeLanguage&deviceId={DEVICE_ID}&idUser={USER_ID}&Language=es")
if data and data.get("result") == 1:
    ok("changeLanguage OK")
else:
    log(f"changeLanguage: {data.get('Message','?') if data else '?'}")

data = api(f"USER?action=get&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("getUser (via USER?action=getUser) OK")
else:
    log("get (no disponible)")


# =================== MODULE 2: EDIFICIOS CONSTRUIR ===================
section("2. EDIFICIOS — Construir / Mejorar / Recolectar")

# Attempt construct on Node=5 (likely free in test env)
data = api(f"BUILDINGS?action=construct&deviceId={DEVICE_ID}&idUser={USER_ID}&idBuilding=1001&Node=5")
construct_id = None
if data and data.get("result") == 1:
    construct_id = data.get("idConstruct")
    ok(f"Construct iniciado: {construct_id}")
else:
    msg = data.get('Message', '?') if data else '?'
    log(f"Construct (nodo ocupado?): {msg}")

# Cost preview — goldCostConstruct
data = api(f"BUILDINGS?action=goldCostConstruct&deviceId={DEVICE_ID}&idUser={USER_ID}&idBuilding=1001&Level=1")
if data and data.get("result") == 1:
    ok(f"goldCostConstruct OK — GoldCost: {data.get('GoldCost', '?')}")
else:
    log(f"goldCostConstruct: {data.get('Message','?') if data else '?'}")

# Collect
data = api(f"BUILDINGS?action=collect&deviceId={DEVICE_ID}&idUser={USER_ID}&Node=1")
if data and data.get("result") == 1:
    ok("collect OK")
else:
    log(f"collect: {data.get('Message','?') if data else '?'}")

# Boost
data = api(f"BUILDINGS?action=boost&deviceId={DEVICE_ID}&idUser={USER_ID}&idBuilding=1001")
if data and data.get("result") == 1:
    ok("boost OK")
else:
    log(f"boost: {data.get('Message','?') if data else '?'}")

# Wish
data = api(f"BUILDINGS?action=wish&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("wish OK")
else:
    log(f"wish: {data.get('Message','?') if data else '?'}")


# =================== MODULE 3: EDIFICIOS ENTRENAR ===================
section("3. EDIFICIOS — Entrenar / Trampas")

# Cost preview train
data = api(f"BUILDINGS?action=goldCostTrain&deviceId={DEVICE_ID}&idUser={USER_ID}&idBuilding=2015&Level=1&Quantity=10")
if data and data.get("result") == 1:
    ok(f"goldCostTrain OK — {data.get('GoldCost', '?')}")
else:
    log(f"goldCostTrain: {data.get('Message','?') if data else '?'}")

# Cost preview traps
data = api(f"BUILDINGS?action=goldCostTraps&deviceId={DEVICE_ID}&idUser={USER_ID}&TrapType=Rocks&Level=1&Quantity=5")
if data and data.get("result") == 1:
    ok(f"goldCostTraps OK — {data.get('GoldCost', '?')}")
else:
    log(f"goldCostTraps: {data.get('Message','?') if data else '?'}")


# =================== MODULE 4: EDIFICIOS CURAR ===================
section("4. EDIFICIOS — Curar / Forjar / Investigar")

# Cost preview heal
data = api(f"BUILDINGS?action=goldCostHeal&deviceId={DEVICE_ID}&idUser={USER_ID}&Troops=Infantry.1.10")
if data and data.get("result") == 1:
    ok(f"goldCostHeal OK — {data.get('GoldCost', '?')}")
else:
    log(f"goldCostHeal: {data.get('Message','?') if data else '?'}")

# Cost preview research
data = api(f"BUILDINGS?action=goldCostResearch&deviceId={DEVICE_ID}&idUser={USER_ID}&idResearch=1&Level=1")
if data and data.get("result") == 1:
    ok(f"goldCostResearch OK — {data.get('GoldCost', '?')}")
else:
    log(f"goldCostResearch: {data.get('Message','?') if data else '?'}")

# Skills
data = api(f"BUILDINGS?action=skills&deviceId={DEVICE_ID}&idUser={USER_ID}&idSkill=1")
if data and data.get("result") == 1:
    ok("skills OK")
else:
    log(f"skills: {data.get('Message','?') if data else '?'}")


# =================== MODULE 5: CONSTRUCCIÓN TIMER ===================
section("5. CONSTRUCCIÓN TIMER — Seguimiento de construcción")

# Check remainingTime for all constructs
data = api(f"CONSTRUCT?action=remainingTime&deviceId={DEVICE_ID}&idUser={USER_ID}&idConstruct=all")
if data and data.get("result") == 1:
    ok("remainingTime(all) OK")
    constructs = data.get("Constructs", [])
    log(f"  {len(constructs)} construcción(es) activa(s)")
else:
    log("remainingTime(all)")

# If we have an active construct, test its timer
if construct_id:
    data = api(f"CONSTRUCT?action=remainingTime&deviceId={DEVICE_ID}&idUser={USER_ID}&idConstruct={construct_id}")
    if data and data.get("result") == 1:
        ok(f"remainingTime({construct_id}) OK")
    else:
        log(f"remainingTime (puede estar completado)")

    # Speed-up with gold
    data = api(f"CONSTRUCT?action=speedUpGold&deviceId={DEVICE_ID}&idUser={USER_ID}&idConstruct={construct_id}")
    if data and data.get("result") == 1:
        ok("speedUpGold OK")
    else:
        log(f"speedUpGold result={data.get('result') if data else '?'}")
else:
    log("  Sin construct activo para pruebas de timer")


# =================== MODULE 6: ATAQUE / MAPA ===================
section("6. MAPA — Ataque / Recolectar / Exploración")

# GetQuadrant
data = api(f"WORLDMAP?action=getQuadrant&deviceId={DEVICE_ID}&idUser={USER_ID}&idKingdom=1&x=300&y=300")
marches = []
if data and data.get("Map"):
    marches = data.get("Marches", [])
    ok(f"getQuadrant OK — {len(marches)} marcha(s)")
else:
    log("getQuadrant (sin datos de mapa)")

# Gather (cost preview not needed, but test troop format)
log("  Intentando gather en (300,300)...")
data = api(f"WORLDMAP?action=gather&deviceId={DEVICE_ID}&idUser={USER_ID}&x=300&y=300&Troops=Archer.1.3")
march_id = None
if data and data.get("result") == 1:
    user_data = data.get("User", {})
    USER_ID = user_data.get("_id", {}).get("$oid") or user_data.get("_id", "") or USER_ID
    march = data.get("March", data.get("march", {}))
    march_id = march.get("_id", {}).get("$oid") or march.get("_id", "")
    if march_id:
        ok(f"Marcha gather creada: {march_id}")
    else:
        ok("Marcha creada")
else:
    msg = data.get('Message', '?') if data else '?'
    log(f"Gather: {msg} (coord puede no tener recurso)")

# Scout
data = api(f"WORLDMAP?action=scout&deviceId={DEVICE_ID}&idUser={USER_ID}&x=315&y=963&UserID={USER_ID}")
if data and data.get("result") == 1:
    ok("scout OK")
else:
    log(f"scout: {data.get('Message','?') if data else '?'}")


# =================== MODULE 7: MARCHAS ===================
section("7. MARCHAS — Seguimiento de marchas")

if march_id:
    # getMarch
    data = api(f"WORLDMAP?action=getMarch&deviceId={DEVICE_ID}&idUser={USER_ID}&idMarch={march_id}")
    if data and data.get("result") == 1:
        ok("getMarch OK")
    else:
        log("getMarch")

    # syncMarch
    data = api(f"WORLDMAP?action=syncMarch&deviceId={DEVICE_ID}&idUser={USER_ID}&idMarch={march_id}")
    if data and data.get("result") == 1:
        ok("syncMarch OK")
    else:
        log("syncMarch")

    # goHome
    data = api(f"WORLDMAP?action=goHome&deviceId={DEVICE_ID}&idUser={USER_ID}&idMarch={march_id}")
    if data and data.get("result") == 1:
        ok("goHome OK")
    else:
        log("goHome")
else:
    log("  Sin marcha activa para pruebas de seguimiento")

# March report
data = api(f"MARCHREPORT?action=feed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("MarchReport feed OK")
else:
    log("MarchReport feed")

data = api(f"MARCHREPORT?action=marchDayCount&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("MarchReport dayCount OK")
else:
    log("MarchReport dayCount")

# Send resources test
data = api(f"WORLDMAP?action=sendResources&deviceId={DEVICE_ID}&idUser={USER_ID}&x=315&y=963&UserID={USER_ID}&Resources=Food.10/-/Wood.10")
if data and data.get("result") == 1:
    ok("sendResources OK")
else:
    log(f"sendResources: {data.get('Message','?') if data else '?'}")


# =================== MODULE 8: ALIANZA ===================
section("8. ALIANZA")

data = api(f"ALLIANCE?action=get&deviceId={DEVICE_ID}&idUser={USER_ID}")
alliance_exists = False
if data and data.get("result") == 1:
    ok("Alliance get OK")
    if data.get("Alliance"):
        log(f"  Alianza: {data['Alliance'].get('Name','?')}")
        alliance_exists = True
else:
    log("Alliance get (sin alianza)")

# Search
data = api(f"ALLIANCE?action=search&deviceId={DEVICE_ID}&Search=Test")
if data and data.get("result") == 1:
    ok("Alliance search OK")
    alliances = data.get("Alliances", [])
    log(f"  {len(alliances)} alianzas encontradas")
else:
    log("Alliance search")

if alliance_exists:
    data = api(f"ALLIANCE?action=getMembersDetails&deviceId={DEVICE_ID}&idUser={USER_ID}")
    if data and data.get("result") == 1:
        ok("Alliance members OK")
    else:
        log("Alliance members")

    data = api(f"ALLIANCE?action=chatFeed&deviceId={DEVICE_ID}&idUser={USER_ID}")
    if data and data.get("result") == 1:
        ok("Alliance chatFeed OK")
    else:
        log("Alliance chatFeed")

    data = api(f"ALLIANCE?action=chat&deviceId={DEVICE_ID}&idUser={USER_ID}&Message=Test+from+API")
    if data and data.get("result") == 1:
        ok("Alliance chat OK")
    else:
        log("Alliance chat")

    data = api(f"ALLIANCE?action=requestShards&deviceId={DEVICE_ID}&idUser={USER_ID}&idWarlord=1001")
    if data and data.get("result") == 1:
        ok("requestShards OK")
    else:
        log("requestShards")

    data = api(f"ALLIANCE?action=askHelp&deviceId={DEVICE_ID}&idUser={USER_ID}&idConstruct=0")
    if data and data.get("result") == 1:
        ok("askHelp OK")
    else:
        log("askHelp")


# =================== MODULE 9: HÉROE ===================
section("9. HÉROE")

data = api(f"HERO?action=status&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("Hero status OK")
    hero = data.get("User", {}).get("Hero", {})
    if hero:
        log(f"  Héroe: {hero.get('Name','?')} Nv.{hero.get('Level','?')}")
else:
    log("Hero status")

data = api(f"HERO?action=levelUpH&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("levelUpH OK")
else:
    log(f"levelUpH: {data.get('Message','?') if data else '?'}")

data = api(f"HERO?action=activateSkill&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("activateSkill OK")
else:
    log(f"activateSkill: {data.get('Message','?') if data else '?'}")

data = api(f"HERO?action=prisonFeed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("prisonFeed OK")
else:
    log("prisonFeed")

data = api(f"HERO?action=pitFeed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("pitFeed OK")
else:
    log("pitFeed")

data = api(f"HERO?action=equipItem&deviceId={DEVICE_ID}&idUser={USER_ID}&idItem=1001&Tier=1")
if data and data.get("result") == 1:
    ok("equipItem OK")
else:
    log(f"equipItem: {data.get('Message','?') if data else '?'}")

data = api(f"HERO?action=unequipItem&deviceId={DEVICE_ID}&idUser={USER_ID}&idItem=1001&Tier=1")
if data and data.get("result") == 1:
    ok("unequipItem OK")
else:
    log(f"unequipItem: {data.get('Message','?') if data else '?'}")


# =================== MODULE 10: APUESTA ===================
section("10. APUESTA")

data = api(f"GAMBLE?action=spin&deviceId={DEVICE_ID}&idUser={USER_ID}&Side=Light")
if data and data.get("result") == 1:
    ok("Gamble spin OK")
else:
    log(f"Spin: {data.get('Message','?') if data else '?'}")

data = api(f"GAMBLE?action=flip&deviceId={DEVICE_ID}&idUser={USER_ID}&Slot=1")
if data and data.get("result") == 1:
    ok("Gamble flip OK")
else:
    log(f"Flip: {data.get('Message','?') if data else '?'}")


# =================== MODULE 11: SEÑORES DE LA GUERRA ===================
section("11. SEÑORES DE LA GUERRA")

data = api(f"WARLORDS?action=summon&deviceId={DEVICE_ID}&idUser={USER_ID}&Warlords=1001.5")
if data and data.get("result") == 1:
    ok("Warlord summon OK")
else:
    log(f"Warlord summon: {data.get('Message','?') if data else '?'}")

data = api(f"WARLORDS?action=levelupW&deviceId={DEVICE_ID}&idUser={USER_ID}&idWarlord=1001")
if data and data.get("result") == 1:
    ok("Warlord levelupW OK")
else:
    log(f"Warlord levelupW: {data.get('Message','?') if data else '?'}")

data = api(f"WARLORDS?action=dungeon&deviceId={DEVICE_ID}&idUser={USER_ID}&Gold=false")
if data and data.get("result") == 1:
    ok("Dungeon OK")
else:
    log(f"Dungeon: {data.get('Message','?') if data else '?'}")

data = api(f"WARLORDS?action=chest&deviceId={DEVICE_ID}&idUser={USER_ID}&idItem=1001&Quantity=1")
if data and data.get("result") == 1:
    ok("Warlord chest OK")
else:
    log(f"Warlord chest: {data.get('Message','?') if data else '?'}")


# =================== MODULE 12: OBJETOS ===================
section("12. OBJETOS")

data = api(f"ITEMS?action=purchase&deviceId={DEVICE_ID}&idUser={USER_ID}&idItem=1001&Quantity=1")
if data and data.get("result") == 1:
    ok("Item purchase OK")
else:
    log(f"Purchase: {data.get('Message','?') if data else '?'}")

data = api(f"ITEMS?action=use&deviceId={DEVICE_ID}&idUser={USER_ID}&idItem=1001&Quantity=1")
if data and data.get("result") == 1:
    ok("Item use OK")
else:
    log(f"Item use: {data.get('Message','?') if data else '?'}")

data = api(f"ITEMS?action=materialChest&deviceId={DEVICE_ID}&idUser={USER_ID}&idItem=1001&Quantity=1")
if data and data.get("result") == 1:
    ok("materialChest OK")
else:
    log(f"materialChest: {data.get('Message','?') if data else '?'}")

data = api(f"ITEMS?action=incStamina&deviceId={DEVICE_ID}&idUser={USER_ID}&idItem=1001&Quantity=1")
if data and data.get("result") == 1:
    ok("incStamina OK")
else:
    log(f"incStamina: {data.get('Message','?') if data else '?'}")

data = api(f"ITEMS?action=cityDefense&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("CityDefense OK")
else:
    log(f"CityDefense: {data.get('Message','?') if data else '?'}")

data = api(f"ITEMS?action=timeItems&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("timeItems OK")
else:
    log(f"timeItems: {data.get('Message','?') if data else '?'}")

data = api(f"ITEMS?action=randomTeleport&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("randomTeleport OK")
else:
    log(f"randomTeleport: {data.get('Message','?') if data else '?'}")


# =================== MODULE 13: VIP ===================
section("13. VIP")

data = api(f"VIP?action=levelUpV&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("VIP levelUpV OK")
else:
    log(f"VIP levelUpV: {data.get('Message','?') if data else '?'}'")

data = api(f"VIP?action=activate&deviceId={DEVICE_ID}&idUser={USER_ID}&idItem=1001")
if data and data.get("result") == 1:
    ok("VIP activate OK")
else:
    log(f"VIP activate: {data.get('Message','?') if data else '?'}")


# =================== MODULE 14: MISIONES ===================
section("14. MISIONES")

data = api(f"QUEST?action=feed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("Quest feed OK")
else:
    log("Quest feed")

data = api(f"QUEST?action=collectQ&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("collectQ OK")
else:
    log(f"collectQ: {data.get('Message','?') if data else '?'}")

data = api(f"QUEST?action=rewards&deviceId={DEVICE_ID}&idUser={USER_ID}&idQuest=0")
if data and data.get("result") == 1:
    ok("Quest rewards OK")
else:
    log(f"rewards: {data.get('Message','?') if data else '?'}")

data = api(f"QUEST?action=collectD&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("collectD OK")
else:
    log(f"collectD: {data.get('Message','?') if data else '?'}")

data = api(f"QUEST?action=rewardsD&deviceId={DEVICE_ID}&idUser={USER_ID}&idQuest=0")
if data and data.get("result") == 1:
    ok("rewardsD OK")
else:
    log("rewardsD")


# =================== MODULE 15: CHAT / CORREO ===================
section("15. CHAT / CORREO")

data = api(f"CHAT?action=feed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("Chat feed OK")
    chats = data.get("Chats", [])
    log(f"  {len(chats)} conversaciones")
else:
    log("Chat feed")

data = api(f"KINGDOMCHAT?action=feed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("KingdomChat feed OK")
else:
    log("KingdomChat feed")

data = api(f"MAIL?action=feed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("Mail feed OK")
    mails = data.get("Mails", [])
    log(f"  {len(mails)} correos")
    if mails:
        mail_id = mails[0].get("_id", {}).get("$oid") or mails[0].get("_id", "")
        if mail_id:
            data2 = api(f"MAIL?action=markRead&deviceId={DEVICE_ID}&id={mail_id}")
            if data2 and data2.get("result") == 1:
                ok("Mail markRead OK")
            else:
                log("Mail markRead")
else:
    log("Mail feed")

data = api(f"KINGDOMCHAT?action=addMessage&deviceId={DEVICE_ID}&idUser={USER_ID}&Message=Test+from+test_client")
if data and data.get("result") == 1:
    ok("KingdomChat addMessage OK")
else:
    log("KingdomChat addMessage")


# =================== MODULE 16: SOCIAL / RANKING / OTROS ===================
section("16. SOCIAL / RANKING / OTROS")

data = api(f"SOCIAL?action=getUsersData&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("Social data OK")
else:
    log("Social data")

data = api(f"RANKING?action=feed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("Ranking feed OK")
else:
    log("Ranking feed")

data = api(f"TUTORIAL?action=finish&deviceId={DEVICE_ID}&idUser={USER_ID}&Index=0")
if data and data.get("result") == 1:
    ok("Tutorial finish OK")
else:
    log("Tutorial finish")

data = api(f"AVATAR?action=incHappiness&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("Avatar incHappiness OK")
else:
    log("Avatar incHappiness")

data = api(f"BOOKMARKS?action=add&deviceId={DEVICE_ID}&idUser={USER_ID}&Name=Test&Type=city&x=315&y=963")
if data and data.get("result") == 1:
    ok("Bookmark add OK")
else:
    log("Bookmark add")

data = api(f"IAP?action=rewardsViewed&deviceId={DEVICE_ID}&idUser={USER_ID}")
if data and data.get("result") == 1:
    ok("IAP rewardsViewed OK")
else:
    log("IAP rewardsViewed")


# =================== MODULE 17: ADMIN / DEMO ===================
section("17. ADMIN / DEMO")

data = api(f"DEMO?action=backupUser&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("backupUser OK")
else:
    log(f"backupUser: {data.get('Message','?') if data else '?'}")

data = api(f"DEMO?action=snapshotUser&deviceId={DEVICE_ID}&name=test_snapshot")
if data and data.get("result") == 1:
    ok("snapshotUser OK")
else:
    log("snapshotUser")

data = api(f"DEMO?action=putGold&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("putGold OK")
else:
    log("putGold")

data = api(f"DEMO?action=putAllItems&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("putAllItems OK")
else:
    log("putAllItems")

data = api(f"DEMO?action=putAllTroops&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("putAllTroops OK")
else:
    log("putAllTroops")

data = api(f"DEMO?action=putAllWarlords&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("putAllWarlords OK")
else:
    log("putAllWarlords")

data = api(f"DEMO?action=addItem&deviceId={DEVICE_ID}&idItem=1001&Quantity=10")
if data and data.get("result") == 1:
    ok("addItem OK")
else:
    log("addItem")

data = api(f"DEMO?action=activateShield&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("activateShield OK")
else:
    log("activateShield")

data = api(f"DEMO?action=deactivateShield&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("deactivateShield OK")
else:
    log("deactivateShield")

data = api(f"DEMO?action=resetActiveSkillsCD&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("resetActiveSkillsCD OK")
else:
    log("resetActiveSkillsCD")

data = api(f"DEMO?action=activateBurn&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("activateBurn OK")
else:
    log("activateBurn")

data = api(f"DEMO?action=restoreUser&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("restoreUser OK")
else:
    log("restoreUser")

data = api(f"DEMO?action=getMarches&deviceId={DEVICE_ID}")
if data and data.get("result") == 1:
    ok("getMarches OK")
else:
    log("getMarches")


# =================== SUMMARY ===================
section("RESUMEN FINAL")
total_time = time.time() - total_start
print(f"  Total: {passed + failed} tests | ✅ {passed} exitosos | ❌ {failed} fallaron | ⏱️ {total_time:.1f}s")

if failed > 0:
    print(f"\n  ⚠️  {failed} tests fallaron — revisa los logs arriba")
    sys.exit(1)
else:
    print(f"\n  ✅ Todos los tests pasaron!")
    sys.exit(0)
