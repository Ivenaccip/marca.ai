"""Diagramas SVG del mapa del sistema marca.ai (mapa general, ciclo del cliente y orquestación).

Los datos salen de final.json; los textos de presentación, de x_final.json (parámetro T).
Ningún texto se recorta: las cajas crecen hasta que cabe todo. Si algo no cabe, se anota en WARN.
"""
import json, sys, math, re, html as _h, unicodedata

WARN = []

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
    'manual_con_plantilla': ('manual', 'A mano con plantilla (aún no es agente)'),
}
def auton_key(a):
    a = (a or '').lower()
    if 'manual' in a or 'plantilla' in a: return 'manual_con_plantilla'
    if 'borr' in a or 'aprob' in a: return 'borrador_con_aprobacion'
    if 'asist' in a: return 'asistido'
    if 'auto' in a: return 'automatico'
    return 'asistido'

def agent_state(name, T):
    """Estado (no autonomía): 'rule' = regla de n8n sin IA; 'on' = encendido hasta marzo; 'later' = se enciende después."""
    if name in (T or {}).get('reglas_n8n', []): return 'rule'
    if name in (T or {}).get('encendidos', []): return 'on'
    return 'later'

# ---------------- medición aproximada de texto ----------------
# em por carácter, medidos con las fuentes reales y redondeados hacia arriba
EM = {'mono': 0.6, 'sans': 0.49, 'display': 0.55}
def tw(s, size, kind='sans'):
    return len(str(s)) * size * EM[kind]

def wrap_px(s, max_px, size, kind='sans'):
    max_chars = max(4, int(max_px / (size * EM[kind])))
    words, lines, cur = str(s).split(), [], ''
    for w in words:
        if not cur: cur = w
        elif len(cur) + 1 + len(w) <= max_chars: cur += ' ' + w
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    for l in lines:
        if len(l) > max_chars:
            WARN.append(f'palabra que no cabe en {max_px:.0f}px: {l}')
    return lines or ['']

def svg_lines(x, y, lines, cls, lh=16, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ''
    if len(lines) == 1:
        return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{a}>{esc(lines[0])}</text>'
    t = ''.join(f'<tspan x="{x:.1f}" dy="{0 if i == 0 else lh}">{esc(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}"{a}>{t}</text>'

def svg_text(x, y, s, cls, size=12.5, kind='sans', max_px=None, lh=16, anchor=None):
    lines = wrap_px(s, max_px, size, kind) if max_px else [str(s)]
    return svg_lines(x, y, lines, cls, lh, anchor), len(lines)

# ---------------- glifos ----------------
def glyph(cx, cy, key, r=5.5, extra=''):
    k = AUTON[key][0]
    if k == 'auto':
        return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" class="g-fill{extra}"/>'
    if k == 'draft':
        return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" class="g-ring{extra}"/>'
                f'<path d="M{cx:.1f} {cy - r:.1f} A{r} {r} 0 0 1 {cx:.1f} {cy + r:.1f} Z" class="g-fill{extra}"/>')
    if k == 'manual':
        return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" class="g-ring g-dash{extra}"/>'
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" class="g-ring{extra}"/>'

def rule_glyph(cx, cy, s=10):
    return f'<rect x="{cx - s / 2:.1f}" y="{cy - s / 2:.1f}" width="{s}" height="{s}" rx="1.5" class="g-rule"/>'

def led(cx, cy, r=3.4):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" class="led"/>'

def badge(x, y, label, kind='new', h=18, size=10):
    """kind: new (bermellón), human (tinta), agent (contorno)."""
    w = max(44, len(label) * size * 0.6 + 16)
    cls = {'new': ('badge-new', 't-badge'), 'human': ('badge-human', 't-badge-h'), 'agent': ('badge-agent', 't-badge-a')}[kind]
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="{h / 2}" class="{cls[0]}"/>'
            f'<text x="{x + w / 2:.1f}" y="{y + h / 2 + size * 0.36:.1f}" class="{cls[1]}" text-anchor="middle">{esc(label)}</text>'), w

# ---------------- chips ----------------
MINI_NEW_W = 38
def chip_width(c, size=12, pad=11):
    w = tw(c['label'], size, 'mono') + 2 * pad
    if c.get('rule'): w += 16
    if c.get('nuevo'): w += MINI_NEW_W + 4
    return w

