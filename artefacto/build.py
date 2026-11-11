"""Arma el HTML completo del artefacto. Uso: python3 build.py final.json x_final.json salida.html"""
import json, sys, re
from collections import Counter, defaultdict
from urllib.parse import urlparse
import gen_page
from gen_page import *

CSS = r"""
:root{
  /* Plano de un sistema operativo: papel frío y tinta pizarra; la señal bermellón marca lo que te falta,
     lo NUEVO y lo que está encendido. Capas de arriba abajo (dirección, pilares, cerebro, tuberías, herramientas). */
  --bg:#F3F4F6; --surface:#FFFFFF; --surface-2:#F8F9FB; --ink:#141C28; --muted:#566174; --line:#D5DAE2; --line-strong:#A7B1BF;
  --signal:#C2410C; --on-signal:#FFFFFF; --ceo:#141C28; --on-ceo:#F3F4F6;
  --ok:#1E6E30; --warn:#9A4F00; --crit:#C92A2A;
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
.sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.wrap{max-width:1340px;margin:0 auto;padding:0 20px}
.top{padding-top:44px;padding-bottom:20px}
.eyebrow{font-family:var(--font-mono);font-size:12.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin:0}
h1{font-family:var(--font-display);font-weight:800;font-size:clamp(32px,4.4vw,54px);line-height:1.04;letter-spacing:-.02em;margin:10px 0 14px;text-wrap:balance;max-width:22ch}
.lede{font-size:18px;max-width:66ch;margin:0}
.legend{margin:18px 0 0;display:grid;gap:4px;font-size:14px;color:var(--muted)}
.legend ul{display:flex;flex-wrap:wrap;gap:6px 20px;margin:0;padding:0;list-style:none;align-items:center}
.legend li{display:flex;align-items:center;gap:7px}
.legend-in{margin:0 0 18px}
.legend-h{font-family:var(--font-mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;margin:8px 0 0}
.legend .on-s{font-family:var(--font-mono);font-weight:700;font-size:13px;color:var(--ink)}
.legend .dim-s{font-family:var(--font-mono);font-size:13px;color:var(--muted)}
.led{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--signal);flex:none}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:24px 0 0;max-width:1060px}
.stat.span2{grid-column:span 2}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 14px}
.stat b{display:block;font-family:var(--font-display);font-size:26px;line-height:1.1;font-variant-numeric:tabular-nums}
.stat span{font-size:13px;color:var(--muted);display:block}
.toc{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
.toc ul{display:flex;gap:0;overflow-x:auto;list-style:none;margin:0 auto;padding:8px 20px;max-width:1340px}
.toc a{display:inline-block;padding:6px 7px;border-radius:8px;text-decoration:none;font-size:14px;white-space:nowrap;color:var(--muted)}
.toc a:hover{background:var(--surface);color:var(--ink)}
section{padding:40px 0 6px;scroll-margin-top:calc(var(--toc-h, 51px) + 1px)}
h2{font-family:var(--font-display);font-weight:800;font-size:clamp(24px,3vw,34px);letter-spacing:-.01em;line-height:1.1;margin:0 0 8px;text-wrap:balance}
h3{font-family:var(--font-display);text-wrap:balance}
.sec-lede{max-width:72ch;color:var(--muted);margin:0 0 18px}
figure{margin:0}
.fig{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:10px;overflow-x:auto}
figcaption{font-size:14px;color:var(--muted);margin:10px 4px 0;max-width:92ch}
figcaption p{margin:0 0 8px}
.grid{display:grid;gap:14px}
.pillars{grid-template-columns:repeat(auto-fill,minmax(min(100%,380px),1fr));align-items:start}
.card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px;min-width:0}
.card h3{font-size:21px;margin:0;display:flex;gap:10px;align-items:center;line-height:1.2}
.card h3 .ttl{flex:1 1 0;min-width:0}
#pilares article,.gap-card,details.flow{scroll-margin-top:calc(var(--toc-h, 51px) + 13px)}
#pilares article:target,.gap-card:target,details.flow:target{outline:2px solid var(--signal);outline-offset:2px}
.swatch{width:12px;height:12px;border-radius:3px;flex:none}
.tag-new{font-family:var(--font-mono);font-size:11px;font-weight:600;letter-spacing:.06em;background:var(--signal);color:var(--on-signal);border-radius:999px;padding:2px 9px;flex:none}
.tag{font-family:var(--font-mono);font-size:11.5px;border:1px solid var(--line-strong);border-radius:10px;padding:1px 9px;color:var(--muted);white-space:normal;max-width:100%;overflow-wrap:anywhere}
.mission{margin:8px 0 4px}
.owner{font-size:14px;color:var(--muted);margin:0 0 12px}
.agents{list-style:none;margin:0 0 14px;padding:0;display:grid;gap:10px}
.agents li{display:grid;grid-template-columns:18px minmax(0,1fr);gap:4px 8px;padding-top:10px;border-top:1px solid var(--line)}
.agents .nm{font-family:var(--font-mono);font-weight:500;font-size:14px}
.agents .ag-on .nm{font-weight:700}
.agents .led{margin:0 2px 1px 7px;vertical-align:middle}
.agents .au{font-size:12.5px;color:var(--muted)}
.agents .st-on{color:var(--signal);font-weight:600}
.agents .st-rule{color:var(--ink);font-weight:600}
.agents .ms{grid-column:2;font-size:14.5px}
.agents .io{grid-column:2;font-size:13px;color:var(--muted)}
.agents .st-note{color:var(--ink);border-left:2px solid var(--signal);padding-left:8px}
.agents .st-note a{color:inherit}
.g{width:12px;height:12px;margin-top:4px;flex:none}
.g circle,.g path,.g rect{stroke:var(--ink)}
.kv{display:grid;grid-template-columns:110px minmax(0,1fr);gap:6px 10px;font-size:14px;margin:0}
.kv dt{color:var(--muted)}
.kv dd{margin:0;display:flex;flex-wrap:wrap;gap:5px;min-width:0}
.kvlist{margin:0;padding-left:18px;font-size:13.5px;line-height:1.45}
.kvlist li{margin:0 0 4px}
.chip{font-family:var(--font-mono);font-size:12px;background:var(--surface-2);border:1px solid var(--line);border-radius:10px;padding:1px 9px;white-space:normal;overflow-wrap:anywhere;max-width:100%}
.brain{grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));align-items:start}
.brain .card h3{font-size:17px}
.brain .kv{grid-template-columns:minmax(0,1fr);gap:4px}
.brain .kv dt{margin-top:4px}
.brain p{margin:6px 0 10px;font-size:14.5px}
.feeds{list-style:none;margin:12px 0 0;padding:10px 0 0;border-top:1px solid var(--line);font-size:13.5px;display:grid;gap:4px}
.feeds b{font-weight:600}
.feeds .extra{color:var(--muted)}
.cols2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:14px;margin-top:14px;align-items:start}
ol.rules,ul.rules{margin:0;padding-left:22px;display:grid;gap:8px;max-width:80ch}
.wide{margin-top:14px}
.wide h3{margin:0 0 4px;font-size:19px}
.wide .sub{color:var(--muted);font-size:14px;margin:0 0 12px}
.pages,.pipes-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,420px),1fr));gap:10px 26px;font-size:14.5px}
.pages li,.pipes-list li{border-top:1px solid var(--line);padding-top:9px;min-width:0}
.pages b,.pipes-list b{display:block;font-weight:600}
.pipes-list b{font-family:var(--font-mono);font-size:13.5px}
.blocks{grid-template-columns:repeat(auto-fill,minmax(min(100%,340px),1fr));align-items:start;margin:0 0 18px}
.blocks .card{padding:14px 16px}
.blocks .card h3{font-family:var(--font-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:500;margin:0 0 6px}
.blocks .card p{margin:0;font-size:15px;line-height:1.5}
.flows{display:grid;gap:10px}
details.flow{background:var(--surface);border:1px solid var(--line);border-radius:14px}
details.flow > summary{cursor:pointer;padding:14px 18px;font-family:var(--font-display);font-weight:700;font-size:17px;list-style:none;display:grid;grid-template-columns:12px minmax(0,1fr) auto;column-gap:10px;align-items:baseline}
details.flow > summary::-webkit-details-marker{display:none}
details.flow > summary::before{content:"+";font-family:var(--font-mono);font-weight:500;color:var(--muted)}
details.flow[open] > summary::before{content:"\2212"}
details.flow .fname{min-width:0}
details.flow .cnt{font-family:var(--font-mono);font-size:12px;color:var(--muted);font-weight:400;white-space:nowrap}
details.flow .tbl{border:0;border-top:1px solid var(--line);border-radius:0 0 14px 14px}
.meter{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:0 0 14px}
.cells{display:flex;gap:4px;flex-wrap:wrap}
.cells i{width:16px;height:16px;border-radius:4px;background:var(--signal)}
.cells i.k{background:var(--line-strong)}
.filters{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px}
.filters button{font:inherit;font-size:14px;color:var(--ink);background:var(--surface);border:1px solid var(--line-strong);border-radius:999px;padding:5px 12px;cursor:pointer;min-height:36px}
.filters button[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.gaps{grid-template-columns:repeat(auto-fill,minmax(min(100%,360px),1fr));align-items:start}
.gap-card{display:flex;flex-direction:column;gap:8px}
.gap-card[hidden]{display:none}
.gap-head{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.pc-n{font-family:var(--font-mono);font-size:12px;font-weight:600;min-width:26px;height:22px;padding:0 6px;border-radius:6px;border:1px solid var(--line-strong);display:inline-flex;align-items:center;justify-content:center}
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
.srcs{font-size:12.5px;color:var(--muted);margin:0;overflow-wrap:anywhere}
.srcs a{color:var(--muted)}
.off{font-family:var(--font-mono);font-size:10.5px;border:1px solid var(--line-strong);border-radius:4px;padding:0 4px;margin-left:3px;white-space:nowrap}
.gantt{list-style:none;margin:6px 0 4px;padding:0;display:grid;gap:8px;max-width:1000px}
.gantt li{display:grid;grid-template-columns:150px minmax(0,1fr);gap:12px;align-items:center}
.gantt .gl{font-size:13.5px;white-space:nowrap}
.gantt .gl b{font-family:var(--font-mono);font-weight:600}
.gantt .gl .gd{color:var(--muted);font-family:var(--font-mono);font-size:12.5px}
.gantt .gd::before{content:"· "}
.gantt-axis div span:last-child{text-align:right}
.gantt .track{position:relative;height:14px;background:var(--surface-2);border:1px solid var(--line);border-radius:999px}
.gantt .bar{position:absolute;top:-1px;bottom:-1px;background:var(--ink);border-radius:999px}
.gantt-axis{display:grid;grid-template-columns:150px minmax(0,1fr);gap:12px;font-family:var(--font-mono);font-size:12px;color:var(--muted);margin:0 0 18px;max-width:1000px}
.gantt-axis div{display:flex;justify-content:space-between;gap:10px}
.phases{grid-template-columns:repeat(auto-fit,minmax(min(100%,270px),1fr));align-items:start}
.phase .n{font-family:var(--font-mono);font-size:12px;color:var(--muted);letter-spacing:.06em;text-transform:uppercase}
.phase h3{font-size:19px;margin:2px 0 2px}
.phase .dur{font-size:13.5px;color:var(--muted);margin:0 0 8px}
.phase ul{margin:0 0 10px;padding-left:18px;font-size:14.5px;display:grid;gap:4px}
.phase .ok{font-size:13.5px;border-top:1px solid var(--line);padding-top:8px;margin:0}
.rhythm{grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));align-items:start}
.rhythm h3{font-size:16px;margin:0 0 8px;font-family:var(--font-mono);font-weight:500;letter-spacing:.06em;text-transform:uppercase}
.rhythm ul{list-style:none;margin:0;padding:0;display:grid;gap:10px;font-size:14.5px}
.rhythm li small{display:block;color:var(--muted);font-size:12.5px}
.tbl{overflow-x:auto;background:var(--surface);border:1px solid var(--line);border-radius:14px}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top;overflow-wrap:anywhere}
th{font-family:var(--font-mono);font-size:12px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:500;overflow-wrap:normal}
tr:last-child td{border-bottom:0}
.stack-t{table-layout:fixed}
.stack-t th:nth-child(1){width:20%} .stack-t th:nth-child(2){width:25%} .stack-t th:nth-child(3){width:25%} .stack-t th:nth-child(4){width:30%}
td.cost{font-variant-numeric:tabular-nums}
td.cost small{display:block;color:var(--muted);font-size:13px;margin-top:3px;line-height:1.45}
.risk-t th:first-child{width:42%}
.flow-t th:nth-child(1){width:64px} .flow-t th:nth-child(2){width:18%} .flow-t th:nth-child(4){width:24%}
.flow-t td:first-child{font-family:var(--font-mono);color:var(--muted)}
.qs{margin:0;padding-left:22px;display:grid;gap:8px;font-size:16px;max-width:80ch}
.qs li{scroll-margin-top:calc(var(--toc-h, 51px) + 13px)}
.qs li:target{outline:2px solid var(--signal);outline-offset:4px;border-radius:4px}
.changes{grid-template-columns:repeat(auto-fill,minmax(min(100%,360px),1fr));align-items:start}
.changes h3{font-size:18px;margin:0 0 10px}
.changes ul{margin:0;padding-left:18px;display:grid;gap:7px;font-size:14.5px}
.src{list-style:none;margin:0;padding:0;font-size:14px}
.src > li{display:grid;grid-template-columns:120px minmax(0,1fr);gap:4px 14px;padding:12px 0;border-top:1px solid var(--line)}
.st{font-family:var(--font-mono);font-size:11.5px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;padding-top:2px}
.st-correcta{color:var(--ok)} .st-matizar{color:var(--warn)} .st-incorrecta{color:var(--crit)} .st-no_verificable{color:var(--muted)}
.src .body{display:grid;gap:6px;min-width:0}
.src p{margin:0}
.src .loc{font-family:var(--font-mono);font-size:12px;color:var(--muted)}
.src .loc a{color:var(--ink)}
.src .lbl{font-weight:600}
.src .old,.src .conf{color:var(--muted)}
footer.wrap{padding:40px 20px 56px;color:var(--muted);font-size:13.5px}
footer.wrap p{margin:0;padding-top:18px;border-top:1px solid var(--line)}
.diagram{display:block;width:100%;height:auto;min-width:1060px;color:var(--ink);font-family:var(--font-body)}
.diagram text{fill:currentColor}
.diagram .box{fill:var(--surface);stroke:var(--line-strong);stroke-width:1.2}
.diagram .box-dashed{stroke-dasharray:5 4}
.diagram .box-ceo{fill:var(--ceo);stroke:var(--ceo)}
.diagram .t-on-ceo{fill:var(--on-ceo)}
.diagram .dot-on-ceo{fill:var(--on-ceo)}
.diagram .box-brain{fill:var(--surface-2);stroke:var(--ink);stroke-width:1.8}
.diagram .box-pipes{fill:var(--surface-2)}
.diagram .chip{fill:var(--surface);stroke:var(--line-strong);stroke-width:1}
.diagram .chip-tool{fill:none;stroke-dasharray:3 3}
.diagram .chip-dash{stroke-dasharray:3 3}
.diagram .edge{stroke:var(--muted);stroke-width:1.6;fill:none}
.diagram .edge-dash{stroke-dasharray:5 4}
.diagram .edge-strong{stroke:var(--signal);stroke-width:2.2}
.diagram .arrowhead{fill:var(--muted)}
.diagram .arrowhead-hot{fill:var(--signal)}
.diagram .t-title{font-family:var(--font-display);font-weight:700;font-size:19px}
.diagram .t-title-s{font-family:var(--font-display);font-weight:700;font-size:16px}
.diagram .t-sub{font-size:12.5px;fill:var(--muted)}
.diagram .t-sub.t-on-ceo{fill:var(--on-ceo);opacity:.82}
.diagram .t-sub.t-strong{opacity:1}
.diagram .t-pillar{font-family:var(--font-display);font-weight:700;font-size:15px}
.diagram .t-owner{font-size:11.5px;fill:var(--muted)}
.diagram .t-agent{font-family:var(--font-mono);font-size:12px}
.diagram .t-on{font-weight:700}
.diagram .t-later{fill:var(--muted)}
.diagram .g-later{opacity:.6}
.diagram .led{fill:var(--signal)}
.diagram .g-rule{fill:none;stroke:var(--ink);stroke-width:1.5}
.diagram .t-chip{font-family:var(--font-mono);font-size:12px}
.diagram .t-chip-s{font-family:var(--font-mono);font-size:11px}
.diagram .t-edge{font-family:var(--font-mono);font-size:11.5px;fill:var(--muted)}
.diagram .t-cluster{font-family:var(--font-mono);font-size:11px;letter-spacing:.08em;fill:var(--muted);font-weight:500}
.diagram .t-cond{font-size:11.5px;fill:var(--muted)}
.diagram .badge-new{fill:var(--signal)}
.diagram .t-badge{font-family:var(--font-mono);font-size:10px;font-weight:600;fill:var(--on-signal);letter-spacing:.06em}
.diagram .t-badge-mini{font-family:var(--font-mono);font-size:8.5px;font-weight:600;fill:var(--on-signal);letter-spacing:.04em}
.diagram .badge-human{fill:var(--ink)}
.diagram .t-badge-h{font-family:var(--font-mono);font-size:10px;font-weight:600;fill:var(--bg);letter-spacing:.04em}
.diagram .badge-agent{fill:var(--surface);stroke:var(--ink);stroke-width:1.4}
.diagram .t-badge-a{font-family:var(--font-mono);font-size:10px;font-weight:600;fill:var(--ink);letter-spacing:.04em}
.diagram .g-fill{fill:var(--ink)}
.diagram .g-ring{fill:none;stroke:var(--ink);stroke-width:1.4}
.diagram .g-dash{stroke:var(--muted);stroke-dasharray:2.2 2}
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
@media (min-width:561px){ .toc ul{flex-wrap:wrap;overflow-x:visible} }
@media (max-width:560px){
  .toc::after{content:"";position:absolute;top:0;right:0;bottom:1px;width:36px;background:linear-gradient(to right,transparent,var(--bg));pointer-events:none;transition:opacity .15s}
  .toc.at-end::after{opacity:0}
  .kv{grid-template-columns:minmax(0,1fr)}
  .src > li{grid-template-columns:minmax(0,1fr)}
  .lede{font-size:16.5px}
  .tbl.stackable{overflow:visible}
  .tbl.stackable table,.tbl.stackable tbody,.tbl.stackable tr,.tbl.stackable td{display:block;width:auto}
  .tbl.stackable thead{display:none}
  .tbl.stackable tr{padding:8px 14px 10px;border-bottom:1px solid var(--line)}
  .tbl.stackable tr:last-child{border-bottom:0}
  .tbl.stackable td{border:0;padding:2px 0}
  .tbl.stackable td::before{content:attr(data-label);display:block;font-family:var(--font-mono);font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin-top:6px}
  .gantt li,.gantt-axis{grid-template-columns:104px minmax(0,1fr)}
  details.flow > summary{font-size:16px;grid-template-columns:12px minmax(0,1fr)}
  details.flow .cnt{grid-column:2}
  .gantt .gd{display:block}
  .gantt .gd::before{content:""}
}
"""

