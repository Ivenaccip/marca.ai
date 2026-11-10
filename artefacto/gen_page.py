"""Genera el artefacto (una página HTML) del mapa del sistema marca.ai a partir de final.json."""
import json, sys, math, re, html as _h, unicodedata

def esc(s):
    return _h.escape(str(s if s is not None else ''), quote=True)

def slug(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-') or 'x'

# ---------------- colores por pilar ----------------
SLOTS = ['marca', 'marketing', 'ventas', 'producto', 'clientes', 'admin', 'legal', 'auto', 'extra']
def color_slot(p):
    t = (p.get('id', '') + ' ' + p.get('nombre', '')).lower()
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    rules = [('automat', 'auto'), ('legal', 'legal'), ('riesgo', 'legal'), ('admin', 'admin'), ('finanz', 'admin'),
             ('client', 'clientes'), ('post', 'clientes'), ('exito', 'clientes'), ('producto', 'producto'), ('entrega', 'producto'),
             ('venta', 'ventas'), ('comercial', 'ventas'), ('marca', 'marca'), ('contenido', 'marca'), ('marketing', 'marketing'),
             ('crecim', 'marketing'), ('cerebro', 'auto'), ('notion', 'auto')]
    for k, v in rules:
        if k in t:
            return v
    return 'extra'

CLUSTER = {'marca': 'Atraer', 'marketing': 'Atraer', 'ventas': 'Convertir', 'producto': 'Entregar', 'clientes': 'Entregar',
           'admin': 'Sostener', 'legal': 'Sostener', 'extra': 'Sostener', 'auto': 'Sostener'}
CLUSTER_ORDER = ['Atraer', 'Convertir', 'Entregar', 'Sostener']
SLOT_ORDER = {s: i for i, s in enumerate(['marca', 'marketing', 'ventas', 'producto', 'clientes', 'admin', 'legal', 'extra', 'auto'])}

def is_layer_pillar(p):
    t = (p.get('id', '') + ' ' + p.get('nombre', '')).lower()
    return 'automat' in t or 'cerebro' in t or 'notion' in t or 'orquest' in t

AUTON = {
    'automatico': ('auto', 'Automático'),
    'borrador_con_aprobacion': ('draft', 'Borrador + tu aprobación'),
    'asistido': ('assist', 'Asistido (lo opera una persona)'),
}
def auton_key(a):
    a = (a or '').lower()
    if 'borr' in a or 'aprob' in a: return 'borrador_con_aprobacion'
    if 'asist' in a: return 'asistido'
    if 'auto' in a: return 'automatico'
    return 'asistido'

# ---------------- utilidades SVG ----------------
def wrap(s, max_chars):
    words, lines, cur = str(s).split(), [], ''
    for w in words:
        if not cur: cur = w
        elif len(cur) + 1 + len(w) <= max_chars: cur += ' ' + w
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines or ['']

def svg_text(x, y, s, cls, lh=None, max_chars=None, anchor=None, max_lines=None):
    lines = wrap(s, max_chars) if max_chars else [str(s)]
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]; lines[-1] = lines[-1].rstrip('.,;:') + '…'
    a = f' text-anchor="{anchor}"' if anchor else ''
    if len(lines) == 1:
        return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{a}>{esc(lines[0])}</text>', 1
    lh = lh or 16
    t = ''.join(f'<tspan x="{x:.1f}" dy="{0 if i == 0 else lh}">{esc(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{a}>{t}</text>', len(lines)

def glyph(cx, cy, key, r=5.5):
    k = AUTON[key][0]
    if k == 'auto':
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-fill"/>'
    if k == 'draft':
        return (f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-ring"/>'
                f'<path d="M{cx} {cy - r} A{r} {r} 0 0 1 {cx} {cy + r} Z" class="g-fill"/>')
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" class="g-ring"/>'

def chips_layout(items, x0, x1, y0, ch=26, gap=8, cw=7.2, pad=11):
    """Distribuye chips (texto mono) en filas; devuelve [(x,y,w,txt)], alto total."""
    out, x, y = [], x0, y0
    for t in items:
        w = len(t) * cw + 2 * pad
        if x + w > x1 and x > x0:
            x = x0; y += ch + gap
        out.append((x, y, w, t)); x += w + gap
    return out, (y - y0) + ch

def rect_exit(cx, cy, hw, hh, ux, uy):
    tx = hw / abs(ux) if abs(ux) > 1e-6 else 1e9
    ty = hh / abs(uy) if abs(uy) > 1e-6 else 1e9
    t = min(tx, ty)
    return cx + ux * t, cy + uy * t

# ---------------- MAPA GENERAL ----------------
def svg_map(F, pillars, layer_pillars, people):
    W = 1280; M = 32
    o = []
    # Fila 1: Tú · Jefe de gabinete · Equipo humano
    y1, h1 = 28, 88
    o.append(f'<rect x="{M}" y="{y1}" width="250" height="{h1}" rx="14" class="box-ceo"/>')
    o.append(svg_text(M + 20, y1 + 36, 'Tú', 't-title t-on-ceo')[0])
    o.append(svg_text(M + 20, y1 + 58, 'CEO y cara de la marca: grabas, decides y apruebas', 't-sub t-on-ceo', lh=16, max_chars=34)[0])
    jx, jw = 362, 390
    o.append(f'<rect x="{jx}" y="{y1}" width="{jw}" height="{h1}" rx="14" class="box"/>')
    o.append(svg_text(jx + 20, y1 + 36, 'Jefe de gabinete', 't-title')[0])
    o.append(f'<rect x="{jx + jw - 78}" y="{y1 + 18}" width="60" height="20" rx="10" class="badge-new"/>')
    o.append(svg_text(jx + jw - 48, y1 + 32, 'NUEVO', 't-badge', anchor='middle')[0])
    o.append(svg_text(jx + 20, y1 + 58, 'Agente que lee el cerebro y arma tu plan del día, la revisión semanal y las alertas', 't-sub', lh=16, max_chars=52)[0])
    # flecha Tú <-> Jefe
    o.append(f'<line x1="{M + 254}" y1="{y1 + 44}" x2="{jx - 4}" y2="{y1 + 44}" class="edge" marker-end="url(#arr)" marker-start="url(#arr-s)"/>')
    o.append(svg_text((M + 250 + jx) / 2, y1 + 34, 'prioridades', 't-edge', anchor='middle')[0])
    o.append(svg_text((M + 250 + jx) / 2, y1 + 64, 'aprobaciones', 't-edge', anchor='middle')[0])
    # Equipo humano
    ex = 832; ew = W - M - ex
    o.append(f'<rect x="{ex}" y="{y1}" width="{ew}" height="{h1}" rx="14" class="box box-dashed"/>')
    o.append(svg_text(ex + 20, y1 + 30, 'Equipo humano', 't-title-s')[0])
    cl, _ = chips_layout(people[:7], ex + 20, ex + ew - 16, y1 + 44, ch=24, gap=6, cw=6.6, pad=9)
    for (x, y, w, t) in cl:
        if y + 24 > y1 + h1 - 4: break
        o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="24" rx="12" class="chip"/>')
        o.append(f'<text x="{x + w / 2:.1f}" y="{y + 16:.1f}" class="t-chip-s" text-anchor="middle">{esc(t)}</text>')

    # Columnas de pilares
    N = len(pillars)
    gx = 12
    cw = (W - 2 * M - gx * (N - 1)) / N
    top = 196
    name_chars = max(10, int((cw - 26) / (15 * 0.6)))
    ag_chars = max(10, int((cw - 44) / 7.2))
    # alto de tarjeta: nombre (1-2 líneas) + dueño + agentes
    def card_rows(p):
        nl = len(wrap(p['nombre'], name_chars))
        rows = sum(min(2, len(wrap(a['nombre'], ag_chars))) for a in p['agentes'][:6])
        return nl, rows
    owner_chars = max(12, int((cw - 22) / 6.3))
    max_nl = max(card_rows(p)[0] for p in pillars)
    max_rows = max(card_rows(p)[1] for p in pillars)
    max_ol = max(min(2, len(wrap('dueño: ' + (p.get('dueno_humano') or ''), owner_chars))) for p in pillars)
    head = 22 + max_nl * 19 + 8 + max_ol * 14
    ch = head + 14 + max_rows * 17 + len(max(pillars, key=lambda p: len(p['agentes']))['agentes'][:6]) * 7 + 18
    # bus
    jcx = jx + jw / 2
    xs = [M + i * (cw + gx) + cw / 2 for i in range(N)]
    o.append(f'<line x1="{jcx}" y1="{y1 + h1}" x2="{jcx}" y2="{150}" class="edge"/>')
    o.append(f'<line x1="{xs[0]:.1f}" y1="150" x2="{xs[-1]:.1f}" y2="150" class="edge"/>')
    o.append(svg_text(jcx + 10, 140, 'plan del día · tareas por pilar', 't-edge')[0])
    for x in xs:
        o.append(f'<line x1="{x:.1f}" y1="150" x2="{x:.1f}" y2="{top - 4}" class="edge" marker-end="url(#arr)"/>')
    # etiquetas de cadena de valor (sobre la primera columna de cada grupo)
    seen = set()
    for i, p in enumerate(pillars):
        c = CLUSTER[p['_slot']]
        if c in seen: continue
        seen.add(c)
        o.append(svg_text(M + i * (cw + gx), top - 12, c.upper(), 't-cluster')[0])
    for i, p in enumerate(pillars):
        x = M + i * (cw + gx)
        o.append(f'<a href="#p-{esc(p["_anchor"])}" class="card-link"><title>Ver detalle de {esc(p["nombre"])}</title>')
        o.append(f'<rect x="{x:.1f}" y="{top}" width="{cw:.1f}" height="{ch:.1f}" rx="12" class="box card"/>')
        o.append(f'<path d="M{x:.1f} {top + 12} A12 12 0 0 1 {x + 12:.1f} {top} H{x + cw - 12:.1f} A12 12 0 0 1 {x + cw:.1f} {top + 12} V{top + 7} H{x:.1f} Z" class="pc-{p["_slot"]}"/>')
        t, nl = svg_text(x + 13, top + 32, p['nombre'], 't-pillar', lh=19, max_chars=name_chars, max_lines=2)
        o.append(t)
        yy = top + 32 + (nl - 1) * 19 + 20
        owner = p.get('dueno_humano') or ''
        if owner:
            o.append(svg_text(x + 13, yy, 'dueño: ' + owner, 't-owner', lh=14, max_chars=owner_chars, max_lines=2)[0])
        if p.get('nuevo'):
            o.append(f'<rect x="{x + cw - 60:.1f}" y="{top - 9}" width="50" height="18" rx="9" class="badge-new"/>')
            o.append(svg_text(x + cw - 35, top + 4, 'NUEVO', 't-badge', anchor='middle')[0])
        ya = top + head + 16
        for a in p['agentes'][:6]:
            k = auton_key(a.get('autonomia'))
            o.append(glyph(x + 19, ya - 4, k))
            t, n = svg_text(x + 32, ya, a['nombre'], 't-agent', lh=15, max_chars=ag_chars, max_lines=2)
            o.append(t)
            ya += n * 17 + 7
        o.append('</a>')
    bottom = top + ch
    # Cerebro (Notion)
    by = bottom + 46
    bases = [b['nombre'] for b in F['cerebro_notion']['bases']]
    cl, chh = chips_layout(bases, M + 270, W - M - 18, 0, ch=26, gap=8)
    bh = max(96, chh + 36)
    for i, x in enumerate(xs):
        o.append(f'<line x1="{x:.1f}" y1="{bottom + 4}" x2="{x:.1f}" y2="{by - 4}" class="edge" marker-end="url(#arr)" marker-start="url(#arr-s)"/>')
    if N > 1:
        o.append(svg_text((xs[0] + xs[1]) / 2, bottom + 28, 'lee y escribe', 't-edge', anchor='middle')[0])
    o.append(f'<rect x="{M}" y="{by}" width="{W - 2 * M}" height="{bh}" rx="16" class="box box-brain"/>')
    o.append(svg_text(M + 22, by + 36, 'Cerebro', 't-title')[0])
    o.append(svg_text(M + 22, by + 58, 'Notion: la única fuente de verdad. Los chats se pasan el trabajo por aquí, no por memoria.', 't-sub', lh=16, max_chars=36, max_lines=3)[0])
    for (x, y, w, t) in cl:
        o.append(f'<rect x="{x:.1f}" y="{by + 18 + y:.1f}" width="{w:.1f}" height="26" rx="13" class="chip chip-brain"/>')
        o.append(f'<text x="{x + w / 2:.1f}" y="{by + 18 + y + 17:.1f}" class="t-chip" text-anchor="middle">{esc(t)}</text>')
    # Tuberías
    ty = by + bh + 46
    comps = [c['nombre'] for c in F['capa_automatizacion']]
    for lp in layer_pillars:
        for a in lp['agentes'][:4]:
            if a['nombre'] not in comps: comps.append(a['nombre'])
    cl, chh = chips_layout(comps, M + 270, W - M - 18, 0, ch=26, gap=8)
    th = max(86, chh + 36)
    mid = W / 2
    o.append(f'<line x1="{mid}" y1="{by + bh + 4}" x2="{mid}" y2="{ty - 4}" class="edge" marker-end="url(#arr)" marker-start="url(#arr-s)"/>')
    o.append(svg_text(mid + 12, by + bh + 28, 'eventos · webhooks · tareas programadas', 't-edge')[0])
    o.append(f'<rect x="{M}" y="{ty}" width="{W - 2 * M}" height="{th}" rx="16" class="box box-pipes"/>')
    o.append(svg_text(M + 22, ty + 36, 'Tuberías', 't-title')[0])
    o.append(svg_text(M + 22, ty + 58, 'Automatización + sesiones en la nube con Remote Control', 't-sub', lh=16, max_chars=36, max_lines=2)[0])
    for (x, y, w, t) in cl:
        o.append(f'<rect x="{x:.1f}" y="{ty + 18 + y:.1f}" width="{w:.1f}" height="26" rx="13" class="chip"/>')
        o.append(f'<text x="{x + w / 2:.1f}" y="{ty + 18 + y + 17:.1f}" class="t-chip" text-anchor="middle">{esc(t)}</text>')
    # Herramientas
    hy = ty + th + 46
    tools = []
    for s in F['stack_recomendado']:
        t = re.split(r'[(/,+]| o ', s['herramienta'])[0].strip()
        if t and t not in tools and len(t) <= 26: tools.append(t)
    tools = tools[:16]
    cl, chh = chips_layout(tools, M + 270, W - M - 18, 0, ch=26, gap=8)
    hh = max(70, chh + 30)
    o.append(f'<line x1="{mid}" y1="{ty + th + 4}" x2="{mid}" y2="{hy - 4}" class="edge" marker-end="url(#arr)" marker-start="url(#arr-s)"/>')
    o.append(svg_text(mid + 12, ty + th + 28, 'APIs · conectores MCP', 't-edge')[0])
    o.append(svg_text(M + 22, hy + 30, 'Herramientas', 't-title-s')[0])
    o.append(svg_text(M + 22, hy + 50, 'lo que tocan clientes y equipo', 't-sub')[0])
    for (x, y, w, t) in cl:
        o.append(f'<rect x="{x:.1f}" y="{hy + 12 + y:.1f}" width="{w:.1f}" height="26" rx="6" class="chip chip-tool"/>')
        o.append(f'<text x="{x + w / 2:.1f}" y="{hy + 12 + y + 17:.1f}" class="t-chip" text-anchor="middle">{esc(t)}</text>')
    H = hy + hh + 20
    defs = ('<defs>'
            '<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" class="arrowhead"/></marker>'
            '<marker id="arr-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 Z" class="arrowhead"/></marker>'
            '</defs>')
    aria = ('Mapa del sistema por capas: tú y el jefe de gabinete arriba; debajo, un chat por pilar con sus agentes; '
            'todos leen y escriben en el cerebro de Notion; debajo, las tuberías de automatización y las herramientas.')
    return f'<svg viewBox="0 0 {W} {H:.0f}" role="img" aria-label="{esc(aria)}" class="diagram">{defs}{"".join(o)}</svg>'

# ---------------- CICLO DEL CLIENTE ----------------
def svg_cycle(steps, kpis):
    W, H = 1280, 850
    cx, cy, rx, ry = 640, 425, 516, 312
    n = len(steps)
    bw, bh = 184, 78
    o, pos = [], []
    for i in range(n):
        th = -math.pi / 2 + 2 * math.pi * i / n
        pos.append((cx + rx * math.cos(th), cy + ry * math.sin(th)))
    for i in range(n):
        (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % n]
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        sx, sy = rect_exit(x1, y1, bw / 2 + 6, bh / 2 + 6, ux, uy)
        ex, ey = rect_exit(x2, y2, bw / 2 + 8, bh / 2 + 8, -ux, -uy)
        cls = 'edge edge-strong' if i == n - 1 else 'edge'
        o.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" class="{cls}" marker-end="url(#arr2)"/>')
    for i, s in enumerate(steps):
        x, y = pos[i]
        X, Y = x - bw / 2, y - bh / 2
        o.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{bw}" height="{bh}" rx="12" class="box"/>')
        o.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="7" height="{bh}" rx="3" class="pc-{s["slot"]}"/>')
        o.append(svg_text(X + 18, Y + 22, f'{i + 1:02d}', 't-step-n')[0])
        o.append(svg_text(X + 44, Y + 22, s['titulo'], 't-step', max_chars=17, max_lines=1)[0])
        o.append(svg_text(X + 18, Y + 42, s['detalle'], 't-sub', lh=15, max_chars=26, max_lines=2)[0])
        if s.get('humano'):
            o.append(f'<rect x="{X + bw - 64:.1f}" y="{Y - 10:.1f}" width="58" height="20" rx="10" class="badge-human"/>')
            o.append(svg_text(X + bw - 35, Y + 4, s['humano'], 't-badge-h', anchor='middle')[0])
    o.append(svg_text(cx, cy - 48, 'Cada cliente entregado', 't-center', anchor='middle')[0])
    o.append(svg_text(cx, cy - 18, 'alimenta al siguiente', 't-center', anchor='middle')[0])
    o.append(svg_text(cx, cy + 14, 'lo que se mide en cada vuelta:', 't-sub', anchor='middle')[0])
    for j, k in enumerate(kpis[:3]):
        w = len(k) * 7.2 + 24
        o.append(f'<rect x="{cx - w / 2:.1f}" y="{cy + 28 + j * 34:.1f}" width="{w:.1f}" height="26" rx="13" class="chip"/>')
        o.append(f'<text x="{cx:.1f}" y="{cy + 28 + j * 34 + 17:.1f}" class="t-chip" text-anchor="middle">{esc(k)}</text>')
    defs = ('<defs><marker id="arr2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0 0 L10 5 L0 10 Z" class="arrowhead"/></marker></defs>')
    aria = 'Ciclo del cliente en ' + str(n) + ' pasos, de la pieza de contenido al referido que vuelve a empezar el ciclo.'
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(aria)}" class="diagram">{defs}{"".join(o)}</svg>'

# ---------------- ORQUESTACIÓN ----------------
def svg_orq(nodes, edges):
    W = 1280; n = len(nodes); gap = 54
    bw = (W - 64 - gap * (n - 1)) / n; bh = 92; y = 30
    o = []
    for i, (t, sub, cls) in enumerate(nodes):
        x = 32 + i * (bw + gap)
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="{bh}" rx="12" class="box {cls}"/>')
        inv = ' t-on-ceo' if 'box-ceo' in cls else ''
        o.append(svg_text(x + 14, y + 28, t, 't-title-s' + inv, max_chars=int((bw - 20) / 8.6), max_lines=1)[0])
        o.append(svg_text(x + 14, y + 50, sub, 't-sub' + inv, lh=15, max_chars=int((bw - 20) / 6.5), max_lines=3)[0])
        if i < n - 1:
            x2 = x + bw + gap
            o.append(f'<line x1="{x + bw + 3:.1f}" y1="{y + bh / 2}" x2="{x2 - 3:.1f}" y2="{y + bh / 2}" class="edge" marker-end="url(#arr3)"/>')
            o.append(svg_text(x + bw + gap / 2, y + bh / 2 - 9, edges[i], 't-edge', anchor='middle')[0])
    defs = ('<defs><marker id="arr3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0 0 L10 5 L0 10 Z" class="arrowhead"/></marker></defs>')
    aria = 'Cómo se pasa el trabajo entre agentes: todo pasa por Notion y nada sale sin tu aprobación.'
    return f'<svg viewBox="0 0 {W} {y + bh + 30}" role="img" aria-label="{esc(aria)}" class="diagram">{defs}{"".join(o)}</svg>'