def chips_layout(items, x0, x1, y0, ch=26, gap=8, size=12, pad=11):
    """items: dicts {label, rule, nuevo, dashed, title}. Devuelve [(x, y, w, item)] y el alto total."""
    out, x, y = [], x0, y0
    for c in items:
        w = chip_width(c, size, pad)
        if x + w > x1 and x > x0:
            x = x0; y += ch + gap
        if x + w > x1 + 0.5:
            WARN.append(f'chip más ancho que su caja: {c["label"]}')
        out.append((x, y, w, c)); x += w + gap
    return out, (y - y0) + ch

def chip_svg(x, y, w, c, ch=26, size=12, pad=11, rect_cls='chip', text_cls='t-chip', rx=None):
    rx = ch / 2 if rx is None else rx
    o = []
    if c.get('title'):
        o.append(f'<g><title>{esc(c["title"])}</title>')
    cls = rect_cls + (' chip-dash' if c.get('dashed') else '')
    o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{ch}" rx="{rx}" class="{cls}"/>')
    tx = x + pad
    if c.get('rule'):
        o.append(rule_glyph(tx + 5, y + ch / 2, 9))
        tx += 16
    tcls = text_cls + (' t-later' if c.get('dashed') else '')
    o.append(f'<text x="{tx:.1f}" y="{y + ch / 2 + size * 0.36:.1f}" class="{tcls}">{esc(c["label"])}</text>')
    if c.get('nuevo'):
        bx = x + w - pad + 4 - MINI_NEW_W
        o.append(f'<rect x="{bx:.1f}" y="{y + ch / 2 - 7:.1f}" width="{MINI_NEW_W}" height="14" rx="7" class="badge-new"/>')
        o.append(f'<text x="{bx + MINI_NEW_W / 2:.1f}" y="{y + ch / 2 + 3.2:.1f}" class="t-badge-mini" text-anchor="middle">NUEVO</text>')
    if c.get('title'):
        o.append('</g>')
    return ''.join(o)

def rect_exit(cx, cy, hw, hh, ux, uy):
    tx = hw / abs(ux) if abs(ux) > 1e-6 else 1e9
    ty = hh / abs(uy) if abs(uy) > 1e-6 else 1e9
    t = min(tx, ty)
    return cx + ux * t, cy + uy * t

DEFS = ('<defs>'
        '<marker id="{p}arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" class="arrowhead"/></marker>'
        '<marker id="{p}arr-s" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0 L0 5 L10 10 Z" class="arrowhead"/></marker>'
        '<marker id="{p}arr-hot" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" class="arrowhead-hot"/></marker>'
        '</defs>')

# ---------------- MAPA GENERAL ----------------
def chat_of(p):
    m = re.search(r'«([^»]+)»', p.get('chat', '') or '')
    return m.group(1) if m else ''

