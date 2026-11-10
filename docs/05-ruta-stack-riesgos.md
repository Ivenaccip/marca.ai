# Ruta, stack y riesgos

La ruta por fases de noviembre de 2026 a junio de 2027, con la duración, los entregables y el criterio de éxito de cada fase; el stack recomendado con su costo aproximado; los 13 riesgos con su mitigación y las 7 preguntas abiertas. La fuente es [data/arquitectura.json](../data/arquitectura.json) (campos `roadmap`, `stack_recomendado`, `riesgos` y `preguntas_abiertas`) y los datos verificados con fuentes al 10 de noviembre de 2026 están en [data/verificacion.json](../data/verificacion.json). Si algo de este documento no cuadra con esos archivos, mandan ellos.

**Mapa visual interactivo del sistema:** https://claude.ai/artifact/FtyWRkr6M2jFp4Mnu5BFDN

> Estado al 10 de noviembre de 2026: arranca la Fase 0 (10 al 30 de noviembre), sin agentes. Lo que vence primero: las líneas de prepago con terminación 6 deben quedar vinculadas a la CURP a más tardar el domingo 15 de noviembre; confírmalo con tu compañía ([punto ciego 1](04-lo-que-te-falta.md#pc1)).

## Contenido

1. [Ruta por fases](#ruta-por-fases)
   - [Fase 0. Cimientos de negocio: solo lo que tiene fecha o protege dinero](#fase-0)
   - [Fase 1. Un flujo automatizado, el dinero con dueño y el primer ayudante](#fase-1)
   - [Fase 2. Automatiza lo repetido y entrega como sistema](#fase-2)
   - [Fase 3. Recurrencia, referidos y una semana fuera](#fase-3)
2. [Stack recomendado](#stack-recomendado)
3. [Riesgos](#riesgos)
4. [Preguntas abiertas](#preguntas-abiertas)

Documentos hermanos: [README](../README.md) (estado actual y tabla de agentes), [01-arquitectura.md](01-arquitectura.md) (visión, pilares y orquestación), [02-cerebro-notion.md](02-cerebro-notion.md) (las 10 bases), [03-flujos-y-ritmo.md](03-flujos-y-ritmo.md) (flujos, cadencias y presupuestos de tiempo y corridas) y [04-lo-que-te-falta.md](04-lo-que-te-falta.md) (puntos ciegos y datos verificados).

## Ruta por fases

| Fase | Nombre | Duración |
|---|---|---|
| [Fase 0](#fase-0) | Cimientos de negocio: solo lo que tiene fecha o protege dinero | 3 semanas (10 al 30 de noviembre de 2026); sin agentes |
| [Fase 1](#fase-1) | Un flujo automatizado, el dinero con dueño y el primer ayudante | 9 semanas (1 de diciembre de 2026 al 31 de enero de 2027); los criterios se miden del 11 al 31 de enero |
| [Fase 2](#fase-2) | Automatiza lo repetido y entrega como sistema | 2 meses (1 de febrero al 31 de marzo de 2027) |
| [Fase 3](#fase-3) | Recurrencia, referidos y una semana fuera | 13 semanas (abril a junio de 2027) |

Reglas que cruzan todas las fases: a mano 5–10 veces con plantilla antes de automatizar; máximo 2 automatizaciones nuevas por semana; ningún agente se enciende sin cumplir su condición y sin su ficha completa en la [tabla del README](../README.md#tabla-de-agentes-y-automatizaciones); y tus horas de gestión ≤5 por semana, que son criterio de éxito de las Fases 1, 2 y 3 (la Fase 0 se mide por trámites cerrados; ver el [presupuesto de tu tiempo](03-flujos-y-ritmo.md#presupuesto-de-tu-tiempo-5-horas-de-gestión-a-la-semana)).

<a id="fase-0"></a>

### Fase 0. Cimientos de negocio: solo lo que tiene fecha o protege dinero

**Duración:** 3 semanas (10 al 30 de noviembre de 2026); sin agentes.

**Entregables**

| # | Cuándo | Entregable |
|:-:|---|---|
| 1 | Hoy al domingo 15 de noviembre | Cada línea de WhatsApp del negocio vinculada a la CURP del titular correcto (las de prepago con terminación 6 vencen el 15; confírmalo con tu compañía), PIN de verificación en dos pasos activo y decisión por número: API de ManyChat, coexistencia o se queda en la app |
| 2 | Semana del 16 de noviembre | Candados (Bitwarden con acceso de emergencia; 2FA sin SMS en Gmail, Meta, banco, Pipedrive, ManyChat, GitHub y Claude; segundo administrador en Meta), persona de confianza nombrada y tabla de cuentas críticas a nombre de la marca |
| 3 | Semana del 16 de noviembre | Cita con la contadora para la primera semana de diciembre con 4 temas (simulación 2027 con 4 escenarios, cómo facturar anticipos e hitos, qué necesita cada mes y tratamiento fiscal de setters), opinión de cumplimiento descargada y respuestas a las 7 preguntas abiertas, empezando por qué vendes y a qué ticket (si hay capacitación o comunidad, ese flujo se diseña antes que cualquier agente) |
| 4 | Semana del 16 de noviembre | Búsqueda de tu marca en MARCia (clases 35, 41 y 42) y etiquetado de tus repos como «mío», «de cliente» o «dudoso» |
| 5 | Semana del 23 de noviembre | Oferta en una página (Diagnóstico pagado, Implementación e Iguala con precio de lista más IVA, precio piso, esquema de pago, capacidad máxima y próxima fecha de arranque) enviada a los setters ese mismo día, y 3 llamadas de 20 minutos con tus mejores clientes (posicionamiento, testimonio con permiso y referido) que terminan en la página de Posicionamiento |
| 6 | Antes del 30 de noviembre | Plan de compensación v1 con tus últimas 10 ventas, carta provisional firmada por cada setter y el editor, y abogado contratado (laboral con el modelo de operación completo, contrato marco, NDA y aviso de privacidad) con entrega antes del 15 de enero |
| 7 | Antes del 30 de noviembre | Cuenta del negocio con apartado de Impuestos, hoja de dinero (cobros, reserva, comisiones y flujo de 13 semanas), regla escrita para setters («un pago existe cuando aparece en mi banca») y carpeta «Expediente de proveedor» |
| 8 | Antes del 30 de noviembre | Pipedrive con etapas canónicas y campos obligatorios (fuente de lista cerrada, setter, hora de entrada, motivo de pérdida con fecha de recontacto, precio más IVA y campos de traspaso), entrada de leads manuales y una página web simple con la oferta, el aviso de privacidad integral y el botón a WhatsApp o a tu agenda (la haces en una tarde) |

**Qué se enciende:** ningún agente. Dos checklists se aplican a mano desde ya: Voz (una página con la que revisas guiones, copys y respuestas contra la Guía de voz, las promesas prohibidas y las políticas de anuncios de Meta) y Llavero (alta y baja de accesos y tabla de cuentas críticas; hoy lo ejecutas tú y, desde enero, también el asistente). El repo con sus instrucciones ya existe, pero los chats, las 10 bases de Notion y los flujos de n8n se construyen en Fase 1.

**Criterio de éxito.** Al 30 de noviembre, medido por trámites cerrados y no por sistema construido:

- [ ] Ninguna línea suspendida
- [ ] Cero cuentas críticas protegidas solo con SMS o a nombre de terceros
- [ ] 100% de setters y editor con carta provisional firmada
- [ ] Oferta de una página en manos de los setters
- [ ] Abogado contratado con fecha de entrega
- [ ] Junta de régimen agendada
- [ ] Página web con aviso integral publicada

<a id="fase-1"></a>

### Fase 1. Un flujo automatizado, el dinero con dueño y el primer ayudante

**Duración:** 9 semanas (1 de diciembre de 2026 al 31 de enero de 2027); los criterios se miden del 11 al 31 de enero.

**Entregables**

| # | Cuándo | Entregable |
|:-:|---|---|
| 1 | 1 al 11 de diciembre | Un solo flujo automatizado nuevo: ManyChat (aviso simplificado, «Acepto», calificación y agenda directa para leads A) → n8n → Pipedrive con lead_id, cola con dueño sincronizado en Live Chat y reasignación a los 30 minutos, LeadSubmitted a Meta (nativo en Instagram y Messenger; desde n8n en WhatsApp), formulario de lead manual y 2–3 plantillas de reapertura de la ventana de 24 horas aprobadas por Meta (con su costo sumado al costo comercial) |
| 2 | 1 al 11 de diciembre | Evento «Pago recibido» (formulario de 3 campos y webhook de Stripe) que pasa el deal a «Ganado» y crea el Proyecto desde la plantilla «Proyecto ganado» (checklist de kickoff, recordatorio en Calendar por cada pago de hito, acta con aceptación tácita, encuesta, testimonio y referido) |
| 3 | Diciembre | Notion con las 10 bases mínimas, CLAUDE.md raíz, skills /inicio, /cierre y /pedir-aprobacion, el chat «Ventas» y el chat «Automatizaciones y Gabinete» con el mensaje único de las 7:10; flujo de errores de n8n por correo y botón rojo |
| 4 | Primera semana de diciembre | Junta de régimen con la contadora y regla fiscal escrita para anticipos e hitos; antes del 31, compras deducibles si tu régimen lo permite y solicitud de marca ante el IMPI |
| 5 | Primera semana de diciembre | Vacante del asistente de operación y administración de medio tiempo publicada |
| 6 | 12 de diciembre al 6 de enero | Sin escalar pauta; cierra lo que ya está en propuesta (algunas empresas quieren ejercer presupuesto antes de fin de año) y haz a mano propuestas, facturas, cobranza y kickoff con sus plantillas |
| 7 | Lunes 4 de enero | Paquete de diciembre a la contadora (primer cierre hecho a mano) |
| 8 | Enero | Entra el asistente (suplente con límites bajos, «Pago recibido», cobranza, paquete de la contadora, higiene de Pipedrive, reportes semanales a clientes y Bandeja de Tareas) y se firman los contratos definitivos antes del 31 |
| 9 | Desde el 11 de enero | Pauta optimizada por lead calificado con tope de costo, regla automática de tope diario y decisiones solo en la junta del lunes; Pulso en versión «oportunidades» si tienes 2 o más setters |

**Qué se enciende:** los chats «Ventas» y «Automatizaciones y Gabinete». Agentes: Anfitrión (1 al 11 de diciembre) y Gabinete (diciembre, después de comprobar que el conector de Google Calendar aparece en la rutina); Pulso, desde el 11 de enero y solo con 2 o más setters. Reglas de n8n sin IA: Repartidor y Centinela en versión mínima (correo de errores de n8n). Como plantilla, a mano: Bienvenida («Proyecto ganado»), Guardián y Entrega desde Fase 1, y Notario con las plantillas del abogado desde enero.

**Criterio de éxito.** Del 11 al 31 de enero:

- [ ] ≥90% de leads con fuente trazable (lo cuenta el Gabinete cada lunes con un filtro de Pipedrive)
- [ ] Mediana de primera respuesta humana ≤15 minutos hábiles en leads A
- [ ] 100% de los pagos registrados como «Pago recibido» en 1 día hábil o menos
- [ ] Cero comisiones pagadas sin CFDI
- [ ] Paquete de diciembre enviado el 4 de enero
- [ ] Contratos definitivos firmados
- [ ] Tus horas de gestión ≤5 por semana (bloques «Gestión»)
- [ ] 8 o menos corridas de Claude al día

<a id="fase-2"></a>

### Fase 2. Automatiza lo repetido y entrega como sistema

**Duración:** 2 meses (1 de febrero al 31 de marzo de 2027).

**Entregables**

| # | Entregable |
|:-:|---|
| 1 | Automatiza solo lo que ya hiciste 5–10 veces igual: Cierre (borrador de propuesta desde la transcripción, desde la quinta propuesta), Cobra en borradores (después de 5–10 facturas a mano) y recordatorios de cobro con plantilla preaprobada desde cobranza@ vía n8n, ya con Filtro y Portero |
| 2 | Enlace desde el cierre de enero (1 de febrero) y Brújula como reporte semanal en cuanto haya 4 semanas de datos |
| 3 | Producto con el siguiente proyecto vendido: Arquitecto disparado por «Pago recibido» o «Diagnóstico pagado», Andamio con su plan B, Escuadrón e Inspector; censo de repos por derechos del Arqueólogo |
| 4 | Bienvenida, Guardián y Entrega siguen como plantillas y se automatizan cuando haya 2 proyectos simultáneos |
| 5 | Abre otro chat (Producto y clientes, Marketing y marca o Administración y legal) solo si su pilar ya tiene trabajo cada semana |
| 6 | Centinela con Healthchecks.io y Telegram cuando haya 5 flujos críticos; cotización de seguro de responsabilidad civil profesional y ciberriesgo |

**Qué se enciende:** Cierre (desde la quinta propuesta hecha a mano), Cobra en borradores (después de 5–10 facturas a mano y con la regla fiscal escrita), Enlace (1 de febrero) y Brújula (con 4 semanas de datos); Filtro y Portero, reglas de n8n, con el primer envío automático; Arquitecto, Andamio, Escuadrón e Inspector con el siguiente proyecto vendido, y el censo de repos del Arqueólogo; Centinela con Healthchecks.io y Telegram cuando haya 5 flujos críticos. Guionista (con 4 semanas de parrilla hecha a mano y el ranking de Brújula) y Voz como skill del chat tienen condición de Fase 2, pero no están entre los 7 agentes que se encienden hasta marzo: si entran como excepción o esperan está por confirmar ([01-arquitectura.md](01-arquitectura.md#por-definir-o-por-confirmar)). Otro chat (Producto y clientes, Marketing y marca o Administración y legal) se abre solo si su pilar ya tiene trabajo cada semana.

**Criterio de éxito.**

- [ ] 2 proyectos de «Pago recibido» a acta firmada con desviación de estimación ≤1.15
- [ ] Cero facturas canceladas por método o datos equivocados
- [ ] 100% de recordatorios de cobro salidos de plantillas aprobadas
- [ ] Cola de entrega ≤4 semanas (o pauta pausada según la regla)
- [ ] Horas de gestión ≤5 por semana

<a id="fase-3"></a>

### Fase 3. Recurrencia, referidos y una semana fuera

**Duración:** 13 semanas (abril a junio de 2027).

**Entregables**

| # | Entregable |
|:-:|---|
| 1 | Referidos con plantillas aprobadas por Meta (Boca a Boca) y links wa.me con código por referidor; Eco automatiza la encuesta al firmar el acta |
| 2 | Iguala con factura mensual automática el día 1 (Cobra) y resumen de horas usadas |
| 3 | Boletín (lista propia) y Altavoz (audiencias prestadas) |
| 4 | Vigía, Escudo y Aduana como agentes solo si el volumen lo justifica (si no, siguen como checklist mensual de 20 minutos); respaldo con restauración de prueba |
| 5 | Declaración anual de abril presentada sin sorpresas |
| 6 | Coordinador de proyectos si los reportes semanales se atrasan; líder de setters desde 3 setters |
| 7 | Prueba final: una semana fuera sin que se detengan leads, cobros ni entregas |

**Qué se enciende:** Boca a Boca, Eco, la factura mensual automática de igualas (Cobra), Boletín y Altavoz; Vigía, Escudo y Aduana como agentes solo si el volumen lo justifica.

**Criterio de éxito.**

- [ ] Una semana completa fuera sin que se detengan leads, cobros ni entregas
- [ ] Al menos 1 referido por cada 3 clientes entregados en 60 días
- [ ] ≥20% del ingreso mensual recurrente (si vendes iguala)
- [ ] Cero incidentes con cliente en el trimestre
- [ ] Horas de gestión ≤5 por semana

## Stack recomendado

Una herramienta por función ([principio 6](01-arquitectura.md#principios)): Pipedrive = embudo; Notion = estado, reglas y memoria; ManyChat = conversaciones y permisos; n8n = eventos y relojes; Claude = criterio y borradores, y solo despierta cuando hay algo que decidir; Blotato = publicación; Google Sheets = hoja de dinero. Trello y Airtable no se usan, para no partir el cerebro.

Los costos son aproximados y van tal cual los da la arquitectura, en la moneda de cada proveedor. Los precios que se pudieron revisar se verificaron el 10 de noviembre de 2026 ([datos verificados](04-lo-que-te-falta.md#datos-verificados)); lo que dice «por confirmar» no se verificó. Confírmalos en la página de precios de cada uno antes de contratar.

| # | Función | Herramienta | Alternativa | Costo aproximado |
|:-:|---|---|---|---|
| 1 | Cerebro: estado, reglas y memoria del negocio | Notion Plus (los invitados no ocupan asiento; sin portales bastan 1–2 miembros: tú y el asistente) | Notion Business solo si necesitas Notion AI completo o Custom Agents (consumen créditos a US$10 por cada 1,000 desde el 4 de mayo de 2026 y solo se compran en Business o Enterprise) | US$10 por miembro al mes en pago anual o US$12 mensual (Business US$20 o US$24) |
| 2 | CRM y embudo | Pipedrive Growth para ti y el asistente; los setters trabajan desde ManyChat Live Chat y solo reciben asiento si lo necesitan | Pipedrive Premium con más de 3 setters si quieres reparto nativo (confirma que incluya la función de equipos; si no, la cola sigue en n8n); HubSpot Sales Starter | aprox. US$39 por asiento al mes en pago anual (Lite ~US$14, Premium ~US$49–59, Ultimate ~US$79; por confirmar en pipedrive.com/pricing) |
| 3 | Conversaciones y bot en Instagram, Messenger y WhatsApp | ManyChat Pro | Automatizaciones de DM de Blotato (solo Instagram y Facebook) | aprox. US$29 al mes en pago anual o US$39 mensual con 2,500 contactos activos; contacto extra ~US$0.05 (mensual) o ~US$0.038 (anual) |
| 4 | WhatsApp de ventas | WhatsApp Business Platform (API) vía ManyChat con número a nombre de la marca; decisión por número: API, coexistencia o se queda en la app | App WhatsApp Business para tus referidos 1 a 1 (listas de difusión de hasta 256 contactos que guardaron tu número; sin automatización, varios agentes ni plantillas) | por mensaje desde el 1 de octubre de 2026, según tablas de proveedores para México: servicio y utilidad aprox. US$0.0085 y marketing aprox. US$0.0397; las conversaciones que abre un anuncio de clic a WhatsApp son gratis por 72 h (confirma en tu cuenta) |
| 5 | Pauta y señal de conversiones | Meta Ads + Conversions API (acción nativa de ManyChat en Instagram y Messenger; desde n8n para WhatsApp), optimizando por LeadSubmitted al calificar | LinkedIn Ads (Fase 3) | presupuesto aparte, aprobado por semana en la junta del lunes y con regla automática de tope diario |
| 6 | Publicación y programación en redes | Blotato Starter | Meta Business Suite (gratis, solo Facebook e Instagram) | US$29 al mes (20 cuentas conectadas y 1,250 créditos de IA; Creator US$97) |
| 7 | Edición de video | Editor humano con su propio software | Adobe Express (conector: voz limpia, formatos y resumen) solo si la edición la hace IA | honorarios por pieza (por confirmar); Adobe por confirmar con tu plan |
| 8 | Diseño gráfico (carruseles, one-pagers y media kit) | Canva (ya conectado) | Adobe Express | por confirmar (tu plan actual) |
| 9 | Eventos en tiempo real, relojes y envíos con plantilla | n8n Cloud Starter | Make | aprox. €20 al mes en pago anual o €24 mensual (2,500 ejecuciones y 5 simultáneas; Pro aprox. €50 o €60 con 10,000; por confirmar en n8n.io/pricing) |
| 10 | Agentes: chats por pilar y tareas programadas | Claude Code en la nube con plan Max (tope de 15 corridas programadas al día, en research preview) y Remote Control cuando la tarea necesite tu computadora | Ultra si te falta uso (su tope de corridas no se encontró; por confirmar); el plan Pro no alcanza ni para la Fase 1 (5 corridas al día) | US$100 al mes en Max (Ultra US$200; Pro US$20); Max y Ultra solo en pago mensual; confirma en claude.com/pricing |
| 11 | IA dentro de los flujos y en lo que entregas | API de Claude (Console, workspace con límite de gasto) | Batch API para tareas no urgentes (50% de descuento) | por uso: Haiku 5.5 US$0.10/0.50 por millón de tokens de entrada/salida en prompts de hasta 100K tokens (arriba, US$0.50/2.50) y Sonnet 5.5 US$2/10 (lecturas de caché US$0.10 por millón) |
| 12 | Monitoreo y alertas | Flujo de errores de n8n por correo (Fase 1) | Healthchecks.io + Telegram para P0 desde 5 flujos críticos | US$0 en Fase 1; plan gratuito de Healthchecks con límites por confirmar; Telegram gratis |
| 13 | Bóveda de contraseñas y acceso de emergencia | Bitwarden Premium (el acceso de emergencia es de Premium) | 1Password | US$19.80 al año (aprox. US$1.65 al mes) |
| 14 | Código, instrucciones de agentes, issues y catálogo de automatizaciones | GitHub Free (repo marca.ai, Actions, issues y gitleaks en cada PR) | GitHub Team con Secret Protection si sumas desarrolladores | US$0 (2,000 minutos de Actions al mes en repos privados); Secret Protection aprox. US$19 por committer activo (por confirmar) |
| 15 | Hosting y previews de entregas | En la cuenta del cliente desde el kickoff | Vercel Pro solo si hospedas tú (el plan Hobby no permite uso comercial, ni un despliegue hecho por un consultor pagado para un cliente) | US$0 para ti; Vercel Pro aprox. US$20 por usuario al mes |
| 16 | Página web simple (oferta, aviso de privacidad integral y botón a WhatsApp o a tu agenda) | Google Sites u otra herramienta que permita uso comercial, con tu dominio (la haces en una tarde) | Sitio estático en un hosting con plan comercial | aprox. US$0 más el dominio (por confirmar) |
| 17 | Llamadas, grabación y transcripciones | Zoom (ya conectado) | Google Meet | por confirmar (tu plan actual) |
| 18 | Correo, agenda, archivos, hojas y buzones cobranza@ y avisos@ | Google Workspace (ya conectado) | — | por confirmar (tu plan actual; los buzones pueden ser alias si tu cuenta es de Workspace con dominio propio) |
| 19 | Cobro | SPEI directo a la cuenta del negocio para anticipos y tickets grandes; Stripe México para tarjeta | Mercado Pago Link de pago | SPEI según tu banco; Stripe 3.6% + $3 MXN más IVA por tarjeta nacional (internacionales 0.5% más; meses sin intereses aparte); Mercado Pago 3.49% + $4 al instante (3.19% a 7 días y 2.95% a 30 días, más IVA) |
| 20 | Validación de transferencias | Validador CEP de Banxico | — | gratis |
| 21 | Facturación CFDI 4.0 | Portal o PAC que ya use tu contadora (hasta ~15 facturas al mes) | Facturapi por API cuando pases de ~15 facturas al mes; portal gratuito del SAT | por confirmar (por plan o por timbre) |
| 22 | Firma de contratos | Firma electrónica de Google Docs si tu plan de Workspace la incluye | Servicio de firma electrónica con constancia de conservación NOM-151 | por confirmar |
| 23 | Registro de marca | IMPI: búsqueda en MARCia y solicitud en Marca en Línea | Abogado de propiedad industrial si aparece algo parecido | aprox. $2,800 MXN por clase en línea con IVA (cerca de $3,130 en ventanilla; confirma la tarifa vigente) |
| 24 | Seguro de responsabilidad civil profesional y ciberriesgo (Fase 2) | Cotización con un corredor de seguros | — | por confirmar (depende de tus ingresos y del límite de responsabilidad de tus contratos) |
| 25 | Audiencia propia (Fase 3) | Canal de correo de ManyChat Pro + Canal de WhatsApp (gratis) | Herramienta de newsletter dedicada cuando la lista pase de unos 1,000 suscriptores | incluido en ManyChat Pro; la dedicada, por confirmar |
| 26 | Analítica de la página web y links | Google Analytics 4 con la taxonomía de UTMs | — | gratis |
| 27 | Prospección B2B (espera; Fase 3 o después) | Apollo.io (ya conectado), siempre detrás de Filtro y con aviso de privacidad | LinkedIn Sales Navigator | por confirmar |

- **Lo que espera hasta que haya volumen:** Pipedrive Premium, asientos de Pipedrive para setters que trabajen bien desde ManyChat, Facturapi por API (hasta ~15 facturas al mes basta el portal o PAC de la contadora), Vercel Pro (previews en la cuenta del cliente), Notion Business, Apollo, newsletter dedicada y Adobe Express para post-producción si hay editor humano.
- **Cómo no se dispara el gasto** (riesgo 9): inventario con tope por herramienta, límite de gasto en la Console, tarjeta virtual con tope y revisión mensual en pesos.
- **Total mensual:** por definir. Depende de tus planes actuales ([pregunta abierta 6](#preguntas-abiertas)) y de si algún setter necesita asiento de Pipedrive; se arma en la primera revisión mensual del stack en pesos.

## Riesgos

Los 13 riesgos de la arquitectura, cada uno con su mitigación.

| # | Riesgo | Mitigación |
|:-:|---|---|
| 1 | Sobre-ingeniería: por ser ingeniero, pasar semanas perfeccionando agentes, bases y flujos en lugar de grabar y vender; la parte divertida se come la Fase 0. | Fase 0 sin agentes y medida por trámites cerrados; un solo flujo automatizado nuevo en diciembre; 7 agentes encendidos hasta marzo; 10 bases; 2 chats en Fase 1; regla de 5–10 veces a mano; máximo 2 automatizaciones nuevas por semana; horas de gestión ≤5 como criterio de cada fase; revisión trimestral que apaga agentes sin uso en 30 días. |
| 2 | Dependencia total de Meta: un bloqueo de tu perfil, de la cuenta publicitaria o del número corta pauta, DMs y WhatsApp al mismo tiempo (en 2026 hubo reportes de prensa sobre oleadas de suspensiones). | Portafolio a nombre de la marca con 2 administradores y 2FA, solo integraciones oficiales (ManyChat y Blotato), opt-in y plantillas aprobadas, checklist de promesas prohibidas contra las políticas de anuncios, página web propia con aviso y botón a tu agenda, lista propia de correo (Fase 3) y revisión mensual de la calidad de la cuenta y del número. |
| 3 | Agentes con tus permisos: las tareas programadas arrancan con todos tus conectores con escritura, todo lo que hacen aparece como tú y el conector de Notion llega a tus páginas privadas. | Conectores mínimos por rutina, Gmail de Claude solo para borradores, envíos solo por n8n con plantillas preaprobadas, Filtro e interruptor general; archivar en vez de borrar; revisión de 10 minutos de cambios de agentes en la junta del lunes con el historial de Notion; Anfitrión sin llaves. |
| 4 | Piezas en vista previa o que cambian: rutinas en research preview con tope diario (15 en Max) y mínimo de una hora; reportes de conectores de Google que no aparecen en rutinas en la nube; ManyChat, WhatsApp y Meta cambiaron precios y reglas en 2026. | n8n lleva los relojes y lo crítico que toca clientes; Claude solo decide; plan B documentado para cada disparo por API (n8n crea la Tarea y te avisa); instrucciones en el repo para recrear cualquier rutina; probar el Gabinete con Calendar antes de depender de él; revisión mensual del stack en pesos. |
| 5 | Fuga de datos o de cartera: setters que atienden desde su WhatsApp personal, accesos de más, exportaciones, llaves en variables de entorno o datos de clientes en el repo. | Canales a nombre de la marca; setters en Live Chat con sus conversaciones (asiento de Pipedrive solo si hace falta); sin portales ni bases espejo; bajas en 24 horas; network secrets; gitleaks en cada PR; respaldo fuera de GitHub en carpeta restringida (últimos 3); retención corta de ejecuciones en n8n. |
| 6 | Pasivo laboral y fiscal silencioso: setters reclasificados como empleados por cómo se operan, comisiones sin CFDI, facturas con el método equivocado, declaraciones fuera de tiempo o sellos digitales (CSD) restringidos que te impiden facturar. | Abogado laboral revisando el modelo de operación completo; cola abierta sin órdenes diarias ni sanciones; carta provisional antes del 30 de noviembre y contrato definitivo antes del 31 de enero; Plan de compensación sobre lo cobrado; regla fiscal escrita de la contadora para anticipos e hitos; vencimientos en el mensaje matutino; declaraciones presentadas aunque sean en ceros. |
| 7 | Memoria dividida: cada chat recuerda cosas distintas y los agentes se contradicen (por ejemplo, cotizan con precios viejos). | Precedencia de memoria escrita, páginas canónicas que solo tú cambias, dueños del dato definidos (Pipedrive antes del pago, Notion después, ManyChat conversaciones) y /cierre obligatorio al final de cada sesión. |
| 8 | Notion como punto único de falla: sin respaldo externo, historial limitado por plan (30 días en Plus, por confirmar) y límites de API (alrededor de 3 solicitudes por segundo y 100 resultados por consulta). | Exportación mensual fuera de Notion y fuera de GitHub (carpeta de Drive restringida o archivo cifrado; últimos 3) con restauración de prueba cada trimestre; leads en Pipedrive y conversaciones en ManyChat; agentes que leen por vistas guardadas. |
| 9 | Costos en dólares que crecen solos: suscripciones, asientos de Pipedrive, mensajes de WhatsApp (ahora también los de servicio), API de Claude y ejecuciones de n8n; un error en un fin de semana puede costar lo de un mes. | Herramientas que esperan hasta que haya volumen (Pipedrive Premium, Facturapi por API, Vercel Pro, Notion Business, Apollo y newsletter dedicada); inventario con tope por herramienta; límite de gasto en la Console; tarjeta virtual con tope; revisión mensual en pesos. |
| 10 | Tu salud y tu tiempo: si te enfermas dos semanas no hay videos, ni respuestas, ni cobros, ni aprobaciones. | Asistente desde enero que puede pausar todo y opera cobranza y reportes; banco de 3–4 semanas de videos; acceso de emergencia en Bitwarden; Manual de contingencia de una página; bloques protegidos en Calendar; presupuesto de 5 horas de gestión. |
| 11 | Vender más de lo que puedes entregar: el embudo funciona, la entrega se atora y tu marca personal paga las quejas. | Sección Capacidad en la oferta (máximo de proyectos en construcción y próxima fecha de arranque que los setters citan tal cual), semanas de cola en el Tablero, pausa de pauta y alza de 10–15% en propuestas nuevas si la cola pasa de 4 semanas, y desarrollador freelance tras 2 semanas seguidas así. |
| 12 | Diciembre mide mal y cobra lento: del 12 de diciembre al 6 de enero los decisores se van, la subasta navideña encarece la pauta y tu contadora está en cierre de año. | No escalar pauta en esas fechas, cerrar lo que ya está en propuesta, construir y hacer a mano; medir los criterios de Fase 1 desde el 11 de enero; mandar el paquete de diciembre el lunes 4 de enero. |
| 13 | Cobros atorados en corporativos: alta de proveedor de semanas y pagos a 30, 60 o más días. | Expediente de proveedor listo, pregunta del alta y del plazo de pago en la Propuesta, anticipo antes de iniciar, opinión de cumplimiento positiva cada mes y factoraje de Cadenas Productivas de Nafin si el cliente participa. |

## Preguntas abiertas

Son 7, en este orden, y se contestan en la semana del 16 de noviembre (Fase 0, entregable 3), empezando por la primera. Sus respuestas afinan el sistema antes de construirlo.

| # | Pregunta | Qué mueve la respuesta |
|:-:|---|---|
| 1 | ¿Qué vendes hoy y a qué ticket (proyectos a la medida, diagnósticos, capacitaciones, comunidad, soporte) y qué quieres empujar en 2027? Si hay capacitación o una comunidad de pago, ese flujo se diseña antes que cualquier agente (una comunidad sería otra línea con su propio cobro recurrente, cancelaciones y aviso de privacidad). | Qué flujo se diseña primero (si hay capacitación, el [flujo 7](03-flujos-y-ritmo.md#flujo-7)) y la oferta en una página: Diagnóstico pagado, Implementación e Iguala con precio de lista más IVA, precio piso y capacidad ([punto ciego 7](04-lo-que-te-falta.md#pc7)). |
| 2 | ¿En qué régimen fiscal estás hoy, cuánto cobraste aproximadamente de enero a octubre de 2026 y tu contadora ya te dijo cómo facturar anticipos e hitos (PUE por cada pago o PPD con complementos)? | La junta de régimen y la simulación 2027 ([punto ciego 3](04-lo-que-te-falta.md#pc3)), la tasa de reserva de la hoja de dinero ([punto ciego 6](04-lo-que-te-falta.md#pc6)) y la regla escrita de facturación de anticipos e hitos que Cobra necesita antes de encenderse. |
| 3 | ¿Cuántos setters tienes, desde qué número atienden, en qué país viven, si tienen RFC, si firmaron algo y cómo trabajan hoy (horario, metas diarias, exclusividad)? | La carta provisional y la revisión del modelo laboral ([punto ciego 4](04-lo-que-te-falta.md#pc4)), el Plan de compensación y el tratamiento fiscal de cada setter ([punto ciego 5](04-lo-que-te-falta.md#pc5)); Pulso solo con 2 o más setters, Pipedrive Premium con más de 3, líder de setters desde 3 y Lupa como agente con 4 o más. |
| 4 | ¿Qué números de WhatsApp usa el negocio, a nombre de quién está cada línea, en qué dígito termina y si ya está vinculada a una CURP? ¿Alguno ya está en la API vía ManyChat o todo vive en la app? | Las fechas de vinculación a la CURP y la decisión por número: API de ManyChat, coexistencia o se queda en la app ([punto ciego 1](04-lo-que-te-falta.md#pc1)). |
| 5 | ¿La edición la hará una persona o IA? ¿Quién es tu persona de confianza para el acceso de emergencia y el segundo administrador de Meta? ¿Tienes presupuesto para un asistente de medio tiempo desde enero? | Si existe Tijeras (solo si la edición la hace IA); quién es segundo administrador de Meta y contacto de emergencia en Bitwarden ([punto ciego 2](04-lo-que-te-falta.md#pc2)); y la vacante del asistente de la primera semana de diciembre ([punto ciego 13](04-lo-que-te-falta.md#pc13)). |
| 6 | ¿Qué planes tienes hoy de Claude, Notion y Pipedrive, con qué tarjeta se pagan y tu banco permite un usuario de solo consulta? | El tope de corridas (Max 15, Pro 5) y el costo del stack ([presupuesto de corridas](03-flujos-y-ritmo.md#presupuesto-de-corridas-de-claude)). Si tu banco permite un usuario de solo consulta, conviene usarlo para revisar los depósitos de «Pago recibido». |
| 7 | ¿Tienes clientes con NDA o contratos que limiten usar sus datos, su código o su nombre? ¿Ya publicaste algún aviso de privacidad? ¿Tu nombre de marca ya está registrado ante el IMPI? | Qué casos puedes publicar y con qué permiso ([punto ciego 8](04-lo-que-te-falta.md#pc8)), qué código puedes reutilizar ([punto ciego 10](04-lo-que-te-falta.md#pc10)), el aviso de privacidad ([punto ciego 9](04-lo-que-te-falta.md#pc9)) y el registro de tu marca ante el IMPI ([punto ciego 12](04-lo-que-te-falta.md#pc12)). |

