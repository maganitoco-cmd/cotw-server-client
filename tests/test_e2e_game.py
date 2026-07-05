#!/usr/bin/env python3
"""
COTW End-to-End Game Progression Test
DeviceID: test050726 (user fresco)

NO DEMO ACTIONS — only recursos naturales del juego.
Proxy: localhost:9000/api/ → COTW server

Flujo:
  PHASE 1: Crear usuario (reset + loginJustUser)
  PHASE 2: Construir infraestructura
  PHASE 3: Mejorar Townhall
  PHASE 4: Entrenar tropas
  PHASE 5: Investigar
  PHASE 6: Héroe
  PHASE 7: Mapa mundial (usando coordenadas del usuario)
  PHASE 8: Estado final
"""
import urllib.request
import json
import time
import sys

BASE = "http://localhost:9000/api"
DEVICE_ID = "test050726"
ID_USER = None
USER_COORDS = [695, 649]  # populated from login

# ── Helpers ──────────────────────────────────────────────────────────

def api(endpoint, silent=False):
    """Call COTW API. Returns parsed JSON dict or None on network error.
    Automatically injects deviceId and idUser if not present.
    Always logs result=-1 messages at info level (not silent).
    """
    global ID_USER, USER_COORDS
    url = f"{BASE}/{endpoint}"
    if "deviceId=" not in url:
        sep = "&" if "?" in url else "?"
        url += f"{sep}deviceId={DEVICE_ID}"
    if ID_USER and "idUser=" not in url:
        url += f"&idUser={ID_USER}"

    for attempt in range(2):
        try:
            start = time.time()
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = json.loads(resp.read().decode())
            elapsed = int((time.time() - start) * 1000)
        except Exception as e:
            if not silent:
                print(f"  🌐 NETWORK ERROR (attempt {attempt+1}): {e}")
            time.sleep(1)
            continue

        result = data.get("result")

        # Always show result=-1 since these are informative
        if result == -1:
            msg = (data.get("Message") or data.get("message") or "Unknown error")[:300]
            print(f"  ❌ result=-1: {msg}")
            # Still return data so caller can inspect
        elif result == 0:
            msg = (data.get("Message") or data.get("message") or "")[:150]
            if not silent:
                print(f"  ⚠️  result=0: {msg}")
        elif not silent:
            size = len(json.dumps(data, default=str))
            print(f"  ✅ HTTP 200 | result={result} | {elapsed}ms | {size}B")

        # Auto-extract ID_USER from User._id
        u = data.get("User")
        if u and u.get("_id"):
            uid = u["_id"]
            ID_USER = uid.get("$oid", uid) if isinstance(uid, dict) else uid

        # Auto-extract coordinates
        p = data.get("User", {}).get("Player", {})
        coords = p.get("Coordinates")
        if coords:
            USER_COORDS = coords

        return data

    return None


def node_of(data, id_building):
    """Find building node by idBuilding in User.Buildings list."""
    if not data:
        return None
    for b in (data.get("User", {}) or {}).get("Buildings", []):
        if b.get("idBuilding") == id_building:
            return b.get("Node")
    return None


def level_of(data, id_building):
    """Find building level by idBuilding."""
    if not data:
        return 0
    for b in (data.get("User", {}) or {}).get("Buildings", []):
        if b.get("idBuilding") == id_building:
            return b.get("Level", 0)
    return 0


def has_building(data, id_building):
    """Check if building exists."""
    if not data:
        return False
    return any(
        b.get("idBuilding") == id_building
        for b in (data.get("User", {}) or {}).get("Buildings", [])
    )


def collect_all(data):
    """Attempt to collect from all existing building nodes."""
    if not data:
        return
    blds = (data.get("User", {}) or {}).get("Buildings", [])
    for b in blds:
        node = b.get("Node")
        if node:
            r = api(f"BUILDINGS?action=collect&Node={node}", silent=True)
            if r and r.get("result") == 1:
                resources = r.get("Resources", {})
                gold = resources.get("Gold", {}) if isinstance(resources, dict) else {}
                gold_qty = gold.get("Quantity", "?")
                print(f"    Recolectado Node={node} | gold={gold_qty}")