def svg_map(F, pillars, layer_pillars, people_all, T):
    T = T or {}
    fase1 = set(T.get('chats_fase1', []))
    nuevos = set(T.get('nuevos_chips', []))
    W = 1280; M = 32
    o = []
    y1 = 28
    # ---------- fila 1: Tú · Jefe de gabinete · Equipo humano ----------
    tu_x, tu_w = M, 252
    gab_x, gab_w = tu_x + tu_w + 150, 340
    team_x = gab_x + gab_w + 28
    team_w = W - M - team_x
    # Tú
    tu_sub = wrap_px(T['ceo_sub'], tu_w - 40, 12.5)
    tu_items = []
    for it in T['ceo_lines']:
        ls = wrap_px(it, tu_w - 52, 12.5)
        tu_items.append(ls)
    n_tu = len(tu_sub) + sum(len(l) for l in tu_items)
    tu_h = 34 + 22 + (n_tu - 1) * 16 + 4 * (len(tu_items)) + 18
    # Gabinete
    gab_sub = wrap_px(T['gab_sub'], gab_w - 40, 12.5)
    gab_h = 58 + (len(gab_sub) - 1) * 16 + 24 + 16
    # Equipo humano (orden fijo; los condicionales van en «+N»)
    fixed = T['equipo']
    cond = [p for p in people_all if not any(p.split(' (')[0] == f.split(' (')[0] for f in fixed)]
    team_items = [{'label': f, 'nuevo': f in nuevos} for f in fixed]
    if cond:
        team_items.append({'label': f'+{len(cond)} si aplica', 'dashed': True,
                           'title': 'Si aplica: ' + ', '.join(cond)})
    tcl, tch = chips_layout(team_items, team_x + 20, team_x + team_w - 16, y1 + 46, ch=24, gap=6, size=11, pad=9)
    team_h = 46 + tch + 18
    h1 = max(tu_h, gab_h, team_h)
    # cajas
    o.append('<g class="node">')
    o.append(f'<rect x="{tu_x}" y="{y1}" width="{tu_w}" height="{h1}" rx="14" class="box-ceo"/>')
    o.append(svg_lines(tu_x + 20, y1 + 34, ['Tú'], 't-title t-on-ceo'))
    yy = y1 + 56
    o.append(svg_lines(tu_x + 20, yy, tu_sub, 't-sub t-on-ceo', 16)); yy += len(tu_sub) * 16 + 4
    for ls in tu_items:
        o.append(f'<circle cx="{tu_x + 24}" cy="{yy - 4:.1f}" r="2" class="dot-on-ceo"/>')
        o.append(svg_lines(tu_x + 32, yy, ls, 't-sub t-on-ceo t-strong', 16)); yy += len(ls) * 16 + 4
    o.append('</g>')
    o.append('<g class="node">')
    o.append(f'<rect x="{gab_x}" y="{y1}" width="{gab_w}" height="{h1}" rx="14" class="box"/>')
    o.append(led(gab_x + 25, y1 + 28, 4.6))
    o.append(svg_lines(gab_x + 36, y1 + 34, ['Jefe de gabinete'], 't-title t-on'))
    b, bw_ = badge(gab_x + gab_w - 78, y1 + 18, 'NUEVO', 'new', 20)
    o.append(b)
    o.append(svg_lines(gab_x + 20, y1 + 58, gab_sub, 't-sub', 16))
    o.append(svg_lines(gab_x + 20, y1 + 58 + len(gab_sub) * 16 + 8, [T['gab_pilar']], 't-owner'))
    o.append('</g>')
    o.append('<g class="node">')
    o.append(f'<rect x="{team_x}" y="{y1}" width="{team_w}" height="{h1}" rx="14" class="box box-dashed"/>')
    o.append(svg_lines(team_x + 20, y1 + 30, ['Equipo humano'], 't-title-s'))
    for (x, y, w, c) in tcl:
        o.append(chip_svg(x, y, w, c, ch=24, size=11, pad=9, text_cls='t-chip-s'))
    o.append('</g>')
    # flechas Gabinete → Tú y Tú → Gabinete (dos flechas, cada una con su etiqueta)
    ax0, ax1 = tu_x + tu_w + 6, gab_x - 6
    ya, yb = y1 + h1 / 2 - 14, y1 + h1 / 2 + 14
    o.append(f'<line x1="{ax1}" y1="{ya:.1f}" x2="{ax0}" y2="{ya:.1f}" class="edge" marker-end="url(#m-arr)"/>')
    o.append(svg_lines((ax0 + ax1) / 2, ya - 8, [T['edge_gab_ceo']], 't-edge', anchor='middle'))
    o.append(f'<line x1="{ax0}" y1="{yb:.1f}" x2="{ax1}" y2="{yb:.1f}" class="edge" marker-end="url(#m-arr)"/>')
    o.append(svg_lines((ax0 + ax1) / 2, yb + 18, [T['edge_ceo_gab']], 't-edge', anchor='middle'))

    # ---------- columnas de pilares ----------
    N = len(pillars)
    gx = 12
    cw = (W - 2 * M - gx * (N - 1)) / N
    bus_y = y1 + h1 + 20
    band_y = bus_y + 30
    band_h = 58
    top = band_y + band_h + 16
    owners = T.get('duenos_mapa', {})
    def name_lines(p): return wrap_px(p['nombre'], cw - 26, 15, 'display')
    def owner_lines(p): return wrap_px('dueño: ' + owners.get(p['id'], ''), cw - 24, 11.5)
    max_nl = max(len(name_lines(p)) for p in pillars)
    max_ol = max(len(owner_lines(p)) for p in pillars)
    head = 22 + max_nl * 19 + 8 + max_ol * 14
    max_ag = max(len(p['agentes']) for p in pillars)
    ag_px = cw - 32 - 12
    for p in pillars:
        for a in p['agentes']:
            extra = 10 if agent_state(a['nombre'], T) == 'on' else 0
            if tw(a['nombre'], 12, 'mono') + extra > ag_px:
                WARN.append(f'nombre de agente largo: {a["nombre"]}')
    ch = head + 12 + max_ag * 24
    jcx = gab_x + gab_w / 2
    xs = [M + i * (cw + gx) + cw / 2 for i in range(N)]
    groups = []
    for i, p in enumerate(pillars):
        c = chat_of(p) or p['nombre']
        if groups and groups[-1]['chat'] == c:
            groups[-1]['idx'].append(i)
        else:
            groups.append({'chat': c, 'idx': [i], 'cluster': CLUSTER[p['_slot']]})
    gcs = []
    for g in groups:
        g['x0'] = M + g['idx'][0] * (cw + gx)
        g['x1'] = M + g['idx'][-1] * (cw + gx) + cw
        gcs.append((g['x0'] + g['x1']) / 2)
    o.append(f'<line x1="{jcx}" y1="{y1 + h1}" x2="{jcx}" y2="{bus_y}" class="edge"/>')
    o.append(f'<line x1="{min(gcs[0], jcx):.1f}" y1="{bus_y}" x2="{max(gcs[-1], jcx):.1f}" y2="{bus_y}" class="edge"/>')
    o.append(svg_lines(jcx + 10, bus_y - 8, [T.get('bus_label', '')], 't-edge'))
    for gcx in gcs:
        o.append(f'<line x1="{gcx:.1f}" y1="{bus_y}" x2="{gcx:.1f}" y2="{band_y - 4}" class="edge" marker-end="url(#m-arr)"/>')
    opening = T.get('chat_apertura', {})
    for g in groups:
        gw = g['x1'] - g['x0']
        o.append('<g class="node">')
        o.append(f'<rect x="{g["x0"]:.1f}" y="{band_y}" width="{gw:.1f}" height="{band_h}" rx="10" class="box chat-band"/>')
        o.append(svg_lines(g['x0'] + 12, band_y + 16, [g['cluster'].upper()], 't-cluster'))
        name = 'Chat «' + g['chat'] + '»'
        if tw(name, 13.5, 'display') > gw - 24:
            WARN.append(f'nombre de chat largo: {name}')
        o.append(svg_lines(g['x0'] + 12, band_y + 34, [name], 't-chat'))
        cond_txt = opening.get(g['chat'], '')
        if cond_txt:
            if tw(cond_txt, 11.5) > gw - 24:
                WARN.append(f'condición de apertura larga: {cond_txt}')
            o.append(svg_lines(g['x0'] + 12, band_y + 50, [cond_txt], 't-cond'))
        if g['chat'] in fase1:
            b, _ = badge(g['x1'] - 62, band_y + 6, 'FASE 1', 'human', 16)
            o.append(b)
        o.append('</g>')
    for i, p in enumerate(pillars):
        x = M + i * (cw + gx)
        o.append(f'<a href="#p-{esc(p["_anchor"])}" class="card-link"><title>Ver la ficha de {esc(p["nombre"])}</title><g class="node">')
        o.append(f'<rect x="{x:.1f}" y="{top}" width="{cw:.1f}" height="{ch:.1f}" rx="12" class="box card"/>')
        o.append(f'<path d="M{x:.1f} {top + 12} A12 12 0 0 1 {x + 12:.1f} {top} H{x + cw - 12:.1f} A12 12 0 0 1 {x + cw:.1f} {top + 12} V{top + 7} H{x:.1f} Z" class="pc-{p["_slot"]}"/>')
        o.append(svg_lines(x + 13, top + 32, name_lines(p), 't-pillar', 19))
        yy = top + 32 + (max_nl - 1) * 19 + 20
        o.append(svg_lines(x + 13, yy, owner_lines(p), 't-owner', 14))
        if p.get('nuevo'):
            b, _ = badge(x + cw - 60, top - 9, 'NUEVO', 'new', 18)
            o.append(b)
        ya = top + head + 18
        for a in p['agentes']:
            st = agent_state(a['nombre'], T)
            k = auton_key(a.get('autonomia'))
            if st == 'rule':
                o.append(rule_glyph(x + 19, ya - 4))
            else:
                o.append(glyph(x + 19, ya - 4, k, extra=' g-later' if st == 'later' else ''))
            cls = {'on': 't-agent t-on', 'later': 't-agent t-later', 'rule': 't-agent'}[st]
            o.append(svg_lines(x + 32, ya, [a['nombre']], cls))
            if st == 'on':
                o.append(led(x + 32 + tw(a['nombre'], 12, 'mono') + 8, ya - 4))
            ya += 24
        o.append('</g></a>')
    bottom = top + ch

    # ---------- Cerebro ----------
    by = bottom + 46
    lw = 336  # ancho de la columna de texto de las cajas anchas
    brain_sub = wrap_px(T['brain_sub'], lw - 44, 12.5)
    base_items = [{'label': b['nombre'], 'nuevo': b['nombre'] in nuevos} for b in F['cerebro_notion']['bases']]
    cl, chh = chips_layout(base_items, M + lw, W - M - 18, 0, ch=26, gap=8)
    bh = max(36 + 22 + (len(brain_sub) - 1) * 16 + 20, chh + 36)
    for i, x in enumerate(xs):
        o.append(f'<line x1="{x:.1f}" y1="{bottom + 4}" x2="{x:.1f}" y2="{by - 4}" class="edge" marker-end="url(#m-arr)" marker-start="url(#m-arr-s)"/>')
    if N > 1:
        o.append(svg_lines((xs[0] + xs[1]) / 2, bottom + 28, ['lee y escribe'], 't-edge', anchor='middle'))
    o.append('<g class="node">')
    o.append(f'<rect x="{M}" y="{by}" width="{W - 2 * M}" height="{bh}" rx="16" class="box box-brain"/>')
    o.append(svg_lines(M + 22, by + 36, ['Cerebro'], 't-title'))
    o.append(svg_lines(M + 22, by + 58, brain_sub, 't-sub', 16))
    for (x, y, w, c) in cl:
        o.append(chip_svg(x, by + 18 + y, w, c, rect_cls='chip chip-brain'))
    o.append('</g>')

    # ---------- Tuberías = pilar Automatizaciones ----------
    ty = by + bh + 46
    lp = layer_pillars[0] if layer_pillars else None
    rename = T.get('rename', {})
    comps = []
    rules = T.get('reglas_n8n', [])
    for c in F['capa_automatizacion']:
        lab = rename.get(c['nombre'], c['nombre'])
        comps.append({'label': lab, 'nuevo': lab in nuevos,
                      'rule': any(re.match(re.escape(r) + r'\b', lab) for r in rules)})
    if lp:
        labels = T.get('chip_labels', {})
        for a in lp['agentes']:
            an = a['nombre']
            if an.lower() == 'gabinete': continue
            if any(re.search(r'\b' + re.escape(an.lower()) + r'\b', c['label'].lower()) for c in comps): continue
            comps.append({'label': labels.get(an, an), 'dashed': auton_key(a.get('autonomia')) == 'manual_con_plantilla',
                          'rule': an in rules})
    cl, chh = chips_layout(comps, M + lw, W - M - 18, 0, ch=26, gap=8)
    p_pilar = wrap_px(T['pipes_pilar'], lw - 44, 15, 'display')
    p_chat = wrap_px(T['pipes_chat'], lw - 44, 13.5, 'display')
    p_owner = wrap_px('dueño: ' + owners.get(lp['id'] if lp else '', ''), lw - 44, 11.5)
    p_sub = wrap_px(T['pipes_sub'], lw - 44, 12.5)
    left_h = 36 + 24 + len(p_pilar) * 19 + len(p_chat) * 18 + len(p_owner) * 14 + 8 + len(p_sub) * 16 + 10
    th = max(left_h, chh + 36)
    mid = W / 2
    o.append(f'<line x1="{mid}" y1="{by + bh + 4}" x2="{mid}" y2="{ty - 4}" class="edge" marker-end="url(#m-arr)" marker-start="url(#m-arr-s)"/>')
    o.append(svg_lines(mid + 12, by + bh + 28, [T.get('pipes_edge', '')], 't-edge'))
    anchor = lp['_anchor'] if lp else 'automatizaciones'
    o.append(f'<a href="#p-{esc(anchor)}" class="card-link"><title>Ver la ficha del pilar {esc(lp["nombre"] if lp else "")}</title><g class="node">')
    o.append(f'<clipPath id="m-clip-pipes"><rect x="{M}" y="{ty}" width="{W - 2 * M}" height="{th}" rx="16"/></clipPath>')
    o.append(f'<rect x="{M}" y="{ty}" width="{W - 2 * M}" height="{th}" rx="16" class="box box-pipes card"/>')
    o.append(f'<rect x="{M}" y="{ty}" width="{W - 2 * M}" height="7" class="pc-auto" clip-path="url(#m-clip-pipes)"/>')
    o.append(svg_lines(M + 22, ty + 38, ['Tuberías'], 't-title'))
    if T.get('pipes_fase1'):
        b, _ = badge(M + 22 + 104, ty + 23, 'FASE 1', 'human', 16)
        o.append(b)
    yy = ty + 62
    o.append(svg_lines(M + 22, yy, p_pilar, 't-pillar', 19)); yy += len(p_pilar) * 19
    o.append(svg_lines(M + 22, yy, p_chat, 't-chat', 18)); yy += len(p_chat) * 18 - 2
    o.append(svg_lines(M + 22, yy, p_owner, 't-owner', 14)); yy += len(p_owner) * 14 + 8
    o.append(svg_lines(M + 22, yy, p_sub, 't-sub', 16))
    for (x, y, w, c) in cl:
        o.append(chip_svg(x, ty + 18 + y, w, c))
    o.append('</g></a>')

    # ---------- Herramientas ----------
    hy = ty + th + 46
    tools = [{'label': t, 'nuevo': t in nuevos} for t in T['tools']]
    cl, chh = chips_layout(tools, M + lw, W - M - 18, 0, ch=26, gap=8)
    hh = max(70, chh + 30)
    o.append(f'<line x1="{mid}" y1="{ty + th + 4}" x2="{mid}" y2="{hy - 4}" class="edge" marker-end="url(#m-arr)" marker-start="url(#m-arr-s)"/>')
    o.append(svg_lines(mid + 12, ty + th + 28, ['APIs · conectores MCP'], 't-edge'))
    o.append('<g class="node free">')
    o.append(svg_lines(M + 22, hy + 30, ['Herramientas'], 't-title-s'))
    o.append(svg_lines(M + 22, hy + 50, ['lo que tocan clientes y equipo'], 't-sub'))
    for (x, y, w, c) in cl:
        o.append(chip_svg(x, hy + 12 + y, w, c, rect_cls='chip chip-tool', rx=6))
    o.append('</g>')
    H = hy + hh + 20
    aria = T.get('aria_map', '')
    return f'<svg viewBox="0 0 {W} {H:.0f}" role="img" aria-label="{esc(aria)}" class="diagram">{DEFS.replace("{p}", "m-")}{"".join(o)}</svg>'