# ---------------- utilidades HTML ----------------
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

def rule_glyph_html():
    return '<svg class="g" viewBox="0 0 12 12" aria-hidden="true"><rect x="1.5" y="1.5" width="9" height="9" rx="1.5" fill="none" stroke-width="1.5"/></svg>'

def chips(items):
    return ''.join(f'<span class="chip">{esc(i)}</span>' for i in items if i)

def kv_items(items):
    """Chips si todo es corto; lista si algún elemento pasa de 38 caracteres."""
    items = [i for i in items if i]
    if any(len(i) > 38 for i in items):
        return '<ul class="kvlist">' + ''.join(f'<li>{esc(i)}</li>' for i in items) + '</ul>'
    return chips(items)

def cap(s):
    s = str(s).strip()
    if s and s[0].islower() and not s.startswith('n8n'):
        return s[0].upper() + s[1:]
    return s

def md_links(escaped):
    """Convierte [texto](#ancla) en enlaces, sobre texto ya escapado."""
    return re.sub(r'\[([^\]]+)\]\((#[\w-]+)\)', r'<a href="\2">\1</a>', escaped)

def short_role(h):
    """Nombre corto de un rol humano ('' si no es del equipo)."""
    s = h.split(':')[0]
    s = re.sub(r'\s*\(.*?\)', '', s).strip()
    s = re.sub(r'\s*\(.*$', '', s).strip()
    if len(s) > 30:
        s = re.split(r',| y | que | para ', s)[0].strip()
    low = s.lower()
    if low in ('tú', 'tu', 'tú (ceo)') or low.startswith('tú ') or 'cliente' in low or 'aliado' in low or 'anfitri' in low:
        return ''
    return s[:1].upper() + s[1:]