def try_complete_construct(cid, label=""):
    """Try to check construct status via remainingTime.
    Returns True if construct seems done (RemainingTime <= 1).
    """
    if not cid:
        return False
    time.sleep(1)
    r = api(f"CONSTRUCT?action=remainingTime&idConstruct={cid}", silent=True)
    if r and r.get("result") == 1:
        remaining = r.get("RemainingTime", 999)
        status = r.get("Status", r.get("status", ""))
        print(f"    {label}: remainingTime={remaining}s status={status}")
        # If remaining is small or status indicates done
        if isinstance(remaining, (int, float)):
            if remaining <= 1:
                return True
            # Try speedUpGold if we have resources and remaining is reasonable
            if remaining > 1:
                speed_r = api(f"CONSTRUCT?action=speedUpGold&idConstruct={cid}", silent=True)
                if speed_r and speed_r.get("result") == 1:
                    print(f"    {label}: speedUpGold OK")
                    return True
                else:
                    msg = speed_r.get("Message", "?")[:100] if speed_r else "?"
                    if "RESOURCES" not in msg:
                        print(f"    {label}: speedUpGold skipped ({msg})")
    elif r and r.get("result") == -1:
        msg = r.get("Message", "?")[:200]
        print(f"    {label}: remainingTime error: {msg}")
    return False


def refresh():
    """Re-login and return data."""
    data = api("USER?action=loginJustUser", silent=True)
    return data


def section(n, title):
    print(f"\n{'=' * 60}")
    print(f"PHASE {n}: {title}")
    print(f"{'=' * 60}")


# ── Main test flow ───────────────────────────────────────────────────

section(1, "Crear usuario (reset + login)")

data = api("USER?action=reset")
if data is None:
    print("FATAL: No se pudo conectar al servidor (reset)")
    sys.exit(1)
if data.get("result") == 1:
    u = data.get("User", {})
    uid = u.get("_id", {})
    ID_USER = uid.get("$oid", uid) if isinstance(uid, dict) else uid
    print(f"  Usuario creado: {ID_USER}")
else:
    msg = data.get("Message", "?")[:200]
    print(f"  reset result={data.get('result')}: {msg}")
    # Podría existir ya, seguimos

data = refresh()
if data is None or data.get("result") != 1:
    print("FATAL: No se pudo hacer login")
    sys.exit(1)

user = data.get("User", {})
player = user.get("Player", {})
coords = player.get("Coordinates", "?")
print(f"  Username: {player.get('UserName', '?')}")
print(f"  Coordenadas: {coords}")
blds = user.get("Buildings", [])
print(f"  Buildings: {len(blds)}")
for b in blds:
    print(f"    - idBuilding={b.get('idBuilding')} Lvl={b.get('Level')} Node={b.get('Node')}")

th_node = node_of(data, 1001)
print(f"  Townhall Node={th_node} Lvl={level_of(data, 1001)}")

# ─────────────────────────────────────────────────────────────────────
section(2, "Construir infraestructura (recursos naturales)")

# Collect initial resources
collect_all(data)

# Build needed infrastructure (skip if already exists)
# idBuilding -> (primary_node, alt_node, name)
build_plan = [
    (1002, 1, 2, "Wall"),           # Usually node 2
    (2002, 4, 14, "Academy"),
    (2003, 5, 15, "Hospital"),
    (2007, 6, 16, "Forge"),
    (2006, 9, 19, "Embassy"),
    (2008, 7, 17, "Pit"),
    (2009, 18, 20, "Wishing Well"),
]

data = refresh()
existing_ids = set()
if data:
    existing_ids = {b.get("idBuilding") for b in (data.get("User", {}) or {}).get("Buildings", [])}
print(f"  Ya existen: {sorted(existing_ids)}")

