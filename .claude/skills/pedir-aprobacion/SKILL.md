---
name: pedir-aprobacion
description: Pide una aprobación humana en marca.ai. Úsala antes de gastar dinero, contactar por primera vez a alguien en nombre de la marca, publicar, tocar cualquier tema fiscal, cambiar precios, descuentos, comisiones o accesos, cambiar una página canónica, activar una automatización o crear o cambiar una plantilla de envío. Primero revisa la Matriz de aprobaciones (aprobación por excepción); si hace falta, crea la tarjeta en la base Aprobaciones de Notion con vencimiento de 48 horas. La decisión nunca se toma en el chat.
argument-hint: "[qué necesitas aprobar]"
---

# /pedir-aprobacion

Solicitud: «$ARGUMENTS»

Si viene vacía, usa lo que se estaba preparando en la sesión; si no queda claro qué se va a aprobar, pregúntalo en una línea.

## Reglas que no cambian

- Se decide en la base Aprobaciones, nunca en el chat. Si el dueño escribe aquí «sí, apruébalo», contesta con el enlace a la tarjeta: el Estado se cambia ahí, porque esa es la evidencia.
- Nada se ejecuta antes de que la tarjeta esté en «Aprobada». Si el borrador cambia después de aprobarse, la aprobación ya no vale: actualiza el borrador y pide otra.
- Ventanas de decisión de 10 minutos: 9:30 y 17:30. No interrumpas al dueño fuera de ellas. Solo las 3–5 emergencias P0 escritas en `pilares/automatizaciones/gabinete/CLAUDE.md` pueden interrumpirlo; si lo que pides es una de ellas, sigue lo que diga ese archivo.
- Deciden el dueño y, desde enero, el asistente de operación dentro de su límite en la Matriz (montos por definir en la Matriz).

## 1. ¿Hace falta aprobar?

Pide aprobación para cualquiera de estos tipos (son los valores de la propiedad Tipo):

| Tipo | Cuándo |
|---|---|
| Gasto | Cualquier gasto de dinero |
| Primer contacto | Primer mensaje que inicia la marca con una persona o empresa |
| Publicación | Publicar en nombre de la marca |
| Impuestos | Cualquier tema fiscal (por ejemplo un CFDI distinto a la propuesta, una cancelación o el preliminar de impuestos) |
| Precio o descuento | Precios, descuentos y cambios de alcance con precio |
| Comisiones | Comisiones y liquidaciones |
| Acceso | Dar acceso a una persona o a una herramienta |
| Página canónica | Cambiar una página canónica de Conocimiento y decisiones |
| Activar automatización | Encender un agente o una automatización |
| Plantilla de envío | Crear o cambiar el texto de una plantilla que envía n8n |

Antes de crear la tarjeta, revisa la Matriz de aprobaciones (enlace en «Enlaces del cerebro en Notion» del CLAUDE.md raíz; por definir hasta que exista el cerebro). Se aprueba por excepción: no se vuelve a aprobar lo que coincide con algo ya aprobado, por ejemplo:

- factura igual a la propuesta aprobada;
- recordatorio con plantilla aprobada;
- publicación dentro de la parrilla aprobada;
- respuestas del bot cuando la persona escribe primero;
- presupuesto semanal de pauta ya aprobado.

Si coincide, no crees tarjeta: di qué regla de la Matriz aplica y con qué aprobación previa coincide (con su enlace) y sigue. Si hay duda, crea la tarjeta. Si la Matriz aún no existe, solo esas 5 excepciones valen; todo lo demás de la tabla pide tarjeta. Cambiar el texto de una plantilla obliga a aprobarla de nuevo.

## 2. Arma la tarjeta

**Título:** qué se aprueba, en una línea y con el monto si hay.