# ---------------- CICLO DEL CLIENTE ----------------
def svg_cycle(steps, kpis, T=None):
    T = T or {}
    W = 1280
    n = len(steps)
    bw = 210
    t_px, d_px = bw - 60, bw - 30
    tl = [wrap_px(s['titulo'], t_px, 14.5, 'display') for s in steps]
    dl = [wrap_px(s['detalle'], d_px, 12.5) for s in steps]
    bh = 22 + (max(len(x) for x in tl) - 1) * 18 + 8 + max(len(x) for x in dl) * 15 + 12
    rx, ry = 512, 322
    cx = 640
    cy = ry + bh / 2 + 24
    H = int(cy + ry + bh / 2 + 24)
    o, pos = [], []
    for i in range(n):
        th = -math.pi / 2 + 2 * math.pi * i / n
        pos.append((cx + rx * math.cos(th), cy + ry * math.sin(th)))
    segs = []
    for i in range(n):
        (x1, y1), (x2, y2) = pos[i], pos[(i + 1) % n]
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        sx, sy = rect_exit(x1, y1, bw / 2 + 6, bh / 2 + 6, ux, uy)
        ex, ey = rect_exit(x2, y2, bw / 2 + 8, bh / 2 + 8, -ux, -uy)
        segs.append((sx, sy, ex, ey))
        hot = i == n - 1
        o.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" class="edge{" edge-strong" if hot else ""}" marker-end="url(#c-arr{"-hot" if hot else ""})"/>')
    def seg_clear(bx, by, bwid, bhh):
        # distancia mínima entre la etiqueta (rectángulo) y cualquier flecha
        best = 1e9
        for (sx, sy, ex, ey) in segs:
            for k in range(41):
                px, py = sx + (ex - sx) * k / 40, sy + (ey - sy) * k / 40
                dx = max(bx - px, 0, px - (bx + bwid)); dy = max(by - py, 0, py - (by + bhh))
                best = min(best, math.hypot(dx, dy))
        return best
    for i, s in enumerate(steps):
        x, y = pos[i]
        X, Y = x - bw / 2, y - bh / 2
        o.append('<g class="node">')
        o.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{bw}" height="{bh:.1f}" rx="12" class="box"/>')
        if s.get('slot2'):
            o.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="7" height="{bh / 2:.1f}" rx="3" class="pc-{s["slot"]}"/>')
            o.append(f'<rect x="{X:.1f}" y="{Y + bh / 2:.1f}" width="7" height="{bh / 2:.1f}" rx="3" class="pc-{s["slot2"]}"/>')
        else:
            o.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="7" height="{bh:.1f}" rx="3" class="pc-{s["slot"]}"/>')
        o.append(svg_lines(X + 18, Y + 22, [f'{i + 1:02d}'], 't-step-n'))
        o.append(svg_lines(X + 44, Y + 22, tl[i], 't-step', 18))
        o.append(svg_lines(X + 18, Y + 22 + (len(tl[i]) - 1) * 18 + 20, dl[i], 't-sub', 15))
        if s.get('humano'):
            kind = 'agent' if s['humano'] == 'AGENTE' else 'human'
            bwid = max(44, len(s['humano']) * 6 + 16)
            cands = [(X + bw - bwid - 6, Y - 10), (X + 14, Y - 10), (X + bw - bwid - 6, Y + bh - 10), (X + 14, Y + bh - 10)]
            pick = next((c for c in cands if seg_clear(c[0], c[1], bwid, 20) >= 12), None)
            if pick is None:
                pick = max(cands, key=lambda c: seg_clear(c[0], c[1], bwid, 20))
                WARN.append(f'etiqueta {s["humano"]} del paso {i + 1} cerca de una flecha')
            b, _ = badge(pick[0], pick[1], s['humano'], kind, 20)
            o.append(b)
        o.append('</g>')
    o.append(svg_lines(cx, cy - 52, [T.get('cycle_center1', 'Cada cliente entregado')], 't-center', anchor='middle'))
    o.append(svg_lines(cx, cy - 22, [T.get('cycle_center2', 'alimenta al siguiente')], 't-center', anchor='middle'))
    o.append(svg_lines(cx, cy + 10, ['lo que se mide en cada vuelta:'], 't-sub', anchor='middle'))
    for j, k in enumerate(kpis[:3]):
        w = tw(k, 12, 'mono') + 24
        o.append(f'<rect x="{cx - w / 2:.1f}" y="{cy + 24 + j * 34:.1f}" width="{w:.1f}" height="26" rx="13" class="chip"/>')
        o.append(f'<text x="{cx:.1f}" y="{cy + 24 + j * 34 + 17:.1f}" class="t-chip" text-anchor="middle">{esc(k)}</text>')
    aria = T.get('aria_cycle', '')
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(aria)}" class="diagram">{DEFS.replace("{p}", "c-")}{"".join(o)}</svg>'