for bid, node1, node2, name in build_plan:
    if bid in existing_ids:
        print(f"  {name} (id={bid}) ya existe")
        continue

    for node_attempt in [node1, node2]:
        print(f"\n  Construyendo {name} (id={bid}) node={node_attempt}...")
        r = api(f"BUILDINGS?action=construct&idBuilding={bid}&Node={node_attempt}", silent=True)
        if r is None:
            continue
        if r.get("result") == 1:
            cid = r.get("idConstruct")
            print(f"    ✅ Construct iniciado: {cid}")
            if cid:
                try_complete_construct(cid, name)
            break
        elif r.get("result") == -1:
            msg = r.get("Message", "?")[:200]
            if "Busy" in msg:
                print(f"    Node busy, probando otro...")
                continue
            print(f"    No se pudo: {msg}")
            break

# Collect again after any completes
time.sleep(1)
data = refresh()
collect_all(data)

# ─────────────────────────────────────────────────────────────────────
section(3, "Mejorar Townhall")

data = refresh()
th_node = node_of(data, 1001)
th_lvl = level_of(data, 1001)
print(f"  Townhall Node={th_node} Lvl={th_lvl}")

if th_node:
    for i in range(3):
        r = api(f"BUILDINGS?action=levelUpB&Node={th_node}", silent=True)
        if r and r.get("result") == 1:
            cid = r.get("idConstruct")
            if cid:
                print(f"  ✅ Townhall mejorado (intento {i+1}) construct={cid}")
                try_complete_construct(cid, f"TH Lvl up")
                data = refresh()
                th_lvl = level_of(data, 1001)
                print(f"  Townhall ahora Lvl={th_lvl}")
        else:
            msg = r.get("Message", "?")[:200] if r else "no response"
            print(f"  No se pudo mejorar más: {msg}")
            break
        time.sleep(0.5)
else:
    print("  ERROR: No se encontró Townhall en buildings")

# ─────────────────────────────────────────────────────────────────────
section(4, "Entrenar tropas (recursos naturales)")

data = refresh()
bld_list = []
if data:
    bld_list = (data.get("User", {}) or {}).get("Buildings", [])
existing_ids = {b.get("idBuilding") for b in bld_list}
print(f"  Edificios disponibles: {sorted(existing_ids)}")

# Training buildings to construct if missing
training_builds = [
    (2014, 10, "Barracks (Infantry)"),
    (2012, 12, "Archer Range"),
    (2013, 11, "Stable (Cavalry)"),
    (2015, 13, "Siege Workshop"),
]

for tbid, tnode, tname in training_builds:
    if tbid not in existing_ids:
        print(f"\n  Construyendo {tname} (id={tbid})...")
        r = api(f"BUILDINGS?action=construct&idBuilding={tbid}&Node={tnode}", silent=True)
        if r and r.get("result") == 1:
            cid = r.get("idConstruct")
            print(f"    ✅ Construido: {cid}")
            if cid:
                try_complete_construct(cid, tname)
        elif r and r.get("result") == -1:
            msg = r.get("Message", "?")[:200]
            print(f"    No construido: {msg}")

# Now train troops (small qty since natural resources)
train_plan = [
    (2014, "Infantry", 1, 5),
    (2012, "Archer", 1, 3),
    (2013, "Cavalry", 1, 2),
    (2015, "Siege", 1, 1),
]

for tbl_id, ttype, lvl, qty in train_plan:
    print(f"\n  Entrenando {ttype} Lvl.{lvl} x{qty}...")
    r = api(f"BUILDINGS?action=train&idBuilding={tbl_id}&Level={lvl}&Quantity={qty}", silent=True)
    if r and r.get("result") == 1:
        cid = r.get("idConstruct")
        if cid:
            print(f"    ✅ Entrenamiento iniciado: {cid}")
            try_complete_construct(cid, f"{ttype}")
    elif r and r.get("result") == -1:
        msg = r.get("Message", "?")[:200]
        print(f"    No entrenado: {msg}")

# ─────────────────────────────────────────────────────────────────────
section(5, "Investigar (recursos naturales)")

data = refresh()
print(f"  Academy exists: {has_building(data, 2002)}")

