# Spec: COTW Test Client v1

## Objetivo
Cliente web tipo juego medieval para probar el 100% del API de COTW, con panel de stats que mide latencia de cada llamada.

## Alcance v1
- **Login**: deviceId input + auto-login
- **Dashboard**: recursos, tropas, hero stats
- **Acciones**: build, train, heal, research, attack, gather, scout, monster
- **Stats panel**: tabla con endpoint, elapsedTime, tamaño respuesta, timestamp
- **API base configurable**: input para cambiar URL del servidor COTW

## No en v1
- Chat, Alliance, Social (v2)
- Mapa interactivo (v2)
- DEMO/admin tools (v3)

## Diseño visual
- Tema oscuro medieval (dark wood + gold accents)
- 3 paneles:
  1. Barra lateral izquierda: acciones disponibles
  2. Área central: resultado de la acción + estado del juego
  3. Panel inferior: tabla de stats (API calls)

## Tasks
- [ ] 1. HTML skeleton: layout 3-panel con CSS medieval
- [ ] 2. API client JS: wrapper para fetch con medición de tiempo
- [ ] 3. Login flow: guardar deviceId, idUser, session
- [ ] 4. Dashboard: mostrar User data del login response
- [ ] 5. Actions panel: botones para cada endpoint con params
- [ ] 6. Stats tracker: tabla con historial de API calls
- [ ] 7. Test file: tests funcionales básicos (HTML validation, API connectivity)