# ---------------- ORQUESTACIÓN ----------------
def svg_orq(Q, aria=''):
    """Fila 1: n8n · eventos → Tareas → Chat → Aprobaciones → Tú → Se ejecuta (con un arco «o lo despierta por API»).
    Fila 2: Gabinete · 7:10 debajo de Tareas: prioriza la cola y te manda el mensaje de las 7:10."""
    W = 1280; M = 32
    nodes = Q['fila']; edges = Q['flechas']
    n = len(nodes); gap = 62
    bw = (W - 2 * M - gap * (n - 1)) / n
    tl = [wrap_px(nd['t'], bw - 26, 16, 'display') for nd in nodes]
    sl = [wrap_px(nd['s'], bw - 26, 12.5) for nd in nodes]
    bh1 = 26 + (max(len(x) for x in tl) - 1) * 19 + 8 + max(len(x) for x in sl) * 15 + 12
    y_arc = 34
    y1 = y_arc + 30
    o = []
    xs = [M + i * (bw + gap) for i in range(n)]
    for i, nd in enumerate(nodes):
        x = xs[i]
        inv = ' t-on-ceo' if 'box-ceo' in nd.get('cls', '') else ''
        o.append('<g class="node">')
        o.append(f'<rect x="{x:.1f}" y="{y1}" width="{bw:.1f}" height="{bh1:.1f}" rx="12" class="box {nd.get("cls", "")}"/>')
        o.append(svg_lines(x + 13, y1 + 26, tl[i], 't-title-s' + inv, 19))
        o.append(svg_lines(x + 13, y1 + 26 + (len(tl[i]) - 1) * 19 + 22, sl[i], 't-sub' + inv, 15))
        o.append('</g>')
        if i < n - 1:
            x2 = x + bw + gap
            yl = y1 + bh1 / 2
            o.append(f'<line x1="{x + bw + 3:.1f}" y1="{yl:.1f}" x2="{x2 - 3:.1f}" y2="{yl:.1f}" class="edge" marker-end="url(#o-arr)"/>')
            el = wrap_px(edges[i], gap - 6, 11.5, 'mono')
            o.append(svg_lines(x + bw + gap / 2, yl - 9 - (len(el) - 1) * 14, el, 't-edge', 14, anchor='middle'))
    # arco: n8n → Chat (despierta por API)
    a0 = xs[0] + bw / 2; a2 = xs[2] + bw / 2
    o.append(f'<path d="M{a0:.1f} {y1 - 3} V{y_arc} H{a2:.1f} V{y1 - 5}" class="edge edge-dash" marker-end="url(#o-arr)"/>')
    o.append(svg_lines((a0 + a2) / 2, y_arc - 8, [Q['arco']], 't-edge', anchor='middle'))
    if tw(Q['arco'], 11.5, 'mono') > (a2 - a0) - 10:
        WARN.append('etiqueta del arco más ancha que el arco')
    # fila 2: Gabinete bajo Tareas
    G = Q['gabinete']
    gw = 270
    gx_ = xs[1] + bw / 2 - gw / 2
    gtl = wrap_px(G['t'], gw - 42, 16, 'display')
    gsl = wrap_px(G['s'], gw - 26, 12.5)
    gh = 26 + (len(gtl) - 1) * 19 + 8 + len(gsl) * 15 + 12
    y2 = y1 + bh1 + 74
    o.append('<g class="node">')
    o.append(f'<rect x="{gx_:.1f}" y="{y2}" width="{gw}" height="{gh:.1f}" rx="12" class="box"/>')
    o.append(led(gx_ + 18, y2 + 20, 4.2))
    o.append(svg_lines(gx_ + 29, y2 + 26, gtl, 't-title-s t-on', 19))
    o.append(svg_lines(gx_ + 13, y2 + 26 + (len(gtl) - 1) * 19 + 22, gsl, 't-sub', 15))
    o.append('</g>')
    cxT = xs[1] + bw / 2
    o.append(f'<line x1="{cxT:.1f}" y1="{y2 - 3}" x2="{cxT:.1f}" y2="{y1 + bh1 + 5:.1f}" class="edge" marker-end="url(#o-arr)"/>')
    o.append(svg_lines(cxT + 10, y1 + bh1 + 41, [Q['gab_sube']], 't-edge'))
    cxU = xs[4] + bw / 2
    ym = y2 + gh / 2
    o.append(f'<path d="M{gx_ + gw + 3:.1f} {ym:.1f} H{cxU:.1f} V{y1 + bh1 + 5:.1f}" class="edge" marker-end="url(#o-arr)"/>')
    o.append(svg_lines((gx_ + gw + cxU) / 2, ym - 8, [Q['gab_msg']], 't-edge', anchor='middle'))
    H = y2 + gh + 26
    return f'<svg viewBox="0 0 {W} {H:.0f}" role="img" aria-label="{esc(aria)}" class="diagram">{DEFS.replace("{p}", "o-")}{"".join(o)}</svg>'