for rid in [1, 2, 3, 4, 5]:
    print(f"\n  Investigando tech id={rid}...")
    r = api(f"BUILDINGS?action=research&idResearch={rid}", silent=True)
    if r and r.get("result") == 1:
        cid = r.get("idConstruct")
        if cid:
            print(f"    ✅ Investigación iniciada: {cid}")
            try_complete_construct(cid, f"Research {rid}")
    elif r and r.get("result") == -1:
        msg = r.get("Message", "?")[:250]
        print(f"    No investigado: {msg}")
        if "requirements" in msg.lower() or "Config" in msg:
            print(f"    (saltando más invest. — requisitos no cumplidos)")
            break

# ─────────────────────────────────────────────────────────────────────
section(6, "Héroe")

# Status
r = api("HERO?action=status")
if r and r.get("result") == 1:
    u = r.get("User", {}) or {}
    hero = u.get("Hero", {}) or {}
    hid = hero.get("idHero", hero.get("_id", "?"))
    hlvl = hero.get("Level", "?")
    hexp = hero.get("Exp", hero.get("Experience", "?"))
    print(f"  Héroe: {hid} Level={hlvl} Exp={hexp}")

    # Level up
    r2 = api("HERO?action=levelUpH", silent=True)
    if r2 and r2.get("result") == 1:
        print(f"  ✅ Hero levelUpH OK")
    elif r2 and r2.get("result") == -1:
        msg = r2.get("Message", "?")[:200]
        print(f"  levelUpH: {msg}")

    # Activate skill
    r3 = api("HERO?action=activateSkill", silent=True)
    if r3 and r3.get("result") == 1:
        print(f"  ✅ activateSkill OK")
    elif r3 and r3.get("result") == -1:
        msg = r3.get("Message", "?")[:200]
        print(f"  activateSkill: {msg}")
else:
    msg = r.get("Message", "?")[:200] if r else "no response"
    print(f"  Hero status: {msg}")

# Prison feed
r = api("HERO?action=prisonFeed", silent=True)
if r and r.get("result") == 1:
    print(f"  ✅ prisonFeed OK")
elif r and r.get("result") == -1:
    print(f"  prisonFeed: {r.get('Message','?')[:150]}")

# Pit feed
r = api("HERO?action=pitFeed", silent=True)
if r and r.get("result") == 1:
    print(f"  ✅ pitFeed OK")
elif r and r.get("result") == -1:
    print(f"  pitFeed: {r.get('Message','?')[:150]}")

# ─────────────────────────────────────────────────────────────────────
section(7, "Mapa mundial")

# Use coordinates relative to user's position
cx, cy = USER_COORDS
print(f"  Usuario en [{cx}, {cy}]")

# GetQuadrant around user
qx = max(100, cx - 50)
qy = max(100, cy - 50)
print(f"  Query Quadrant ({qx},{qy})...")
r = api(f"WORLDMAP?action=getQuadrant&idKingdom=1&x={qx}&y={qy}", silent=True)
if r and r.get("result") == 1:
    marches = r.get("Marches", [])
    print(f"  Quadrant: {len(marches)} marchas visibles")
elif r and r.get("result") == -1:
    print(f"  Quadrant: {r.get('Message','?')[:200]}")

# Scout near user (+10 offset)
scout_coords = [
    (cx + 10, cy + 10),
    (cx + 20, cy + 20),
    (max(1, cx - 5), max(1, cy - 5)),
]
for sx, sy in scout_coords:
    r = api(f"WORLDMAP?action=scout&x={sx}&y={sy}", silent=True)
    if r and r.get("result") == 1:
        print(f"  ✅ Scout ({sx},{sy}) OK")
        break
    elif r and r.get("result") == -1:
        msg = r.get("Message", "?")[:150]
        print(f"  Scout ({sx},{sy}): {msg}")

