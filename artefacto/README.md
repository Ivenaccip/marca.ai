# Mapa visual del sistema

`index.html` es la página del mapa publicada en https://claude.ai/artifact/FtyWRkr6M2jFp4Mnu5BFDN. Se genera desde la arquitectura validada; no se edita a mano.

```bash
cd artefacto && python3 build.py ../data/arquitectura.json textos.json index.html ../data/verificacion.json
```

- `gen_page.py`: dibuja los diagramas SVG (mapa general, ciclo del cliente y orquestación). No recorta textos: si uno no cabe, su caja crece y el build lo cuenta como aviso.
- `build.py`: arma la página completa (secciones, flujos paso a paso, estilos claro y oscuro, filtros de puntos ciegos y fuentes). Al terminar imprime cuántos avisos hubo; debe dar 0.
- `textos.json`: textos de la página que no salen de la arquitectura: títulos, pies de figura, pasos del ciclo, chats de Fase 1, qué agentes están encendidos antes de abril y cuáles son reglas de n8n, y los ajustes de presentación de las verificaciones por índice (`verificaciones_extra`). Las verificaciones mismas salen de `data/verificacion.json`.

Si cambias pilares, agentes, bases o reglas en `data/arquitectura.json`, regenera `index.html` en el mismo PR y vuelve a publicar el artefacto.