**Propiedades** (nombres de la base Aprobaciones; si en Notion una fila de esta tabla son dos propiedades, como «Monto MXN» y «Riesgo», «Aprobada por» y «Fecha de aprobación» o «Id de ejecución» y «Evidencia», como las arma [docs/02-cerebro-notion.md](../../../docs/02-cerebro-notion.md#aprobaciones), llena las dos):

| Propiedad | Qué va |
|---|---|
| Tipo | Uno de los 10 valores de la tabla de arriba |
| Monto MXN y Riesgo | Monto en pesos; di si es más IVA o con IVA incluido. Si el costo es en dólares, conviértelo y anota el tipo de cambio. 0 si no hay dinero. Riesgo: qué puede salir mal, en una línea (si la base ya trae una escala de Riesgo, usa su valor; la escala está por definir al crear la base) |
| Borrador exacto (vista previa) | El texto, monto, destinatarios o cambio exacto que se va a ejecutar, completo. Si es un correo, también el enlace al borrador de Gmail |
| Última edición del borrador | Fecha y hora de la última versión del borrador |
| Solicitada por | El agente o la persona que pide |
| Estado | «Pendiente» |
| Vence | 48 horas después de crearla |
| Regla aplicada | La regla de la Matriz que dice quién aprueba y con qué límite |
| Aprobada por y fecha | Vacío: lo llena quien decide |
| Id de ejecución y evidencia | Vacío: desde Fase 2 lo llena el Portero |

**Relaciones:** la Tarea de origen y, según el caso, el Proyecto, la factura en Facturas y cobros, la persona en Personas y accesos o la página en Conocimiento y decisiones.

**Cuerpo de la tarjeta**, en 4 líneas:

- **Qué:** la acción exacta y sobre qué o quién.
- **Por qué:** el motivo en 1 o 2 líneas y qué pasa si no se aprueba.
- **Enlace:** al borrador, documento o evidencia.
- **Quién decide:** según la Matriz; si la Matriz no lo dice, el dueño.

Según el tipo:

- **Activar automatización:** enlaza la fila del agente en la tabla del README y confirma que se cumplió su condición (la tarea hecha a mano 5–10 veces igual), que su ficha tiene dueño, conectores, interruptor y plan B y, si toca clientes, que pasó el checklist de salida a producción y de 3 a 7 días en modo sombra. Máximo 2 automatizaciones nuevas por semana.
- **Plantilla de envío:** pega el texto exacto. n8n la enviará desde cobranza@ o avisos@ pasando por Filtro y el interruptor general.

## 3. Crea la tarjeta y avisa

1. Crea la tarjeta en Aprobaciones con todo lo anterior.
2. Si hay Tarea relacionada, pásala a «Esperando aprobación».
3. Responde en 3 líneas: enlace a la tarjeta; Tipo y monto; Vence y la ventana en que se decide (la siguiente: 9:30 o 17:30).
4. No ejecutes nada. Sigue con otra cosa de la sesión.

## 4. Después de la decisión

- **Aprobada:** se ejecuta solo lo aprobado, una vez y sin cambios. Correos nuevos o a la medida: el conector de Gmail de Claude solo deja el borrador y lo envía una persona. Plantillas preaprobadas: las envía n8n desde cobranza@ o avisos@. Desde Fase 2, el Portero ejecuta lo que sale por n8n y guarda la evidencia; antes, lo ejecuta el dueño o el asistente.
- **Rechazada:** no se ejecuta; anota el motivo en la Tarea.
- **Sin decisión:** la tarjeta pasa a la siguiente ventana del dueño y nunca escala a un puesto vacío. A las 48 h vence («Vencida») y no se ejecuta; si todavía hace falta, se pide de nuevo.
- **Falló:** no reintentes pasos que envían; avisa al dueño.

## Si la base Aprobaciones aún no existe

Dilo, deja la tarjeta completa como texto en el chat y no ejecutes la acción: el dueño la hace a mano o espera a que exista la base. Nunca la des por aprobada por una respuesta en el chat.
