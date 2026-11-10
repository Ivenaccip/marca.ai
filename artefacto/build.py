"""Arma el HTML completo del artefacto. Uso: python3 build.py final.json extra.json salida.html"""
import json, sys, re
from gen_page import *

CSS = r"""
:root{
  /* Plano de un sistema operativo: papel frío y tinta pizarra; la señal bermellón marca SOLO lo que te falta.
     Layout: capas de arriba abajo (dirección → pilares → cerebro → tuberías → herramientas), luego el detalle. */
  --bg:#F3F4F6; --surface:#FFFFFF; --surface-2:#F8F9FB; --ink:#141C28; --muted:#566174; --line:#D5DAE2; --line-strong:#A7B1BF;
  --signal:#C2410C; --on-signal:#FFFFFF; --ceo:#141C28; --on-ceo:#F3F4F6;
  --ok:#2B8A3E; --warn:#B35C00; --crit:#C92A2A;
  --c-marca:#6741D9; --c-marketing:#C2255C; --c-ventas:#2B8A3E; --c-producto:#1971C2; --c-clientes:#0B7285;
  --c-admin:#B35C00; --c-legal:#5C677D; --c-auto:#343A40; --c-extra:#7950F2;
  --font-display:"Schibsted Grotesk","Helvetica Neue",Arial,sans-serif;
  --font-body:"IBM Plex Sans","Segoe UI",Roboto,Arial,sans-serif;
  --font-mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0D1219; --surface:#141B25; --surface-2:#18212D; --ink:#E6EAF0; --muted:#9BA6B6; --line:#263041; --line-strong:#3B475A;
    --signal:#FF8656; --on-signal:#1C0D06; --ceo:#E6EAF0; --on-ceo:#0D1219;
    --ok:#4ADE80; --warn:#FBBF24; --crit:#FF7B7B;
    --c-marca:#A78BFA; --c-marketing:#F472B6; --c-ventas:#4ADE80; --c-producto:#60A5FA; --c-clientes:#22D3EE;
    --c-admin:#FBBF24; --c-legal:#AAB4C3; --c-auto:#CBD5E1; --c-extra:#C4B5FD;
    color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#0D1219; --surface:#141B25; --surface-2:#18212D; --ink:#E6EAF0; --muted:#9BA6B6; --line:#263041; --line-strong:#3B475A;
  --signal:#FF8656; --on-signal:#1C0D06; --ceo:#E6EAF0; --on-ceo:#0D1219;
  --ok:#4ADE80; --warn:#FBBF24; --crit:#FF7B7B;
  --c-marca:#A78BFA; --c-marketing:#F472B6; --c-ventas:#4ADE80; --c-producto:#60A5FA; --c-clientes:#22D3EE;
  --c-admin:#FBBF24; --c-legal:#AAB4C3; --c-auto:#CBD5E1; --c-extra:#C4B5FD;
  color-scheme:dark;
}
*{box-sizing:border-box}
html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font-body);font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit}
:focus-visible{outline:2.5px solid var(--signal);outline-offset:2px;border-radius:6px}
.wrap{max-width:1340px;margin:0 auto;padding:0 20px}
.top{padding:44px 0 20px}
.eyebrow{font-family:var(--font-mono);font-size:12.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin:0}
h1{font-family:var(--font-display);font-weight:800;font-size:clamp(32px,4.4vw,54px);line-height:1.04;letter-spacing:-.02em;margin:10px 0 14px;text-wrap:balance;max-width:22ch}
.lede{font-size:18px;max-width:66ch;margin:0}
.legend{display:flex;flex-wrap:wrap;gap:8px 20px;margin:18px 0 0;padding:0;list-style:none;font-size:14px;color:var(--muted);align-items:center}
.legend li{display:flex;align-items:center;gap:8px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:24px 0 0;max-width:900px}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 14px}
.stat b{display:block;font-family:var(--font-display);font-size:26px;line-height:1.1;font-variant-numeric:tabular-nums}
.stat span{font-size:13px;color:var(--muted)}
.toc{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
.toc ul{display:flex;gap:2px;overflow-x:auto;list-style:none;margin:0 auto;padding:8px 20px;max-width:1340px}
.toc a{display:inline-block;padding:6px 10px;border-radius:8px;text-decoration:none;font-size:14px;white-space:nowrap;color:var(--muted)}
.toc a:hover{background:var(--surface);color:var(--ink)}
section{padding:40px 0 6px;scroll-margin-top:52px}
h2{font-family:var(--font-display);font-weight:800;font-size:clamp(24px,3vw,34px);letter-spacing:-.01em;line-height:1.1;margin:0 0 8px;text-wrap:balance}
h3{font-family:var(--font-display);text-wrap:balance}
.sec-lede{max-width:72ch;color:var(--muted);margin:0 0 18px}
figure{margin:0}
.fig{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:10px;overflow-x:auto}
figcaption{font-size:14px;color:var(--muted);margin:10px 4px 0;max-width:86ch}
.grid{display:grid;gap:14px}
.pillars{grid-template-columns:repeat(auto-fill,minmax(min(100%,380px),1fr))}
.card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px}
.card h3{font-size:21px;margin:0;display:flex;gap:10px;align-items:center;flex-wrap:wrap;line-height:1.2}
.swatch{width:12px;height:12px;border-radius:3px;flex:none}
.tag-new{font-family:var(--font-mono);font-size:11px;font-weight:600;letter-spacing:.06em;background:var(--signal);color:var(--on-signal);border-radius:999px;padding:2px 9px}
.tag{font-family:var(--font-mono);font-size:11.5px;border:1px solid var(--line-strong);border-radius:999px;padding:1px 9px;color:var(--muted);white-space:nowrap}
.mission{margin:8px 0 4px}
.owner{font-size:14px;color:var(--muted);margin:0 0 12px}
.agents{list-style:none;margin:0 0 14px;padding:0;display:grid;gap:10px}
.agents li{display:grid;grid-template-columns:18px 1fr;gap:4px 8px;padding-top:10px;border-top:1px solid var(--line)}
.agents .nm{font-family:var(--font-mono);font-weight:500;font-size:14px}
.agents .au{font-size:12.5px;color:var(--muted)}
.agents .ms{grid-column:2;font-size:14.5px}
.agents .io{grid-column:2;font-size:13px;color:var(--muted)}
.g{width:12px;height:12px;margin-top:4px}
.g circle,.g path{stroke:var(--ink)}
.kv{display:grid;grid-template-columns:110px 1fr;gap:6px 10px;font-size:14px;margin:0}
.kv dt{color:var(--muted)}
.kv dd{margin:0;display:flex;flex-wrap:wrap;gap:5px}
.kvlist{margin:0;padding-left:18px;font-size:13.5px;line-height:1.45}
.kvlist li{margin:0 0 4px}
.chip{font-family:var(--font-mono);font-size:12px;background:var(--surface-2);border:1px solid var(--line);border-radius:999px;padding:1px 9px;white-space:nowrap}
.brain{grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr))}
.brain .card h3{font-size:17px}
.brain p{margin:6px 0 10px;font-size:14.5px}
.feeds{font-size:13px;color:var(--muted);margin:8px 0 0}
.cols2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:14px;margin-top:14px}
ol.rules{margin:0;padding-left:22px;display:grid;gap:8px;max-width:80ch}
.meter{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:0 0 14px}
.cells{display:flex;gap:4px}
.cells i{width:16px;height:16px;border-radius:4px;background:var(--signal)}
.cells i.k{background:var(--line-strong)}
.filters{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px}
.filters button{font:inherit;font-size:14px;color:var(--ink);background:var(--surface);border:1px solid var(--line-strong);border-radius:999px;padding:5px 12px;cursor:pointer;min-height:36px}
.filters button[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.gaps{grid-template-columns:repeat(auto-fill,minmax(min(100%,360px),1fr))}
.gap-card{display:flex;flex-direction:column;gap:8px}
.gap-card[hidden]{display:none}
.gap-head{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.prio{font-family:var(--font-mono);font-size:11.5px;font-weight:600;border-radius:6px;padding:1px 8px}
.prio-P0{background:var(--signal);color:var(--on-signal)}
.prio-P1{border:1.5px solid var(--signal);color:var(--signal)}
.prio-P2{border:1px solid var(--line-strong);color:var(--muted)}
.gap-card h3{font-size:18px;margin:0;line-height:1.25}
.gap-card p{margin:0;font-size:14.5px}
.why{color:var(--muted)}
.first{background:var(--surface-2);border:1px dashed var(--line-strong);border-radius:10px;padding:8px 10px;font-size:14px}
.first b{font-family:var(--font-mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);display:block}
.ei{font-size:12.5px;color:var(--muted);font-family:var(--font-mono)}
.timeline{display:flex;height:12px;border-radius:999px;overflow:hidden;margin:4px 0 14px;border:1px solid var(--line)}
.timeline span{display:block;height:100%}
.phases{grid-template-columns:repeat(auto-fit,minmax(min(100%,270px),1fr))}
.phase .n{font-family:var(--font-mono);font-size:12px;color:var(--muted);letter-spacing:.06em;text-transform:uppercase}
.phase h3{font-size:19px;margin:2px 0 2px}
.phase .dur{font-size:13.5px;color:var(--muted);margin:0 0 8px}
.phase ul{margin:0 0 10px;padding-left:18px;font-size:14.5px;display:grid;gap:4px}
.phase .ok{font-size:13.5px;border-top:1px solid var(--line);padding-top:8px;margin:0}
.rhythm{grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr))}
.rhythm h3{font-size:16px;margin:0 0 8px;font-family:var(--font-mono);font-weight:500;letter-spacing:.06em;text-transform:uppercase}
.rhythm ul{list-style:none;margin:0;padding:0;display:grid;gap:10px;font-size:14.5px}
.rhythm li small{display:block;color:var(--muted);font-size:12.5px}
.tbl{overflow-x:auto;background:var(--surface);border:1px solid var(--line);border-radius:14px}
table{border-collapse:collapse;width:100%;font-size:14.5px;min-width:640px}
th,td{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:var(--font-mono);font-size:12px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:500}
tr:last-child td{border-bottom:0}
td.cost{font-variant-numeric:tabular-nums;white-space:nowrap}
.qs{margin:0;padding-left:22px;display:grid;gap:8px;font-size:16px;max-width:80ch}
.src{list-style:none;margin:0;padding:0;display:grid;gap:10px;font-size:14px}
.src li{display:grid;grid-template-columns:110px 1fr;gap:4px 12px;padding:10px 0;border-top:1px solid var(--line)}
.st{font-family:var(--font-mono);font-size:11.5px;font-weight:600;letter-spacing:.04em;text-transform:uppercase}
.st-correcta{color:var(--ok)} .st-matizar{color:var(--warn)} .st-incorrecta{color:var(--crit)} .st-no_verificable{color:var(--muted)}
.src .fix{color:var(--muted);grid-column:2}
.src a{word-break:break-all;color:var(--muted)}
.note{font-size:14px;color:var(--muted);border-left:3px solid var(--line-strong);padding:2px 0 2px 12px;max-width:80ch}
footer{padding:40px 0 56px;color:var(--muted);font-size:13.5px}
.diagram{display:block;width:100%;height:auto;min-width:1060px;color:var(--ink);font-family:var(--font-body)}
.diagram text{fill:currentColor}
.diagram .box{fill:var(--surface);stroke:var(--line-strong);stroke-width:1.2}
.diagram .box-dashed{stroke-dasharray:5 4}
.diagram .box-ceo{fill:var(--ceo);stroke:var(--ceo)}
.diagram .t-on-ceo{fill:var(--on-ceo)}
.diagram .box-brain{fill:var(--surface-2);stroke:var(--ink);stroke-width:1.8}
.diagram .box-pipes{fill:var(--surface-2)}
.diagram .chip{fill:var(--surface);stroke:var(--line-strong);stroke-width:1}
.diagram .chip-tool{fill:none;stroke-dasharray:3 3}
.diagram .edge{stroke:var(--muted);stroke-width:1.6;fill:none}
.diagram .edge-strong{stroke:var(--signal);stroke-width:2.2}
.diagram .arrowhead{fill:var(--muted)}
.diagram .t-title{font-family:var(--font-display);font-weight:700;font-size:19px}
.diagram .t-title-s{font-family:var(--font-display);font-weight:700;font-size:16px}
.diagram .t-sub{font-size:12.5px;fill:var(--muted)}
.diagram .t-sub.t-on-ceo{fill:var(--on-ceo);opacity:.82}
.diagram .t-pillar{font-family:var(--font-display);font-weight:700;font-size:15px}
.diagram .t-owner{font-size:11.5px;fill:var(--muted)}
.diagram .t-agent{font-family:var(--font-mono);font-size:12px}
.diagram .t-chip{font-family:var(--font-mono);font-size:12px}
.diagram .t-chip-s{font-family:var(--font-mono);font-size:11px}
.diagram .t-edge{font-family:var(--font-mono);font-size:11.5px;fill:var(--muted)}
.diagram .t-cluster{font-family:var(--font-mono);font-size:11px;letter-spacing:.08em;fill:var(--muted);font-weight:500}
.diagram .badge-new{fill:var(--signal)}
.diagram .t-badge{font-family:var(--font-mono);font-size:10px;font-weight:600;fill:var(--on-signal);letter-spacing:.06em}
.diagram .badge-human{fill:var(--ink)}
.diagram .t-badge-h{font-family:var(--font-mono);font-size:10px;font-weight:600;fill:var(--bg);letter-spacing:.04em}
.diagram .g-fill{fill:var(--ink)}
.diagram .g-ring{fill:none;stroke:var(--ink);stroke-width:1.4}
.diagram .g-dash{stroke:var(--muted);stroke-dasharray:2.2 2}
.diagram .t-agent-m{fill:var(--muted)}
.diagram .chat-band{fill:var(--surface-2)}
.diagram .t-chat{font-family:var(--font-display);font-weight:700;font-size:13.5px}
.diagram .t-step-n{font-family:var(--font-mono);font-size:12px;fill:var(--muted)}
.diagram .t-step{font-family:var(--font-display);font-weight:700;font-size:14.5px}
.diagram .t-center{font-family:var(--font-display);font-weight:800;font-size:24px}
.diagram a.card-link{cursor:pointer}
.diagram a.card-link:hover .card{stroke:var(--ink);stroke-width:2}
.diagram a.card-link:focus{outline:none}
.diagram a.card-link:focus-visible .card{stroke:var(--signal);stroke-width:2.5}
""" + ''.join(f".pc-{s}{{fill:var(--c-{s})}} .bg-{s}{{background:var(--c-{s})}}\n" for s in SLOTS) + r"""
@media (prefers-reduced-motion: no-preference){ html{scroll-behavior:smooth} }
@media (max-width:560px){ .kv{grid-template-columns:1fr} .src li{grid-template-columns:1fr} .lede{font-size:16.5px} }
"""