def dur_weeks(d):
    """Duración real de una fase: solo el número del inicio, en semanas (un mes = 4.3 semanas)."""
    m = re.match(r'\s*(\d+(?:[.,]\d+)?)\s*(semana|mes)', d or '', re.I)
    if not m:
        return None, ''
    v = float(m.group(1).replace(',', '.'))
    if m.group(2).lower().startswith('mes'):
        w = round(v * 4.3, 1)
        return w, f'~{w:g} sem'
    return v, f'{v:g} sem'

def split_cost(c):
    """Separa un monto corto de su nota larga (solo si el monto es corto)."""
    c = (c or '').strip()
    cands = [i for i in (c.find(' ('), c.find('; ')) if i > 0]
    if not cands:
        return c, ''
    i = min(cands)
    head, rest = c[:i].strip(), c[i:].strip()
    if len(head) > 90 or len(rest) < 3:
        return c, ''
    if rest.startswith(';'):
        rest = rest[1:].strip()
    if rest.startswith('(') and rest.endswith(')') and rest.count('(') == 1:
        rest = rest[1:-1]
    elif rest.startswith('('):
        j = rest.find(')')
        after = rest[j + 1:].lstrip() if j > 0 else ''
        if after.startswith(';') and '(' not in rest[1:j]:
            inner, after = rest[1:j].strip(), after[1:].strip()
            if len(inner) <= 20:
                head, rest = f'{head} ({inner})', after   # paréntesis corto: se queda con el monto
            else:
                rest = f'{inner}. {cap(after)}'          # paréntesis largo: pasa a ser la primera frase de la nota
    return head, rest

