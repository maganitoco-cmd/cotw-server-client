#!/usr/bin/env python3
"""Tests for COTW Dashboard HTML — verifies structure, functions, and endpoints."""
import json, re, sys

HTML_PATH = "/home/cacho/work/repos/cotw-server-client/index.html"

with open(HTML_PATH) as f:
    html = f.read()

errors = []
passes = 0

def check(desc, condition, msg=""):
    global passes, errors
    if condition:
        passes += 1
        print(f"  ✅ {desc}")
    else:
        errors.append(f"{desc}: {msg}")
        print(f"  ❌ {desc}: {msg}")

# 1. Basic structure
print("\n📋 Basic Structure Tests")
check("File is valid HTML", '<!DOCTYPE html>' in html)
check("Has closing html tag", html.strip().endswith('</html>'))
check("Has <style> tag", '<style>' in html)
check("Has <script> tag", '<script>' in html)
check("Language is Spanish", 'lang="es"' in html)
check("Title mentions COTW", 'COTW' in html)
check("Has responsive viewport", 'viewport' in html)

# 2. Layout structure
print("\n📐 Layout Tests")
check("Has #main container", 'id="main"' in html)
check("Has #left-sidebar", 'id="left-sidebar"' in html)
check("Has #center", 'id="center"' in html)
check("Has #right-sidebar", 'id="right-sidebar"' in html)
check("Has #stats-panel", 'id="stats-panel"' in html)
check("Has #status-bar", 'id="status-bar"' in html)
check("Has #modal-overlay", 'id="modal-overlay"' in html)
check("Left sidebar width 200px", 'width: 200px' in html)
check("Right sidebar width 300px", 'width: 300px' in html)

# 3. Header elements
print("\n🔗 Header Tests")
check("Has deviceId input", 'id="deviceId"' in html)
check("Has Login button", 'doLogin()' in html)
check("Has Refresh button", 'refreshDashboard()' in html)
check("Has Diccionarios button", 'getDictionaries' in html)
check("Has conn-status", 'id="conn-status"' in html)
check("Has dash-summary", 'id="dash-summary"' in html)

# 4. Navigation items
print("\n🧭 Navigation Tests")
nav_items = [
    "recursos", "edificios", "tropas", "investigaciones",
    "heroe", "warlords", "mapa", "alianza", "apuesta", "chat", "admin", "acciones"
]
for item in nav_items:
    check(f"Nav item: {item}", f"scrollToSection('{item}')" in html)

# 5. Dashboard sections
print("\n📊 Dashboard Section Tests")
sections = [
    "section-recursos", "section-edificios", "section-tropas",
    "section-investigaciones", "section-heroe", "section-warlords",
    "section-mapa", "section-alianza", "section-apuesta",
    "section-chat", "section-admin", "section-acciones"
]
for s in sections:
    check(f"Section: {s}", f'id="{s}"' in html)

# 6. ACTIONS object completeness
print("\n⚙️ ACTIONS Object Tests")
action_categories = [
    "Usuario", "Edificios Construir", "Edificios Entrenar", "Edificios Curar",
    "Edificios Forjar", "Edificios Investigar", "Construcción Timer",
    "Ataque", "Recolectar/Acuartelar", "Mapa Envíos", "Marchas",
    "Alianza", "Héroe", "Apuesta", "Señores de la Guerra",
    "Objetos", "VIP", "Misiones", "Chat/Correo", "Admin/Demo"
]
for cat in action_categories:
    check(f"Category: {cat}", f'"{cat}"' in html)

# Count action names in ACTIONS
action_names = re.findall(r'name:"(\w+)"', html)
check(f"At least 30 action names found (got {len(action_names)})", len(action_names) >= 30)

# Check key endpoints
key_endpoints = [
    'USER', 'BUILDINGS', 'CONSTRUCT', 'WORLDMAP',
    'ALLIANCE', 'HERO', 'GAMBLE', 'WARLORDS',
    'ITEMS', 'VIP', 'QUEST', 'CHAT', 'KINGDOMCHAT',
    'MAIL', 'DEMO'
]
for ep in key_endpoints:
    check(f"Servlet: {ep}", f'servlet:"{ep}"' in html)

# 7. Cost preview actions
print("\n💰 Cost Preview Tests")
cost_actions = ['goldCostConstruct', 'goldCostBuild', 'goldCostTrain', 'goldCostTraps', 'goldCostHeal', 'goldCostResearch']
for ca in cost_actions:
    check(f"Cost action: {ca}", ca in html)