# Gather near user
gather_coords = [
    (cx + 5, cy + 5),
    (cx + 15, cy + 15),
    (max(1, cx - 10), max(1, cy - 10)),
]
for gx, gy in gather_coords:
    r = api(f"WORLDMAP?action=gather&x={gx}&y={gy}&Troops=Infantry.1.1", silent=True)
    if r and r.get("result") == 1:
        march = r.get("March", r.get("march", {}))
        mid = march.get("_id", {}) or march.get("_id", "")
        if isinstance(mid, dict):
            mid = mid.get("$oid", "")
        print(f"  ✅ Gather ({gx},{gy}) march={mid}")
        if mid:
            api(f"WORLDMAP?action=syncMarch&idMarch={mid}", silent=True)
            api(f"WORLDMAP?action=goHome&idMarch={mid}", silent=True)
            print(f"    Marcha sincronizada y regresada")
        break
    elif r and r.get("result") == -1:
        msg = r.get("Message", "?")[:150]
        print(f"  Gather ({gx},{gy}): {msg}")
        if "Troops" in msg or "RESOURCES" in msg:
            print(f"    (sin tropas disponibles para gather)")
            break

# Monster attack
mx, my = max(1, cx - 3), max(1, cy - 3)
r = api(f"WORLDMAP?action=monster&x={mx}&y={my}&Troops=Infantry.1.1", silent=True)
if r and r.get("result") == 1:
    print(f"  ✅ Monster ({mx},{my}) OK")
elif r and r.get("result") == -1:
    print(f"  Monster: {r.get('Message','?')[:200]}")

# ─────────────────────────────────────────────────────────────────────
section(8, "Estado final")

print("  Refresh final...")
data = refresh()

if data and data.get("result") == 1:
    user = data.get("User", {})
    player = user.get("Player", {})
    buildings = user.get("Buildings", [])
    troops_container = user.get("Troops", {})
    hero = user.get("Hero", {})

    print(f"\n  ┌── INFORME FINAL ──────────────────────")
    print(f"  │ Username:  {player.get('UserName', '?')}")
    print(f"  │ ID:        {ID_USER}")
    print(f"  │ Coords:    {player.get('Coordinates', '?')}")
    print(f"  │ Edificios: {len(buildings)} construidos")
    hid = hero.get("idHero", hero.get("_id", hero.get("Name", "?")))
    print(f"  │ Héroe:     {hid} Level={hero.get('Level', '?')}")
    print(f"  │")

    print(f"  ├── EDIFICIOS ────────────────────────")
    for b in buildings:
        n = b.get("Node", "?")
        l = b.get("Level", "?")
        bid = b.get("idBuilding", "?")
        print(f"  │   Node {n:>2}: idBuilding={bid} Lvl={l}")

    print(f"  ├── TROPAS ───────────────────────────")
    troop_total = 0
    for ttype in ["Infantry", "Archer", "Cavalry", "Siege"]:
        td = troops_container.get(ttype, {})
        for tl in td.get("Troops", []):
            active = tl.get("Active", 0)
            if active > 0:
                print(f"  │   {ttype:>10} Lvl{tl.get('Level')}: {active} activas")
                troop_total += active
    if troop_total == 0:
        print(f"  │   (sin tropas — requiere tiempo o speedUp con recursos)")

    print(f"  ├── ITEMS / RECURSOS ─────────────────")
    gold = user.get("Gold", {})
    if isinstance(gold, dict):
        print(f"  │   Gold: {gold.get('Quantity', 0)}")
    food = user.get("Food", {})
    if isinstance(food, dict):
        print(f"  │   Food: {food.get('Quantity', 0)}")
    wood = user.get("Wood", {})
    if isinstance(wood, dict):
        print(f"  │   Wood: {wood.get('Quantity', 0)}")
    stone = user.get("Stone", {})
    if isinstance(stone, dict):
        print(f"  │   Stone: {stone.get('Quantity', 0)}")

    print(f"  └──────────────────────────────────────")
    print(f"\n  🎮 E2E TEST COMPLETE — {len(buildings)} edificios, {troop_total} tropas, Hero Lvl{hero.get('Level', '?')}")
else:
    print(f"  ❌ No se pudo obtener estado final")