def parse_feeds(t):
    m = re.match(r'\s*Quién:\s*(.*?)\s*Cada cuándo:\s*(.*?)\s*Desde dónde:\s*(.*)$', t or '', re.S)
    if not m:
        return None
    quien, cuando, desde = m.group(1), m.group(2), m.group(3).strip()
    extra = ''
    m2 = re.match(r'(.+?\.)\s+([A-ZÁÉÍÓÚÑ«].*)$', desde, re.S)
    if m2:
        desde, extra = m2.group(1), m2.group(2)
    return quien, cuando, desde, extra

def link_list(urls, official):
    def is_off(host):
        return any(host == d or host.endswith('.' + d) for d in official)
    parsed = []
    for u in urls:
        u = u.strip().rstrip(').,;')
        if not u.startswith('http'):
            continue
        parsed.append((u, urlparse(u).netloc.lower()))
    parsed.sort(key=lambda t: 0 if is_off(t[1]) else 1)
    counts = Counter(h for _, h in parsed)
    k = defaultdict(int)
    out = []
    for u, h in parsed:
        disp = h[4:] if h.startswith('www.') else h
        if counts[h] > 1:
            k[h] += 1
            disp += f' ({k[h]})'
        out.append(f'<a href="{esc(u)}" title="{esc(u)}">{esc(disp)}</a>' + ('<span class="off">oficial</span>' if is_off(h) else ''))
    return ' · '.join(out)

def split_blocks(text, blocks, repl):
    for a, b in repl.items():
        text = text.replace(a, b)
    idx = [text.find(bl['start']) for bl in blocks]
    assert all(i >= 0 for i in idx), [bl['start'] for bl, i in zip(blocks, idx) if i < 0]
    assert idx == sorted(idx) and idx[0] == 0, idx
    out = []
    for j, bl in enumerate(blocks):
        seg = text[idx[j]: idx[j + 1] if j + 1 < len(idx) else len(text)].strip()
        if bl.get('strip') and seg.startswith(bl['strip']):
            seg = seg[len(bl['strip']):]
        out.append((bl['label'], cap(seg)))
    return out


