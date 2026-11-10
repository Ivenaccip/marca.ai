# Lo que te falta

Los 17 puntos ciegos que encontró la arquitectura: lo que hoy le falta a tu operación y que normalmente no ve un ingeniero de IA. Van por prioridad: 10 son P0 y 7 son P1; no hay P2. Cada uno trae explicación, por qué importa, dónde se conecta con el sistema, el primer paso, esfuerzo, impacto, pilar y fuentes. Al final están la proporción 90/10 y las 29 verificaciones de datos con su fuente. La fuente es [data/arquitectura.json](../data/arquitectura.json) (campos `puntos_ciegos` y `proporcion_90_10`) y [data/verificacion.json](../data/verificacion.json); si algo de aquí no cuadra con esos archivos, mandan ellos.

**Mapa visual interactivo del sistema:** https://claude.ai/artifact/FtyWRkr6M2jFp4Mnu5BFDN

> Estado al 10 de noviembre de 2026: Fase 0 (10 al 30 de noviembre), sin agentes. Casi todos los primeros pasos de abajo son trámites o pláticas con personas, no sistema: la Fase 0 se mide por trámites cerrados.

## Contenido

1. [Con fecha límite cercana](#con-fecha-límite-cercana)
2. [Los 17 de un vistazo](#los-17-de-un-vistazo)
3. [Prioridad P0](#prioridad-p0)
4. [Prioridad P1](#prioridad-p1)
5. [Proporción 90/10](#proporción-9010)
6. [Datos verificados](#datos-verificados)

Documentos hermanos: [README](../README.md), [01-arquitectura.md](01-arquitectura.md) (visión, pilares y orquestación), [02-cerebro-notion.md](02-cerebro-notion.md) (las 10 bases), [03-flujos-y-ritmo.md](03-flujos-y-ritmo.md) (flujos, cadencias y presupuestos) y [05-ruta-stack-riesgos.md](05-ruta-stack-riesgos.md) (ruta por fases, stack y riesgos).

## Con fecha límite cercana

Hoy es martes 10 de noviembre de 2026. Esto es lo que tiene fecha en las próximas semanas, en orden. Los primeros pasos de los puntos 1 a 14 dicen «hoy» o «esta semana»; la ruta de la Fase 0 los reparte en las 3 semanas de noviembre, como en esta tabla (detalle en [05-ruta-stack-riesgos.md](05-ruta-stack-riesgos.md#ruta-por-fases)). Lo que la ruta no reparte, la lista de decisiones y los bloques en Calendar del punto 13, se queda en esta semana.

| Fecha | Qué vence o qué toca | Punto ciego |
|---|---|---|
| **Hoy, martes 10 de noviembre** | Lista todas las líneas que usan tú y tus setters para el negocio y confirma en el portal de cada compañía o en gob.mx que estén vinculadas a la CURP del titular correcto, empezando por las que terminan en 6. Descarga tu opinión de cumplimiento en sat.gob.mx; si no sale positiva, mándasela a tu contadora para que corrija la causa. | [1](#pc1), [11](#pc11) |
| **Hoy al domingo 15 de noviembre (5 días)** | Cada línea de WhatsApp del negocio vinculada a la CURP del titular correcto (las de prepago con terminación 6 vencen el 15; confírmalo con tu compañía), PIN de verificación en dos pasos activo y decisión por número: API de ManyChat, coexistencia o se queda en la app. Una línea suspendida no hace ni recibe llamadas ni SMS, así que tampoco llegan los códigos de WhatsApp ni del banco. | [1](#pc1) |
| **Esta semana (al domingo 15 de noviembre)** | Lista las 15 decisiones que te consultaron el último mes por WhatsApp y Gmail, con aprobador, límite en MXN y si se aprueban por excepción, y crea en Google Calendar los bloques fijos de grabación, las ventanas de 9:30 y 17:30 y los bloques «Gestión». | [13](#pc13) |
| Semana del 16 de noviembre | Candados (Bitwarden con acceso de emergencia; 2FA sin SMS; segundo administrador en Meta), persona de confianza nombrada y tabla de cuentas críticas a nombre de la marca; cita con la contadora para la primera semana de diciembre y opinión de cumplimiento descargada; búsqueda de tu marca en MARCia y etiquetado de tus repos. | [2](#pc2), [3](#pc3), [10](#pc10), [11](#pc11), [12](#pc12) |
| Semana del 23 de noviembre | Oferta en una página enviada a los setters ese mismo día y 3 llamadas de 20 minutos con tus mejores clientes que terminan en la página de Posicionamiento. | [7](#pc7), [8](#pc8) |
| Antes del lunes 30 de noviembre | Plan de compensación v1; carta provisional firmada por cada setter y el editor; abogado contratado con entrega antes del 15 de enero; cuenta del negocio con apartado de Impuestos, hoja de dinero, regla escrita para setters y carpeta «Expediente de proveedor»; Pipedrive con campos obligatorios; página web con el aviso de privacidad integral. El 30 vencen también las líneas de prepago con terminación 7. | [1](#pc1), [4](#pc4), [5](#pc5), [6](#pc6), [9](#pc9), [10](#pc10), [11](#pc11), [14](#pc14), [15](#pc15) |
| Primera semana de diciembre | Junta de régimen con tu contadora (simulación 2027 con 4 escenarios) y vacante del asistente de medio tiempo publicada para que entre en enero. | [3](#pc3), [13](#pc13) |
| Del 1 al 11 de diciembre | El único flujo automatizado nuevo de la Fase 1: ManyChat (aviso simplificado, «Acepto», calificación y agenda directa para leads A) → n8n → Pipedrive con lead_id, cola con reasignación a los 30 minutos, LeadSubmitted a Meta y 2–3 plantillas de reapertura de la ventana de 24 horas; y el evento «Pago recibido» que crea el Proyecto desde la plantilla «Proyecto ganado». | [1](#pc1), [9](#pc9), [14](#pc14), [15](#pc15), [16](#pc16) |
| Diciembre, antes de crear la primera rutina | En el README, la tabla agente → corridas al día → conectores permitidos; 1 sola corrida programada (el Gabinete a las 7:10) con solo los conectores que usa, después de probar que el de Google Calendar aparece en ella. | [17](#pc17) |
| Martes 15 de diciembre | Vencen las líneas de prepago con terminación 8. | [1](#pc1) |
| Antes del jueves 31 de diciembre | Solicitud de marca ante el IMPI y compras deducibles si tu régimen lo permite. El 31 vencen las líneas de prepago con terminación 9. | [1](#pc1), [3](#pc3), [12](#pc12) |
| Viernes 1 de enero de 2027 | Entrarían en vigor el tope de RESICO de persona física de 5 millones y la opción de IVA de 7% sobre lo cobrado (aprobados por el Congreso; al 10 de noviembre no se encontró su publicación en el DOF). | [3](#pc3) |
| Antes del lunes 11 de enero | Hoja de 6 celdas con el costo por lead calificado máximo y regla automática de tope diario en Ads Manager, antes de escalar la pauta. | [16](#pc16) |
| Antes del viernes 15 de enero | Entrega del abogado (laboral con el modelo de operación completo, contrato marco, NDA y aviso de privacidad). | [4](#pc4), [9](#pc9), [10](#pc10) |
| Del lunes 11 al domingo 31 de enero | Se miden los criterios de la Fase 1, entre ellos: mediana de primera respuesta humana ≤15 minutos hábiles en leads A, 100% de los pagos registrados como «Pago recibido» en 1 día hábil o menos, cero comisiones pagadas sin CFDI, tus horas de gestión ≤5 por semana y 8 o menos corridas de Claude al día. | [5](#pc5), [6](#pc6), [13](#pc13), [14](#pc14), [17](#pc17) |
| Antes del domingo 31 de enero | Contratos definitivos firmados; desde ese día la regla «sin firma no hay accesos ni leads» aplica para todos. | [4](#pc4) |

## Los 17 de un vistazo

| # | Punto ciego | Prioridad | Pilar | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|:-:|---|:-:|:-:|---|
| 1 | [Tu número de WhatsApp de ventas puede caerse este mes, y la API tiene reglas que cambian tu operación](#pc1) | P0 | [Ventas y setters](../pilares/ventas/CLAUDE.md) | Bajo | Alto | Hoy al domingo 15 de noviembre (la terminación 6 vence el 15) |
| 2 | [¿A nombre de quién están tus cuentas, números y tarjetas? Si están a nombre de otro, el canal es de otro](#pc2) | P0 | [Legal, riesgo y accesos](../pilares/legal/CLAUDE.md) | Bajo | Alto | Semana del 16 de noviembre; criterio de Fase 0 al 30 de noviembre |
| 3 | [Tu régimen fiscal 2027 se decide antes de enero, y las reglas ya cambiaron](#pc3) | P0 | [Administración y finanzas](../pilares/admin/CLAUDE.md) | Medio | Alto | Semana del 16 de noviembre (cita); primera semana de diciembre (junta de régimen) |
| 4 | [Tus setters pueden ser legalmente tus empleados: no por el contrato, sino por cómo los diriges](#pc4) | P0 | [Legal, riesgo y accesos](../pilares/legal/CLAUDE.md) | Medio | Alto | 30 de noviembre (carta provisional y abogado contratado); 31 de enero (contrato definitivo) |
| 5 | [Comisiones sin reglas escritas: pagas por dinero que no entró y cada lead que regresa es un pleito](#pc5) | P0 | [Ventas y setters](../pilares/ventas/CLAUDE.md) | Medio | Alto | 30 de noviembre (Plan de compensación v1) |
| 6 | [Cada cobro trae dinero que no es tuyo, y una captura de pantalla no es un pago](#pc6) | P0 | [Administración y finanzas](../pilares/admin/CLAUDE.md) | Bajo | Alto | 30 de noviembre (cuenta del negocio, hoja de dinero y regla para setters) |
| 7 | [Tu oferta no tiene precio piso ni tope de capacidad: puedes vender con pérdida o vender lo que no alcanzas a entregar](#pc7) | P0 | [Producto y desarrollo](../pilares/producto/CLAUDE.md) | Bajo | Alto | Semana del 23 de noviembre (oferta en una página) |
| 8 | [No sabes por qué te compran ni puedes demostrarlo: faltan posicionamiento y casos con permiso](#pc8) | P0 | [Marca y contenido estratégico](../pilares/marca/CLAUDE.md) | Medio | Alto | Semana del 23 de noviembre (3 llamadas y página de Posicionamiento) |
| 9 | [Cada lead de ManyChat, WhatsApp o Zoom te obliga bajo la nueva ley de datos personales](#pc9) | P0 | [Legal, riesgo y accesos](../pilares/legal/CLAUDE.md) | Bajo | Alto | 30 de noviembre (aviso integral publicado en tu página web) |
| 10 | [La propuesta no basta como contrato, tu código reciclado podría no ser tuyo y lo que hace la IA sola no tiene autor](#pc10) | P0 | [Legal, riesgo y accesos](../pilares/legal/CLAUDE.md) | Medio | Alto | Semana del 16 de noviembre (etiquetado de repos); 30 de noviembre (abogado contratado); 15 de enero (plantillas) |
| 11 | [Una empresa grande no te paga hasta que pasas su alta de proveedor, y después te paga según su calendario](#pc11) | P1 | [Administración y finanzas](../pilares/admin/CLAUDE.md) | Bajo | Alto | Hoy (opinión de cumplimiento); 30 de noviembre (expediente de proveedor) |
| 12 | [El nombre de tu marca no es tuyo hasta que lo registras en el IMPI](#pc12) | P1 | [Marca y contenido estratégico](../pilares/marca/CLAUDE.md) | Bajo | Alto | Semana del 16 de noviembre (búsqueda en MARCia); 31 de diciembre (solicitud ante el IMPI) |
| 13 | [Tú eres el cuello de botella del sistema que estás construyendo](#pc13) | P1 | [Automatizaciones y operación del sistema](../pilares/automatizaciones/CLAUDE.md) | Bajo | Alto | Esta semana (lista de decisiones y bloques fijos en Calendar); primera semana de diciembre (vacante del asistente) |
| 14 | [Nadie mide cuánto tarda en contestarse un lead ni qué dicen tus setters en tu nombre](#pc14) | P1 | [Ventas y setters](../pilares/ventas/CLAUDE.md) | Medio | Alto | 30 de noviembre (campos obligatorios en Pipedrive); se mide del 11 al 31 de enero |
| 15 | [El setter vende y tú heredas la promesa: falta el traspaso de la venta a la entrega](#pc15) | P1 | [Clientes y post-venta](../pilares/clientes/CLAUDE.md) | Bajo | Alto | Tu próximo cierre; plantilla «Proyecto ganado» del 1 al 11 de diciembre |
| 16 | [Meta optimiza tu pauta para conseguir mensajes, no clientes](#pc16) | P1 | [Marketing y adquisición](../pilares/marketing/CLAUDE.md) | Medio | Alto | Antes del 11 de enero (cuando se escala la pauta) |
| 17 | [Tus tareas programadas tienen tope diario y gastan tu cuota: n8n vigila, Claude decide](#pc17) | P1 | [Automatizaciones y operación del sistema](../pilares/automatizaciones/CLAUDE.md) | Bajo | Alto | Antes de crear la primera rutina (Fase 1, diciembre) |

Por pilar: Legal, riesgo y accesos 4; Ventas y setters 3; Administración y finanzas 3; Marca y contenido estratégico 2; Automatizaciones y operación del sistema 2; Producto y desarrollo 1; Clientes y post-venta 1; Marketing y adquisición 1. Los 17 son de impacto alto; 10 son de esfuerzo bajo y 7 de esfuerzo medio.

## Prioridad P0

Los 10 puntos P0. Cada uno tiene un entregable en la Fase 0 (10 al 30 de noviembre).

<a id="pc1"></a>

### 1. Tu número de WhatsApp de ventas puede caerse este mes, y la API tiene reglas que cambian tu operación

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Ventas y setters](../pilares/ventas/CLAUDE.md) | Desconocido | Bajo | Alto | Hoy al domingo 15 de noviembre (la terminación 6 vence el 15) |

**Explicación.** Se juntan cinco cosas. (1) Cada línea celular debe quedar vinculada a una CURP; en prepago el plazo va por último dígito (terminación 6: 15 de noviembre; 7: 30 de noviembre; 8: 15 de diciembre; 9: 31 de diciembre de 2026). Una línea suspendida no hace ni recibe llamadas ni SMS (solo emergencias), así que no te llegan los códigos de WhatsApp ni del banco; hay 90 días después de la suspensión para regularizarla y conservar el número, y el trámite en gob.mx funciona aun suspendida. La línea es de quien la registra: si el chip lo compró tu setter, el número es de él. (2) Por la API oficial solo puedes mandar texto libre dentro de las 24 horas siguientes al último mensaje del cliente; después, solo plantillas aprobadas y pagadas. (3) Desde el 1 de octubre de 2026 Meta cobra también los mensajes de servicio (según tablas de proveedores para México: servicio y utilidad cerca de US$0.0085 y marketing cerca de US$0.0397); siguen gratis las conversaciones que abre un anuncio de clic a WhatsApp dentro de su ventana de 72 horas. (4) Conectar a ManyChat el número que hoy usas en la app no es neutro: hay que decidir si va en coexistencia (app y API en el mismo número, con funciones de la app limitadas), si el bot usa un número nuevo o si tus referidos se quedan en la app; hacerlo sin decidir puede costarte historial, listas o grupos. (5) Desde el 15 de enero de 2026 la API prohíbe los chatbots de IA de propósito general: un bot que atiende y vende tus servicios sí está permitido, siempre que no funcione como asistente de preguntas libres. Y las extensiones o apps no oficiales para programar mensajes son causa de bloqueo.

**Por qué importa.** Si se cae el número pierdes de golpe conversaciones abiertas, referidos e historial, y un número nuevo empieza sin reputación. Si el setter contesta fuera de la ventana de 24 horas ya no puede mandar un mensaje normal y cada reapertura cuesta.

**Dónde se conecta.** Ventas (cola de setters y referidos 1 a 1), Marketing (el Anfitrión cierra la primera conversación con cita u horario), Legal (tabla de cuentas críticas: línea, titular, CURP, quién la usa y PIN) y Automatizaciones (Filtro y plantillas de reapertura).

**Primer paso.** Hoy: lista todas las líneas que usan tú y tus setters para el negocio y confirma en el portal de cada compañía o en gob.mx que estén vinculadas a la CURP del titular correcto, empezando por las que terminan en 6 (vencen el domingo 15; confírmalo con tu compañía). Esta semana: activa el PIN de verificación en dos pasos en cada WhatsApp del negocio, deja de usar extensiones y decide por número si va a la API de ManyChat, en coexistencia o se queda en la app.

**En la ruta.** Fase 0, entregable 1. Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://www.infobae.com/mexico/2026/07/25/registro-de-lineas-con-curp-fechas-limite-de-la-crt-en-2026-segun-el-ultimo-digito-del-numero/>
- <https://www.elimparcial.com/tecnologia/2026/08/06/la-crt-permite-recuperar-lineas-telefonicas-suspendidas-por-no-registrarlas-a-tiempo-si-el-tramite-se-realiza-dentro-de-los-90-dias-posteriores-a-la-suspension/>
- <https://es.euronews.com/2026/10/09/registro-telefonos-moviles-con-curp-que-pasa-con-whatsapp-redes-suspenden-linea>
- <https://respond.io/blog/whatsapp-pricing-change-2026>
- <https://support.twilio.com/hc/en-us/articles/53100462475931-Notice-Changes-to-WhatsApp-s-Pricing-October-2026>
- <https://respond.io/blog/whatsapp-general-purpose-chatbots-ban>

<a id="pc2"></a>

### 2. ¿A nombre de quién están tus cuentas, números y tarjetas? Si están a nombre de otro, el canal es de otro

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Legal, riesgo y accesos](../pilares/legal/CLAUDE.md) | Desconocido | Bajo | Alto | Semana del 16 de noviembre; criterio de Fase 0 al 30 de noviembre |

**Explicación.** Lo que decide quién se queda con un canal es la titularidad legal, no quién lo usa: si el portafolio de Meta, una línea, el dominio o la tarjeta que paga la pauta están a nombre de un setter, del editor o de un familiar, una baja o un pleito te deja sin canal, y recuperar un portafolio de Meta puede tardar semanas sin soporte garantizado. El mismo problema aparece si todo se recupera con tu Gmail o con un SMS: quien entra a tu correo o clona tu chip (SIM swap) reinicia todo en minutos. Base mínima: todo a nombre tuyo o de tu empresa, dos administradores en cada cuenta crítica, una bóveda con acceso de emergencia para una persona de confianza y doble factor con passkey o app (no SMS).

**Por qué importa.** Es el riesgo más barato de prevenir y el más caro de sufrir: sin canal no entran leads, sin la tarjeta se pausa la pauta y sin acceso de emergencia nadie puede operar si te pasa algo.

**Dónde se conecta.** Legal (tabla de cuentas críticas y checklist de alta y baja), Marketing (portafolio de Meta y segundo administrador), Ventas (líneas de WhatsApp) y Automatizaciones (network secrets y Bitwarden).

**Primer paso.** Esta semana elige a tu persona de confianza y pregúntale si acepta ser segundo administrador de Meta y contacto de emergencia; luego haz en una página privada de Notion la tabla de cuentas críticas (cuenta, dueño legal, administradores 1 y 2, tipo de 2FA y tarjeta que paga) y pasa a nombre de la marca lo que esté a nombre de otro. Después: Bitwarden Premium (US$19.80 al año) con acceso de emergencia y 2FA sin SMS en Gmail, Meta, banco, Pipedrive, ManyChat, GitHub y Claude.

**En la ruta.** Fase 0, entregable 2. Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://bitwarden.com/blog/bitwarden-launches-emergency-access/>
- <https://alternativeto.net/news/2026/1/bitwarden-enhances-premium-and-families-plans-with-more-security-features-and-raises-prices>
- <https://support.chatarchitect.com/books/meta-business-portfolio-setup/page/best-practices-for-making-a-business-portfolio-more-secure>
- <https://piunikaweb.com/2026/03/28/meta-ban-wave-facebook-instagram-threads-users-locked-out/>

<a id="pc3"></a>

### 3. Tu régimen fiscal 2027 se decide antes de enero, y las reglas ya cambiaron

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Administración y finanzas](../pilares/admin/CLAUDE.md) | Desconocido | Medio | Alto | Semana del 16 de noviembre (cita); primera semana de diciembre (junta de régimen) |

**Explicación.** En 2026, en RESICO de persona física pagas de 1% a 2.5% sobre lo cobrado sin restar gastos, con tope de 3.5 millones de pesos al año; en actividad empresarial pagas sobre la utilidad (cobrado menos gastos con factura) con tarifa progresiva; una sociedad (S.A.S. o S.A. de C.V.) separa tu patrimonio y facilita venderle a corporativos. Para 2027 el Congreso ya aprobó subir el tope de RESICO de persona física a 5 millones, y la Ley de Ingresos 2027 trae la opción de pagar el IVA con una tasa de 7% sobre lo efectivamente cobrado, sin acreditar el IVA de tus gastos (al cliente le sigues facturando 16%). Al 10 de noviembre no se encontró su publicación en el DOF; entrarían en vigor el 1 de enero de 2027. El IVA de 7% conviene si tienes poco IVA acreditable y puede salir más caro con mucha pauta, software y comisiones facturadas con IVA.

**Por qué importa.** Es la decisión con más pesos en juego del año: define cuánto apartas de cada cobro, si las comisiones son deducibles y si tus clientes empresa te retienen, y no siempre se puede cambiar a mitad de año.

**Dónde se conecta.** Administración (tasa de reserva de la hoja de dinero y reglas fiscales escritas de la contadora), Ventas (comisiones deducibles) y Cobra (retenciones y tipo de factura).

**Primer paso.** Esta semana agenda con tu contadora una junta para la primera semana de diciembre con 4 temas: simulación 2027 con 4 escenarios (RESICO con IVA normal, RESICO con IVA de 7%, actividad empresarial y S.A.S.), incluyendo cómo y cuándo se elige la opción de 7% y cómo se combina con las retenciones de tus clientes empresa; cómo facturar anticipos e hitos; qué necesita cada mes; y el tratamiento fiscal de tus setters. Mándale antes lo cobrado y lo gastado de enero a octubre por categoría.

**En la ruta.** Fase 0, entregable 3 (cita con la contadora) y Fase 1, entregable 4 (junta de régimen y regla fiscal escrita). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://www.tiempo.com.mx/nacional/diputados-aprueban-reforma-a-la-ley-isr-deducciones-resico-2027/>
- <https://www.razon.com.mx/mexico/2026/10/28/avala-senado-leyes-de-ingresos-y-de-derechos/>
- <https://idconline.mx/fiscal-contable/2026/10/21/resico-2027-te-conviene-el-nuevo-esquema-para-pagar-solo-el-7-de-iva>
- <https://www.satfacil.com.mx/blog/limite-resico-3-5-millones-que-hacer>
- <https://www.pwc.com/mx/es/archivo/2026/paquete-economico-mx-2027.pdf>

<a id="pc4"></a>

### 4. Tus setters pueden ser legalmente tus empleados: no por el contrato, sino por cómo los diriges

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Legal, riesgo y accesos](../pilares/legal/CLAUDE.md) | Desconocido | Medio | Alto | 30 de noviembre (carta provisional y abogado contratado); 31 de enero (contrato definitivo) |

**Explicación.** El artículo 285 de la Ley Federal del Trabajo considera trabajadores a vendedores e impulsores de ventas cuando su actividad es permanente, salvo que no ejecuten personalmente el trabajo o solo intervengan en operaciones aisladas; lo que decide es si hay subordinación. Y la subordinación se ve en la operación: una lista diaria de prioridades es una orden; un cierre del día o un scorecard diario es supervisión; un SLA de 15 minutos obliga a estar disponible en horario aunque nadie diga «horario»; y formularios diarios, exclusividad, sanciones o pago fijo suman. Ponerle «comisión mercantil» al contrato no cambia la relación. Si un comisionista demanda, la Suprema Corte ha resuelto que la indemnización se calcula con el promedio de lo que ganó en el último año (artículo 289).

**Por qué importa.** Un setter que gana una demanda puede cobrar indemnización de 3 meses, salarios vencidos de hasta 12 meses, prestaciones y cuotas del IMSS; con 5 o 10 setters el pasivo se multiplica y puede aparecer años después.

**Dónde se conecta.** Ventas (cola abierta, lista opcional de oportunidades y reporte semanal de resultados), Legal (carta provisional y contrato definitivo), Personas y accesos (sin firma no hay leads) y Administración (pago solo por resultado contra CFDI).

**Primer paso.** Esta semana contrata a un abogado laboral y llévale el modelo de operación completo, no solo el contrato: cómo reciben leads, qué les pides cada día, cómo los mides y cómo les pagas. Pídele dos cosas: la carta provisional de una página para que la firmen antes del 30 de noviembre, y el costo de cada opción (independientes con cola abierta, pago solo por resultado y coaching voluntario, o contratar formalmente al mejor setter si quieres horarios y metas diarias).

**En la ruta.** Fase 0, entregable 6 (carta provisional y abogado laboral) y Fase 1, entregable 8 (contratos definitivos antes del 31 de enero). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://mley.mx/LFT/articulo/285/>
- <https://mexico.justia.com/federales/leyes/ley-federal-del-trabajo/titulo-sexto/capitulo-ix/>
- <https://scjn.gob.mx/sites/default/files/sinopsis_asuntos_destacados/documento/2016-11/2S-230211-JFFGS-443_0.pdf>
- <https://idconline.mx/laboral/2024/11/13/diferencias-clave-entre-comision-mercantil-y-laboral-segun-la-lft>

<a id="pc5"></a>

### 5. Comisiones sin reglas escritas: pagas por dinero que no entró y cada lead que regresa es un pleito

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Ventas y setters](../pilares/ventas/CLAUDE.md) | Desconocido | Medio | Alto | 30 de noviembre (Plan de compensación v1) |

**Explicación.** Falta el Plan de compensación de 1–2 páginas: (1) venta = dinero cobrado y registrado como «Pago recibido», no el «sí» ni la cita; (2) base sin IVA y sin comisión de pasarela; (3) si el cliente paga por hitos, la comisión se paga en la misma proporción; (4) clawback si hay reembolso dentro de N días; (5) atribución: un lead es de quien lo registró primero en Pipedrive, los que tú traes son tuyos (sin comisión, o una tarifa menor si un setter solo agenda) y se define qué gana el setter en citas que el bot agenda directo; (6) un «ahora no» que cierra dentro de 90 días es del setter original y después de quien lo reactive; (7) cortes los días 1 y 16. Si das recompensa por referir a un cliente empresa, que sea para la empresa (horas o descuento): muchas políticas de compras prohíben dinero a la persona. Lado fiscal: para deducirlas necesitas el CFDI del setter y pagar por transferencia si la erogación pasa de $2,000 (partirla en pagos chicos no la vuelve deducible, y pagar mal también te hace perder el IVA acreditable); si eres persona moral y le pagas a un setter persona física, tienes que retenerle según su régimen; los que viven en otro país tienen otro tratamiento.

**Por qué importa.** La comisión dirige la conducta: si pagas por cita te llenan la agenda de gente que no compra y si pagas al «sí» pagas sobre dinero que nunca entró; sin regla de atribución cada lead que regresa es un pleito; sin CFDI esas comisiones no reducen tu ISR.

**Dónde se conecta.** Ventas (Plan de compensación en Conocimiento), Administración (pestaña de comisiones de la hoja de dinero), Pipedrive (Fuente, Setter, Referido por y fecha de registro obligatorios) y Legal (anexo del contrato).

**Primer paso.** Esta semana platica 20 minutos con cada setter para acordar las 7 reglas (cuéntales que es para pagarles más rápido y sin pleitos); escribe la versión 1 con tus últimas 10 ventas (quién trajo el lead, quién lo atendió, cuánto se cobró de verdad y si hubo reembolso) y mándale a tu contadora la lista de setters (país, persona física o moral y régimen) para que te devuelva una tabla de una página: qué CFDI pides, qué retienes y cómo pagas.

**En la ruta.** Fase 0, entregable 6 (Plan de compensación v1). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://sdv.com.mx/compendio/ley-isr/articulo-27/>
- <https://idconline.mx/fiscal-contable/2024/07/22/pagos-en-efectivo-son-deducibles-para-impuestos>
- <https://www.quotapath.com/blog/fair-clawback-policies/>

<a id="pc6"></a>

### 6. Cada cobro trae dinero que no es tuyo, y una captura de pantalla no es un pago

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Administración y finanzas](../pilares/admin/CLAUDE.md) | Desconocido | Bajo | Alto | 30 de noviembre (cuenta del negocio, hoja de dinero y regla para setters) |

**Explicación.** De cada pago, 16 de cada 116 pesos son IVA que solo guardas para el SAT; otra parte es ISR, otra la comisión del setter y otra el costo del proyecto. Sistema simple: cuenta solo del negocio donde entra todo cobro, apartado de Impuestos con transferencia semanal sugerida, tarjeta del negocio para pauta y software, tu sueldo fijo (60–70% de la utilidad promedio) y un colchón de 3 meses. Una sola hoja de dinero con 4 pestañas: cobros, reserva de impuestos, comisiones y flujo de caja a 13 semanas (cobros esperados contra pagos con fecha fija: comisiones, pauta, herramientas en dólares, contadora, impuestos del mes y la anual de abril). Y una regla: un pago existe cuando aparece en tu banca; circulan comprobantes de SPEI falsos y una transferencia dudosa se valida con el CEP de Banxico.

**Por qué importa.** Un negocio de proyectos puede ser rentable y quedarse sin efectivo: la pauta se cobra cada semana, los setters cada quincena y muchas empresas pagan a 30 o 60 días; si te gastas el IVA, el día 17 no tendrás con qué pagar y vienen recargos.

**Dónde se conecta.** Administración (hoja de dinero y evento «Pago recibido»), Tablero del CEO (cobrado, cartera vencida y reserva) y Ventas (los setters nunca confirman pagos).

**Primer paso.** Esta semana manda por escrito a tus setters la regla «un pago existe cuando aparece en mi banca» y pregúntale a tu contadora qué porcentaje apartar de cada cobro mientras se define el régimen; abre una cuenta solo del negocio con apartado de Impuestos y arma la hoja de dinero con tu saldo de hoy, los cobros esperados de Pipedrive y tus pagos fijos.

**En la ruta.** Fase 0, entregable 7. Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://www.banxico.org.mx/validador-cep-spei/>
- <https://www.elimparcial.com/dinero/2025/11/12/alertan-sobre-fraudes-bancarios-como-identificar-una-transferencia-bancaria-falsa/>
- <https://www.pluxee.mx/blog/resico-que-es-quien-aplica-y-como-funciona/>

<a id="pc7"></a>

### 7. Tu oferta no tiene precio piso ni tope de capacidad: puedes vender con pérdida o vender lo que no alcanzas a entregar

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Producto y desarrollo](../pilares/producto/CLAUDE.md) | Desconocido | Bajo | Alto | Semana del 23 de noviembre (oferta en una página) |

**Explicación.** Separa lo que vendes en 3 formas de cobro: diagnóstico pagado (100% por adelantado; ahí se cobra el descubrimiento profundo y se acredita si contratan), implementación a precio fijo con anticipo e hitos atados a entregables (por ejemplo 50/30/20 con aceptación tácita) e iguala mensual con horas incluidas, si se acumulan o no, tiempo de respuesta y precio de la hora extra. Para cada servicio: precio piso = (horas × tu costo por hora + IA e infraestructura + freelance + contingencia) ÷ (1 − % de comisión del setter − margen objetivo). Cotiza siempre «más IVA»: si un setter dice «$50,000» sin aclarar, pierdes 13.8% (16/116). La pasarela (Stripe: 3.6% + $3 MXN más IVA por tarjeta nacional, y 0.5% más en internacionales) y los meses sin intereses también salen de tu margen. Y falta el freno: tú haces todos los descubrimientos y diseñas cada proyecto, así que sin un máximo de proyectos en construcción (por ejemplo 2 más 1 diagnóstico) y una «próxima fecha de arranque» que los setters citen tal cual, el embudo funciona, la entrega se atora y tu marca personal paga las quejas.

**Por qué importa.** Sin anticipo financias al cliente y la comisión del setter; sin precio piso los setters negocian descuentos a ciegas; sin tope de capacidad prometes fechas que no cumples; sin iguala cada mes empiezas en cero.

**Dónde se conecta.** Producto (página «Oferta y precios vigentes» con la sección Capacidad), Ventas (Propuesta y Playbook), Administración (cobros y comisiones), Matriz de aprobaciones (si la cola de entrega pasa de 4 semanas se pausa la pauta y las propuestas nuevas suben 10–15%) y Tablero del CEO (semanas de cola de entrega).

**Primer paso.** Esta semana define con tu contadora tu costo por hora (lo que necesitas ganar al mes ÷ horas realmente facturables) y escribe la oferta en una página: Diagnóstico pagado, Implementación e Iguala con precio de lista más IVA, precio piso, esquema de pago, capacidad máxima y próxima fecha de arranque; mándasela a tus setters el mismo día.

**En la ruta.** Fase 0, entregable 5 (oferta en una página). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://stripe.com/en-mx/pricing>
- <https://docs.stripe.com/payments/mx-installments>
- <https://support.stripe.com/questions/taxes-on-stripe-fees-for-mexico-based-businesses>

<a id="pc8"></a>

### 8. No sabes por qué te compran ni puedes demostrarlo: faltan posicionamiento y casos con permiso

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Marca y contenido estratégico](../pilares/marca/CLAUDE.md) | Desconocido | Medio | Alto | Semana del 23 de noviembre (3 llamadas y página de Posicionamiento) |

**Explicación.** Para quien paga, «ingeniero de IA» suena igual que cientos de freelancers, agencias y «lo hago yo con ChatGPT». Posicionarte es decidir y escribir: para quién eres (1–2 industrias o un tipo de empresa), qué problema caro resuelves, contra qué alternativas te comparan y por qué tú; de ahí salen los pilares editoriales (contenido para compradores: dinero, tiempo, riesgo y «¿aplica a mi negocio?», no tutoriales para colegas) y la oferta de entrada que el bot ofrece. Y en B2B nadie contrata por un video bonito, sino porque vio a alguien parecido a él con resultados; pero si tu contrato no dice nada o firmaste confidencialidad, no puedes usar el nombre del cliente, su logo ni capturas. La Ley Federal de Protección al Consumidor (artículo 32) exige publicidad veraz y comprobable, y usar la imagen de una persona requiere su consentimiento (artículo 87 de la Ley Federal del Derecho de Autor). Hazlo sistema: cláusula de caso de éxito con niveles (nombre, logo, cifras, video o anónimo), línea base desde el kickoff y petición de testimonio en el pico de satisfacción.

**Por qué importa.** Sin posicionamiento los setters venden «lo que el cliente pida», cada proyecto sale a la medida (y reciclar código deja de funcionar), compites por precio y la pauta atrae curiosos; sin casos tus setters cierran con promesas: más objeciones, ciclos largos y descuentos.

**Dónde se conecta.** Marca (Posicionamiento y Guía de voz en Conocimiento), Ventas (guiones, calificación y referidos), Marketing (CTA y palabras clave), Clientes (permiso de uso por niveles) y Legal (cláusula en las plantillas).

**Primer paso.** Esta semana escribe a tus 3 mejores clientes y pídeles 20 minutos por Zoom (con permiso para grabar) con 4 preguntas por adelantado: ¿qué problema tenías?, ¿qué otras opciones consideraste?, ¿por qué nos elegiste?, ¿qué cambió después?; al final pide testimonio con permiso por niveles y a quién se lo recomendarían. Con las transcripciones escribe tu posicionamiento en una página con el método de April Dunford.

**En la ruta.** Fase 0, entregable 5 (3 llamadas con tus mejores clientes y página de Posicionamiento). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://www.aprildunford.com>
- <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFDA.pdf>
- <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf>
- <https://expansion.mx/mercadotecnia/2023/08/22/profeco-publica-dof-guia-de-publicidad-para-influencers>

<a id="pc9"></a>

### 9. Cada lead de ManyChat, WhatsApp o Zoom te obliga bajo la nueva ley de datos personales

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Legal, riesgo y accesos](../pilares/legal/CLAUDE.md) | Desconocido | Bajo | Alto | 30 de noviembre (aviso integral publicado en tu página web) |

**Explicación.** Desde el 21 de marzo de 2025 rige una nueva Ley Federal de Protección de Datos Personales en Posesión de los Particulares (reformada el 14 de noviembre de 2025); el INAI desapareció y la autoridad es la Secretaría Anticorrupción y Buen Gobierno. Cuando el bot pide nombre, empresa, teléfono y presupuesto, o grabas una llamada, tú eres el «responsable»: necesitas aviso de privacidad integral en tu página web y aviso simplificado en el bot, en WhatsApp y en Zoom con liga al integral; decir para qué usas los datos; guardar prueba del consentimiento y atender los derechos ARCO (acceso, rectificación, cancelación y oposición). Según IDC la ley nueva ya no exige listar en el aviso las transferencias, pero decir con quién compartes (setters, ManyChat, Pipedrive, Meta y contadora) sigue siendo buena práctica y lo piden los corporativos. Meta además exige permiso previo para que tú inicies mensajes por WhatsApp. Para no tener cuatro versiones del permiso, una sola fuente: el «Acepto» vive en ManyChat (fecha, canal y versión del texto) y n8n lo copia al deal.

**Por qué importa.** Las multas van de 100 a 320,000 UMA y pueden duplicarse con datos sensibles; sin consentimiento guardado no puedes defenderte de una queja ni demostrar el opt-in ante Meta; y los corporativos lo piden en su alta de proveedor.

**Dónde se conecta.** Legal (página «Datos que guardamos», versiones del aviso y bitácora ARCO), Marketing (primer mensaje del Anfitrión), Ventas (frase de grabación en Zoom; los leads manuales reciben el link) y Automatizaciones (Filtro consulta ManyChat y Pipedrive, no Notion).

**Primer paso.** Esta semana escribe en Notion la página «Datos que guardamos» (fuente → dato → para qué → dónde vive → quién lo ve → proveedor y país) y con ella pide a tu abogado el aviso integral, el simplificado para ManyChat, WhatsApp y Zoom y la frase de grabación; antes del 30 de noviembre publica el integral en una página web simple con tu oferta y el botón a WhatsApp o a tu agenda.

**En la ruta.** Fase 0, entregables 6 (abogado: aviso de privacidad) y 8 (página web con el aviso integral). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>
- <https://idconline.mx/corporativo/2025/04/01/nueva-ley-de-proteccion-de-datos-cambios-en-derechos-y-obligaciones>
- <https://www.legiscope.com/blog/lfpdppp-mexico-guia-cumplimiento.html>

<a id="pc10"></a>

### 10. La propuesta no basta como contrato, tu código reciclado podría no ser tuyo y lo que hace la IA sola no tiene autor

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P0 | [Legal, riesgo y accesos](../pilares/legal/CLAUDE.md) | Desconocido | Medio | Alto | Semana del 16 de noviembre (etiquetado de repos); 30 de noviembre (abogado contratado); 15 de enero (plantillas) |

**Explicación.** La Ley Federal del Derecho de Autor presume que en una obra por encargo los derechos patrimoniales son de quien la encarga y paga, salvo pacto en contrario (artículo 83), y en caso de duda el contrato se interpreta a favor del autor (artículo 83 bis): eso puede incluir lo genérico que construyas durante su proyecto. Además, en el Amparo Directo 6/2025 la Suprema Corte resolvió que solo una persona física puede ser autora y que una obra generada solo por IA no se protege: lo que tus agentes generen sin aporte humano demostrable puede no ser algo que puedas ceder o defender. Se resuelve con un contrato marco (una vez por cliente) y la Propuesta firmada como anexo de alcance: lo hecho a la medida se cede al pagar el 100%; tus componentes previos siguen siendo tuyos con licencia perpetua no exclusiva; usas herramientas de IA bajo tu dirección; código, prompts y documentación son confidenciales; aceptación tácita (5 días hábiles sin observaciones por escrito); cambios con costo; límite de responsabilidad; y encargo de datos. El límite reduce el riesgo pero no lo elimina: un seguro de responsabilidad civil profesional para empresas de tecnología (errores y omisiones) cubre reclamos y gastos de defensa; la responsabilidad civil general no cubre errores profesionales.

**Por qué importa.** Sin esto un cliente molesto puede reclamar el componente que reutilizas, el último pago se atora en «ajustes», un competidor podría alegar que no hay derechos que ceder y, si un bot tuyo da un dato equivocado a los clientes de tu cliente, el reclamo sale de tu patrimonio.

**Dónde se conecta.** Legal (plantillas del abogado), Producto (repos clasificados por derechos; revisión humana y registro de decisiones en cada PR como evidencia de tu aporte), Clientes (acta de entrega) y Administración (cobro por hitos y costo del seguro dentro del precio piso).

**Primer paso.** Esta semana pide a un abogado de contratos y propiedad intelectual cotización por 4 plantillas (contrato marco, carta provisional para colaboradores, NDA y acta de entrega) con la cláusula de herramientas preexistentes y de uso de IA; mientras llegan, agrega esa cláusula a tus propuestas y etiqueta cada repo como «mío», «de cliente» o «dudoso» (los dudosos no se reutilizan). En Fase 2 pide a un corredor cotización de responsabilidad civil profesional y de ciberriesgo.

**En la ruta.** Fase 0, entregables 4 (etiquetado de repos) y 6 (abogado: contrato marco y NDA); Fase 2, entregable 6 (cotización del seguro). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://mley.mx/LFDA/articulo/83/>
- <https://mley.mx/LFDA/articulo/83-bis/>
- <https://www.scjn.gob.mx/sites/default/files/listas/documento_dos/2025-06/AD%206-2025.pdf>
- <https://expansion.mx/tecnologia/2025/07/16/obras-hechas-con-ia-no-tienen-derecho-de-autor-scjn>
- <https://www.chubb.com/mx-es/empresas/seguro-de-responsabilidad-civil-profesional-para-empresas-de-tecnologia.html>

## Prioridad P1

Los 7 puntos P1. Sus entregables caen en las Fases 0 y 1 (del 10 de noviembre al 31 de enero).

<a id="pc11"></a>

### 11. Una empresa grande no te paga hasta que pasas su alta de proveedor, y después te paga según su calendario

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P1 | [Administración y finanzas](../pilares/admin/CLAUDE.md) | Desconocido | Bajo | Alto | Hoy (opinión de cumplimiento); 30 de noviembre (expediente de proveedor) |

**Explicación.** Antes del primer pago, el área de compras de un corporativo pide un expediente: Constancia de Situación Fiscal, opinión de cumplimiento del SAT (la «32-D») positiva y reciente (algunas la piden con menos de 30 días de emitida), carátula bancaria, identificación o acta, contrato, NDA, aviso de privacidad y a veces póliza de seguro. Si tu opinión sale negativa por una declaración atrasada (aunque sea en ceros), se atora el pago. Ya dado de alta, tu factura entra a su ciclo de pagos, que puede ser de 30, 60 o más días, y una factura con el método equivocado (PUE o PPD) te la regresan: pide a tu contadora la regla escrita para anticipos e hitos antes de facturar el primero. Si ese cliente está en Cadenas Productivas de Nafin, puedes adelantar el cobro con factoraje: la afiliación del proveedor no tiene costo y solo pagas el descuento por los días que adelantas.

**Por qué importa.** El proyecto puede estar entregado y el dinero detenido semanas por un papel, mientras tú ya pagaste pauta, herramientas y, si no aplicas la regla de comisión sobre lo cobrado, comisiones; la promesa de arrancar en 48 horas es irreal con corporativos si no lo preguntas antes. Tener el expediente listo acorta el primer cobro y te hace ver como proveedor formal frente a agencias grandes.

**Dónde se conecta.** Administración (expediente de proveedor, descarga mensual de la Constancia y la 32-D y plazo real de pago de cada cliente en Clientes), Ventas (la Propuesta pregunta por el alta, los documentos, los días y el plazo de pago), hoja de dinero (cobros con fecha real en el flujo de 13 semanas) y Legal (NDA y aviso de privacidad tipo).

**Primer paso.** Hoy descarga tu opinión de cumplimiento en sat.gob.mx; si no sale positiva, mándasela a tu contadora para que corrija la causa. Esta semana arma en Google Drive la carpeta «Expediente de proveedor» (Constancia, 32-D, carátula bancaria con CLABE, comprobante de domicilio, identificación, aviso de privacidad y NDA tipo) y agrega a tu plantilla de propuesta la pregunta «¿Cuál es su proceso de alta de proveedor, qué documentos piden, en cuántos días y cuál es su plazo de pago?» y la cláusula de anticipo antes de iniciar.

**En la ruta.** Fase 0, entregables 3 (opinión de cumplimiento) y 7 (carpeta «Expediente de proveedor»). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://www.satfacil.com.mx/blog/opinion-cumplimiento-sat-positiva>
- <https://www.elcontribuyente.mx/2023/01/para-que-sirve-la-opinion-de-cumplimiento-o-carta-32-d-del-sat/>
- <https://www.nafin.com/portalnf/files/secciones/modulo-de-atencion-virtual/pdf/factoraje/cadenas_productivas.pdf>
- <https://www.banamex.com/es/empresasygobierno/financiamiento/corto-plazo/cadenas-nafinsa.htm>

<a id="pc12"></a>

### 12. El nombre de tu marca no es tuyo hasta que lo registras en el IMPI

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P1 | [Marca y contenido estratégico](../pilares/marca/CLAUDE.md) | Desconocido | Bajo | Alto | Semana del 16 de noviembre (búsqueda en MARCia); 31 de diciembre (solicitud ante el IMPI) |

**Explicación.** En México el uso exclusivo de una marca lo da el registro ante el IMPI, no tener el dominio, la cuenta de Instagram ni años publicando. Cada peso de pauta y cada video hacen más valioso un nombre que alguien más podría registrar primero. Se registra por clase; para ti probablemente 42 (desarrollo de software e IA), 41 (capacitación) y 35 (consultoría y publicidad). La solicitud en línea cuesta alrededor de $2,800 pesos por clase con IVA (cerca de $3,130 en ventanilla; confírmalo en la tarifa vigente), el examen tarda de 4 a 6 meses si no hay objeciones (algunas guías calculan de 6 a 12 meses en total) y el registro dura 10 años renovables. Si tu marca es tu propio nombre, pregúntale al abogado si conviene registrarlo tal cual o junto con tu logo.

**Por qué importa.** Si otro lo registra antes en tus clases, puede obligarte a cambiar de nombre, bajar contenido o negociar con él justo cuando la marca ya vende; además, clientes corporativos y plataformas piden pruebas de titularidad para verificar cuentas o defenderte de suplantaciones.

**Dónde se conecta.** Marca (decidir el nombre definitivo en la página de Posicionamiento antes de registrarlo), Legal (tabla de cuentas críticas y vencimientos: expediente, clases y renovación; revisión mensual de suplantaciones) y roadmap (el registro pasa de la Fase 3 a la Fase 1).

**Primer paso.** Esta semana busca tu nombre y sus variantes en MARCia, el buscador del IMPI, en las clases 35, 41 y 42; si está libre, presenta en diciembre la solicitud en Marca en Línea a nombre de quien será dueño de la marca (tú o tu sociedad, según lo que decidas con la contadora en la junta de régimen), y si aparece algo parecido, paga una hora con un abogado de propiedad industrial antes de presentar.

**En la ruta.** Fase 0, entregable 4 (búsqueda en MARCia) y Fase 1, entregable 4 (solicitud ante el IMPI antes del 31 de diciembre). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://www.elimparcial.com/mexico/2026/07/14/como-registrar-una-marca-ante-el-impi-el-caso-del-pato-merlin-explica-el-tramite-costo-y-beneficios-en-2026/>
- <https://praxiumconsultores.com/blog/cuanto-cuesta-registrar-una-marca-en-el-impi>
- <https://www.noticiasgobierno.com/como-registrar-marca-impi-2026/>

<a id="pc13"></a>

### 13. Tú eres el cuello de botella del sistema que estás construyendo

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P1 | [Automatizaciones y operación del sistema](../pilares/automatizaciones/CLAUDE.md) | Desconocido | Bajo | Alto | Esta semana (lista de decisiones y bloques fijos en Calendar); primera semana de diciembre (vacante del asistente) |

**Explicación.** La regla «nada sale sin mi OK», más grabar, cerrar, desarrollar y supervisar, te vuelve el engrane sin repuesto: si viajas, grabas o te enfermas, las aprobaciones vencen, los leads se enfrían y nadie puede apretar el botón rojo a las 11 de la noche. El primer diseño de este sistema ya sumaba más de 9 horas de rituales a la semana contra una meta de 5. Faltan cuatro piezas de gestión: un presupuesto de 5 horas de gestión medido con bloques «Gestión» en Calendar; aprobación por excepción (lo que coincide con algo ya aprobado no se vuelve a aprobar: factura igual a la propuesta aprobada, recordatorio con plantilla aprobada, publicación dentro de la parrilla aprobada); un primer puesto, un asistente de operación y administración de medio tiempo y no técnico desde enero, que sea suplente con límites bajos y pueda pausar todo pero no reactivar; y una agenda de creador: bloques de grabación sin interrupciones, dos ventanas de aprobación de 10 minutos y un banco de 3–4 semanas de videos. Hasta que entre el asistente, nada escala a un puesto vacío: una tarjeta sin decisión vence y pasa a tu siguiente ventana.

**Por qué importa.** Un lead que espera 2 días una aprobación ya se enfrió y una fecha fiscal no espera; cansado grabas peor y cierras menos; y un sistema que solo funciona contigo no aguanta una semana fuera.

**Dónde se conecta.** Matriz de aprobaciones (Conocimiento), Aprobaciones, Gabinete (mensaje único de las 7:10 y bloques protegidos), asistente de operación (dueño operativo de Administración y Clientes) y Google Calendar.

**Primer paso.** Esta semana revisa tu WhatsApp y tu Gmail del último mes y lista las 15 decisiones que te consultaron; ponles aprobador, límite en MXN y si se aprueban por excepción; crea en Google Calendar los bloques fijos de grabación, las ventanas de 9:30 y 17:30 y los bloques «Gestión»; en la primera semana de diciembre publica la vacante del asistente de medio tiempo para que entre en enero.

**En la ruta.** Fase 1, entregables 5 (vacante del asistente) y 8 (entra el asistente en enero). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://www.paulgraham.com/makersschedule.html>

<a id="pc14"></a>

### 14. Nadie mide cuánto tarda en contestarse un lead ni qué dicen tus setters en tu nombre

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P1 | [Ventas y setters](../pilares/ventas/CLAUDE.md) | Desconocido | Medio | Alto | 30 de noviembre (campos obligatorios en Pipedrive); se mide del 11 al 31 de enero |

**Explicación.** La rapidez de la primera respuesta humana es la palanca más barata de ventas: en el estudio publicado en Harvard Business Review en 2011, las empresas que intentaron contactar dentro de la primera hora tuvieron casi 7 veces más probabilidad de calificar al prospecto (las cifras de «21 veces» o «100 veces» que circulan vienen de otro estudio). Pero la velocidad no debe depender de un setter pegado al teléfono: cola abierta (lo toma quien esté disponible y se reasigna sin sanción a los 30 minutos), el bot ofrece a los leads A agendar directo en tu página de citas y la primera conversación cierra con cita u horario para contestar dentro de la ventana de 24 horas de WhatsApp. Por lead necesitas hora de entrada, hora del primer contacto humano y motivo de pérdida de lista cerrada (incluido «ahora no» con fecha de recontacto). Y como el cliente lee lo que escribe el setter como si lo dijeras tú: prueba de alta antes de tocar leads reales y lectura mensual de conversaciones.

**Por qué importa.** Cada lead que espera horas es pauta tirada; cada «ahora no» sin fecha de recontacto es un lead que pagaste y tiraste; un setter que promete lo que no puedes entregar genera reembolsos y comentarios que pegan directo a tu marca personal.

**Dónde se conecta.** Ventas (Repartidor, Playbook y Diccionario comercial), Marketing (el Anfitrión agenda a los leads A), Pipedrive (hora de entrada, actividad «Primer contacto» y motivo de pérdida obligatorios) y Tablero del CEO (mediana de primera respuesta).

**Primer paso.** Esta semana escríbele a tu propio Instagram y a tu WhatsApp de negocio como si fueras prospecto (o pídeselo a un amigo) en 3 horarios distintos y anota cuánto tardan en contestarte y qué te dicen; lee 3 conversaciones recientes de cada setter. Con eso escribe en una línea el tiempo de respuesta objetivo por canal y los 6–8 motivos de pérdida, y hazlos obligatorios en Pipedrive.

**En la ruta.** Fase 0, entregable 8 (Pipedrive con campos obligatorios) y criterio de Fase 1 (mediana de primera respuesta humana ≤15 minutos hábiles en leads A). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://scholarsarchive.byu.edu/facpub/9711>
- <https://ainora.lt/blog/lead-response-time-statistics-every-study-2026>

<a id="pc15"></a>

### 15. El setter vende y tú heredas la promesa: falta el traspaso de la venta a la entrega

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P1 | [Clientes y post-venta](../pilares/clientes/CLAUDE.md) | Desconocido | Bajo | Alto | Tu próximo cierre; plantilla «Proyecto ganado» del 1 al 11 de diciembre |

**Explicación.** Tus setters cobran por cerrar, no porque el proyecto salga bien, así que es normal que prometan fechas, funciones o resultados que no conoces. Antes de cualquier kickoff necesitas por escrito: dolor del cliente, qué se le prometió con sus palabras, presupuesto, fecha esperada, quién decide y quién paga, qué datos y sistemas tiene y qué resultado lo haría feliz; y una lista de «clientes que no aceptamos». En el kickoff: patrocinador y responsable interno, cuentas de APIs, nube y WhatsApp creadas a nombre del cliente (te invita como usuario), canal oficial y 3 métricas de línea base.

**Por qué importa.** Una promesa del setter que no puedes cumplir se convierte en «me engañaron» contra tu marca, no contra el setter; un cliente mal elegido consume tiempo, no da testimonio y a veces no paga; y si las cuentas quedan a tu nombre, alguien queda de rehén al terminar.

**Dónde se conecta.** Clientes (plantilla «Proyecto ganado» con su checklist de kickoff), Ventas (campos de traspaso en Pipedrive y Propuesta), Producto (brief técnico después del pago) y Legal (cuentas a nombre del cliente).

**Primer paso.** En tu próximo cierre, antes del kickoff, haz una llamada de 15 minutos con el setter: ¿qué le prometiste?, ¿a quién?, ¿para cuándo?, ¿qué te preocupa de este cliente?; escribe las respuestas en la plantilla «Proyecto ganado» y, con lo que aprendas, la página «Clientes que no aceptamos» con 5 señales.

**En la ruta.** Fase 0, entregable 8 (campos de traspaso en Pipedrive) y Fase 1, entregable 2 (plantilla «Proyecto ganado»). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.** La arquitectura no cita fuentes externas para este punto.

<a id="pc16"></a>

### 16. Meta optimiza tu pauta para conseguir mensajes, no clientes

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P1 | [Marketing y adquisición](../pilares/marketing/CLAUDE.md) | Desconocido | Medio | Alto | Antes del 11 de enero (cuando se escala la pauta) |

**Explicación.** En los anuncios que abren WhatsApp o Instagram Direct, Meta busca a quien más probablemente te escriba, porque solo aprende de lo que le reportas. Pero con volúmenes B2B (pocas ventas al mes) Meta no junta suficientes compras para aprender: según su guía de la fase de aprendizaje, un conjunto de anuncios necesita alrededor de 50 eventos de optimización en 7 días para salir de ella, y cada cambio importante la reinicia. Regla: optimiza por el evento de más volumen que sí predice venta (LeadSubmitted cuando el prospecto pasa la calificación) y manda lead calificado y compra desde Pipedrive solo para medir y dar valor. Dato técnico: la acción nativa de ManyChat solo envía LeadSubmitted y Purchase y está documentada para Instagram y Messenger; para WhatsApp el evento sale de n8n a la Conversions API (pide un dataset ligado a tu cuenta de WhatsApp Business, la API en la nube y el ctwa_clid). Necesitas un tope: lo que vale un lead calificado = (ticket × margen − comisión) × tasa de cierre; de ahí sale el costo por lead calificado máximo. Y una regla de atribución escrita: desde el 12 de enero de 2026 Meta dejó de reportar las ventanas de 7 y 28 días por visualización, así que sus números y los de tu CRM nunca van a cuadrar.

**Por qué importa.** Cada peso extra compra más curiosos que preguntan «¿precio?» y desaparecen; mover presupuestos cada mañana reinicia el aprendizaje; y tus setters se saturan mientras el costo por venta sube aunque el costo por conversación se vea bonito.

**Dónde se conecta.** Marketing (Anfitrión, Brújula y la junta del lunes), Automatizaciones (lead_id, ctwa_clid y eventos desde n8n) y Ventas (etapas que equivalen a calificado y compra).

**Primer paso.** Antes de escalar la pauta (desde el 11 de enero), abre una hoja con 6 celdas (ticket, margen, comisión, % de cierre de calificados, IVA no acreditable y % del margen que aceptas invertir), llénala con tus últimos 10 proyectos y fija el costo por lead calificado máximo; crea en Ads Manager una regla automática que pause si el gasto del día pasa el tope; decide presupuesto y creativos solo en la junta del lunes y, antes de optimizar a LeadSubmitted, comprueba en el Administrador de eventos que esté llegando.

**En la ruta.** Fase 1, entregable 9 (pauta optimizada por lead calificado desde el 11 de enero). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://help.manychat.com/hc/en-us/articles/14580897414300-Conversions-API-CAPI-integration>
- <https://community.manychat.com/general-q-a-43/ads-optimization-3661>
- <https://developers.facebook.com/documentation/ads-commerce/conversions-api/business-messaging>
- <https://developers.facebook.com/blog/post/2025/10/16/ads-insights-api-metric-availability-updates/>
- <https://ppc.land/meta-restricts-attribution-windows-and-data-retention-in-ads-insights-api/>

<a id="pc17"></a>

### 17. Tus tareas programadas tienen tope diario y gastan tu cuota: n8n vigila, Claude decide

| Prioridad | Pilar | Dominio | Esfuerzo | Impacto | Fecha límite cercana |
|:-:|---|---|:-:|:-:|---|
| P1 | [Automatizaciones y operación del sistema](../pilares/automatizaciones/CLAUDE.md) | Conocido | Bajo | Alto | Antes de crear la primera rutina (Fase 1, diciembre) |

**Explicación.** Lo conoces; va como recordatorio porque cambió el diseño. Las tareas programadas (routines) de Claude Code están en research preview y tienen un tope diario de corridas por cuenta: Pro 5, Max 15 y Team/Enterprise 25 (puede cambiar; no se encontró el de Ultra). Cada corrida gasta del mismo uso de la suscripción con el que desarrollas, también cuentan las que dispara n8n por API, el intervalo mínimo es de una hora, son de tu cuenta individual (lo que hacen aparece a tu nombre) y arrancan con todos tus conectores con permiso de escritura. El primer diseño sumaba 13–19 corridas al día. Además hay reportes abiertos de conectores de Google (Gmail, Calendar y Drive) que no aparecen al configurar rutinas en la nube. Regla: n8n escucha eventos y lleva los relojes (cola, reasignación a los 30 minutos, barridos e interruptor general); Claude despierta solo cuando hay algo que decidir; y el agente que lee mensajes de desconocidos (Anfitrión) vive en ManyChat sin llaves.

**Por qué importa.** Si el sistema depende de 15 corridas al día, el día que se acaba el tope no sale el mensaje matutino ni se arma el repo del cliente, y además te quedas sin cuota para desarrollar; y una rutina con conectores de más es una puerta abierta con tu identidad.

**Dónde se conecta.** Automatizaciones (Gabinete, presupuesto de corridas y plan B de cada disparo por API), Producto (Andamio), tabla de agentes del README (conectores autorizados) y riesgos (piezas en vista previa).

**Primer paso.** Antes de crear la primera rutina, escribe en el README la tabla agente → corridas al día → conectores permitidos y deja 1 corrida programada al día (el Gabinete a las 7:10; los lunes hace también el reporte del embudo en la misma sesión); prueba que el conector de Google Calendar aparezca en esa rutina y quítale los conectores que no usa.

**En la ruta.** Fase 1, entregable 3 (chat «Automatizaciones y Gabinete» con el mensaje de las 7:10). Ver [la ruta por fases](05-ruta-stack-riesgos.md#ruta-por-fases).

**Fuentes.**

- <https://code.claude.com/docs/en/routines>
- <https://www.implicator.ai/anthropic-ships-claude-code-routines-cloud-automations-that-run-without-your-mac.md>
- <https://crackedpm-site.pages.dev/preflight/routines/r-08-usage-and-limits>
- <https://claudeissues.com/issue/87540-bug-bug-report-cloud-routines-cannot-attach-first-party-google-workspace-connect>
- <https://simonwillison.net/2025/Sep/19/notion-lethal-trifecta>

## Proporción 90/10

Tu regla para cualquier lista de ideas o huecos, tal cual la escribiste: «Cuando te pida ideas necesito que un 90% de la información esté enfocada a temas que no conozco. No quiero tener un sesgo de la información que sabes de mí. El otro 10% puede ser enfocado a cosas que sí se relacionan con lo que ya sé.»

Cómo se aplicó: tú dominas ingeniería de IA, agentes, LLMs, código y automatización técnica. Cada punto ciego se marcó como **desconocido** (áreas que un ingeniero de IA normalmente no domina: legal, fiscal, finanzas, ventas, operación de equipos, experiencia del cliente, marca, distribución, psicología del comprador o riesgo de plataformas) o **conocido** (IA e ingeniería). Como máximo 1 de cada 10 puede ser conocido.

| Dominio | Puntos | Proporción | Cuáles |
|---|:-:|:-:|---|
| Desconocido | 16 | 94.1% | Del [1](#pc1) al [16](#pc16) |
| Conocido | 1 | 5.9% | [17](#pc17) (tope y cuota de las tareas programadas de Claude) |

Lo que dice la arquitectura (campo `proporcion_90_10`):

> 16 de 17 puntos ciegos (94.1%) son de dominio desconocido (plataformas y telecomunicaciones, titularidad legal de cuentas, fiscal, laboral, compensación comercial, dinero y caja, oferta y capacidad, posicionamiento y casos, datos personales, contratos y propiedad intelectual, compras corporativas, registro de marca, gestión, operación comercial, experiencia del cliente y economía de la pauta) y 1 de 17 (5.9%) es conocido (tope y cuota de las tareas programadas de Claude). Cumple la regla 90/10 con margen: el punto de cuentas se retituló alrededor de la titularidad legal para que no cuente como seguridad informática, entraron 2 nuevos de dominio desconocido (alta de proveedor y registro de marca) y el de agentes que leen DMs salió de la lista porque ya vive en principios, orquestación y riesgos.

Lo que dejó la revisión de sesgo de la verificación del 10 de noviembre, ya aplicado:

- **El sesgo estaba en las soluciones, no en los huecos.** Casi todo hueco no técnico se resolvía con un agente, una base o un campo nuevo; en lo legal, fiscal, laboral y comercial el paso que cambia el resultado es humano. Por eso los primeros pasos empiezan con una persona antes que con una herramienta: una plática con cada setter (comisiones), una prueba de cliente misterioso y lectura de conversaciones (velocidad), una llamada con el setter antes del kickoff (traspaso), el abogado laboral (setters) y llamadas a clientes (posicionamiento).
- **Lo «conocido» también necesita verificación.** El error de dato más grande apareció en tu propio terreno: el diseño asumía decenas de tareas programadas al día y el tope del plan Max es de 15 corridas ([V2](#v2)).
- **La Fase 0 se mide por trámites cerrados**, no por sistema construido, para que la ingeniería no se coma las semanas que tienen fecha.

## Datos verificados

Los datos duros más sensibles de la arquitectura (plazos, precios, leyes y reglas de plataformas) se revisaron con búsqueda web el 10 de noviembre de 2026: 29 verificaciones, de las que 21 salieron correctas, 7 con matices y 1 se corrigió. Todas las correcciones y matices ya están aplicados en la arquitectura y en estos documentos. Lo que no aparece en esta lista sale de las fuentes de cada punto ciego. La fuente es [data/verificacion.json](../data/verificacion.json).

Nota de método: WebFetch no pudo abrir www.ycloud.com ni developers.facebook.com porque esos dominios no estaban permitidos en la red de la sesión, así que las tarifas oficiales de Meta no se leyeron directo. Varias cifras de precios vienen de fuentes secundarias que coinciden entre sí; cada corrección lo dice cuando es así. El conteo de corridas diarias de [V2](#v2) sale de sumar las cadencias del primer diseño.

**Estados**

- **Correcto:** el dato se confirmó; a veces con una precisión útil que ya se sumó.
- **Con matices:** el dato es correcto en lo general, pero había que precisarlo o quitarle una parte.
- **Corregido:** el dato estaba mal y se corrigió.
- **Sin confirmar:** ninguna verificación quedó completa en este estado, pero varias dejaron un dato suelto sin confirmar; están juntos en [Lo que sigue sin confirmar](#lo-que-sigue-sin-confirmar).

Las afirmaciones se revisaron sobre la versión anterior de los puntos ciegos, que tenía otra numeración; aquí van sin esa referencia y la columna «Dónde está hoy» dice dónde quedó cada una.

| # | Tema | Estado | Dónde está hoy |
|:-:|---|---|---|
| [V1](#v1) | Líneas celulares vinculadas a la CURP | Correcto | [punto ciego 1](#pc1); [Fase 0](05-ruta-stack-riesgos.md#fase-0) |
| [V2](#v2) | Tope de corridas de las tareas programadas | Corregido | [punto ciego 17](#pc17); [presupuesto de corridas](03-flujos-y-ritmo.md#presupuesto-de-corridas-de-claude); [stack](05-ruta-stack-riesgos.md#stack-recomendado) (agentes) |
| [V3](#v3) | Paquete fiscal 2027: tope de RESICO e IVA de 7% | Con matices | [punto ciego 3](#pc3) |
| [V4](#v4) | Precios de WhatsApp desde octubre de 2026 | Con matices | [punto ciego 1](#pc1); [stack](05-ruta-stack-riesgos.md#stack-recomendado) (WhatsApp de ventas) |
| [V5](#v5) | Prohibición de chatbots de IA de propósito general en WhatsApp | Correcto | [punto ciego 1](#pc1); Anfitrión ([pilar marketing](../pilares/marketing/CLAUDE.md)) |
| [V6](#v6) | LeadSubmitted de ManyChat a la Conversions API | Con matices | [punto ciego 16](#pc16); [flujo 1](03-flujos-y-ritmo.md#flujo-1), paso 3 |
| [V7](#v7) | Ventanas de atribución de Meta | Correcto | [punto ciego 16](#pc16); Brújula ([pilar marketing](../pilares/marketing/CLAUDE.md)) |
| [V8](#v8) | Cómo funcionan las tareas programadas de Claude | Correcto | [punto ciego 17](#pc17); [riesgos](05-ruta-stack-riesgos.md#riesgos) 3 y 4; [principio 12](01-arquitectura.md#principios) |
| [V9](#v9) | Nueva ley de datos personales (LFPDPPP) | Con matices | [punto ciego 9](#pc9) |
| [V10](#v10) | Artículo 285 de la Ley Federal del Trabajo | Correcto | [punto ciego 4](#pc4) |
| [V11](#v11) | Obra por encargo (LFDA, artículo 83) y obras hechas solo por IA | Correcto | [punto ciego 10](#pc10) |
| [V12](#v12) | RESICO 2026: tasas y tope | Correcto | [punto ciego 3](#pc3) |
| [V13](#v13) | Deducción de comisiones: CFDI y pagos de más de $2,000 | Correcto | [punto ciego 5](#pc5); [flujo 5](03-flujos-y-ritmo.md#flujo-5), paso 5 |
| [V14](#v14) | Precios de Notion y Custom Agents | Con matices | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (cerebro); [riesgos](05-ruta-stack-riesgos.md#riesgos) 8 |
| [V15](#v15) | Precios de Claude Max, Pro y Ultra | Correcto | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (agentes) |
| [V16](#v16) | Precios de la API de Claude | Correcto | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (IA dentro de los flujos) |
| [V17](#v17) | Remote Control | Correcto | [Orquestación](01-arquitectura.md#orquestación) |
| [V18](#v18) | Comisión de Stripe México | Correcto | [punto ciego 7](#pc7); [stack](05-ruta-stack-riesgos.md#stack-recomendado) (cobro) |
| [V19](#v19) | Comisión de Mercado Pago Link de pago | Correcto | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (cobro) |
| [V20](#v20) | Precio de ManyChat Pro | Correcto | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (conversaciones y bot) |
| [V21](#v21) | Planes de Pipedrive y reparto automático | Con matices | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (CRM y embudo); Repartidor ([pilar ventas](../pilares/ventas/CLAUDE.md)) |
| [V22](#v22) | Precio de n8n Cloud Starter | Correcto | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (eventos y relojes) |
| [V23](#v23) | Límites de la API de Notion | Correcto | [Riesgos](05-ruta-stack-riesgos.md#riesgos) 8 |
| [V24](#v24) | Precio de Bitwarden Premium | Correcto | [punto ciego 2](#pc2); [stack](05-ruta-stack-riesgos.md#stack-recomendado) (bóveda) |
| [V25](#v25) | Precio de Blotato Starter | Correcto | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (publicación) |
| [V26](#v26) | GitHub Free: minutos de Actions y Secret Protection | Correcto | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (código) |
| [V27](#v27) | Vercel: plan Hobby y precio de Pro | Correcto | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (hosting); [flujo 2](03-flujos-y-ritmo.md#flujo-2), paso 6 |
| [V28](#v28) | Estudio de HBR sobre velocidad de respuesta | Correcto | [punto ciego 14](#pc14) |
| [V29](#v29) | App de WhatsApp Business: listas de difusión | Con matices | [stack](05-ruta-stack-riesgos.md#stack-recomendado) (WhatsApp de ventas); [flujo 4](03-flujos-y-ritmo.md#flujo-4), paso 3 |

### Detalle de cada verificación

<a id="v1"></a>

#### V1. Líneas celulares vinculadas a la CURP · Correcto

- **Afirmación revisada:** Las líneas de prepago deben quedar vinculadas a la CURP con fecha según su último dígito (terminación 6: 15 de noviembre; 7: 30 de noviembre; 8: 15 de diciembre; 9: 31 de diciembre de 2026) y una línea suspendida no recibe el SMS para verificar WhatsApp.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado por varias fuentes; al 2 de noviembre la CRT reportaba 100.5 millones de líneas vinculadas. Hoy es 10 de noviembre: a las líneas con terminación 6 les quedan 5 días. Agregar dos datos: la línea suspendida no hace ni recibe llamadas ni SMS (solo emergencias), así que tampoco llegan códigos de bancos ni de WhatsApp; y hay 90 días después de la suspensión para regularizarla y conservar el número. El trámite se hace en el portal oficial de gob.mx y funciona aun con la línea suspendida.
- **Dónde está hoy:** [punto ciego 1](#pc1); [Fase 0](05-ruta-stack-riesgos.md#fase-0).
- **Fuentes:**
  - <https://www.infobae.com/mexico/2026/07/25/registro-de-lineas-con-curp-fechas-limite-de-la-crt-en-2026-segun-el-ultimo-digito-del-numero/>
  - <https://www.xataka.com.mx/telecomunicaciones/mexico-supero-100-millones-lineas-celulares-registradas-todavia-quedan-cuatro-fechas-limite-para-cerrar-ano>
  - <https://www.cronica.com.mx/nacional/2026/11/03/vinculacion-de-lineas-celulares-ya-supera-los-100-millones-gracias-a-la-participacion-ciudadana/>
  - <https://es.euronews.com/2026/10/09/registro-telefonos-moviles-con-curp-que-pasa-con-whatsapp-redes-suspenden-linea>
  - <https://www.elimparcial.com/tecnologia/2026/08/06/la-crt-permite-recuperar-lineas-telefonicas-suspendidas-por-no-registrarlas-a-tiempo-si-el-tramite-se-realiza-dentro-de-los-90-dias-posteriores-a-la-suspension/>

<a id="v2"></a>

#### V2. Tope de corridas de las tareas programadas · Corregido

- **Afirmación revisada:** Claude Code en la nube con plan Max (o Pro «si el uso es bajo») alcanza para las tareas programadas del sistema: Centinela 7:07, Gabinete 7:10 y su barrido cada 2 horas, Pulso 7:50 y 18:40, Pauta y Enlace 8:00, Aduana 8:20, Bibliotecario 22:40, las de lunes y viernes y las que n8n despierta por API.
- **Estado:** Corregido.
- **Corrección o precisión:** Las tareas programadas (routines) tienen un tope diario de corridas iniciadas por cuenta: Pro 5, Max 15, Team/Enterprise 25 (están en research preview y puede cambiar; no se encontró el tope de Ultra). Las cadencias del diseño suman unas 13–14 corridas en un día normal y 17–19 los lunes y viernes, sin contar barridos cada hora (Repartidor, Cobra, Tijeras) ni las corridas que dispara n8n, que cuentan contra el mismo tope; además, cada corrida gasta del uso de la suscripción. Corrección: agrupar en 3–4 rondas al día (matutina 7:07 que haga en una sola sesión Centinela, Gabinete, Pulso, Pauta, Enlace y Aduana; vespertina 18:40; nocturna 22:40), mover los barridos y revisiones de estado a n8n (no necesitan IA) y despertar a Claude solo cuando haya algo que decidir, dejando 4 o 5 corridas libres para eventos. El plan Pro no alcanza ni para la Fase 1.
- **Cómo quedó en el diseño final:** Se fue más lejos que la corrección: 1 tarea programada al día (el Gabinete a las 7:10) más eventos, con meta de 8 o menos corridas al día de las 15 del plan Max; la cola, los relojes y los barridos viven en n8n. Detalle en el [presupuesto de corridas](03-flujos-y-ritmo.md#presupuesto-de-corridas-de-claude).
- **Dónde está hoy:** [punto ciego 17](#pc17); [presupuesto de corridas](03-flujos-y-ritmo.md#presupuesto-de-corridas-de-claude); [stack](05-ruta-stack-riesgos.md#stack-recomendado) (agentes).
- **Fuentes:**
  - <https://www.implicator.ai/anthropic-ships-claude-code-routines-cloud-automations-that-run-without-your-mac.md>
  - <https://crackedpm-site.pages.dev/preflight/routines/r-08-usage-and-limits>
  - <https://code.claude.com/docs/en/routines>

<a id="v3"></a>

#### V3. Paquete fiscal 2027: tope de RESICO e IVA de 7% · Con matices

- **Afirmación revisada:** El paquete fiscal 2027 trae propuestas que cambian la cuenta (tope de RESICO y un esquema opcional de IVA); confirma con tu contadora qué quedó aprobado.
- **Estado:** Con matices.
- **Corrección o precisión:** Ya no son solo propuestas. Reforma a la Ley del ISR: Diputados la aprobó el 14 de octubre, el Senado la aprobó con cambios el 27 de octubre y Diputados avaló esos cambios a inicios de noviembre; sube el tope de RESICO de personas físicas de 3.5 a 5 millones de pesos al año (personas morales de 35 a 50 millones). Ley de Ingresos 2027 (aprobada sin cambios por el Senado el 27 de octubre): incluye la opción de pagar el IVA con una tasa de 7% sobre lo efectivamente cobrado, sin acreditar el IVA de tus gastos; al cliente se le sigue facturando 16%. Al 10 de noviembre no se encontró la publicación en el DOF; entrarían en vigor el 1 de enero de 2027. Cambia el primer paso: la simulación debe tener 4 escenarios (RESICO con IVA normal, RESICO con IVA de 7%, actividad empresarial y S.A.S.). El de 7% conviene si tienes poco IVA acreditable y puede salir más caro con mucha pauta, software y comisiones facturadas con IVA; pregunta a la contadora cómo y cuándo se elige la opción y cómo se combina con las retenciones de tus clientes empresa.
- **Dónde está hoy:** [punto ciego 3](#pc3).
- **Fuentes:**
  - <https://www.tiempo.com.mx/nacional/diputados-aprueban-reforma-a-la-ley-isr-deducciones-resico-2027/>
  - <https://www.razon.com.mx/mexico/2026/10/28/avala-senado-leyes-de-ingresos-y-de-derechos/>
  - <https://forbes.com.mx/?p=1444139>
  - <https://www.excelsior.com.mx/nacional/senado-aprueba-ley-ingresos-2027-preve-captar-mas-10-billones-pesos>
  - <https://idconline.mx/fiscal-contable/2026/10/21/resico-2027-te-conviene-el-nuevo-esquema-para-pagar-solo-el-7-de-iva>
  - <https://www.liderempresarial.com/aprueban-en-congreso-ley-de-isr-2027-que-modificaciones-hicieron-los-diputados-a-la-reforma/>

<a id="v4"></a>

#### V4. Precios de WhatsApp desde octubre de 2026 · Con matices

- **Afirmación revisada:** Desde octubre de 2026 Meta cobra más mensajes: marketing cerca de US$0.04 en México y servicio después de 1,000 gratis al mes por número.
- **Estado:** Con matices.
- **Corrección o precisión:** Desde el 1 de octubre de 2026 Meta cobra por mensaje los mensajes de servicio (respuestas libres dentro de la ventana de 24 horas) y las plantillas de utilidad dentro de esa ventana, que antes eran gratis. En México, según tablas de proveedores: servicio, utilidad y autenticación cerca de US$0.0085 y marketing cerca de US$0.0397. No se encontró confirmación de 1,000 mensajes de servicio gratis al mes (se parece a la regla anterior a noviembre de 2024): quítalo del cálculo. Lo que sí sigue gratis son las conversaciones que abre un anuncio de clic a WhatsApp (ventana de punto de entrada gratuito de 72 horas; algunos proveedores reportan hasta 7 días), así que conviene que la calificación y el primer seguimiento del setter ocurran dentro de esa ventana. Confirmar tarifas en tu cuenta de WhatsApp Business o con ManyChat.
- **Dónde está hoy:** [punto ciego 1](#pc1); [stack](05-ruta-stack-riesgos.md#stack-recomendado) (WhatsApp de ventas).
- **Fuentes:**
  - <https://respond.io/blog/whatsapp-pricing-change-2026>
  - <https://support.twilio.com/hc/en-us/articles/53100462475931-Notice-Changes-to-WhatsApp-s-Pricing-October-2026>
  - <https://teramont.net/blog/whatsapp-business-platform-service-message-pricing-2026>
  - <https://sleekflow.io/blog/whatsapp-business-price>

<a id="v5"></a>

#### V5. Prohibición de chatbots de IA de propósito general en WhatsApp · Correcto

- **Afirmación revisada:** Desde el 15 de enero de 2026 la API de WhatsApp prohíbe los chatbots de IA «de propósito general»; un bot que atiende y vende tus servicios sí está permitido.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado: aplicó a cuentas nuevas desde el 15 de octubre de 2025 y a todas desde el 15 de enero de 2026; salieron ChatGPT, Perplexity y similares. La prohibición aplica cuando la IA es el producto principal que se ofrece; un bot de atención, ventas o avisos de tu negocio está permitido. Regla práctica para el Anfitrión: que solo hable de tus servicios y no funcione como asistente general de preguntas libres.
- **Dónde está hoy:** [punto ciego 1](#pc1); Anfitrión ([pilar marketing](../pilares/marketing/CLAUDE.md)).
- **Fuentes:**
  - <https://respond.io/blog/whatsapp-general-purpose-chatbots-ban>
  - <https://9to5mac.com/2025/10/20/whatsapp-bans-ai-chatbots-from-using-its-business-api/>

<a id="v6"></a>

#### V6. LeadSubmitted de ManyChat a la Conversions API · Con matices

- **Afirmación revisada:** En los anuncios que abren WhatsApp o Instagram Direct, ManyChat manda LeadSubmitted a la Conversions API con una acción nativa cuando el prospecto pasa la calificación.
- **Estado:** Con matices.
- **Corrección o precisión:** La acción nativa de ManyChat («Send event to Meta Conversions API», en Ads Optimization) solo envía dos eventos, LeadSubmitted y Purchase, y su guía cubre anuncios de Instagram y Messenger. Para anuncios de clic a WhatsApp no se encontró confirmación de soporte nativo en ManyChat. Vía segura para WhatsApp: mandar el evento desde n8n a la Conversions API para mensajería de WhatsApp, que pide un dataset ligado a la cuenta de WhatsApp Business, la API en la nube y el ctwa_clid del primer mensaje (el diseño ya lo guarda). Antes de optimizar campañas a ese evento, comprueba en el Administrador de eventos que esté llegando.
- **Dónde está hoy:** [punto ciego 16](#pc16); [flujo 1](03-flujos-y-ritmo.md#flujo-1), paso 3.
- **Fuentes:**
  - <https://help.manychat.com/hc/en-us/articles/14580897414300-Conversions-API-CAPI-integration>
  - <https://community.manychat.com/general-q-a-43/ads-optimization-3661>
  - <https://developers.facebook.com/documentation/ads-commerce/conversions-api/business-messaging>
  - <https://docs.zernio.com/ads/send-whatsapp-conversion>

<a id="v7"></a>

#### V7. Ventanas de atribución de Meta · Correcto

- **Afirmación revisada:** Desde el 12 de enero de 2026 Meta dejó de reportar las ventanas de atribución de 7 y 28 días por visualización.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado por el anuncio de Meta para desarrolladores: la API de Insights dejó de devolver 7 y 28 días por visualización; siguen 1, 7 y 28 días después del clic, 1 día de visualización y 1 día de visualización con interacción. Afecta lo que leen Brújula y Pauta, por eso tiene sentido guardar snapshots propios.
- **Dónde está hoy:** [punto ciego 16](#pc16); Brújula ([pilar marketing](../pilares/marketing/CLAUDE.md)).
- **Fuentes:**
  - <https://developers.facebook.com/blog/post/2025/10/16/ads-insights-api-metric-availability-updates/>
  - <https://ppc.land/meta-restricts-attribution-windows-and-data-retention-in-ads-insights-api/>

<a id="v8"></a>

#### V8. Cómo funcionan las tareas programadas de Claude · Correcto

- **Afirmación revisada:** Las tareas programadas de Claude están en research preview, son de tu cuenta individual (no se comparten con el equipo y lo que hacen aparece como tú), no corren más de una vez por hora y arrancan con todos tus conectores con permiso de escritura.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado: research preview; pertenecen a tu cuenta individual de claude.ai, no las ven tus compañeros y cuentan contra tu tope diario; lo que hacen aparece a tu nombre; todos tus conectores se incluyen por defecto y Claude puede usar sus herramientas de escritura sin pedir permiso durante la corrida; el intervalo mínimo es de una hora; y se pueden disparar por API, así que n8n sí puede despertarlas. Ojo: hay reportes abiertos de conectores de Google (Gmail, Calendar y Drive) que no aparecen al configurar rutinas en la nube; prueba el Gabinete con Google Calendar antes de depender de él.
- **Dónde está hoy:** [punto ciego 17](#pc17); [riesgos](05-ruta-stack-riesgos.md#riesgos) 3 y 4; [principio 12](01-arquitectura.md#principios).
- **Fuentes:**
  - <https://code.claude.com/docs/en/routines>
  - <https://code.claude.com/docs/en/web-scheduled-tasks>
  - <https://claudeissues.com/issue/87540-bug-bug-report-cloud-routines-cannot-attach-first-party-google-workspace-connect>

<a id="v9"></a>

#### V9. Nueva ley de datos personales (LFPDPPP) · Con matices

- **Afirmación revisada:** Desde el 21 de marzo de 2025 rige la nueva LFPDPPP, el INAI desapareció y la autoridad es la Secretaría Anticorrupción y Buen Gobierno; necesitas aviso integral en tu web y uno «corto» en el bot; las multas se fijan en UMAs y se duplican con datos sensibles.
- **Estado:** Con matices.
- **Corrección o precisión:** Fechas, autoridad y multas son correctas (de 100 a 320,000 UMA; pueden subir hasta el doble con datos sensibles). Dos ajustes: la ley nueva habla de aviso «simplificado», no «corto», así que en ManyChat, WhatsApp y Zoom usa un aviso simplificado con liga al integral; y, según IDC, la ley nueva ya no exige listar en el aviso las transferencias de datos, aunque informar con quién compartes (setters, ManyChat, Pipedrive, Meta y contadora) sigue siendo buena práctica y lo piden los clientes corporativos. La ley tuvo una reforma el 14 de noviembre de 2025.
- **Dónde está hoy:** [punto ciego 9](#pc9).
- **Fuentes:**
  - <https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf>
  - <https://idconline.mx/corporativo/2025/04/01/nueva-ley-de-proteccion-de-datos-cambios-en-derechos-y-obligaciones>
  - <https://www.legiscope.com/blog/lfpdppp-mexico-guia-cumplimiento.html>

<a id="v10"></a>

#### V10. Artículo 285 de la Ley Federal del Trabajo · Correcto

- **Afirmación revisada:** El artículo 285 de la Ley Federal del Trabajo considera trabajadores a vendedores e impulsores de ventas cuando su actividad es permanente; ponerle «comisión mercantil» al contrato no basta.
- **Estado:** Correcto.
- **Corrección o precisión:** Texto confirmado. Matiz útil para el contrato: el mismo artículo exceptúa a quien no ejecuta personalmente el trabajo o solo interviene en operaciones aisladas, y lo que decide es si hay subordinación. Para comisionistas, la Suprema Corte ha resuelto que la indemnización se calcula con el salario del artículo 289 (promedio de lo ganado en el último año).
- **Dónde está hoy:** [punto ciego 4](#pc4).
- **Fuentes:**
  - <https://mley.mx/LFT/articulo/285/>
  - <https://mexico.justia.com/federales/leyes/ley-federal-del-trabajo/titulo-sexto/capitulo-ix/>
  - <https://scjn.gob.mx/sites/default/files/sinopsis_asuntos_destacados/documento/2016-11/2S-230211-JFFGS-443_0.pdf>

<a id="v11"></a>

#### V11. Obra por encargo (LFDA, artículo 83) y obras hechas solo por IA · Correcto

- **Afirmación revisada:** La Ley Federal del Derecho de Autor presume que en una obra por encargo los derechos patrimoniales son de quien la encarga y paga, salvo pacto en contrario (art. 83).
- **Estado:** Correcto.
- **Corrección o precisión:** Texto confirmado; el artículo 83 bis pide que el contrato sea claro y, en caso de duda, se interpreta a favor del autor: otra razón para la cláusula de herramientas preexistentes. Agregar: en el Amparo Directo 6/2025 la Suprema Corte resolvió que solo una persona física puede ser autora y que una obra generada solo por IA no se protege; lo que tus agentes generen sin aporte humano demostrable puede no ser una obra que puedas ceder o defender, así que el contrato debe apoyarse también en licencia y confidencialidad.
- **Dónde está hoy:** [punto ciego 10](#pc10).
- **Fuentes:**
  - <https://mley.mx/LFDA/articulo/83/>
  - <https://mley.mx/LFDA/articulo/83-bis/>
  - <https://www.scjn.gob.mx/sites/default/files/listas/documento_dos/2025-06/AD%206-2025.pdf>
  - <https://expansion.mx/tecnologia/2025/07/16/obras-hechas-con-ia-no-tienen-derecho-de-autor-scjn>

<a id="v12"></a>

#### V12. RESICO 2026: tasas y tope · Correcto

- **Afirmación revisada:** En RESICO de persona física pagas de 1% a 2.5% sobre lo cobrado sin restar gastos, con tope de 3.5 millones de pesos al año en 2026.
- **Estado:** Correcto.
- **Corrección o precisión:** Correcto para 2026. Para 2027 el tope sube a 5 millones si se publica la reforma ya aprobada por el Congreso (ver la verificación del paquete 2027).
- **Dónde está hoy:** [punto ciego 3](#pc3).
- **Fuentes:**
  - <https://www.satfacil.com.mx/blog/limite-resico-3-5-millones-que-hacer>
  - <https://www.pluxee.mx/blog/resico-que-es-quien-aplica-y-como-funciona/>
  - <https://www.pwc.com/mx/es/archivo/2026/paquete-economico-mx-2027.pdf>

<a id="v13"></a>

#### V13. Deducción de comisiones: CFDI y pagos de más de $2,000 · Correcto

- **Afirmación revisada:** Para deducir comisiones necesitas el CFDI del setter y pagar por transferencia si el pago pasa de $2,000.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado (LISR art. 27, fracción III): arriba de $2,000 se paga con transferencia, cheque nominativo, tarjeta o monedero autorizado, y con CFDI. Se mide por erogación, no por pago: partirlo en pagos chicos no lo vuelve deducible, y pagar mal también hace perder el IVA acreditable.
- **Dónde está hoy:** [punto ciego 5](#pc5); [flujo 5](03-flujos-y-ritmo.md#flujo-5), paso 5.
- **Fuentes:**
  - <https://sdv.com.mx/compendio/ley-isr/articulo-27/>
  - <https://idconline.mx/fiscal-contable/2024/07/22/pagos-en-efectivo-son-deducibles-para-impuestos>

<a id="v14"></a>

#### V14. Precios de Notion y Custom Agents · Con matices

- **Afirmación revisada:** Notion Plus aprox. US$10–12 por miembro al mes (Business aprox. US$20–24), los invitados no ocupan asiento, y los Custom Agents de Notion son una opción de Fase 3 que consume créditos.
- **Estado:** Con matices.
- **Corrección o precisión:** Precios correctos (Plus US$10 en pago anual o US$12 mensual; Business US$20 o US$24) y los invitados no cuentan como asiento. Matiz: Notion AI completo viene en Business (en Plus es una prueba limitada), y desde el 4 de mayo de 2026 los Custom Agents consumen créditos de Notion a US$10 por cada 1,000, que solo se compran en Business o Enterprise. Con el plan Plus recomendado no hay Custom Agents: si la Fase 3 los contempla, presupuesta el cambio a Business.
- **Cómo quedó en el diseño final:** Se recomienda Notion Plus; Business solo si necesitas Notion AI completo o Custom Agents (consumen créditos a US$10 por cada 1,000 desde el 4 de mayo de 2026 y solo se compran en Business o Enterprise).
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (cerebro); [riesgos](05-ruta-stack-riesgos.md#riesgos) 8.
- **Fuentes:**
  - <https://www.notion.com/help/custom-agent-pricing>
  - <https://www.notion.com/blog/introducing-custom-agents>
  - <https://dupple.com/pricing/notion>

<a id="v15"></a>

#### V15. Precios de Claude Max, Pro y Ultra · Correcto

- **Afirmación revisada:** Claude Max cuesta aprox. US$100 al mes (Pro US$20; Ultra US$200).
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado: entre fines de octubre e inicios de noviembre de 2026 Anthropic renombró Max 5x a «Max» (US$100) y Max 20x a «Ultra» (US$200) sin cambiar precios; Max y Ultra son solo de pago mensual y, según fuentes secundarias, incluyen créditos mensuales de API. Confirmar en claude.com/pricing.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (agentes).
- **Fuentes:**
  - <https://www.usagepricing.com/blueprint/activity/anthropic-2026-11-02-max-20x-becomes-ultra>
  - <https://www.buildmvpfast.com/blog/claude-max-plan-changes-ultra-5-hour-limit-2026>
  - <https://sessionwatcher.com/news/claude-ultra-200-month-max-100-pricing-page>

<a id="v16"></a>

#### V16. Precios de la API de Claude · Correcto

- **Afirmación revisada:** API de Claude por uso: Haiku 5.5 US$0.10/0.50 y Sonnet 5.5 US$2/10 por millón de tokens de entrada/salida; Batch API con 50% de descuento.
- **Estado:** Correcto.
- **Corrección o precisión:** Correcto. Precisión: el precio de Haiku 5.5 aplica a prompts de hasta 100K tokens (arriba de eso, US$0.50/2.50 por millón). En Sonnet 5.5 las lecturas de caché cuestan US$0.10 por millón.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (IA dentro de los flujos).
- **Fuentes:**
  - <https://platform.claude.com/docs/en/about-claude/pricing>

<a id="v17"></a>

#### V17. Remote Control · Correcto

- **Afirmación revisada:** Remote Control se usa solo cuando la tarea necesita tu computadora, porque exige tu máquina encendida; lo que atiende a clientes vive en sesiones en la nube que diriges desde el celular.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado: Remote Control corre como proceso local; si cierras la terminal o la máquina se suspende, la sesión termina. Requiere Claude Code 2.1.51 o posterior y admite una sesión remota por instancia.
- **Dónde está hoy:** [Orquestación](01-arquitectura.md#orquestación).
- **Fuentes:**
  - <https://code.claude.com/docs/en/remote-control>
  - <https://devops.com/claude-code-remote-control-keeps-your-agent-local-and-puts-it-in-your-pocket/>

<a id="v18"></a>

#### V18. Comisión de Stripe México · Correcto

- **Afirmación revisada:** Stripe México cobra 3.6% + $3 MXN más IVA por cobro con tarjeta nacional.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado en la página de precios de Stripe México: las comisiones no incluyen IVA y se les suma 16%. Las tarjetas internacionales llevan 0.5% adicional; el costo de meses sin intereses revísalo aparte en tu panel.
- **Dónde está hoy:** [punto ciego 7](#pc7); [stack](05-ruta-stack-riesgos.md#stack-recomendado) (cobro).
- **Fuentes:**
  - <https://stripe.com/en-mx/pricing>
  - <https://support.stripe.com/questions/taxes-on-stripe-fees-for-mexico-based-businesses>

<a id="v19"></a>

#### V19. Comisión de Mercado Pago Link de pago · Correcto

- **Afirmación revisada:** Mercado Pago Link de pago cobra 3.49% + $4 con dinero al instante.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado en la página oficial, más IVA. Si esperas el dinero, baja: 3.19% a 7 días y 2.95% a 30 días (más $4 e IVA). Los meses sin intereses cuestan aparte.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (cobro).
- **Fuentes:**
  - <https://www.mercadopago.com.mx/herramientas-para-vender/link-de-pago>
  - <https://calcforlife.com/es/calculadora-mercado-pago-comisiones/>

<a id="v20"></a>

#### V20. Precio de ManyChat Pro · Correcto

- **Afirmación revisada:** ManyChat Pro aprox. US$29 al mes en pago anual o US$39 mensual (2,500 contactos activos; US$0.05 por contacto extra).
- **Estado:** Correcto.
- **Corrección o precisión:** Coincide con varias guías de 2026: ManyChat cambió sus planes el 2 de marzo de 2026 (Free, Essential, Pro y Business) y Pro incluye 2,500 contactos activos. El contacto extra cuesta cerca de US$0.05 en pago mensual y cerca de US$0.038 en anual. Las cuentas con plan anterior (legacy) pueden tener otras condiciones.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (conversaciones y bot).
- **Fuentes:**
  - <https://www.activepieces.com/blog/manychat-pricing-2026-plans-and-contact-tier-costs>
  - <https://www.eesel.ai/blog/manychat-pricing>

<a id="v21"></a>

#### V21. Planes de Pipedrive y reparto automático · Con matices

- **Afirmación revisada:** Pipedrive Growth o superior, con asignación round-robin en Premium.
- **Estado:** Con matices.
- **Corrección o precisión:** Los planes actuales son Lite, Growth, Premium y Ultimate (renombrados en 2025), con precio por asiento en pago anual cerca de US$14, US$39, US$49–59 y US$79 (las fuentes discrepan en Premium). La asignación automática estaba en Professional, que hoy equivale a Premium; pero el reparto por turnos asigna a un «equipo» y requiere la función Teams, que solo está en ciertos planes. Confírmalo en pipedrive.com/pricing antes de construir el Repartidor; si Premium no la trae, haz la rotación en n8n. Cada setter ocupa un asiento.
- **Cómo quedó en el diseño final:** Pipedrive Growth para ti y el asistente; los setters trabajan desde ManyChat Live Chat y solo reciben asiento si lo necesitan, y la cola con reasignación (Repartidor) vive en n8n. Premium, solo con más de 3 setters si quieres reparto nativo y confirmando que incluya la función de equipos.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (CRM y embudo); Repartidor ([pilar ventas](../pilares/ventas/CLAUDE.md)).
- **Fuentes:**
  - <https://support.pipedrive.com/en/article/automatic-assignment>
  - <https://www.activepieces.com/blog/pipedrive-pricing-plans-and-total-costs-for-2026>

<a id="v22"></a>

#### V22. Precio de n8n Cloud Starter · Correcto

- **Afirmación revisada:** n8n Cloud Starter aprox. €20 al mes en pago anual o €24 mensual, con 2,500 ejecuciones.
- **Estado:** Correcto.
- **Corrección o precisión:** Coincide con varias fuentes de 2026 (incluye 5 ejecuciones simultáneas); Pro cuesta cerca de €50 en pago anual o €60 mensual con 10,000 ejecuciones. Confirmar en n8n.io/pricing.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (eventos y relojes).
- **Fuentes:**
  - <https://www.jetadmin.io/blog/n8n-pricing/>
  - <https://dupple.com/learn/n8n-pricing>

<a id="v23"></a>

#### V23. Límites de la API de Notion · Correcto

- **Afirmación revisada:** La API de Notion tiene límites de alrededor de 3 solicitudes por segundo y 100 filas por consulta.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado en la documentación: promedio de 3 solicitudes por segundo por integración, con ráfagas permitidas y error 429 al pasarse; las consultas devuelven máximo 100 resultados por página. Notion advierte que puede cambiar los límites por plan. El historial de 30 días en Plus no se reverificó.
- **Dónde está hoy:** [Riesgos](05-ruta-stack-riesgos.md#riesgos) 8.
- **Fuentes:**
  - <https://developers.notion.com/reference/request-limits>
  - <https://developers.notion.com/reference/rate-limits>

<a id="v24"></a>

#### V24. Precio de Bitwarden Premium · Correcto

- **Afirmación revisada:** Bitwarden Premium cuesta US$19.80 al año (aprox. US$1.65 al mes).
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado: subió en enero de 2026 desde US$10 al año, con más funciones de seguridad. El acceso de emergencia es función de Premium.
- **Dónde está hoy:** [punto ciego 2](#pc2); [stack](05-ruta-stack-riesgos.md#stack-recomendado) (bóveda).
- **Fuentes:**
  - <https://alternativeto.net/news/2026/1/bitwarden-enhances-premium-and-families-plans-with-more-security-features-and-raises-prices>
  - <https://pricingsaas.com/companies/bitwarden/diffs/2026Q1>

<a id="v25"></a>

#### V25. Precio de Blotato Starter · Correcto

- **Afirmación revisada:** Blotato Starter aprox. US$29 al mes.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado en la página de precios de Blotato: Starter US$29 al mes con 20 cuentas conectadas y 1,250 créditos de IA; el siguiente plan (Creator) cuesta US$97.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (publicación).
- **Fuentes:**
  - <https://www.blotato.com/pricing.md>

<a id="v26"></a>

#### V26. GitHub Free: minutos de Actions y Secret Protection · Correcto

- **Afirmación revisada:** GitHub Free da 2,000 minutos de Actions en repos privados, un repo privado en Free no tiene escaneo de secretos y Secret Protection cuesta aprox. US$19 por committer activo.
- **Estado:** Correcto.
- **Corrección o precisión:** Los 2,000 minutos al mes de GitHub Free están en la documentación oficial; el precio de Secret Protection (US$19 por committer activo al mes) solo se confirmó en un agregador. Mantener gitleaks en cada PR es la opción sin costo.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (código).
- **Fuentes:**
  - <https://docs.github.com/en/get-started/learning-about-github/githubs-plans>
  - <https://toolradar.com/tools/github/pricing>

<a id="v27"></a>

#### V27. Vercel: plan Hobby y precio de Pro · Correcto

- **Afirmación revisada:** Vercel Pro aprox. US$20 por usuario al mes; el plan Hobby no permite uso comercial.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado: Hobby es solo para uso personal no comercial, y Vercel considera comercial incluso un despliegue hecho por un consultor pagado para un cliente; las entregas a clientes van en Pro o en la cuenta del cliente.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (hosting); [flujo 2](03-flujos-y-ritmo.md#flujo-2), paso 6.
- **Fuentes:**
  - <https://vercel.com/docs/plans/hobby>
  - <https://schematichq.com/blog/vercel-pricing>

<a id="v28"></a>

#### V28. Estudio de HBR sobre velocidad de respuesta · Correcto

- **Afirmación revisada:** En el estudio publicado en Harvard Business Review en 2011, las empresas que intentaron contactar en la primera hora tuvieron casi 7 veces más probabilidad de calificar al prospecto.
- **Estado:** Correcto.
- **Corrección o precisión:** Confirmado (Oldroyd, McElheran y Elkington, HBR 2011). No atribuirle las cifras de «21 veces» o «100 veces» en 5 minutos que circulan en internet: vienen de otro estudio de 2007.
- **Dónde está hoy:** [punto ciego 14](#pc14).
- **Fuentes:**
  - <https://scholarsarchive.byu.edu/facpub/9711>
  - <https://ainora.lt/blog/lead-response-time-statistics-every-study-2026>

<a id="v29"></a>

#### V29. App de WhatsApp Business: listas de difusión · Con matices

- **Afirmación revisada:** La alternativa «App WhatsApp Business» sirve solo 1 a 1, sin envíos masivos.
- **Estado:** Con matices.
- **Corrección o precisión:** La app sí tiene listas de difusión de hasta 256 contactos, pero solo llegan a quien guardó tu número, y en algunos países ofrece mensajes de marketing pagados. Lo que no tiene es automatización, varios agentes ni plantillas por API; para referidos en volumen y con medición, la API vía ManyChat sigue siendo la opción correcta.
- **Dónde está hoy:** [stack](05-ruta-stack-riesgos.md#stack-recomendado) (WhatsApp de ventas); [flujo 4](03-flujos-y-ritmo.md#flujo-4), paso 3.
- **Fuentes:**
  - <https://sendpulse.com/blog/whatsapp-broadcast-lists>
  - <https://www.wati.io/blog/whatsapp-broadcast-guide>

### Lo que sigue sin confirmar

Datos sueltos que las verificaciones y la arquitectura dejaron abiertos. Hasta que se confirmen, se tratan como aproximados. Los costos del stack que dicen «por confirmar» (por ejemplo, tus planes actuales de Zoom, Canva y Google Workspace, la facturación, la firma electrónica y el seguro) están en el [stack recomendado](05-ruta-stack-riesgos.md#stack-recomendado).

| Dato | Qué falta | Dónde o cuándo se confirma |
|---|---|---|
| Tope de corridas del plan Ultra de Claude | No se encontró ([V2](#v2)) | En la documentación de rutinas de Claude Code (code.claude.com/docs/en/routines) o en claude.com/pricing, si llegas a necesitar Ultra |
| Créditos mensuales de API incluidos en Max y Ultra | Solo según fuentes secundarias ([V15](#v15)) | En claude.com/pricing |
| Publicación en el DOF del paquete fiscal 2027 (tope de RESICO de 5 millones e IVA de 7%), y cómo y cuándo se elige la opción de 7% y cómo se combina con las retenciones de tus clientes empresa | No se encontró la publicación al 10 de noviembre; lo demás lo responde tu contadora ([V3](#v3)) | Con tu contadora, en la junta de régimen de la primera semana de diciembre |
| Tarifas de WhatsApp por mensaje en México (servicio y utilidad cerca de US$0.0085; marketing cerca de US$0.0397) | Vienen de tablas de proveedores; las tarifas oficiales de Meta no se leyeron directo ([V4](#v4)) | En tu cuenta de WhatsApp Business o con ManyChat |
| Duración de la ventana gratuita de los anuncios de clic a WhatsApp | 72 horas; algunos proveedores reportan hasta 7 días ([V4](#v4)) | En tu cuenta de WhatsApp Business o con ManyChat |
| 1,000 mensajes de servicio gratis al mes por número | No se encontró confirmación ([V4](#v4)) | Ya se quitó del cálculo |
| Acción nativa de ManyChat para mandar LeadSubmitted en anuncios de clic a WhatsApp | No se encontró soporte ([V6](#v6)) | El evento sale de n8n; compruébalo en el Administrador de eventos antes de optimizar |
| Costo de los meses sin intereses con tarjeta | Va aparte y no viene en las fuentes ([V18](#v18), [V19](#v19)) | En tu panel de Stripe o de Mercado Pago, antes de ofrecerlos |
| Condiciones de las cuentas de ManyChat con plan anterior (legacy) | Pueden ser distintas ([V20](#v20)) | En tu cuenta de ManyChat |
| Precio de Pipedrive Premium (las fuentes discrepan: US$49–59) y si trae la función de equipos para el reparto por turnos | Por confirmar ([V21](#v21)) | En pipedrive.com/pricing, antes de pasar a Premium; mientras, la cola vive en n8n |
| Historial de 30 días de Notion Plus | No se reverificó ([V23](#v23)) | Al contratar el plan |
| Precio de GitHub Secret Protection (cerca de US$19 por committer activo al mes) | Solo se confirmó en un agregador ([V26](#v26)) | Si sumas desarrolladores (GitHub Team); mientras, gitleaks en cada PR |
| Límites del plan gratuito de Healthchecks.io | Por confirmar | Antes de sumarlo a Centinela (con 5 flujos críticos) |
| Qué redes cubre la analítica de Blotato | Por confirmar | Antes de encender Brújula (febrero de 2027) |
| Si ManyChat permite exportar historiales de conversación | Por confirmar: su API no está pensada para eso | Antes de encender Lupa como agente (con 4 o más setters) |
| Cómo se cuentan los 20 días para responder solicitudes ARCO | Por confirmar | Con el abogado |
| Tarifa vigente del IMPI por clase (aprox. $2,800 MXN en línea con IVA; cerca de $3,130 en ventanilla) | Confirmar la tarifa vigente | Antes de presentar la solicitud (diciembre) |
| Requisitos para registrarte como agente capacitador ante la STPS (constancias DC-3) | Por confirmar | Con tu contadora o abogado, solo si vendes capacitación |

