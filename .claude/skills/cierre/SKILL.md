---
name: cierre
description: Cierra una sesión de marca.ai. Úsala al terminar toda sesión de chat, y también cuando el dueño diga que ya terminó o se despida. Deja la fila de la sesión en Bitácora y planes (qué se hizo, decisiones, pendientes, siguiente paso y enlaces), propone las decisiones a Conocimiento y decisiones y avisa si quedó algo que pide aprobación. Sin esta fila, el trabajo no existe para el siguiente agente.
argument-hint: "[nota opcional para la bitácora]"
---

# /cierre: cierre de una sesión

Nota del dueño (opcional): «$ARGUMENTS»

Toda sesión termina aquí: si no hay fila en Bitácora y planes, el trabajo de esta sesión no existe para el siguiente agente.

## 1. Reúne lo de la sesión

- **Chat y pilares:** los que fijó `/inicio`. Si no hubo `/inicio`, pregúntalos. En una sesión de desarrollo del sistema, el pilar es automatizaciones.
- **Inicio y fin:** hora de Ciudad de México (`TZ=America/Mexico_City date`). El inicio es la hora que dio `/inicio` en su resumen; si no la tienes, usa tu mejor estimación y dilo.
- **Qué se hizo**, **decisiones** que tomó el dueño, **pendientes**, **siguiente paso** y **enlaces** (Tareas, Proyecto, deal, borradores de Docs o Gmail, PR, archivos de Drive).
- **Bases leídas y escritas** durante la sesión.

## 2. Revisa lo que pide aprobación

Antes de escribir, busca en lo que se produjo algo que pida aprobación: gasto, primer contacto, publicación, impuestos, precio o descuento, comisiones, acceso, página canónica, activar automatización o plantilla de envío.

- Si algo no tiene tarjeta en Aprobaciones y no lo cubre la Matriz de aprobaciones (aprobación por excepción), avísalo arriba de todo y ofrece `/pedir-aprobacion` ahora. Sin tarjeta aprobada, no se ejecuta.
- Lista las tarjetas creadas en la sesión con su Estado, su Vence y la ventana en que se deciden (9:30 o 17:30).

## 3. Arma la fila de Bitácora y planes

Propiedades de la base, con sus nombres. Si en Notion una fila de esta tabla son dos propiedades (por ejemplo «Agente» y «Pilar», o «Bases leídas» y «Bases escritas», como las arma [docs/02-cerebro-notion.md](../../../docs/02-cerebro-notion.md#bitácora-y-planes)), llena las dos:

| Propiedad | Qué va |
|---|---|
| Tipo | «Sesión» |
| Agente y Pilar | Agente: el Piloto del chat o el agente de la tabla del README que trabajó (por ejemplo Arquitecto; ojo: el agente Cierre de Ventas no es esta skill). Pilar: los pilares del chat |
| Inicio y fin | Fecha y hora de Ciudad de México |
| Resultado | OK / Parcial / Error |
| Resumen (máximo 10 líneas) | Con el formato de abajo |
| Bases leídas y escritas | Las de la sesión |
| Enlace a la sesión | La URL de esta sesión en claude.ai/code si la tienes en tu contexto; si no, pídesela al dueño en una línea o deja el campo vacío |
| Relaciones | Tareas trabajadas o creadas; Conocimiento y decisiones (decisiones propuestas); Métricas, si se tocaron |

«Top 3» y «Horas de gestión del CEO» no se llenan en una sesión: son de los planes del día y las revisiones del Gabinete.

Resumen, máximo 10 líneas:

```
Hecho: ...
Decisiones: ... (o «ninguna»)
Pendientes: ... (cada uno con su Tarea)
Siguiente paso: ... (quién y para cuándo)
Enlaces: ...
Aprobaciones: ... (tarjetas abiertas con su Vence, o «ninguna»)
```

## 4. Actualiza Tareas

- Pon el Estado correcto a cada Tarea trabajada: «Hecha», «En curso», «Esperando aprobación» o «Bloqueada».
- Cada pendiente nuevo queda como Tarea en «Por hacer», con Pilar, Tipo, Prioridad, Fecha límite si la hay, Dueño humano, Origen «agente» e ID externo si lo hay (deal, PR, pieza o folio). Antes de crearla, busca si ya existe por su ID externo o por su título.
- Nunca borres: lo que ya no aplica pasa a «Descartada».

## 5. Propón las decisiones

- Si hubo decisiones, muéstralas junto con la vista previa de la fila y pide confirmación en una sola pregunta. Si no hubo, no preguntes.
- Por cada decisión confirmada, crea una página en Conocimiento y decisiones con Tipo «Decisión», Estado «Propuesta», Pilar y Decidió (el dueño), relacionada con la fila de Bitácora. Deja «Vigente desde» vacío y nunca la marques «Vigente» ni «Canónica»: el dueño la revisa en los 10 minutos de cambios de la junta del lunes.
- Si una decisión cambia una página canónica (por ejemplo «Oferta y precios vigentes», la Matriz de aprobaciones, la Guía de voz o el Plan de compensación), no la edites: pide `/pedir-aprobacion` con Tipo «Página canónica».

## 6. Escribe y confirma

1. Crea la fila en Bitácora y planes y actualiza Tareas y Conocimiento y decisiones como arriba. Fuera de esas tres bases, no escribas en ninguna que no esté en el campo «Puede escribir en» del agente.
2. Responde en 3 líneas: enlace a la fila, Tareas actualizadas o creadas, y aprobaciones pendientes con su Vence. Si algo pide aprobación y no tiene tarjeta, repítelo al final.

**Si Bitácora y planes aún no existe** o esta sesión no tiene conector de Notion: dilo, entrega la fila completa como texto en el chat para pegarla cuando exista el cerebro y no la guardes en el repo (en el repo no van datos del negocio).

**En una rutina o en una sesión sin el dueño presente:** no pidas confirmaciones. Si no hubo novedad, no escribas nada (las corridas sin novedad no escriben). Si la hubo, escribe la fila con Tipo «Corrida» y no crees decisiones en Conocimiento y decisiones. El Gabinete no usa esta skill: su fila es el «Plan del día» que define su instrucción (`pilares/automatizaciones/gabinete/CLAUDE.md`).