def glyph_html(key):
    k = AUTON[key][0]
    if k == 'auto':
        inner = '<circle cx="6" cy="6" r="5" fill="currentColor"/>'
    elif k == 'draft':
        inner = '<circle cx="6" cy="6" r="5" fill="none" stroke-width="1.4"/><path d="M6 1 A5 5 0 0 1 6 11 Z" fill="currentColor"/>'
    elif k == 'manual':
        inner = '<circle cx="6" cy="6" r="5" fill="none" stroke-width="1.4" stroke-dasharray="2.2 2" opacity=".75"/>'
    else:
        inner = '<circle cx="6" cy="6" r="5" fill="none" stroke-width="1.4"/>'
    return f'<svg class="g" viewBox="0 0 12 12" aria-hidden="true">{inner}</svg>'

def chips(items):
    return ''.join(f'<span class="chip">{esc(i)}</span>' for i in items if i)

def weeks(d):
    nums = [float(x) for x in re.findall(r'\d+(?:\.\d+)?', d or '')]
    if not nums: return 4
    v = max(nums)
    dl = (d or '').lower()
    if 'mes' in dl: v *= 4.3
    elif 'día' in dl or 'dia' in dl: v /= 7
    return max(1, v)

def short_role(h):
    """Nombre corto de un rol humano para los chips del mapa ('' si no es del equipo)."""
    s = h.split(':')[0]
    s = re.sub(r'\s*\(.*?\)', '', s).strip()
    s = re.sub(r'\s*\(.*$', '', s).strip()
    if len(s) > 30:
        s = re.split(r',| y | que | para ', s)[0].strip()
    low = s.lower()
    if low in ('tú', 'tu', 'tú (ceo)') or low.startswith('tú ') or 'cliente' in low or 'aliado' in low or 'anfitri' in low:
        return ''
    return s[:1].upper() + s[1:]

