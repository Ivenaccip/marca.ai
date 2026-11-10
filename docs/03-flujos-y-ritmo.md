# Flujos y ritmo

Cómo se mueve el trabajo de punta a punta y con qué ritmo: los 7 flujos del sistema paso por paso, las 15 cadencias agrupadas por frecuencia y los dos presupuestos que lo sostienen, tus 5 horas de gestión a la semana y las corridas diarias de Claude. La fuente es [data/arquitectura.json](../data/arquitectura.json) (campos `flujos`, `cadencias` y `orquestacion`) y los datos verificados con fuentes al 10 de noviembre de 2026 están en [data/verificacion.json](../data/verificacion.json). Si algo de este documento no cuadra con esos archivos, mandan ellos.

**Mapa visual interactivo del sistema:** https://claude.ai/artifact/FtyWRkr6M2jFp4Mnu5BFDN

> Estado al 10 de noviembre de 2026: Fase 0 (10 al 30 de noviembre), sin agentes. Los flujos describen el sistema completo. Mientras un agente no se enciende, su paso lo hace la persona de la columna Actor: «Tú (Cierre desde la quinta propuesta)» quiere decir que hoy lo haces tú y que Cierre lo toma cuando cumpla su condición.

## Contenido

1. [Cómo leer los flujos](#cómo-leer-los-flujos)
2. Los 7 flujos
   - [1. Lead → venta → «Pago recibido» → factura](#flujo-1)
   - [2. Proyecto de cliente: de «Pago recibido» a la entrega](#flujo-2)
   - [3. Ciclo de contenido semanal](#flujo-3)
   - [4. Referidos](#flujo-4)
   - [5. Cierre de mes contable e impuestos (días 1 al 17)](#flujo-5)
   - [6. Alta y baja de un setter independiente](#flujo-6)
   - [7. Capacitación a empresas (solo si confirmas que hoy te pagan por eso)](#flujo-7)
3. [Cadencias](#cadencias)
4. [Tu semana tipo](#tu-semana-tipo)
5. [Presupuesto de tu tiempo: 5 horas de gestión a la semana](#presupuesto-de-tu-tiempo-5-horas-de-gestión-a-la-semana)
6. [Presupuesto de corridas de Claude](#presupuesto-de-corridas-de-claude)
7. [Por definir en este documento](#por-definir-en-este-documento)

Documentos hermanos: [README](../README.md) (los 5 chats y la tabla de agentes y automatizaciones), [CLAUDE.md](../CLAUDE.md) (reglas comunes de los chats), [01-arquitectura.md](01-arquitectura.md) (visión, pilares y orquestación), [02-cerebro-notion.md](02-cerebro-notion.md) (las 10 bases), [04-lo-que-te-falta.md](04-lo-que-te-falta.md) (puntos ciegos y datos verificados) y [05-ruta-stack-riesgos.md](05-ruta-stack-riesgos.md) (ruta por fases, stack y riesgos).

## Cómo leer los flujos

Cada flujo es una tabla con cuatro columnas:

- **Paso:** el orden.
- **Actor:** quién lo hace. «Tú», «Setter», «Cliente», «Prospecto», «Referido», «Contadora», «Editor» y «Asistente» son personas; el asistente de operación de medio tiempo entra en enero y, hasta entonces, lo suyo lo haces tú. «n8n» es la herramienta que escucha eventos y lleva los relojes. Los demás nombres son agentes o reglas de n8n de la [tabla de agentes y automatizaciones del README](../README.md#tabla-de-agentes-y-automatizaciones). Un agente entre paréntesis con su condición, como «Asistente (Enlace desde febrero)», es el que tomará ese paso cuando se encienda.
- **Acción:** qué pasa, tal como lo fija la arquitectura.
- **Herramienta:** dónde pasa.

Tres eventos unen los flujos:

| Evento | Qué es | Qué dispara |
|---|---|---|
| «Lead manual» | Todo lead que llega fuera de ManyChat (LinkedIn, red personal, evento, referido directo, correo o audiencia prestada) se registra en menos de 24 h desde la app de Pipedrive o el formulario que n8n pasa a Pipedrive, con fuente de lista cerrada | El deal en Pipedrive; el lead es de quien lo registró primero |
| «Pago recibido» | Formulario de 3 campos (folio de la propuesta, monto y fecha) que llenas tú, o el asistente desde enero, cuando el depósito aparece en tu banca; los pagos con tarjeta entran solos por el webhook de Stripe | n8n pasa el deal a «Ganado», crea el Proyecto desde la plantilla «Proyecto ganado» y la ficha en Clientes, deja el borrador de CFDI, agrega la reserva de impuestos y la comisión devengada a la hoja de dinero, manda la compra a Meta y deja la Tarea para Producto |
| «Diagnóstico pagado» | El pago del Diagnóstico pagado (100% por adelantado; ahí se cobra el descubrimiento profundo) | Igual que «Pago recibido», crea el Proyecto desde la plantilla «Proyecto ganado» y despierta al Arquitecto |

Los 7 flujos de un vistazo:

| Flujo | Pasos | Arranca con | Termina en |
|---|:-:|---|---|
| [1. Lead → venta → «Pago recibido» → factura](#flujo-1) | 12 | Un lead llega por ManyChat (comentario, DM o anuncio) o se registra como «Lead manual» | CFDI timbrado y enviado desde cobranza@ con PDF y XML, guardado en Drive |
| [2. Proyecto de cliente: de «Pago recibido» a la entrega](#flujo-2) | 11 | La descripción del cliente en Pipedrive, antes del pago | Retro de cierre: estimado contra real, margen y cosecha de componentes |
| [3. Ciclo de contenido semanal](#flujo-3) | 10 | Bloque de contenido del viernes: 6–8 temas y parrilla de la semana siguiente | Los lunes, leads A/B por palabra clave y por pieza; desde Fase 3, el Boletín quincenal |
| [4. Referidos](#flujo-4) | 10 | Encuesta de 2 preguntas al firmar el acta final | Revisión de respuestas, referidos, ventas, bajas y quejas en la junta del lunes |
| [5. Cierre de mes contable e impuestos (días 1 al 17)](#flujo-5) | 12 | Día 1: página «Cierre AAAA-MM» y descarga de estados de cuenta | Acuses archivados y dudas resueltas como reglas fiscales en Conocimiento |
| [6. Alta y baja de un setter independiente](#flujo-6) | 9 | Role-play de 15 minutos con 3 objeciones reales | Baja en 24 horas y liquidación final solo sobre lo cobrado, contra CFDI |
| [7. Capacitación a empresas (solo si confirmas que hoy te pagan por eso)](#flujo-7) | 7 | Propuesta de capacitación desde su plantilla | Encuesta a participantes y patrocinador; caso con permiso y propuesta del siguiente grupo |

<a id="flujo-1"></a>

## 1. Lead → venta → «Pago recibido» → factura

| Paso | Actor | Acción | Herramienta |
|:-:|---|---|---|
| 1 | Tú / Setter | Lead manual: todo lead que llegue fuera de ManyChat (LinkedIn, red personal, evento, referido directo, correo o audiencia prestada) se registra en menos de 24 h desde la app de Pipedrive o el formulario que n8n pasa a Pipedrive, con fuente de lista cerrada, y recibe el link al aviso de privacidad en el primer mensaje; un lead es de quien lo registró primero. | App de Pipedrive o formulario + n8n |
| 2 | Prospecto | Comenta una de las 3–5 palabras clave de la oferta, manda DM o da clic en un anuncio que abre Instagram Direct o WhatsApp. | Instagram / WhatsApp de la marca |
| 3 | Anfitrión | Responde en segundos con texto aprobado, muestra el aviso simplificado con «Acepto» (ManyChat guarda fecha, canal y versión), hace 3–4 preguntas y asigna A/B/C; a los leads A les ofrece agendar directo en tu página de citas y cierra toda primera conversación con cita u horario preferido; envía LeadSubmitted a Meta. | ManyChat Pro + Google Calendar + Conversions API (nativa en Instagram y Messenger; vía n8n en WhatsApp) |
| 4 | n8n | Valida el webhook, crea el lead_id, normaliza el teléfono a +52 (quita el 1 cuando llega como 521), deduplica, copia el consentimiento y crea persona y deal en Pipedrive con fuente, palabra clave y ctwa_clid. | n8n + Pipedrive |
| 5 | Repartidor (n8n) | Pone el lead en la cola: el primer setter disponible que lo toma queda como dueño del deal y de la conversación de ManyChat (n8n sincroniza ambos y reasigna si cambia el dueño); si nadie lo toma en 30 minutos en horario hábil se ofrece al resto sin sanción y te avisa. | n8n + ManyChat Live Chat + Pipedrive |
| 6 | Setter | Contesta desde el número de la marca dentro de la ventana de 24 horas (después, solo con una plantilla de reapertura aprobada), califica, confirma o agenda la cita y registra con etiquetas en ManyChat («cita agendada», «asistió», «no califica» con motivo y «ahora no» con fecha de recontacto de 30, 60 o 90 días) que n8n copia a Pipedrive. | ManyChat Live Chat + Google Calendar + n8n |
| 7 | Tú | Llamada de descubrimiento grabada con aviso al inicio y liga al aviso de privacidad; si el problema necesita descubrimiento profundo, vendes el Diagnóstico pagado en lugar de diseñar gratis. | Zoom |
| 8 | Tú (Cierre desde la quinta propuesta) | Propuesta de 1–2 páginas desde la plantilla: problema, alcance, fuera de alcance, supuestos, precio más IVA de «Oferta y precios vigentes», hitos y pagos y próxima fecha de arranque; pide Constancia de Situación Fiscal, uso de CFDI, correo de facturación y si requieren alta de proveedor (documentos y días); una sola Aprobación de precio. | Google Docs + Gmail (borrador) + Notion Aprobaciones |
| 9 | Cliente | Firma la Propuesta y el contrato marco (la Propuesta firmada es el anexo de alcance) y paga el anticipo por SPEI con el folio en el concepto, o con link de Stripe si es tarjeta; si pide alta de proveedor, le mandas tu expediente el mismo día. | Firma electrónica + banco / Stripe México + Drive |
| 10 | Tú o el asistente | «Pago recibido»: cuando el depósito aparece en tu banca llenas el formulario de 3 campos (folio, monto y fecha); si hay duda validas el CEP en Banxico (nunca una captura); los pagos con tarjeta entran solos por el webhook de Stripe. | Formulario de n8n + banca en línea + validador CEP |
| 11 | n8n | Pasa el deal a «Ganado», crea el Proyecto desde la plantilla «Proyecto ganado» y la ficha en Clientes, deja el borrador de CFDI en Facturas y cobros, agrega la reserva de impuestos y la comisión devengada a la hoja de dinero, manda el evento de compra a Meta y deja la Tarea para Producto. | n8n + Pipedrive + Notion + Google Sheets |
| 12 | Tú o el asistente (Cobra desde Fase 2) | CFDI con el método que dicta la regla escrita de tu contadora (PUE por cada pago, o PPD con complemento) y los datos exactos de la Constancia; si es igual a la propuesta aprobada no se vuelve a aprobar; se timbra, se envía con PDF y XML desde cobranza@ y queda en Drive. | Portal o PAC de la contadora + n8n + Google Drive |

**Lo que conviene saber**

- **Ventana de 24 horas (paso 6).** Por la API oficial solo puedes mandar texto libre dentro de las 24 horas siguientes al último mensaje del cliente; después, solo plantillas aprobadas y pagadas. Desde el 1 de octubre de 2026 Meta cobra también los mensajes de servicio (cerca de US$0.0085 en México, según tablas de proveedores) y siguen gratis las conversaciones que abre un anuncio de clic a WhatsApp dentro de su ventana de 72 horas. Ver [punto ciego 1](04-lo-que-te-falta.md#pc1) y [V4](04-lo-que-te-falta.md#v4).
- **El bot sí está permitido (paso 3)** mientras solo hable de tus servicios: desde el 15 de enero de 2026 la API de WhatsApp prohíbe los chatbots de IA de propósito general. Ver [V5](04-lo-que-te-falta.md#v5).
- **LeadSubmitted (paso 3).** La acción nativa de ManyChat está documentada solo para Instagram y Messenger (para anuncios de clic a WhatsApp no se encontró soporte nativo); en WhatsApp el evento sale de n8n. Antes de optimizar campañas a ese evento, comprueba en el Administrador de eventos que esté llegando. Ver [V6](04-lo-que-te-falta.md#v6).
- **Costo de la tarjeta (paso 9).** Stripe México cobra 3.6% + $3 MXN más IVA por tarjeta nacional (0.5% más en internacionales; meses sin intereses aparte), y sale de tu margen. Ver [punto ciego 7](04-lo-que-te-falta.md#pc7) y [V18](04-lo-que-te-falta.md#v18).
- **Un pago existe cuando aparece en tu banca (paso 10).** Circulan comprobantes de SPEI falsos: una transferencia dudosa se valida con el CEP de Banxico. Ver [punto ciego 6](04-lo-que-te-falta.md#pc6).
- **Método del CFDI (paso 12).** PUE o PPD lo dicta la regla escrita de tu contadora: pídela antes de facturar el primer anticipo, porque una factura con el método equivocado te la regresan. Ver [punto ciego 11](04-lo-que-te-falta.md#pc11).

<a id="flujo-2"></a>

## 2. Proyecto de cliente: de «Pago recibido» a la entrega

| Paso | Actor | Acción | Herramienta |
|:-:|---|---|---|
| 1 | Tú / Setter | La descripción del cliente vive en Pipedrive antes del pago: problema, proceso actual, sistemas y datos que existen, presupuesto, fecha, quién decide y campos de traspaso (qué se le prometió con sus palabras, métrica de éxito y riesgos); si hace falta descubrimiento profundo, se vende el Diagnóstico pagado. | Pipedrive + Zoom |
| 2 | n8n | Con «Pago recibido» (o el pago del Diagnóstico) crea el Proyecto desde la plantilla «Proyecto ganado» con su checklist y un recordatorio en Calendar por cada pago de hito, y deja la Tarea para Producto. | n8n + Notion + Google Calendar |
| 3 | Tú (Arquitecto y Arqueólogo con el siguiente proyecto) | Brief técnico de una página (objetivo medible, métrica base, criterios de aceptación y supuestos), arquitectura con ADR, estimación P50/P90 y qué se reutiliza (solo repos Propios o Licenciables); si la estimación supera lo vendido, se vuelve solicitud de cambio, no trabajo gratis. | Claude Code + Notion + GitHub |
| 4 | Andamio | Crea el repo desde la plantilla del servicio con CLAUDE.md, CI con gitleaks, milestones iguales a los hitos de la Propuesta e issues con criterios; si el disparo por API falla, n8n te deja la Tarea y abres la sesión con un toque. | Claude Code (rutina) + GitHub |
| 5 | Tú + asistente | Kickoff de 45 minutos con el checklist de la plantilla: patrocinador y responsable interno, cuentas de APIs, nube y WhatsApp creadas a nombre del cliente (te invita como usuario), canal oficial, 3 métricas de línea base, calendario de demos y carpeta de Drive compartida. | Zoom + Notion + Google Drive |
| 6 | Escuadrón + Inspector | Los subagentes implementan cada issue «listo» en ramas claude/ con pruebas; el Inspector revisa cada PR (pruebas, E2E, seguridad, secretos y licencias) y tú haces merge; las previews viven en la cuenta del cliente. | Claude Code en la nube + GitHub Actions |
| 7 | Asistente / Tú | Cada viernes: reporte de 5 líneas por correo con la plantilla y demo de 30 minutos; todo lo pedido fuera de la Propuesta se cotiza con horas, precio y nueva fecha y entra solo con aceptación por escrito. | Gmail + Zoom + Notion (Tareas tipo «Cambio») |
| 8 | Tú | Hito terminado y «QA aprobado»: paquete (manual, runbook y HANDOVER), kit de adopción, transferencia de cuentas y llaves, borrado de datos de prueba y acta con 5 días hábiles de aceptación tácita. | Google Docs + Drive |
| 9 | Cliente / asistente | El cliente firma el acta o vence el plazo sin observaciones por escrito; el recordatorio de Calendar dispara la factura del hito y, cuando paga, su «Pago recibido». | Google Calendar + portal o PAC + formulario «Pago recibido» |
| 10 | Asistente / Tú | Al firmar el acta final: encuesta de 2 preguntas, testimonio con permiso por niveles y petición de referido (si es empresa, la recompensa es para la empresa); llamada a los 60 días con oferta de iguala. | Google Forms + Gmail + Calendar |
| 11 | Tú (Arqueólogo desde Fase 2) | Retro de cierre de 45 minutos: estimado contra real con las horas de Calendar, margen del proyecto y cosecha de componentes Propios o Licenciables al repo biblioteca. | Notion + Google Sheets + GitHub |

**Lo que conviene saber**

- **De quién es el código (pasos 3 y 11).** Sin pacto en contrario, la ley presume que lo hecho por encargo es de quien lo encarga y paga (Ley Federal del Derecho de Autor, artículo 83) y una obra generada solo por IA no se protege (Amparo Directo 6/2025 de la Suprema Corte). Por eso solo se reutilizan repos Propios o Licenciables, y la revisión humana y el registro de decisiones en cada PR son evidencia de tu aporte. Ver [punto ciego 10](04-lo-que-te-falta.md#pc10) y [V11](04-lo-que-te-falta.md#v11).
- **Cuentas a nombre del cliente (paso 5).** Si quedan a tu nombre, alguien queda de rehén al terminar. Ver [punto ciego 15](04-lo-que-te-falta.md#pc15).
- **Previews en la cuenta del cliente (paso 6).** El plan Hobby de Vercel no permite uso comercial, ni un despliegue hecho por un consultor pagado para un cliente. Ver [V27](04-lo-que-te-falta.md#v27).

<a id="flujo-3"></a>

## 3. Ciclo de contenido semanal

| Paso | Actor | Acción | Herramienta |
|:-:|---|---|---|
| 1 | Tú (Guionista desde Fase 2) | Viernes, bloque de contenido de 45 minutos: eliges 6–8 temas a partir de objeciones reales, motivos de pérdida, preguntas que se repiten y casos con permiso, como pieza madre y derivados, y apruebas la parrilla de la semana siguiente. | Notion Contenido |
| 2 | Tú (Guionista desde Fase 2) | Guiones en bullets con gancho, CTA y una de las 3–5 palabras clave fijas de la oferta. | Notion |
| 3 | Tú (checklist de Voz) | Revisas cada guion contra la Guía de voz, las promesas prohibidas y las políticas de anuncios de Meta (resultados irreales, atributos personales). | Notion |
| 4 | Tú | Grabas en lote en tu bloque fijo y subes cada bruto a 01_Bruto con su ID (C-0142_bruto.mp4). | Google Drive |
| 5 | Editor | Corta con el brief y entrega en 48 horas o menos en 02_Editado con el mismo ID; máximo 2 rondas (Tijeras solo si la edición es IA). | Google Drive (+ Adobe Express si la edición es IA) |
| 6 | Tú | Una ronda de revisión con checklist: claim comprobable, permiso de quien aparece, etiqueta de IA si aplica, música con licencia, CTA y palabra clave. | Google Drive + Notion |
| 7 | Asistente o editor | Programa en Blotato la parrilla aprobada (lo que está dentro de la parrilla aprobada no se vuelve a aprobar) y mueve la ficha a «Programada». | Blotato + Notion |
| 8 | Anfitrión | Responde comentarios con palabra clave y DMs; cada lead queda con su fuente y su palabra clave. | ManyChat |
| 9 | Gabinete (Brújula desde Fase 2) | Lunes: leads A/B por palabra clave y por pieza (número escrito, no rollup); las que más leads A/B traen pasan a la junta como candidatas a anuncio; vistas de LinkedIn y YouTube a mano solo en piezas que van a pauta. | Pipedrive + Blotato + Notion Métricas |
| 10 | Boletín (Fase 3) | Cada quincena convierte la pieza madre en correo a la lista propia y en mensaje del Canal de WhatsApp. | ManyChat (correo) + Canal de WhatsApp |

**Lo que conviene saber**

- **Claims y permisos (pasos 3 y 6).** La publicidad debe ser veraz y comprobable (Ley Federal de Protección al Consumidor, artículo 32) y usar la imagen de una persona requiere su consentimiento (Ley Federal del Derecho de Autor, artículo 87). Ver [punto ciego 8](04-lo-que-te-falta.md#pc8).
- **Palabras clave (paso 2).** Son 3–5 fijas por oferta, no una por pieza; UTM y atribución por pieza solo en las piezas que van a pauta.
- **Atribución (paso 9).** Desde el 12 de enero de 2026 Meta dejó de reportar las ventanas de 7 y 28 días por visualización: sus números y los de tu CRM nunca van a cuadrar, y por eso se guardan snapshots propios. Ver [punto ciego 16](04-lo-que-te-falta.md#pc16) y [V7](04-lo-que-te-falta.md#v7).
- **Dónde quedan los números (paso 9).** Mientras la [nota 4 de la tabla del README](../README.md#tabla-de-agentes-y-automatizaciones) siga por confirmar, el Gabinete deja los leads A/B en su fila «Plan del día» del lunes y no escribe en Métricas ni en Contenido. Blotato no está entre los conectores de su rutina: entra con Brújula.

<a id="flujo-4"></a>

## 4. Referidos

| Paso | Actor | Acción | Herramienta |
|:-:|---|---|---|
| 1 | Asistente (Eco en Fase 3) | Al firmar el acta final manda la encuesta de 2 preguntas (del 0 al 10 y por qué); con 0–6 te agenda una llamada y a ese cliente nunca se le piden referidos. | Google Forms + Google Calendar |
| 2 | Tú | Con 9–10 pides testimonio con permiso por niveles y a quién se lo recomendaría; si es cliente empresa, la recompensa es para la empresa (horas de soporte o descuento en la siguiente fase), no dinero a la persona: muchas políticas de compras lo prohíben. | Zoom o Gmail |
| 3 | Tú | Hasta Fase 3: cada referido va 1 a 1 desde la app, escrito por ti y sin extensiones, con el link wa.me con el código del referidor para que el referido te escriba primero. | App de WhatsApp Business + Ref URL de ManyChat |
| 4 | Referido | Escribe con el código prellenado; ManyChat detecta el Ref URL y n8n crea el deal con «Referido por» y prioridad A. | ManyChat + n8n + Pipedrive |
| 5 | Setter / Tú | Atienden y cierran siguiendo el flujo 1; los leads que tú traes son tuyos según el Plan de compensación. | Pipedrive + Zoom |
| 6 | Asistente | Con el «Pago recibido» del referido registra la recompensa del referidor en la hoja de dinero (si fuera dinero a una persona, con el tratamiento fiscal que defina la contadora). | Google Sheets |
| 7 | Boca a Boca (Fase 3) | Carril de plantilla aprobada por Meta solo para contactos con opt-in vigente en ManyChat, sin marketing en 30 días y sin quejas; calcula el costo (destinatarios × tarifa vigente de marketing) y pide una Aprobación. | ManyChat + Notion Aprobaciones |
| 8 | Filtro | Verifica opt-in, bajas, frecuencia y horario de cada destinatario. | n8n + ManyChat |
| 9 | Tú | Apruebas lista, texto, incentivo y costo y programas el envío entre semana en horario hábil, en lotes pequeños al inicio. | Notion Aprobaciones + ManyChat |
| 10 | Tú | En la junta del lunes revisas respuestas, referidos, ventas, bajas y quejas por envío. | Pipedrive + ManyChat |

**Lo que conviene saber**

- **Hasta Fase 3, 1 a 1 y sin extensiones (paso 3).** Las extensiones o apps no oficiales para programar mensajes son causa de bloqueo del número. Ver [punto ciego 1](04-lo-que-te-falta.md#pc1).
- **La app no es la API (paso 3).** La app de WhatsApp Business tiene listas de difusión de hasta 256 contactos, pero solo llegan a quien guardó tu número, y no tiene automatización, varios agentes ni plantillas por API. Ver [V29](04-lo-que-te-falta.md#v29).
- **Costo del carril de plantilla (paso 7).** Destinatarios × tarifa vigente de marketing: cerca de US$0.0397 por mensaje en México, según tablas de proveedores; confírmala en tu cuenta. Ver [V4](04-lo-que-te-falta.md#v4).

<a id="flujo-5"></a>

## 5. Cierre de mes contable e impuestos (días 1 al 17)

| Paso | Actor | Acción | Herramienta |
|:-:|---|---|---|
| 1 | Asistente (Enlace desde febrero) | Día 1: crea la página «Cierre AAAA-MM» desde la plantilla con sus fechas (complementos de pago, ISR e IVA del día 17 o siguiente día hábil) y eventos en Calendar. | Notion + Google Calendar |
| 2 | Asistente (tú hasta que entre) | Días 1–2: descarga estados de cuenta y CSV del banco a /Fiscal/AAAA/MM/Bancos. | Banca en línea + Google Drive |
| 3 | Asistente | Revisa la hoja de dinero: cada depósito con su «Pago recibido» y su CFDI, gastos sin comprobante y depósitos que no son ingreso; te deja máximo 10 excepciones. | Google Sheets |
| 4 | Tú | En 15 minutos resuelves las excepciones: qué depósito no es ingreso, qué gasto es personal y a qué proveedor pedirle factura. | Google Sheets |
| 5 | Asistente | Días 1 y 16: corte de comisiones sobre lo cobrado sin IVA; pide el CFDI de cada setter por el monto exacto y lo valida antes de que pagues por SPEI (arriba de $2,000 siempre por transferencia). | Google Sheets + Gmail |
| 6 | Asistente (Enlace desde febrero) | Día 3 (o el siguiente día hábil): arma el paquete con lo que tu contadora pidió (muchas bajan los CFDI directo del SAT y solo necesitan estados de cuenta y la explicación de los depósitos) y el borrador del correo con links y resumen de números. | Gmail + Google Drive |
| 7 | Tú | Revisas y envías el correo a la contadora. | Gmail |
| 8 | Contadora | Hacia el día 10 manda el preliminar de ISR e IVA; lo comparas con la reserva de la hoja de dinero y, si difiere más de 10%, pides la explicación. | Gmail + Google Sheets |
| 9 | Tú | Apruebas el preliminar por escrito en el mismo hilo. | Gmail |
| 10 | Contadora | Presenta las declaraciones y te manda acuse y línea de captura con su vigencia. | Portal del SAT |
| 11 | Tú | Pagas desde el apartado de Impuestos antes de la fecha límite y subes el comprobante (si la línea vence, pides una nueva). | Banca en línea + Google Drive |
| 12 | Asistente | Archiva acuses, cierra la página del mes y registra las dudas resueltas como reglas fiscales en Conocimiento. | Notion |

**Lo que conviene saber**

- **Comisiones deducibles (paso 5).** Arriba de $2,000 se paga por transferencia y con CFDI; se mide por erogación, así que partir el pago en pagos chicos no lo vuelve deducible, y pagar mal también hace perder el IVA acreditable. Ver [punto ciego 5](04-lo-que-te-falta.md#pc5) y [V13](04-lo-que-te-falta.md#v13).
- **Primer cierre (pasos 1 y 6).** El paquete de diciembre se manda a mano el lunes 4 de enero (el día 3 cae en domingo); Enlace entra desde el cierre de enero, el 1 de febrero de 2027.
- **La reserva depende del régimen (paso 8).** El paquete fiscal 2027 ya aprobado por el Congreso (tope de RESICO de persona física a 5 millones y opción de IVA de 7% sobre lo cobrado) no se había publicado en el DOF al 10 de noviembre; se revisa en la junta de régimen de la primera semana de diciembre. Ver [punto ciego 3](04-lo-que-te-falta.md#pc3) y [V3](04-lo-que-te-falta.md#v3).

<a id="flujo-6"></a>

## 6. Alta y baja de un setter independiente

| Paso | Actor | Acción | Herramienta |
|:-:|---|---|---|
| 1 | Tú | Pruebas al candidato con un role-play de 15 minutos con 3 objeciones reales. | Zoom |
| 2 | Tú / asistente | Creas la fila en Personas y accesos en «Alta solicitada» con el checklist de alta. | Notion |
| 3 | Tú | Firma de la carta provisional (confidencialidad, no solicitación, que leads y conversaciones son de la marca y comisión sobre lo cobrado según el Plan v1) y, desde enero, del contrato definitivo de servicios independientes o comisión mercantil con el Plan de compensación como anexo. | Google Docs + firma electrónica |
| 4 | Setter | Firma; regla dura: sin firma no hay accesos ni leads. | Firma electrónica |
| 5 | Tú / asistente | Accesos por rol: ManyChat Live Chat (asiento de Pipedrive solo si lo necesita), página de solo lectura «Cómo trabajamos» y número de la marca; nunca contraseñas compartidas ni exportaciones. | ManyChat + Notion + Pipedrive |
| 6 | Tú | Prueba de alta antes de tomar leads reales: 5 conversaciones de práctica con la rúbrica (es selección de proveedor, no supervisión; el abogado laboral la revisa junto con el modelo de operación). | ManyChat + Notion |
| 7 | Setter | Trabaja como independiente: toma leads de la cola cuando está disponible, sin horario, metas diarias, exclusividad ni formularios; recibe la lista opcional de oportunidades y un reporte semanal de resultados; coaching mensual voluntario. | ManyChat + correo de avisos@ |
| 8 | Tú / asistente | Baja: en 24 horas revocas ManyChat, Pipedrive, portafolio de Meta, Drive y dispositivos vinculados de WhatsApp, rotas contraseñas compartidas y reasignas sus leads. | Bitwarden + ManyChat + Pipedrive |
| 9 | Asistente | Liquidación final solo sobre lo cobrado, con clawbacks según el Plan y contra CFDI. | Google Sheets |

**Lo que conviene saber**

- **Lo que decide si es empleado (pasos 6 y 7).** El artículo 285 de la Ley Federal del Trabajo considera trabajadores a vendedores e impulsores de ventas cuando su actividad es permanente; lo que decide es la subordinación, y esa se ve en la operación (órdenes diarias, horarios, exclusividad, sanciones), no en el nombre del contrato. Ver [punto ciego 4](04-lo-que-te-falta.md#pc4) y [V10](04-lo-que-te-falta.md#v10).
- **Fechas (paso 3).** Carta provisional firmada antes del 30 de noviembre y contrato definitivo antes del 31 de enero. La regla «sin firma no hay accesos ni leads» aplica desde hoy para personas nuevas y desde el 31 de enero para todos.

<a id="flujo-7"></a>

## 7. Capacitación a empresas (solo si confirmas que hoy te pagan por eso)

| Paso | Actor | Acción | Herramienta |
|:-:|---|---|---|
| 1 | Tú / Setter | Propuesta de capacitación desde su plantilla: objetivo, temario, número de participantes, fechas, sede o en línea, precio más IVA y si la empresa pide constancias DC-3. | Google Docs + Pipedrive |
| 2 | Cliente / n8n | Firma y paga el anticipo; «Pago recibido» crea el Proyecto tipo Capacitación desde su plantilla. | Formulario «Pago recibido» + n8n + Notion |
| 3 | Asistente | Logística: fecha, sede o liga de Zoom, materiales y lista de participantes con los datos que pidan las constancias. | Google Calendar + Zoom + Google Drive |
| 4 | Tú | Impartes la capacitación y guardas la lista de asistencia firmada o el registro de asistencia de Zoom. | Zoom + Google Drive |
| 5 | Tú / asistente | Constancias DC-3 si las piden: llevan el número de registro del agente capacitador externo ante la STPS; confirma con tu contadora o abogado si te conviene registrarte (requisitos por confirmar). | Formatos de la STPS |
| 6 | Tú o el asistente | Factura del saldo según la regla fiscal escrita de la contadora. | Portal o PAC de la contadora |
| 7 | Asistente | Encuesta de 2 preguntas a participantes y patrocinador; con buen resultado, caso con permiso y propuesta del siguiente grupo. | Google Forms + Notion Clientes |

**Lo que conviene saber**

- **Solo si aplica.** Este flujo existe solo si confirmas que hoy te pagan por capacitar ([pregunta abierta 1](05-ruta-stack-riesgos.md#preguntas-abiertas)). Si hay capacitación o una comunidad de pago, ese flujo se diseña antes que cualquier agente.
- **Constancias DC-3 (paso 5).** Llevan el número de registro del agente capacitador externo ante la STPS. Si te conviene registrarte como agente capacitador y qué requisitos pide está por confirmar con tu contadora o abogado.

## Cadencias

Son las 15 cadencias de la arquitectura, agrupadas por frecuencia. En la columna Responsable, la flecha (→) quiere decir que el primero lo prepara y el segundo lo decide o lo recibe. Las de gestión cuentan contra tus 5 horas a la semana; el bloque de grabación es producción y el reporte y la demo de los viernes son entrega (ver [Presupuesto de tu tiempo: 5 horas de gestión a la semana](#presupuesto-de-tu-tiempo-5-horas-de-gestión-a-la-semana)).

### Diario (lunes a viernes)

| Actividad | Responsable |
|---|---|
| 7:10 mensaje único: plan del día (máximo 3 prioridades), aprobaciones agrupadas, salud del sistema, gasto anómalo de pauta y vencimientos fiscales de 7 días; lo ajustas en 5 minutos desde el celular | Gabinete → tú |
| 9:30 y 17:30: dos ventanas de aprobación de 10 minutos que absorben facturas, comisiones y liquidaciones; lo que coincide con algo ya aprobado no entra | Tú (el asistente dentro de su límite desde enero) |

Fuera de esas dos ventanas o en un bloque de grabación solo pueden interrumpirte las 3–5 emergencias P0 escritas en [pilares/automatizaciones/gabinete/CLAUDE.md](../pilares/automatizaciones/gabinete/CLAUDE.md#emergencias-p0); hoy están por definir y las eliges tú antes de encender el Gabinete (Fase 1, diciembre). Las tarjetas de Aprobaciones vencen a las 48 h y una tarjeta sin decisión pasa a tu siguiente ventana: nada escala a un puesto vacío.

### Semanal

| Tipo | Actividad | Responsable |
|---|---|---|
| Gestión | Lunes 9:00, junta única de 60 minutos: dinero (hoja de dinero, cartera y reserva), embudo y pauta (presupuesto y creativos de la semana), pipeline y recontactos, proyectos y cola de entrega, operación (fallas y máximo 2 automatizaciones nuevas) y 10 minutos de cambios a páginas canónicas | Tú (el Gabinete prepara; el asistente desde enero) |
| Gestión | Viernes, bloque de contenido de 45 minutos: temas, parrilla aprobada en lote y revisión semanal (semáforo de los 9 KPIs y 3 metas de la próxima semana) | Tú (el Gabinete deja lista la revisión) |
| Producción, no cuenta como gestión | Bloque de grabación en lote de 2–3 horas sin reuniones ni avisos salvo emergencias P0; meta: 3–4 semanas de videos en reserva | Tú (el Gabinete protege el bloque) |
| Entrega | Viernes: reporte de 5 líneas a cada cliente con la plantilla y demo de 30 minutos por proyecto | Asistente (reporte) y tú (demo) |

### Quincenal y mensual

| Actividad | Responsable |
|---|---|
| Días 1 y 16: corte de comisiones con CFDI validado antes de pagar. Días 1–3: cierre con paquete a la contadora el día 3 (o siguiente hábil); preliminar hacia el día 10 y pago antes del día 17 (o siguiente hábil) | Asistente, contadora y tú |

El cierre, paso por paso, está en el [flujo 5](#flujo-5).

### Mensual

| Actividad | Responsable |
|---|---|
| Checklist de 20 minutos: accesos y bajas, respaldo fuera de GitHub (últimos 3), datos personales y solicitudes ARCO, vencimientos (dominio, marca, líneas y tarjetas), calidad de la cuenta de anuncios y del número, suplantaciones, datos sucios en Pipedrive y descarga de Constancia y opinión de cumplimiento para el expediente de proveedor | Asistente → tú |
| Coaching voluntario de 30 minutos con setters, en grupo, con ejemplos de las 3 conversaciones por setter que leíste en el mes | Tú |

### Trimestral

| Actividad | Responsable |
|---|---|
| Revisión del sistema: metas, oferta, precios piso y capacidad con margen real, Plan de compensación y reglas de la cola, posicionamiento con 3 llamadas nuevas a clientes, simulacro del botón rojo, restauración de un respaldo y apagado de agentes sin uso en 30 días | Tú (el Gabinete prepara) |
| Junta con la contadora (enero, abril, julio y octubre): tasa de reserva, proyección de ISR y cambios fiscales; revisión con cada cliente con iguala | Tú, contadora y asistente |

### Anual

| Cuándo | Actividad | Responsable |
|---|---|---|
| Diciembre | Decisión del régimen del año siguiente con 4 escenarios y compras deducibles antes del 31 si tu régimen lo permite | Tú y la contadora |
| Enero | Recalibrar la tasa de reserva, revisar vigencias de e.firma y sello digital (CSD) y presentar el aviso de cambio de régimen si aplica (fecha por confirmar con la contadora) | Contadora y asistente |
| Abril | Declaración anual de persona física (deducciones personales juntadas desde enero) | Contadora y tú |
| Mes por definir (lo fijas con el abogado) | Revisión con el abogado (contratos, aviso de privacidad y cambios de ley), renovaciones (dominio y póliza si la contratas; la marca cada 10 años) y tu protección como independiente (gastos médicos mayores, incorporación voluntaria al IMSS y ahorro para el retiro) | Tú con el abogado y la contadora |

### Disparadores con calendario de los agentes

Además de las cadencias, algunos agentes despiertan por fecha u hora. Esta tabla junta esos disparadores de la [tabla de agentes del README](../README.md#tabla-de-agentes-y-automatizaciones) y dice si gastan una corrida de Claude (ver [Presupuesto de corridas de Claude](#presupuesto-de-corridas-de-claude)).

| Cuándo | Agente | Qué hace | Desde | ¿Gasta corrida de Claude? |
|---|---|---|---|---|
| Lunes a viernes, 7:10 | Gabinete | El mensaje único del día | Fase 1 (diciembre), después de comprobar que el conector de Google Calendar aparece en la rutina | Sí: es la única corrida programada del día |
| Lunes a viernes, 8:00 | Pulso (versión «oportunidades») | n8n manda a cada setter, desde avisos@ con plantilla preaprobada, la lista opcional de oportunidades disponibles | Desde el 11 de enero y solo con 2 o más setters | No: es n8n |
| Lunes, 7:10 | Pulso (reporte semanal) y Brújula | Reporte semanal de resultados por setter; embudo de punta a punta con 3 decisiones propuestas para la junta | Pulso, desde el 11 de enero con 2 o más setters; Brújula, con 4 semanas de datos (febrero de 2027); hasta entonces el Gabinete cuenta los 9 KPIs con filtros de Pipedrive | No es corrida aparte: va dentro de la del Gabinete |
| Lunes, y días 1 y 2 de cada mes | Concilia (pestaña de la hoja de dinero) | El asistente revisa cada lunes, en 15 minutos, la pestaña con el CSV del banco | Con el asistente (enero); como agente solo al pasar de ~40 movimientos al mes | No: es manual |
| Lunes, en la junta de las 9:00 | Pauta (hoja de decisión) | Decide la pauta una vez por semana: costo por lead calificado contra el tope de cada campaña, frecuencia y creativos; propone pausar, duplicar o escalar con su impacto en pesos. Lo diario lo hace la regla automática de tope diario de Ads Manager | Hoy, hoja de decisión en la junta del lunes; como revisión diaria con alertas dentro del mensaje de las 7:10 solo cuando gastes más de ~$1,000 MXN al día | No: es manual; la revisión diaria, cuando entre, va dentro de la corrida del Gabinete |
| Lunes, en la junta de las 9:00 | Alcancía (pestaña de la hoja de dinero) | Transferencia sugerida al apartado de Impuestos y flujo de caja a 13 semanas; n8n agrega la fila de reserva con cada «Pago recibido» y nunca mueve dinero | Pestaña de la hoja de dinero; como agente solo al pasar de ~40 movimientos al mes | No: es manual |
| Viernes | Guardián (plantilla) | Reporte de 5 líneas a cada cliente; lo envía el asistente | Plantilla desde Fase 1; se automatiza como borrador con 2 proyectos simultáneos | No: es manual |
| Viernes | Guionista | Lo invocas en el chat «Marketing y marca» al abrir el bloque de contenido: 6–8 temas y guiones de los que apruebas | Fase 2, con 4 semanas de parrilla hecha a mano y el ranking de Brújula. Por confirmar: no está entre los 7 agentes que se encienden hasta marzo ([01-arquitectura.md](01-arquitectura.md#por-definir-o-por-confirmar)) | No: es una sesión de chat |
| Viernes, con la parrilla aprobada | Cartero (plantilla) | El editor o el asistente programan en Blotato la parrilla aprobada y mueven la ficha a «Programada» | Se automatiza solo si publicas 6 o más piezas por semana durante 4 semanas y programar toma más de 1 hora | No: es manual |
| Días 1 y 16 de cada mes | Reparto (pestaña de la hoja de dinero) | Corte de comisiones sobre lo cobrado sin IVA, con CFDI validado antes de pagar | Lo corta el asistente; como agente solo al pasar de 15 comisiones al mes | No: es manual |
| Días 1 y 3 de cada mes | Enlace | Día 1: página «Cierre AAAA-MM»; día 3 (o siguiente hábil): borrador del paquete para la contadora | Desde el cierre de enero, el 1 de febrero de 2027. Qué pasa cuando el día 1 cae en sábado o domingo: por definir, porque la rutina solo corre de lunes a viernes | No es corrida aparte: va dentro de la del Gabinete |
| Día 1 de cada mes | Cobra (igualas) | Factura de cada iguala activa con el resumen de horas usadas | La factura mensual automática de igualas, en Fase 3 | Por definir en su ficha |
| Primera semana de cada mes | Lupa, Aduana y Vigía (plantilla o checklist) | Lupa: lees 3 conversaciones por setter con la rúbrica. Aduana: datos sucios en Pipedrive. Vigía: cuenta publicitaria, número, respaldo, vencimientos y suplantaciones | Hoy como plantilla o checklist. Como agentes: Lupa, solo con 4 o más setters y si ManyChat permite exportar historiales de conversación (por confirmar); Aduana y Vigía, solo si el volumen lo justifica (Fase 3) | No: es manual |
| Primer lunes de cada mes | Altavoz | Lista de 10–15 oportunidades de audiencias prestadas y borradores de propuesta | Fase 3 (abril de 2027) | Por definir en su ficha |
| Primer martes de cada mes | Boca a Boca | Carril de referidos con plantilla aprobada por Meta, con costo calculado y su Aprobación | Fase 3 (abril de 2027) | Por definir en su ficha |
| Martes de por medio | Boletín | Borrador del correo quincenal y del mensaje del Canal de WhatsApp | Fase 3 (abril de 2027) | Por definir en su ficha |
| Día 60 después de cada entrega | Eco | Llamada a los 60 días con oferta de iguala | Fase 3; antes, un recordatorio en Calendar que disparas a mano | Por definir en su ficha |

## Tu semana tipo

Así se acomodan en tu semana los bloques con día u hora fijos, ya con el sistema completo: el mensaje de las 7:10 llega desde que se enciende el Gabinete (Fase 1, diciembre). Lo que la arquitectura no fija está marcado como por definir.

| Cuándo | Bloque | Duración | ¿Cuenta como gestión? |
|---|---|---|---|
| Lunes a viernes, 7:10 | Lees y ajustas desde el celular el mensaje del Gabinete | 5 minutos | Sí |
| Lunes a viernes, 9:30 y 17:30 | Ventanas de aprobación | 10 minutos cada una | Sí |
| Lunes, 9:00 | Junta única: dinero, embudo y pauta, pipeline y recontactos, proyectos y cola de entrega, operación y cambios a páginas canónicas | 60 minutos | Sí |
| Viernes (hora por definir) | Bloque de contenido: temas, parrilla aprobada en lote y revisión semanal | 45 minutos | Sí |
| Viernes (hora por definir) | Demo con cada cliente | 30 minutos por proyecto | No: es entrega |
| Día y hora por definir | Bloque de grabación en lote, sin reuniones ni avisos salvo emergencias P0 | 2–3 horas | No: es producción |
| Según tu agenda | Llamadas de descubrimiento y de cierre | Sin duración fija | No: es venta |

- **Choque del lunes.** La ventana de 9:30 cae dentro de la junta de 9:00 a 10:00. Cómo se acomoda está por definir: lo decides tú al crear los bloques fijos en Calendar.
- **Esta semana** creas en Google Calendar los bloques fijos de grabación, las ventanas de 9:30 y 17:30 y los bloques «Gestión» (primer paso del [punto ciego 13](04-lo-que-te-falta.md#pc13)).

## Presupuesto de tu tiempo: 5 horas de gestión a la semana

**La regla** ([principio 11](01-arquitectura.md#principios)): tu tiempo es el recurso escaso: 5 horas de gestión a la semana o menos, medidas con bloques «Gestión» en Calendar; si la cola de entrega pasa de 4 semanas, se frena la venta antes que la calidad. El primer diseño de este sistema sumaba más de 9 horas de rituales a la semana; por eso las cadencias se rehicieron con este presupuesto ([punto ciego 13](04-lo-que-te-falta.md#pc13)).

**Cómo se mide.** Cada bloque de gestión va en Google Calendar como «Gestión». El Gabinete los suma y te da el total los lunes; es uno de los 9 KPIs del Tablero del CEO (meta ≤5 por semana) y criterio de éxito de las Fases 1, 2 y 3.

| Bloque | Frecuencia | Por vez | Por semana |
|---|---|--:|--:|
| Mensaje de las 7:10 (lo ajustas desde el celular) | Lunes a viernes | 5 min | 25 min |
| Ventanas de aprobación de 9:30 y 17:30 | Lunes a viernes, 2 al día | 10 min | 100 min |
| Junta única del lunes | Semanal | 60 min | 60 min |
| Bloque de contenido del viernes, con la revisión semanal | Semanal | 45 min | 45 min |
| **Subtotal semanal** | | | **230 min (3 h 50 min)** |
| Excepciones de la hoja de dinero ([flujo 5](#flujo-5), paso 4) | Mensual | 15 min | ≈3.5 min |
| Checklist mensual (Asistente → tú) | Mensual | 20 min | ≈4.6 min |
| Coaching voluntario con setters | Mensual | 30 min | ≈6.9 min |
| **Total de lo que tiene duración fija** | | | **≈245 min (≈4 h 05 min)** |

Lo mensual se reparte entre 4.33 semanas (52 ÷ 12). La arquitectura estima alrededor de 4.5 horas de gestión a la semana en total; lo que tiene duración fija suma unas 4 h 05 min. Para lo que no tiene duración fija (lista de abajo) quedan, según cuál de las dos cuentas uses, entre 30 y 55 minutos antes de llegar a 5 horas.

**Lo que no tiene duración fija** (tiene que caber en lo que queda hasta las 5 horas):

- Revisar y enviar el correo a la contadora ([flujo 5](#flujo-5), paso 7), aprobar por escrito el preliminar de ISR e IVA (paso 9) y pagar desde el apartado de Impuestos (paso 11).
- Pagar por SPEI las comisiones después del corte de los días 1 y 16 (paso 5).
- Leer 3 conversaciones por setter al mes para el coaching (Lupa, hoy manual).
- Contestar lo que el Gabinete marca «Pregunta CEO».
- La revisión trimestral del sistema, la junta trimestral con la contadora y las revisiones anuales: cuentan en tus bloques «Gestión» de la semana en que caen; su duración está por definir (la fijas al agendarlas; la trimestral la prepara el Gabinete).

**Lo que no cuenta como gestión** (es el trabajo que la gestión protege; la visión es que dediques la semana a grabar, cerrar y construir):

- El bloque de grabación en lote de 2–3 horas (producción).
- El reporte de 5 líneas y la demo de 30 minutos por proyecto de los viernes (entrega).
- Las llamadas de descubrimiento y de cierre (venta) y el desarrollo (construir).

**Qué evita que se dispare:**

- Aprobación por excepción: lo que coincide con algo ya aprobado no se vuelve a aprobar (factura igual a la propuesta aprobada, recordatorio con plantilla aprobada, publicación dentro de la parrilla aprobada, respuestas del bot cuando la persona escribe primero y presupuesto semanal de pauta ya aprobado).
- Las dos ventanas absorben facturas, comisiones y liquidaciones; una tarjeta sin decisión vence a las 48 h y pasa a tu siguiente ventana.
- Desde enero el asistente decide dentro de su límite bajo y puede pausar todo, nunca reactivar.
- Solo las 3–5 emergencias P0 pueden interrumpirte fuera de ventana o en un bloque de grabación.

**Antes de enero.** Hasta que entre el asistente, lo que él hará lo haces tú: registrar «Pago recibido», cobranza, paquete de la contadora, higiene de Pipedrive, reportes semanales a clientes y Bandeja de Tareas. Del 12 de diciembre al 6 de enero se trabaja a mano (propuestas, facturas, cobranza y kickoff con sus plantillas). Los criterios de Fase 1, incluidas tus horas de gestión ≤5 por semana, se miden del 11 al 31 de enero.

**Si te pasas de 5 horas.** La arquitectura lo mide, pero no fija qué se recorta: por definir. Lo decides tú en la junta del lunes en que el Gabinete reporte más de 5 horas.

## Presupuesto de corridas de Claude

Las tareas programadas (rutinas) de Claude Code en la nube tienen tope diario de corridas por cuenta. Están en research preview y el tope puede cambiar; antes de Fase 1 confirma los precios en claude.com/pricing y el tope en la documentación de rutinas (code.claude.com/docs/en/routines). Datos verificados en [V2](04-lo-que-te-falta.md#v2), [V8](04-lo-que-te-falta.md#v8) y [V15](04-lo-que-te-falta.md#v15).

| Plan | Tope de corridas al día | Precio aproximado |
|---|:-:|---|
| Pro | 5 | US$20 al mes |
| **Max (recomendado)** | **15** | **US$100 al mes, solo pago mensual** |
| Ultra | No se encontró (por confirmar) | US$200 al mes, solo pago mensual |
| Team/Enterprise | 25 | Por confirmar (la arquitectura no lo trae) |

Lo que tienes que saber de las rutinas:

- Cuentan las corridas por horario y también las que dispara n8n por API.
- Cada corrida gasta del mismo uso de la suscripción con el que desarrollas.
- Hay un intervalo mínimo de una hora entre corridas de una misma rutina.
- Son de tu cuenta individual: lo que hacen aparece a tu nombre.
- Traen por defecto todos tus conectores con permiso de escritura: a cada una se le dejan solo los que usa.
- Las llaves van como secretos de red (network secrets) del entorno en la nube; nunca en el repo, en variables de entorno ni en Notion.
- Hay reportes abiertos de conectores de Google (Gmail, Calendar y Drive) que no aparecen al configurar rutinas en la nube: prueba que Google Calendar aparezca en la rutina del Gabinete antes de depender de ella.

**La regla del diseño:** 1 tarea programada al día (Gabinete, 7:10) más eventos, con meta de 8 o menos de las 15 diarias del plan Max; ningún barrido ni revisión de estado corre en Claude si n8n puede hacerlo sin IA, y las corridas sin novedad no escriben en Bitácora y planes. El primer diseño sumaba 13–19 corridas al día: es la corrección más grande que dejó la verificación ([V2](04-lo-que-te-falta.md#v2)).

| Qué despierta a Claude | Cómo | Corridas | Conectores o herramientas | Desde |
|---|---|---|---|---|
| Gabinete (los lunes incluye el reporte semanal de Pulso y Brújula; los días 1 y 3, Enlace; y, cuando gastes más de ~$1,000 MXN al día, la revisión diaria de Pauta) | Tarea programada de lunes a viernes a las 7:10 (`CRON_TZ=America/Mexico_City`) | 1 al día, de lunes a viernes | Notion, Google Calendar (lectura) y Pipedrive (lectura); al encender Brújula, Pulso, Enlace o la revisión diaria de Pauta, la corrida suma sus conectores y sus bases (ficha final por confirmar; nota 4 de la tabla del README) | Fase 1 (diciembre) |
| Andamio | Rutina que n8n dispara por API con «Pago recibido» (plan B: n8n crea la Tarea, te avisa y abres la sesión con un toque) | 1 por disparo; cuenta contra el tope | GitHub y Notion | Con el siguiente proyecto vendido |
| Cobra | Por evento: «Pago recibido», hito aceptado o día 1 de cada iguala activa | Por definir: si n8n lo dispara por API, cada evento cuenta contra el tope | Los de su ficha | Fase 2 |
| Cierre, Arquitecto y los demás agentes de chat | n8n deja una Tarea y tú abres la sesión del chat | 0: no son tareas programadas, pero sus sesiones gastan la misma cuota de uso | Los del CLAUDE.md de su pilar | Según su condición |
| Inspector | Check de GitHub Actions con claude-code-action en cada PR | 0: no es una tarea programada. Si gasta API o la cuota de tu suscripción depende de cómo se configure la acción: por definir al encenderlo | GitHub Actions + claude-code-action, Playwright y gitleaks | Con el siguiente proyecto vendido |
| Repartidor, Pulso (8:00), Centinela, Filtro y Portero | Flujos de n8n sin IA | 0 | No aplica: no usan conectores de Claude | Repartidor y Centinela, Fase 1; Pulso, desde el 11 de enero; Filtro y Portero, Fase 2 |

Cuántas corridas hay en un día:

| Día | Programadas | Por evento | Total |
|---|:-:|---|:-:|
| Hoy (Fase 0) | 0 | 0 | 0 |
| Lunes a viernes, desde que se enciende el Gabinete (Fase 1) | 1 | 0 | 1 |
| Sábado y domingo | 0 | Solo si hay un evento | 0 o más |
| Lunes a viernes con «Pago recibido» de un proyecto nuevo (con Producto encendido) | 1 | 1 (Andamio) | 2 |
| Desde Fase 2 | 1 | Andamio y, si se implementa por API, Cobra | Meta: 8 o menos de 15 |

- **Cómo se mide.** KPI «Corridas de Claude por día (programadas más eventos)»: meta ≤8 de las 15 del plan Max, con el historial de rutinas, cada semana. Es criterio de éxito de la Fase 1 (del 11 al 31 de enero).
- **Si algo falla.** Cada disparo por API tiene su plan B: n8n crea la Tarea, te avisa y abres la sesión con un toque. Si el mensaje de las 7:10 no llega, eso ya es una falla (Centinela), y la rutina se recrea con las instrucciones de [su archivo](../pilares/automatizaciones/gabinete/CLAUDE.md).
- **Qué plan.** Max. Según la arquitectura, Pro no alcanza ni para la Fase 1 (tope de 5 corridas al día; la meta del diseño admite hasta 8), y cada corrida gasta de la misma cuota con la que desarrollas. Si te falta uso, Ultra (tope por confirmar). Tu plan actual está por confirmar ([pregunta abierta 6](05-ruta-stack-riesgos.md#preguntas-abiertas)).
- **Fase 3.** Boletín (martes de por medio), Altavoz (primer lunes del mes), Boca a Boca (primer martes del mes) y Eco (día 60 después de la entrega) tienen disparador de calendario. Brújula y Enlace, por ejemplo, van dentro de la corrida del Gabinete; cómo corren estos cuatro sin romper la regla de 1 tarea programada al día está por definir en la ficha de cada uno, antes de encenderlos.

## Por definir en este documento

Lo que este documento deja abierto, con quién o cuándo se cierra. Hasta que se defina, cada agente lo trata como «Pregunta CEO». La lista completa del sistema está en [01-arquitectura.md](01-arquitectura.md#por-definir-o-por-confirmar).

| Qué | Quién o cuándo |
|---|---|
| Día y hora del bloque de grabación y hora del bloque de contenido y de las demos del viernes | Tú, esta semana, al crear los bloques fijos en Google Calendar ([punto ciego 13](04-lo-que-te-falta.md#pc13)) |
| Cómo se acomoda la ventana de 9:30 de los lunes, que cae dentro de la junta de 9:00 a 10:00 | Tú, al crear esos bloques |
| Qué cuenta como «horario hábil» para la reasignación de 30 minutos del Repartidor | Tú, antes de construir el flujo (Fase 1, del 1 al 11 de diciembre) |
| Horario permitido y tope de mensajes por contacto que revisa Filtro | Tú, antes de encender Filtro (Fase 2) |
| Las 3–5 emergencias P0 que pueden interrumpirte | Tú, antes de encender el Gabinete (Fase 1, diciembre), por PR a [gabinete/CLAUDE.md](../pilares/automatizaciones/gabinete/CLAUDE.md#emergencias-p0) |
| Qué se recorta si tus horas de gestión pasan de 5 | Tú, en la junta del lunes en que el Gabinete lo reporte |
| Duración de la revisión trimestral, de la junta trimestral con la contadora y de las revisiones anuales | Tú, al agendarlas |
| Mes de la revisión anual con el abogado | Tú, con el abogado |
| Fecha del aviso de cambio de régimen, si aplica | Por confirmar con la contadora (enero) |
| Si Cobra corre como Tarea o con disparo por API (y cuántas corridas suma) | En su ficha, antes de encenderlo (Fase 2) |
| Cómo corren Boletín, Altavoz, Boca a Boca y Eco | En la ficha de cada uno, antes de encenderlos (Fase 3) |
| Qué hace Enlace cuando el día 1 cae en sábado o domingo, porque la rutina del Gabinete solo corre de lunes a viernes | Tú, antes de encender Enlace (1 de febrero de 2027); queda escrito en [gabinete/CLAUDE.md](../pilares/automatizaciones/gabinete/CLAUDE.md) |
| Si Guionista (y Voz como skill) entran en Fase 2 aunque no estén entre los 7 agentes que se encienden hasta marzo | Tú, antes de encender cualquiera de los dos ([01-arquitectura.md](01-arquitectura.md#por-definir-o-por-confirmar)) |
| Si el Inspector gasta API o la cuota de tu suscripción | Al configurar claude-code-action, con el siguiente proyecto vendido |
| Conectores y bases finales de la rutina del Gabinete al sumar Brújula, Pulso, Enlace y la revisión diaria de Pauta | Por confirmar al encender cada uno (nota 4 de la [tabla del README](../README.md#tabla-de-agentes-y-automatizaciones)) |
| Tope de corridas del plan Ultra y tu plan actual de Claude | Por confirmar: el tope, en la documentación de rutinas y en claude.com/pricing; tu plan, con la pregunta abierta 6 (semana del 16 de noviembre) |
| Si te conviene registrarte como agente capacitador ante la STPS (constancias DC-3) y sus requisitos | Por confirmar con tu contadora o abogado, solo si confirmas que vendes capacitación |