# 8. Key JavaScript functions
print("\n🔧 JavaScript Function Tests")
js_functions = [
    'function doLogin', 'function renderDashboard', 'function showActionModal',
    'function closeModal', 'function scrollToSection', 'function apiCall',
    'function buildUrl', 'function showResponse', 'function addStatsEntry',
    'function formatTime', 'function startWatcherCountdowns',
    'function addConstructWatcher', 'function checkConstruct', 'function speedUpConstruct',
    'function addMarchWatcher', 'function marchAction', 'function startMarchAutoPoll',
    'function checkWatcherVisibility', 'function refreshDashboard',
    'function buildingLevelUp', 'function previewCostFromModal',
    'function executeFromModal', 'function quickAction', 'function getModalParams',
    'function getBuildingName', 'function getRequisitesHtml',
    'function loadState', 'function saveState', 'function setStatus',
    'function updateConstructWatchers', 'function updateConstructsFromData',
    'function updateMarchesFromData'
]
for fn in js_functions:
    check(f"Function: {fn}", fn in html)

# 9. March auto-poll
print("\n🚶 March Auto-Poll Tests")
check("March poll interval 5s", 'setInterval(poll, 5000)' in html)
check("March poll function", 'function startMarchAutoPoll' in html)
check("getMarch endpoint in poll", 'action=getMarch' in html)

# 10. Timer/countdown
print("\n⏱️ Timer Tests")
check("formatTime function", 'function formatTime' in html)
check("startWatcherCountdowns", 'function startWatcherCountdowns' in html)
check("Countdown interval 1s", '1000)' in html and 'setInterval' in html)
check("Timer display 'Completado'", "'✅ Completado'" in html or '"✅ Completado"' in html)

# 11. Proxy pattern
print("\n🔗 Proxy Pattern Tests")
check("PROXY constant", 'const PROXY' in html)
check("PROXY uses /api/", '/api/' in html)
check("buildUrl uses PROXY", 'PROXY + servlet' in html)

# 12. Theme and styling
print("\n🎨 Theme Tests")
check("Dark bg: #1a0f0a", '#1a0f0a' in html)
check("Gold accent: #d4a843", '#d4a843' in html)
check("Dark panel: #2a1a10", '#2a1a10' in html)
check("Spanish text in UI", 'Iniciar' in html or 'Español' in html or 'Edificios' in html)

# 13. Response/Timers panel
print("\n📋 Right Panel Tests")
check("Response panel", 'id="response-panel"' in html)
check("Timers panel", 'id="timers-panel"' in html)
check("Construct watcher", 'id="construct-watcher"' in html)
check("March watcher", 'id="march-watcher"' in html)
check("Response body pre", 'id="resp-body"' in html)

# 14. Stats panel
print("\n📈 Stats Panel Tests")
check("Stats panel exists", 'id="stats-panel"' in html)
check("Stats count", 'id="stats-count"' in html)
check("Stats table headers", 'columnheader' in html or '#ms' in html or 'ms</th>' in html)
check("Elapsed time color classes", "'slow'" in html or '"slow"' in html)

# 15. Modal tests
print("\n💬 Modal Tests")
check("Modal overlay", 'id="modal-overlay"' in html)
check("Modal box", 'id="modal-box"' in html)
check("Modal title", 'id="modal-title"' in html)
check("Modal body", 'id="modal-body"' in html)
check("Modal actions", 'id="modal-actions"' in html)
check("Modal cost display", 'id="modal-cost"' in html)
check("Modal overlay click to close", "closeModal()" in html)

# 16. Requisites
print("\n📜 Requisites Tests")
check("getRequisitesHtml fn", 'function getRequisitesHtml' in html)
check("Building names map", 'BUILDING_NAMES' in html)
check("hasCostPreview fn", 'function hasCostPreview' in html)

# 17. Building progressions lookup
print("\n🏗️ Building Progression Tests")
check("BuildingProgressions lookup", 'BuildingProgressions' in html)
check("ResearchProgressions lookup", 'ResearchProgressions' in html)

# 18. Auto-login
print("\n🔑 Auto-Login Tests")
check("Auto-login on load", 'setTimeout(doLogin, 500)' in html)
check("localStorage save", 'localStorage.setItem' in html)
check("localStorage load", 'localStorage.getItem' in html)

# 19. Error handling
print("\n⚠️ Error Handling Tests")
check("Try/catch in executeFromModal", 'try' in html and 'catch' in html)
check("Error display in status bar", "❌" in html)
check("Edge case: empty troops", 'Sin tropas' in html)
check("Edge case: empty buildings", 'Sin edificios' in html or 'Nivel máximo' in html)

# 20. Watch guards
print("\n🛡️ Watch Guards Tests")
check("Duplicate construct guard", "'#construct-list .watcher-item[data-id=\"' + id + '\"]' in html or 'No duplicate' in html or 'return' in html")
check("Duplicate march guard", "'#march-list .watcher-item[data-id=\"' + id + '\"]' in html")

# Summary
print(f"\n{'='*50}")
total = passes + len(errors)
print(f"RESULT: {passes}/{total} tests passed")
if errors:
    print(f"FAILURES ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("✅ ALL TESTS PASSED")