def build(F, X):
    allp = F['pillars_sorted']
    cols = [p for p in allp if not p['_layer']]
    layer = [p for p in allp if p['_layer']]
    people = []
    for p in allp:
        for h in p.get('personas', []):
            hn = short_role(h)
            if hn and hn not in people:
                people.append(hn)
    n_agents = sum(len(p['agentes']) for p in allp)
    gaps = F['puntos_ciegos']
    n_unknown = sum(1 for g in gaps if g.get('dominio') == 'desconocido')
    p0 = sum(1 for g in gaps if g.get('prioridad') == 'P0')
    H = []
    H.append('<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">')
    H.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    H.append(f'<title>{esc(X["title"])}</title>')
    H.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    H.append('<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&family=Schibsted+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">')
    H.append(f'<style>{CSS}</style></head><body>')
    # ---- cabecera
    H.append('<header class="wrap top">')
    H.append(f'<p class="eyebrow">{esc(X["eyebrow"])}</p>')
    H.append(f'<h1>{esc(X["h1"])}</h1>')
    H.append(f'<p class="lede">{esc(F["vision"])}</p>')
    H.append('<ul class="legend">'
             '<li><span class="tag-new">NUEVO</span> lo que no habías contemplado</li>'
             f'<li>{glyph_html("automatico")} automático</li>'
             f'<li>{glyph_html("borrador_con_aprobacion")} borrador que tú apruebas</li>'
             f'<li>{glyph_html("asistido")} asistido: lo opera una persona</li>'
             f'<li>{glyph_html("manual_con_plantilla")} a mano con plantilla: todavía no es agente</li></ul>')
    H.append('<div class="stats">'
             f'<div class="stat"><b>{len(allp)}</b><span>pilares: áreas con dueño</span></div>'
             f'<div class="stat"><b>{esc(X.get("n_chats", ""))}</b><span>{esc(X.get("n_chats_label", "chats"))}</span></div>'
             f'<div class="stat"><b>{esc(X.get("n_activos", n_agents))}</b><span>agentes encendidos hasta marzo, de {n_agents} diseñados</span></div>'
             f'<div class="stat"><b>{len(F["cerebro_notion"]["bases"])}</b><span>bases en Notion</span></div>'
             f'<div class="stat"><b>{len(gaps)}</b><span>puntos ciegos · {p0} urgentes</span></div>'
             '</div></header>')
    nav = [('mapa', 'Mapa'), ('ciclo', 'Ciclo del cliente'), ('pilares', 'Pilares y agentes'), ('agentes', 'Cómo trabajan'),
           ('cerebro', 'Cerebro en Notion'), ('falta', 'Lo que te falta'), ('ruta', 'Ruta'), ('ritmo', 'Ritmo'),
           ('stack', 'Herramientas'), ('riesgos', 'Riesgos'), ('preguntas', 'Preguntas'), ('fuentes', 'Fuentes')]
    H.append('<nav class="toc" aria-label="Secciones"><ul>' + ''.join(f'<li><a href="#{a}">{esc(t)}</a></li>' for a, t in nav) + '</ul></nav>')
    H.append('<main class="wrap">')
    # ---- mapa
    H.append('<section id="mapa"><h2>Mapa general</h2>')
    H.append(f'<p class="sec-lede">{esc(X["map_lede"])}</p>')
    H.append(f'<figure><div class="fig">{svg_map(F, cols, layer, people, X)}</div>'
             f'<figcaption>{esc(X["map_caption"])}</figcaption></figure></section>')
    # ---- ciclo
    H.append('<section id="ciclo"><h2>El ciclo del cliente</h2>')
    H.append(f'<p class="sec-lede">{esc(X["cycle_lede"])}</p>')
    H.append(f'<figure><div class="fig">{svg_cycle(X["cycle"], X["cycle_kpis"])}</div>'
             f'<figcaption>{esc(X["cycle_caption"])}</figcaption></figure></section>')
    # ---- pilares
    H.append('<section id="pilares"><h2>Pilares y agentes</h2>')
    H.append(f'<p class="sec-lede">{esc(X["pillars_lede"])}</p><div class="grid pillars">')
    for p in allp:
        H.append(f'<article class="card" id="p-{esc(p["_anchor"])}">')
        H.append(f'<h3><span class="swatch bg-{p["_slot"]}" aria-hidden="true"></span>{esc(p["nombre"])}'
                 + (' <span class="tag-new">NUEVO</span>' if p.get('nuevo') else '') + '</h3>')
        H.append(f'<p class="mission">{esc(p["mision"])}</p>')
        if p.get('dueno_humano'):
            H.append(f'<p class="owner">Dueño: {esc(p["dueno_humano"])}</p>')
        if p.get('chat'):
            H.append(f'<p class="owner">Chat: {esc(p["chat"])}</p>')
        H.append('<ul class="agents">')
        for a in p['agentes']:
            k = auton_key(a.get('autonomia'))
            io = ' → '.join(x for x in [a.get('disparador', ''), a.get('salida', '')] if x)
            H.append(f'<li>{glyph_html(k)}<div><span class="nm">{esc(a["nombre"])}</span> <span class="au">· {esc(AUTON[k][1])}</span></div>'
                     f'<div class="ms">{esc(a.get("mision", ""))}</div>'
                     + (f'<div class="io">{esc(io)}</div>' if io else '')
                     + (f'<div class="io"><b>Se enciende:</b> {esc(a["se_enciende"])}</div>' if a.get('se_enciende') else '') + '</li>')
        H.append('</ul><dl class="kv">')
        for lab, key in [('Personas', 'personas'), ('Herramientas', 'herramientas'), ('Notion', 'bases_notion'), ('KPIs', 'kpis'), ('Rituales', 'rituales')]:
            if p.get(key):
                items = [i for i in p[key] if i]
                if any(len(i) > 38 for i in items):
                    H.append(f'<dt>{lab}</dt><dd><ul class="kvlist">' + ''.join(f'<li>{esc(i)}</li>' for i in items) + '</ul></dd>')
                else:
                    H.append(f'<dt>{lab}</dt><dd>{chips(items)}</dd>')
        H.append('</dl></article>')
    H.append('</div></section>')
    # ---- orquestación
    O = F['orquestacion']
    H.append('<section id="agentes"><h2>Cómo trabajan los chats y los agentes</h2>')
    H.append(f'<p class="sec-lede">{esc(O["descripcion"])}</p>')
    H.append(f'<figure><div class="fig">{svg_orq(X["orq_nodes"], X["orq_edges"])}</div>'
             f'<figcaption>{esc(X["orq_caption"])}</figcaption></figure>')
    H.append('<div class="cols2"><div class="card"><h3>Reglas del sistema</h3><ol class="rules">'
             + ''.join(f'<li>{esc(r)}</li>' for r in O['reglas']) + '</ol></div>'
             '<div class="card"><h3>Principios</h3><ol class="rules">'
             + ''.join(f'<li>{esc(r)}</li>' for r in F['principios']) + '</ol></div></div></section>')
    # ---- cerebro
    C = F['cerebro_notion']
    H.append('<section id="cerebro"><h2>El cerebro en Notion</h2>')
    H.append(f'<p class="sec-lede">{esc(X["brain_lede"])}</p><div class="grid brain">')
    for b in C['bases']:
        H.append(f'<article class="card"><h3>{esc(b["nombre"])}</h3><p>{esc(b.get("proposito", ""))}</p><dl class="kv">')
        if b.get('propiedades'): H.append(f'<dt>Campos</dt><dd>{chips(b["propiedades"][:9])}</dd>')
        if b.get('relaciones'): H.append(f'<dt>Se conecta con</dt><dd>{chips(b["relaciones"])}</dd>')
        H.append('</dl>')
        if b.get('quien_alimenta'): H.append(f'<p class="feeds">La alimenta: {esc(b["quien_alimenta"])}</p>')
        H.append('</article>')
    H.append('</div><div class="cols2">')
    H.append('<div class="card"><h3>Tableros por rol</h3><ul class="rules">' + ''.join(f'<li>{esc(d)}</li>' for d in C.get('dashboards', [])) + '</ul></div>')
    if C.get('permisos'):
        H.append('<div class="card"><h3>Quién ve qué</h3><ul class="rules">' + ''.join(f'<li>{esc(d)}</li>' for d in C['permisos']) + '</ul></div>')
    H.append('</div></section>')
    # ---- lo que te falta
    order = {'P0': 0, 'P1': 1, 'P2': 2}
    gaps_sorted = sorted(gaps, key=lambda g: (order.get(g.get('prioridad'), 3)))
    pil_names = {p['id']: p['nombre'] for p in allp}
    H.append('<section id="falta"><h2>Lo que te falta</h2>')
    H.append(f'<p class="sec-lede">{esc(X["gaps_lede"])}</p>')
    cells = ''.join('<i></i>' if g.get('dominio') == 'desconocido' else '<i class="k"></i>' for g in gaps_sorted)
    H.append(f'<div class="meter"><div class="cells" aria-hidden="true">{cells}</div>'
             f'<span><b>{n_unknown} de {len(gaps)}</b> están fuera de tu terreno técnico ({round(100 * n_unknown / max(1, len(gaps)))}%). '
             f'El resto ({len(gaps) - n_unknown}) es de IA e ingeniería.</span></div>')
    H.append('<div class="filters" role="group" aria-label="Filtrar por prioridad">'
             '<button type="button" id="f-all" data-f="all" aria-pressed="true">Todos</button>'
             '<button type="button" id="f-p0" data-f="P0" aria-pressed="false">P0 · antes de escalar</button>'
             '<button type="button" id="f-p1" data-f="P1" aria-pressed="false">P1 · próximo trimestre</button>'
             '<button type="button" id="f-p2" data-f="P2" aria-pressed="false">P2 · después</button></div>')
    H.append('<div class="grid gaps">')
    for g in gaps_sorted:
        pr = g.get('prioridad', 'P2')
        pn = pil_names.get(g.get('pilar', ''), g.get('pilar', ''))
        H.append(f'<article class="card gap-card" data-p="{esc(pr)}"><div class="gap-head"><span class="prio prio-{esc(pr)}">{esc(pr)}</span>'
                 + (f'<span class="tag">{esc(pn)}</span>' if pn else '')
                 + ('<span class="tag">tu terreno</span>' if g.get('dominio') == 'conocido' else '') + '</div>')
        H.append(f'<h3>{esc(g["titulo"])}</h3><p>{esc(g["explicacion"])}</p>')
        if g.get('por_que_importa'): H.append(f'<p class="why">{esc(g["por_que_importa"])}</p>')
        H.append(f'<div class="first"><b>Primer paso</b>{esc(g["primer_paso"])}</div>')
        ei = ' · '.join(x for x in [f'esfuerzo {g["esfuerzo"]}' if g.get('esfuerzo') else '', f'impacto {g["impacto"]}' if g.get('impacto') else ''] if x)
        if ei: H.append(f'<span class="ei">{esc(ei)}</span>')
        H.append('</article>')
    H.append('</div></section>')
    # ---- ruta
    R = F['roadmap']
    wk = [weeks(r.get('duracion', '')) for r in R]
    tot = sum(wk) or 1
    shades = ['var(--ink)', 'var(--c-producto)', 'var(--c-clientes)', 'var(--line-strong)']
    H.append('<section id="ruta"><h2>Ruta de implementación</h2>')
    H.append(f'<p class="sec-lede">{esc(X["road_lede"])}</p>')
    H.append('<div class="timeline" aria-hidden="true">' + ''.join(f'<span style="width:{100 * w / tot:.1f}%;background:{shades[i % 4]}"></span>' for i, w in enumerate(wk)) + '</div>')
    H.append('<div class="grid phases">')
    for i, r in enumerate(R):
        H.append(f'<article class="card phase"><span class="n">{esc(r["fase"])}</span><h3>{esc(r["nombre"])}</h3>'
                 f'<p class="dur">{esc(r.get("duracion", ""))}</p><ul>' + ''.join(f'<li>{esc(e)}</li>' for e in r['entregables']) + '</ul>'
                 + (f'<p class="ok"><b>Listo cuando:</b> {esc(r["criterio_exito"])}</p>' if r.get('criterio_exito') else '') + '</article>')
    H.append('</div></section>')
    # ---- ritmo
    groups = {}
    for c in F['cadencias']:
        groups.setdefault(c['frecuencia'].strip().capitalize(), []).append(c)
    H.append('<section id="ritmo"><h2>El ritmo de la semana y del año</h2>')
    H.append(f'<p class="sec-lede">{esc(X["rhythm_lede"])}</p><div class="grid rhythm">')
    for fq, items in groups.items():
        H.append(f'<div class="card"><h3>{esc(fq)}</h3><ul>' + ''.join(
            f'<li>{esc(c["actividad"])}' + (f'<small>{esc(c["responsable"])}</small>' if c.get('responsable') else '') + '</li>' for c in items) + '</ul></div>')
    H.append('</div></section>')
    # ---- stack
    H.append('<section id="stack"><h2>Herramientas recomendadas</h2>')
    H.append(f'<p class="sec-lede">{esc(X["stack_lede"])}</p><div class="tbl"><table><thead><tr><th>Para qué</th><th>Herramienta</th><th>Alternativa</th><th>Costo mensual</th></tr></thead><tbody>')
    for s in F['stack_recomendado']:
        H.append(f'<tr><td>{esc(s["funcion"])}</td><td><b>{esc(s["herramienta"])}</b></td><td>{esc(s.get("alternativa", ""))}</td><td class="cost">{esc(s.get("costo_aprox", ""))}</td></tr>')
    H.append('</tbody></table></div></section>')
    # ---- riesgos
    H.append('<section id="riesgos"><h2>Riesgos y cómo cubrirte</h2><div class="tbl"><table><thead><tr><th>Riesgo</th><th>Mitigación</th></tr></thead><tbody>')
    for r in F['riesgos']:
        H.append(f'<tr><td>{esc(r["riesgo"])}</td><td>{esc(r["mitigacion"])}</td></tr>')
    H.append('</tbody></table></div></section>')
    # ---- preguntas
    H.append('<section id="preguntas"><h2>Preguntas para afinar</h2>')
    H.append(f'<p class="sec-lede">{esc(X["q_lede"])}</p><ol class="qs">' + ''.join(f'<li>{esc(q)}</li>' for q in F['preguntas_abiertas']) + '</ol></section>')
    # ---- fuentes
    V = X.get('verificaciones', [])
    H.append('<section id="fuentes"><h2>Fuentes y datos verificados</h2>')
    H.append(f'<p class="sec-lede">{esc(X["src_lede"])}</p><ul class="src">')
    lab = {'correcta': 'Correcto', 'matizar': 'Con matices', 'incorrecta': 'Corregido', 'no_verificable': 'Sin confirmar'}
    for v in V:
        st = v.get('estado', 'no_verificable')
        fuente = v.get('fuente', '')
        link = ''
        m = re.search(r'https?://\S+', fuente or '')
        if m:
            u = m.group(0).rstrip(').,;')
            link = f' <a href="{esc(u)}">{esc(u)}</a>'
        H.append(f'<li><span class="st st-{esc(st)}">{esc(lab.get(st, st))}</span><div>{esc(v["afirmacion"])}{link}</div>'
                 + (f'<div class="fix">{esc(v["correccion"])}</div>' if v.get('correccion') else '') + '</li>')
    H.append('</ul></section></main>')
    H.append(f'<footer class="wrap"><p>{esc(X["footer"])}</p></footer>')
    H.append("""<script>
(function(){
  var bs = document.querySelectorAll('.filters button');
  var cards = document.querySelectorAll('.gap-card');
  bs.forEach(function(b){
    b.addEventListener('click', function(){
      var f = b.getAttribute('data-f');
      bs.forEach(function(o){ o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
      cards.forEach(function(c){ c.hidden = !(f === 'all' || c.getAttribute('data-p') === f); });
    });
  });
})();
</script></body></html>""")
    return ''.join(H)

def prepare(F):
    ps = []
    for p in F['pilares']:
        p = dict(p)
        p['_slot'] = color_slot(p)
        p['_layer'] = is_layer_pillar(p)
        p['_anchor'] = slug(p.get('id') or p['nombre'])
        ps.append(p)
    ps.sort(key=lambda p: (1 if p['_layer'] else 0, CLUSTER_ORDER.index(CLUSTER[p['_slot']]), SLOT_ORDER.get(p['_slot'], 9)))
    F['pillars_sorted'] = ps
    return F

if __name__ == '__main__':
    # uso: python3 build.py <arquitectura.json> <textos.json> <salida.html> [verificacion.json]
    F = prepare(json.load(open(sys.argv[1])))
    X = json.load(open(sys.argv[2]))
    if len(sys.argv) > 4 and 'verificaciones' not in X:
        X['verificaciones'] = json.load(open(sys.argv[4]))['verificaciones']
    open(sys.argv[3], 'w').write(build(F, X))
    print('written', sys.argv[3])
