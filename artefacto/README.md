# Mapa visual del sistema

`index.html` es la página del mapa publicada en https://claude.ai/artifact/FtyWRkr6M2jFp4Mnu5BFDN. Se genera desde la arquitectura validada; no se edita a mano.

```bash
cd artefacto && python3 build.py ../data/arquitectura.json textos.json index.html ../data/verificacion.json
```

- `gen_page.py`: dibuja los diagramas SVG (mapa general, ciclo del cliente y orquestación).
- `build.py`: arma la página completa (secciones, estilos claro y oscuro, filtros de puntos ciegos).
- `textos.json`: textos de la página que no salen de la arquitectura (títulos, pies de figura, pasos del ciclo, chats de Fase 1).

Si cambias pilares, agentes, bases o reglas en `data/arquitectura.json`, regenera `index.html` en el mismo PR y vuelve a publicar el artefacto.