def legend_html(n_on):
    return ('<div class="legend">'
            '<p class="legend-h">Estado</p><ul>'
            f'<li><span class="led" aria-hidden="true"></span><span class="on-s">Nombre</span> en negritas: encendido antes de abril ({n_on})</li>'
            '<li><span class="dim-s">Nombre</span> atenuado en el mapa: se enciende después, con su condición</li>'
            f'<li>{rule_glyph_html()} regla de n8n sin IA: no cuenta como agente</li>'
            '<li><span class="tag-new">NUEVO</span> lo que no estaba en tu lista</li></ul>'
            '<p class="legend-h">Autonomía: cuánta libertad tendrá cada agente al encenderse</p><ul>'
            f'<li>{glyph_html("automatico")} automático</li>'
            f'<li>{glyph_html("borrador_con_aprobacion")} borrador que tú apruebas</li>'
            f'<li>{glyph_html("asistido")} asistido: lo opera una persona</li>'
            f'<li>{glyph_html("manual_con_plantilla")} a mano con plantilla: todavía no es agente</li></ul></div>')

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
    all_agents = [a for p in allp for a in p['agentes']]
    rules = X['reglas_n8n']; on = X['encendidos']
    n_rules = sum(1 for a in all_agents if a['nombre'] in rules)
    n_on = sum(1 for a in all_agents if a['nombre'] in on)
    n_agents = len(all_agents) - n_rules
    assert n_on == len(on) == int(X['n_activos']), (n_on, len(on))
    assert n_rules == len(rules), n_rules
    gaps = F['puntos_ciegos']
    order = {'P0': 0, 'P1': 1, 'P2': 2}
    gaps_sorted = sorted(gaps, key=lambda g: order.get(g.get('prioridad'), 3))
    num_by_title = {g['titulo']: i + 1 for i, g in enumerate(gaps_sorted)}
    n_unknown = sum(1 for g in gaps if g.get('dominio') == 'desconocido')
    prio_count = Counter(g.get('prioridad') for g in gaps)
    official = X.get('fuentes_oficiales', [])
    repl = X.get('reemplazos_presentacion', {})
    pc_by_old = {m['viejo']: m for m in X.get('pc_map', [])}
    for m in X.get('pc_map', []):
        assert m['titulo'] is None or m['titulo'] in num_by_title, m
    def pc_links(escaped, override=None):
        def sub(mo):
            word, old = mo.group(1), int(mo.group(2))
            e = pc_by_old.get(old)
            if override and str(old) in override:
                e = {'titulo': override[str(old)], 'titulo_viejo': e['titulo_viejo'] if e else ''}
            if e and e.get('titulo') in num_by_title:
                n = num_by_title[e['titulo']]
                return f'<a href="#pc-{n}" title="{esc(e["titulo"])}">{word} {n}</a>'
            if e:
                return f'{word} «{esc(e["titulo_viejo"])}»'
            return mo.group(0)
        return re.sub(r'([Pp]unto ciego) #(\d+)', sub, escaped)

    H = []
    H.append('<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">')
    H.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    H.append(f'<title>{esc(X["title"])}</title>')
    H.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    H.append('<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=Schibsted+Grotesk:wght@600;700;800&display=swap" rel="stylesheet">')
    H.append(f'<style>{CSS}</style></head><body>')
    # ---- cabecera
    H.append('<header class="wrap top">')
    H.append(f'<p class="eyebrow">{esc(X["eyebrow"])}</p>')
    H.append(f'<h1>{esc(X["h1"])}</h1>')
    H.append(f'<p class="lede">{esc(F["vision"])}</p>')
    H.append(legend_html(n_on))
    H.append('<div class="stats">'
             f'<div class="stat"><b>{len(allp)}</b><span>pilares: áreas con dueño</span></div>'
             f'<div class="stat"><b>{esc(X.get("n_chats", ""))}</b><span>{esc(X.get("n_chats_label", "chats"))}</span></div>'
             f'<div class="stat span2"><b>{n_on}</b><span>{esc(X["activos_label"])}, de {n_agents} diseñados, más {n_rules} reglas de n8n</span></div>'
             f'<div class="stat"><b>{len(F["cerebro_notion"]["bases"])}</b><span>bases en Notion</span></div>'
             f'<div class="stat"><b>{len(gaps)}</b><span>puntos ciegos · {prio_count.get("P0", 0)} P0 (antes de escalar)</span></div>'
             '</div></header>')
    nav = [('mapa', 'Mapa'), ('ciclo', 'Ciclo'), ('pilares', 'Pilares'), ('agentes', 'Cómo trabajan'),
           ('flujos', 'Flujos'), ('cerebro', 'Cerebro'), ('falta', 'Lo que falta'), ('ruta', 'Ruta'), ('ritmo', 'Ritmo'),
           ('stack', 'Herramientas'), ('riesgos', 'Riesgos'), ('preguntas', 'Preguntas'), ('cambios', 'Qué cambió'), ('fuentes', 'Fuentes')]
    H.append('<nav class="toc" aria-label="Secciones"><ul>' + ''.join(f'<li><a href="#{a}">{esc(t)}</a></li>' for a, t in nav) + '</ul></nav>')
    H.append('<main class="wrap">')
    # ---- mapa
    H.append('<section id="mapa"><h2>Mapa general</h2>')
    H.append(f'<p class="sec-lede">{esc(X["map_lede"])}</p>')
    cap_map = X['map_caption'] if isinstance(X['map_caption'], list) else [X['map_caption']]
    H.append(f'<figure><div class="fig">{svg_map(F, cols, layer, people, X)}</div>'
             '<figcaption>' + ''.join(f'<p>{md_links(esc(c))}</p>' for c in cap_map) + '</figcaption></figure></section>')
    # ---- ciclo
    H.append('<section id="ciclo"><h2>El ciclo del cliente</h2>')
    H.append(f'<p class="sec-lede">{esc(X["cycle_lede"])}</p>')
    H.append(f'<figure><div class="fig">{svg_cycle(X["cycle"], X["cycle_kpis"], X)}</div>'
             f'<figcaption><p>{md_links(esc(X["cycle_caption"]))}</p></figcaption></figure></section>')
    # ---- pilares
    notes = X.get('notas_estado', {})
    assert all(any(a['nombre'] == k for a in all_agents) for k in notes), notes
    H.append('<section id="pilares"><h2>Pilares y agentes</h2>')
    H.append(f'<p class="sec-lede">{esc(X["pillars_lede"])}</p>')
    H.append(legend_html(n_on).replace('class="legend"', 'class="legend legend-in"'))
    H.append('<div class="grid pillars">')
    for p in allp:
        H.append(f'<article class="card" id="p-{esc(p["_anchor"])}">')
        H.append(f'<h3><span class="swatch bg-{p["_slot"]}" aria-hidden="true"></span><span class="ttl">{esc(p["nombre"])}</span>'
                 + ('<span class="tag-new">NUEVO</span>' if p.get('nuevo') else '') + '</h3>')
        H.append(f'<p class="mission">{esc(p["mision"])}</p>')
        if p.get('dueno_humano'):
            H.append(f'<p class="owner">Dueño: {esc(p["dueno_humano"])}</p>')
        if p.get('chat'):
            H.append(f'<p class="owner">Chat: {esc(p["chat"])}</p>')
        H.append('<ul class="agents">')
        for a in p['agentes']:
            st = agent_state(a['nombre'], X)
            k = auton_key(a.get('autonomia'))
            g = rule_glyph_html() if st == 'rule' else glyph_html(k)
            status = {'on': f' · <span class="st-on">uno de los {n_on} encendidos antes de abril</span>',
                      'rule': ' · <span class="st-rule">regla de n8n sin IA</span>', 'later': ''}[st]
            ledh = '<span class="led" aria-hidden="true"></span>' if st == 'on' else ''
            io = ' → '.join(x for x in [a.get('disparador', ''), a.get('salida', '')] if x)
            H.append(f'<li class="ag-{st}">{g}<div><span class="nm">{esc(a["nombre"])}</span>{ledh} <span class="au">· {esc(AUTON[k][1])}{status}</span></div>'
                     f'<div class="ms">{esc(a.get("mision", ""))}</div>'
                     + (f'<div class="io">{esc(io)}</div>' if io else '')
                     + (f'<div class="io"><b>Se enciende:</b> {esc(a["se_enciende"])}</div>' if a.get('se_enciende') else '')
                     + (f'<div class="io st-note"><b>Pendiente de tu decisión:</b> {md_links(esc(notes[a["nombre"]]))}</div>' if a['nombre'] in notes else '') + '</li>')
        H.append('</ul><dl class="kv">')
        for lab, key in [('Personas', 'personas'), ('Herramientas', 'herramientas'), ('Notion', 'bases_notion'), ('KPIs', 'kpis'), ('Rituales', 'rituales')]:
            if p.get(key):
                H.append(f'<dt>{lab}</dt><dd>{kv_items(p[key])}</dd>')
        H.append('</dl></article>')
    H.append('</div></section>')
    # ---- orquestación
    O = F['orquestacion']
    H.append('<section id="agentes"><h2>Cómo trabajan los chats y los agentes</h2>')
    H.append(f'<p class="sec-lede">{esc(X["orq_lede"])}</p>')
    H.append('<div class="grid blocks">' + ''.join(
        f'<div class="card"><h3>{esc(lab)}</h3><p>{esc(txt)}</p></div>' for lab, txt in split_blocks(O['descripcion'], X['orq_bloques'], repl)) + '</div>')
    H.append(f'<figure><div class="fig">{svg_orq(X["orq"], X.get("aria_orq", ""))}</div>'
             f'<figcaption><p>{esc(X["orq_caption"])}</p></figcaption></figure>')
    auto_p = next((p for p in allp if p['_layer']), None)
    rename = X.get('rename', {})
    H.append('<div class="card wide"><h3>Tuberías por dentro</h3>'
             f'<p class="sub">{esc(X["pipes_list_lede"])} <a href="#p-{esc(auto_p["_anchor"])}">{esc(auto_p["nombre"])}</a>.</p><ul class="pipes-list">'
             + ''.join(f'<li><b>{esc(rename.get(c["nombre"], c["nombre"]))}</b>{esc(c["funcion"])}</li>' for c in F['capa_automatizacion'])
             + '</ul></div>')
    H.append('<div class="cols2"><div class="card"><h3>Reglas del sistema</h3><ol class="rules">'
             + ''.join(f'<li>{esc(r)}</li>' for r in O['reglas']) + '</ol></div>'
             '<div class="card"><h3>Principios</h3><ol class="rules">'
             + ''.join(f'<li>{esc(r)}</li>' for r in F['principios']) + '</ol></div></div></section>')
    # ---- flujos
    H.append('<section id="flujos"><h2>Flujos paso a paso</h2>')
    H.append(f'<p class="sec-lede">{esc(X["flows_lede"])}</p><div class="flows">')
    for i, fl in enumerate(F['flujos']):
        m = re.match(r'\s*(\d+)\.\s*(.*)$', fl['nombre'])
        num, name = (m.group(1), m.group(2)) if m else (str(i + 1), fl['nombre'])
        H.append(f'<details class="flow" id="flujo-{esc(num)}"{" open" if i == 0 else ""}><summary>'
                 f'<span class="fname">{esc(num)}. {esc(name)}</span><span class="cnt">{len(fl["pasos"])} pasos</span></summary>'
                 '<div class="tbl stackable"><table class="flow-t"><thead><tr><th>Paso</th><th>Actor</th><th>Acción</th><th>Herramienta</th></tr></thead><tbody>')
        for j, s in enumerate(fl['pasos']):
            H.append(f'<tr><td data-label="Paso">{j + 1}</td><td data-label="Actor"><b>{esc(s.get("actor", ""))}</b></td>'
                     f'<td data-label="Acción">{esc(s.get("accion", ""))}</td><td data-label="Herramienta">{esc(s.get("herramienta", ""))}</td></tr>')
        H.append('</tbody></table></div></details>')
    H.append('</div></section>')
    # ---- cerebro
    C = F['cerebro_notion']
    H.append('<section id="cerebro"><h2>El cerebro en Notion</h2>')
    H.append(f'<p class="sec-lede">{esc(X["brain_lede"])}</p><div class="grid brain">')
    for b in C['bases']:
        H.append(f'<article class="card"><h3>{esc(b["nombre"])}</h3><p>{esc(b.get("proposito", ""))}</p><dl class="kv">')
        if b.get('propiedades'):
            H.append(f'<dt>Campos</dt><dd>{kv_items(b["propiedades"])}</dd>')
        if b.get('relaciones'):
            H.append(f'<dt>Se conecta con</dt><dd>{kv_items(b["relaciones"])}</dd>')
        H.append('</dl>')
        fd = parse_feeds(b.get('quien_alimenta', ''))
        if fd:
            quien, cuando, desde, extra = fd
            H.append('<ul class="feeds">'
                     f'<li><b>Quién:</b> {esc(quien)}</li><li><b>Cada cuándo:</b> {esc(cuando)}</li><li><b>Desde dónde:</b> {esc(desde)}</li>'
                     + (f'<li class="extra">{esc(extra)}</li>' if extra else '') + '</ul>')
        elif b.get('quien_alimenta'):
            H.append(f'<ul class="feeds"><li>{esc(b["quien_alimenta"])}</li></ul>')
        H.append('</article>')
    H.append('</div>')
    if C.get('paginas'):
        items = []
        for pg in C['paginas']:
            mm = re.match(r'(.+?):\s+(.*)$', pg, re.S)
            if mm:
                items.append(f'<li><b>{esc(mm.group(1))}</b>{esc(cap(mm.group(2)))}</li>')
            else:
                items.append(f'<li><b>{esc(pg)}</b></li>')
        H.append(f'<div class="card wide"><h3>Páginas canónicas</h3><p class="sub">{esc(X["pages_lede"])}</p><ul class="pages">{"".join(items)}</ul></div>')
    H.append('<div class="cols2">')
    H.append('<div class="card"><h3>Tableros por rol</h3><ul class="rules">' + ''.join(f'<li>{esc(d)}</li>' for d in C.get('dashboards', [])) + '</ul></div>')
    if C.get('permisos'):
        H.append('<div class="card"><h3>Quién ve qué</h3><ul class="rules">' + ''.join(f'<li>{esc(d)}</li>' for d in C['permisos']) + '</ul></div>')
    H.append('</div></section>')
    # ---- lo que te falta
    pil_names = {p['id']: p['nombre'] for p in allp}
    H.append('<section id="falta"><h2>Lo que te falta</h2>')
    H.append(f'<p class="sec-lede">{esc(X["gaps_lede"])}</p>')
    cells = ''.join('<i></i>' if g.get('dominio') == 'desconocido' else '<i class="k"></i>' for g in gaps_sorted)
    H.append(f'<div class="meter"><div class="cells" aria-hidden="true">{cells}</div>'
             f'<span><b>{n_unknown} de {len(gaps)}</b> están fuera de tu terreno técnico ({round(100 * n_unknown / max(1, len(gaps)))}%). '
             f'El resto ({len(gaps) - n_unknown}) es de IA e ingeniería.</span></div>')
    plab = {'P0': 'P0 · antes de escalar', 'P1': 'P1 · próximo trimestre', 'P2': 'P2 · después'}
    btns = [f'<button type="button" data-f="all" aria-pressed="true">Todos ({len(gaps)})</button>']
    for pr in ['P0', 'P1', 'P2']:
        if prio_count.get(pr):
            btns.append(f'<button type="button" data-f="{pr}" aria-pressed="false">{plab[pr]} ({prio_count[pr]})</button>')
    H.append('<div class="filters" role="group" aria-label="Filtrar por prioridad">' + ''.join(btns) + '</div>')
    H.append('<div class="grid gaps">')
    for i, g in enumerate(gaps_sorted):
        n = i + 1
        pr = g.get('prioridad', 'P2')
        pn = pil_names.get(g.get('pilar', ''), g.get('pilar', ''))
        H.append(f'<article class="card gap-card" id="pc-{n}" data-p="{esc(pr)}"><div class="gap-head">'
                 f'<span class="pc-n"><span class="sr">Punto ciego </span>{n}</span><span class="prio prio-{esc(pr)}">{esc(pr)}</span>'
                 + (f'<span class="tag">{esc(pn)}</span>' if pn else '')
                 + ('<span class="tag">tu terreno</span>' if g.get('dominio') == 'conocido' else '') + '</div>')
        H.append(f'<h3>{esc(g["titulo"])}</h3><p>{esc(g["explicacion"])}</p>')
        if g.get('por_que_importa'):
            H.append(f'<p class="why">{esc(g["por_que_importa"])}</p>')
        H.append(f'<div class="first"><b>Primer paso</b>{esc(g["primer_paso"])}</div>')
        ei = ' · '.join(x for x in [f'esfuerzo {g["esfuerzo"]}' if g.get('esfuerzo') else '', f'impacto {g["impacto"]}' if g.get('impacto') else ''] if x)
        if ei:
            H.append(f'<span class="ei">{esc(ei)}</span>')
        if g.get('fuentes'):
            H.append(f'<p class="srcs">Fuentes: {link_list(g["fuentes"], official)}</p>')
        H.append('</article>')
    H.append('</div></section>')
    # ---- ruta
    R = F['roadmap']
    wk = [dur_weeks(r.get('duracion', '')) for r in R]
    assert all(w for w, _ in wk), wk
    tot = sum(w for w, _ in wk)
    H.append('<section id="ruta"><h2>Ruta de implementación</h2>')
    H.append(f'<p class="sec-lede">{esc(X["road_lede"])}</p>')
    acc = 0
    rows = []
    for r, (w, lab) in zip(R, wk):
        dates = re.search(r'\(([^)]+)\)', r.get('duracion', ''))
        tip = f'{r["fase"]}: {r.get("duracion", "")}'
        rows.append(f'<li><span class="gl"><b>{esc(r["fase"])}</b> <span class="gd">{esc(lab)}</span></span>'
                    f'<span class="track" title="{esc(tip)}"><span class="bar" style="left:{100 * acc / tot:.1f}%;width:{100 * w / tot:.1f}%"></span></span>'
                    f'<span class="sr">{esc(tip)}</span></li>')
        acc += w
    H.append('<ol class="gantt" aria-label="Duración de cada fase">' + ''.join(rows) + '</ol>')
    H.append(f'<div class="gantt-axis" aria-hidden="true"><span></span><div><span>{esc(X["gantt_inicio"])}</span><span>{esc(X["gantt_fin"])}</span></div></div>')
    H.append('<div class="grid phases">')
    for r in R:
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
    H.append(f'<p class="sec-lede">{esc(X["stack_lede"])}</p><div class="tbl stackable"><table class="stack-t"><thead><tr><th>Para qué</th><th>Herramienta</th><th>Alternativa</th><th>Costo aproximado</th></tr></thead><tbody>')
    for s in F['stack_recomendado']:
        head, note = split_cost(s.get('costo_aprox', ''))
        func = rename.get(s['funcion'], s['funcion'])
        H.append(f'<tr><td data-label="Para qué">{esc(func)}</td><td data-label="Herramienta"><b>{esc(s["herramienta"])}</b></td>'
                 f'<td data-label="Alternativa">{esc(s.get("alternativa", ""))}</td>'
                 f'<td class="cost" data-label="Costo aproximado">{esc(head)}' + (f'<small>{esc(note)}</small>' if note else '') + '</td></tr>')
    H.append('</tbody></table></div></section>')
    # ---- riesgos
    H.append('<section id="riesgos"><h2>Riesgos y cómo cubrirte</h2><div class="tbl stackable"><table class="risk-t"><thead><tr><th>Riesgo</th><th>Mitigación</th></tr></thead><tbody>')
    for r in F['riesgos']:
        H.append(f'<tr><td data-label="Riesgo">{esc(r["riesgo"])}</td><td data-label="Mitigación">{esc(r["mitigacion"])}</td></tr>')
    H.append('</tbody></table></div></section>')
    # ---- preguntas
    H.append('<section id="preguntas"><h2>Preguntas para afinar</h2>')
    qx = X.get('preguntas_extra', [])
    H.append(f'<p class="sec-lede">{esc(X["q_lede"])}</p><ol class="qs">' + ''.join(f'<li>{esc(q)}</li>' for q in F['preguntas_abiertas'])
             + ''.join(f'<li id="{esc(q["id"])}">{esc(q["texto"])}</li>' for q in qx) + '</ol></section>')
    # ---- qué cambió
    H.append('<section id="cambios"><h2>Qué cambió tras la crítica</h2>')
    H.append(f'<p class="sec-lede">{esc(X["changes_lede"])}</p><div class="grid changes">')
    for gr in X['cambios_grupos']:
        H.append(f'<div class="card"><h3>{esc(gr["titulo"])}</h3><ul>' + ''.join(f'<li>{esc(it)}</li>' for it in gr['items']) + '</ul></div>')
    H.append('</div></section>')
    # ---- fuentes
    V = X.get('verificaciones', [])
    H.append('<section id="fuentes"><h2>Fuentes y datos verificados</h2>')
    H.append(f'<p class="sec-lede">{esc(X["src_lede"])}</p><ul class="src">')
    lab = {'correcta': 'Correcto', 'matizar': 'Con matices', 'incorrecta': 'Corregido', 'no_verificable': 'Sin confirmar'}
    for v in V:
        st = v.get('estado', 'no_verificable')
        af = v.get('afirmacion', '')
        mm = re.match(r'^([^:]{2,80}):\s+(.*)$', af, re.S)
        loc, claim = (mm.group(1), mm.group(2)) if mm else ('', af)
        corr = v.get('correccion', '')
        for a, b in v.get('reemplazos', {}).items():
            corr = corr.replace(a, b)
        urls = [u for u in re.split(r'\s*\|\s*', v.get('fuente', '') or '') if u.strip().startswith('http')]
        body = []
        ov = v.get('pc_titulo')
        for t in (ov or {}).values():
            assert t in num_by_title, t
        if loc:
            body.append(f'<p class="loc">{pc_links(esc(loc), ov)}</p>')
        if st in ('correcta', 'no_verificable'):
            body.append(f'<p>{pc_links(esc(cap(claim)), ov)}</p>')
            if corr:
                body.append(f'<p class="conf">{esc(corr)}</p>')
        else:
            body.append(f'<p><span class="lbl">Dato vigente:</span> {esc(corr)}</p>')
            if v.get('aplicado'):
                body.append(f'<p><span class="lbl">Quedó así en el diseño:</span> {esc(v["aplicado"])}</p>')
            body.append(f'<p class="old"><span class="lbl">Antes decía:</span> {pc_links(esc(claim), ov)}</p>')
        if urls:
            body.append(f'<p class="srcs">Fuentes: {link_list(urls, official)}</p>')
        H.append(f'<li><span class="st st-{esc(st)}">{esc(lab.get(st, st))}</span><div class="body">{"".join(body)}</div></li>')
    H.append('</ul></section></main>')
    H.append(f'<footer class="wrap"><p>{esc(X["footer"])}</p></footer>')
    H.append("""<script>
(function(){
  var bs = document.querySelectorAll('.filters button');
  var cards = document.querySelectorAll('.gap-card');
  function apply(f){
    bs.forEach(function(o){ o.setAttribute('aria-pressed', o.getAttribute('data-f') === f ? 'true' : 'false'); });
    cards.forEach(function(c){ c.hidden = !(f === 'all' || c.getAttribute('data-p') === f); });
  }
  bs.forEach(function(b){ b.addEventListener('click', function(){ apply(b.getAttribute('data-f')); }); });
  function onHash(){
    var id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    if (el.classList.contains('gap-card') && el.hidden) { apply('all'); el.scrollIntoView(); }
    if (el.tagName === 'DETAILS') el.open = true;
  }
  window.addEventListener('hashchange', onHash);
  // también cuando el enlace apunta al hash que ya está puesto (no hay hashchange)
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    var el = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    if (!el) return;
    if (el.classList.contains('gap-card') && el.hidden) apply('all');
    if (el.tagName === 'DETAILS') el.open = true;
  });
  var toc = document.querySelector('nav.toc');
  function tocH(){ if (toc) document.documentElement.style.setProperty('--toc-h', toc.offsetHeight + 'px'); }
  tocH();
  window.addEventListener('resize', tocH);
  if (window.ResizeObserver && toc) new ResizeObserver(tocH).observe(toc);
  var tul = toc && toc.querySelector('ul');
  function tocEnd(){ toc.classList.toggle('at-end', tul.scrollLeft + tul.clientWidth >= tul.scrollWidth - 2); }
  if (tul) { tul.addEventListener('scroll', tocEnd, { passive: true }); window.addEventListener('resize', tocEnd); tocEnd(); }
  onHash();
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
        # Las verificaciones salen de data/verificacion.json; textos.json solo agrega
        # ajustes de presentación por índice (verificaciones_extra).
        X['verificaciones'] = json.load(open(sys.argv[4]))['verificaciones']
        for i, extra in X.get('verificaciones_extra', {}).items():
            X['verificaciones'][int(i)].update(extra)
    html = build(F, X)
    open(sys.argv[3], 'w').write(html)
    for w in gen_page.WARN:
        print('AVISO:', w)
    print('written', sys.argv[3], len(html), 'bytes;', len(gen_page.WARN), 'avisos')
