<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TNBC Predictor v7 — HCM | Abudala Sualé</title>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
<style>
/*
 * ================================================================
 *  TNBC PREDICTOR — HCM / UEM — VERSÃO 7.0
 *  © 2026 Abudala Sualé — Todos os direitos reservados
 *  Universidade Eduardo Mondlane — Faculdade de Medicina
 *  Hospital Central de Maputo
 * ================================================================
 */

:root{
  /* ── Fundos ── */
  --bg:#F0EDE8;--bg2:#E8E4DE;
  --s:#FFFFFF;--s2:#F8F6F2;--s3:#F0EDE8;
  /* ── Bordas ── */
  --b:#DDD8CF;--bs:#C4BCB0;--bx:#A89D90;
  /* ── Texto ── */
  --t:#1C1814;--m:#5A5248;--f:#968C80;
  /* ── Verde principal ── */
  --g:#1A6B3C;--gd:#135230;--g2:#2A8B54;
  --gl:#E6F2EB;--gll:#C8E4D4;
  /* ── Ouro ── */
  --gold:#A87B30;--goldd:#C49840;
  /* ── Accent azul ── */
  --ac:#1B3F5C;--acl:#E4EDF5;
  /* ── Perigo ── */
  --dn:#7A1F1F;--dm:#C0392B;--dl:#FDECEA;
  /* ── Aviso ── */
  --wn:#7A4E08;--wm:#BE6B15;--wl:#FBF0E0;
  /* ── OK ── */
  --ok:#1A6B3C;--om:#2D8B58;--ol:#E4F2EB;
  /* ── Info ── */
  --in:#1B3F5C;--il:#E4EDF5;
  /* ── Tokens layout ── */
  --r:14px;--rs:8px;--rx:4px;
  --sh:0 1px 3px rgba(20,18,14,.07),0 2px 8px rgba(20,18,14,.05);
  --sh2:0 2px 8px rgba(20,18,14,.10),0 8px 28px rgba(20,18,14,.08);
  --sh3:0 0 0 3px rgba(26,107,60,.14);
}

/* ===== MODO ESCURO ===== */
[data-theme="dark"]{
  --bg:#0E110D;--bg2:#141810;
  --s:#1A1F18;--s2:#21271E;--s3:#1A1F18;
  --b:#2A3328;--bs:#38453A;--bx:#485850;
  --t:#E4EAE0;--m:#90A490;--f:#58705A;
  --g:#34D278;--gd:#28B860;--g2:#3EE882;
  --gl:#0C2014;--gll:#142C1C;
  --gold:#F0C040;--goldd:#D4A830;
  --ac:#5AB0E0;--acl:#0C1E2C;
  --dn:#F09090;--dm:#E04040;--dl:#2A0C0C;
  --wn:#F0A840;--wm:#D08020;--wl:#281808;
  --ok:#34D278;--om:#28B860;--ol:#0C2014;
  --in:#5AB0E0;--il:#0C1C2C;
  --sh:0 1px 4px rgba(0,0,0,.35),0 2px 12px rgba(0,0,0,.25);
  --sh2:0 2px 8px rgba(0,0,0,.45),0 8px 28px rgba(0,0,0,.35);
}
[data-theme="dark"] body::before{
  background-image:
    radial-gradient(circle at 15% 20%, rgba(60,200,116,.08) 0%, transparent 50%),
    radial-gradient(circle at 85% 80%, rgba(91,168,216,.06) 0%, transparent 50%);
}
[data-theme="dark"] header{
  background:linear-gradient(135deg,#0D3D22 0%,#1A6B3C 45%,#0F4F2C 100%);
  border-bottom:none;
  box-shadow:0 2px 20px rgba(0,0,0,.25);
  position:sticky;top:0;z-index:100;
}
[data-theme="dark"] header{
  background:linear-gradient(135deg,#06160D 0%,#0D2C1A 45%,#091F12 100%);
}



*{box-sizing:border-box;margin:0;padding:0}

body{
  font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;
  background:var(--bg);
  color:var(--t);
  font-size:14px;
  line-height:1.65;
  min-height:100vh;
  position:relative;
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
}

/* =============================================
   FUNDO DECORATIVO — padrão médico subtil
   ============================================= */
body::before{
  content:'';
  position:fixed;
  inset:0;
  background-image:
    radial-gradient(circle at 15% 20%, rgba(26,107,60,.06) 0%, transparent 50%),
    radial-gradient(circle at 85% 80%, rgba(27,63,92,.05) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(184,154,62,.03) 0%, transparent 60%);
  pointer-events:none;
  z-index:0;
}

/* SVG molecular background */
body::after{
  content:'';
  position:fixed;
  inset:0;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Ccircle cx='20' cy='20' r='3' fill='none' stroke='%231A6B3C' stroke-width='.4' opacity='.18'/%3E%3Ccircle cx='80' cy='60' r='5' fill='none' stroke='%231B3F5C' stroke-width='.4' opacity='.15'/%3E%3Ccircle cx='60' cy='100' r='2.5' fill='none' stroke='%231A6B3C' stroke-width='.4' opacity='.12'/%3E%3Cline x1='20' y1='20' x2='80' y2='60' stroke='%231A6B3C' stroke-width='.3' opacity='.1'/%3E%3Cline x1='80' y1='60' x2='60' y2='100' stroke='%231B3F5C' stroke-width='.3' opacity='.08'/%3E%3Ccircle cx='100' cy='20' r='4' fill='none' stroke='%23B89A3E' stroke-width='.4' opacity='.12'/%3E%3Cline x1='100' y1='20' x2='80' y2='60' stroke='%23B89A3E' stroke-width='.3' opacity='.08'/%3E%3C/svg%3E");
  pointer-events:none;
  z-index:0;
  opacity:.6;
}

header,main,footer,.tabs{position:relative;z-index:1}

@media print{
  .noprint{display:none!important}
  body::before,body::after{display:none}
  body{background:#fff}
}

/* =============================================
   HEADER
   ============================================= */
header{
  background:linear-gradient(135deg,#0F3D22 0%,#1A6B3C 60%,#1A4A6B 100%);
  border-bottom:3px solid var(--gold);
  position:relative;
  overflow:hidden;
}

header::before{
  content:'';
  position:absolute;
  inset:0;
  background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Ccircle cx='150' cy='50' r='60' fill='none' stroke='rgba(255,255,255,.05)' stroke-width='1'/%3E%3Ccircle cx='50' cy='150' r='40' fill='none' stroke='rgba(255,255,255,.04)' stroke-width='1'/%3E%3Ccircle cx='150' cy='50' r='100' fill='none' stroke='rgba(255,255,255,.03)' stroke-width='1'/%3E%3C/svg%3E") no-repeat right center;
}

.hbar{
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:1rem 2rem;
  flex-wrap:wrap;
  gap:1rem;
  position:relative;
  max-width:1280px;
  margin:0 auto;
}

.hlogo{height:68px;width:auto;filter:brightness(0) invert(1);opacity:.92}

.hcenter{flex:1;text-align:center;padding:0 1.5rem}
.htitle{
  font-family:'Instrument Serif',Georgia,serif;
  font-size:23px;
  font-weight:400;
  color:#fff;
  letter-spacing:.2px;
  text-shadow:0 1px 12px rgba(0,0,0,.4);
}
.hsub{font-size:11px;color:rgba(255,255,255,.65);margin-top:3px;letter-spacing:.04em}

.hactions{display:flex;gap:8px;flex-wrap:wrap}
.btn-hdr{
  background:rgba(255,255,255,.12);
  border:1px solid rgba(255,255,255,.22);
  border-radius:var(--rs);
  padding:7px 14px;
  font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;
  font-size:11px;
  font-weight:500;
  color:#fff;
  cursor:pointer;
  transition:all .2s;
  white-space:nowrap;
  backdrop-filter:blur(4px);
}
.btn-hdr:hover{background:rgba(255,255,255,.24);border-color:rgba(255,255,255,.4)}
.btn-hdr-gold{
  background:rgba(184,154,62,.25);
  border-color:rgba(184,154,62,.5);
  color:var(--gold);
}
.btn-hdr-gold:hover{background:rgba(184,154,62,.4)}

.hmeta{
  background:rgba(0,0,0,.18);
  backdrop-filter:blur(8px);
  -webkit-backdrop-filter:blur(8px);
  padding:.45rem 2rem;
  display:flex;
  gap:2rem;
  flex-wrap:wrap;
  border-top:.5px solid rgba(255,255,255,.12);
  max-width:100%;
}
.mi{font-size:11px;color:rgba(255,255,255,.6)}
.mi strong{color:rgba(255,255,255,.9);font-weight:500;margin-right:4px}

/* =============================================
   TABS
   ============================================= */
.tabs{
  max-width:1160px;
  margin:0 auto;
  padding:1.25rem 1.5rem .5rem;
  display:flex;
  gap:6px;
  flex-wrap:wrap;
}
.tb{
  padding:7px 15px;
  border-radius:var(--rs);
  border:.5px solid var(--bs);
  background:var(--s);
  font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;
  font-size:12px;
  font-weight:500;
  color:var(--m);
  cursor:pointer;
  transition:all .2s;
  white-space:nowrap;
  box-shadow:var(--sh);
}
.tb:hover{border-color:var(--g);color:var(--g)}
.tb.on{
  background:linear-gradient(135deg,var(--g),var(--g2));
  color:#fff;
  border-color:var(--g);
  box-shadow:0 2px 8px rgba(26,107,60,.3);
}
.tc{display:none}
.tc.on{display:block}

/* =============================================
   LAYOUT
   ============================================= */
main{max-width:1160px;margin:0 auto;padding:.75rem 1.5rem 2rem}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:1.25rem}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.25rem}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.col{display:flex;flex-direction:column;gap:1.25rem}

/* =============================================
   CARDS
   ============================================= */
.card{
  background:var(--s);
  border:.5px solid var(--b);
  border-radius:var(--r);
  padding:1.25rem;
  box-shadow:var(--sh);
  transition:box-shadow .2s;
}
.card:hover{box-shadow:var(--sh2)}

.card-accent{border-left:3px solid var(--g)}
.card-gold{border-top:2px solid var(--gold)}
.card-danger{border-left:3px solid var(--dm)}
.card-info{border-left:3px solid var(--ac)}

.ct{
  font-size:10px;
  font-weight:600;
  letter-spacing:.1em;
  text-transform:uppercase;
  color:var(--m);
  margin-bottom:1rem;
  padding-bottom:.65rem;
  border-bottom:.5px solid var(--b);
  display:flex;
  align-items:center;
  gap:8px;
}
.ct-icon{
  width:20px;height:20px;
  border-radius:5px;
  display:flex;align-items:center;justify-content:center;
  font-size:11px;
}
.cti-g{background:var(--gl);color:var(--g)}
.cti-r{background:var(--dl);color:var(--dm)}
.cti-b{background:var(--il);color:var(--ac)}
.cti-w{background:var(--wl);color:var(--wm)}
.cti-gold{background:#FBF5E6;color:var(--gold)}

/* =============================================
   FIELDS
   ============================================= */
.f{margin-bottom:.8rem}
.f:last-child{margin-bottom:0}
.f label{
  display:flex;justify-content:space-between;align-items:center;
  font-size:12px;color:var(--m);margin-bottom:4px;font-weight:500;
}
.f label .rt{font-size:10px;color:var(--f);font-weight:400;font-style:italic}
.f input,.f select{
  width:100%;padding:8px 11px;
  border:.5px solid var(--bs);
  border-radius:var(--rs);
  font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:13px;color:var(--t);
  background:var(--s);
  transition:border-color .15s,box-shadow .15s,background .15s;
  -webkit-appearance:none;appearance:none;
}
.f input:focus,.f select:focus{
  outline:none;border-color:var(--g);
  box-shadow:0 0 0 3px rgba(26,107,60,.12);
  background:var(--gl);
}
.f input[type=range]{padding:4px 0;border:none;background:transparent;accent-color:var(--g)}
.fg2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.fg3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}

/* =============================================
   BUTTONS
   ============================================= */
.btn-g{
  background:linear-gradient(135deg,var(--g),var(--g2));
  color:#fff;border:none;border-radius:var(--rs);
  padding:9px 20px;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:13px;font-weight:500;
  cursor:pointer;transition:all .2s;
  box-shadow:0 2px 8px rgba(26,107,60,.25);
}
.btn-g:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(26,107,60,.35)}
.btn-go{
  background:transparent;border:1px solid var(--g);border-radius:var(--rs);
  padding:9px 20px;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:13px;font-weight:500;
  color:var(--g);cursor:pointer;transition:all .2s;
}
.btn-go:hover{background:var(--gl)}
.btn-sm{
  background:var(--s2);border:.5px solid var(--bs);border-radius:6px;
  padding:5px 12px;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:11px;font-weight:500;
  color:var(--m);cursor:pointer;transition:all .15s;
}
.btn-sm:hover{background:var(--gl);color:var(--g);border-color:var(--g)}
.btnadd{
  display:flex;align-items:center;gap:8px;
  background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;
  border:none;border-radius:var(--rs);
  padding:11px 20px;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:13px;font-weight:500;
  cursor:pointer;width:100%;justify-content:center;margin-top:.5rem;
  box-shadow:0 2px 8px rgba(26,107,60,.25);transition:all .2s;
}
.btnadd:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(26,107,60,.35)}

/* =============================================
   SEMÁFORO
   ============================================= */
.sem{
  display:flex;align-items:center;gap:14px;
  padding:1rem 1.25rem;
  border-radius:var(--rs);
  margin-bottom:1rem;
  border:.5px solid var(--b);
  background:linear-gradient(135deg,var(--s2),var(--s));
}
.sll{display:flex;flex-direction:column;gap:5px}
.sl{
  width:18px;height:18px;border-radius:50%;
  background:var(--b);
  transition:background .4s,box-shadow .4s;
}
.sl.ar{background:#CB4335;box-shadow:0 0 12px rgba(203,67,53,.6)}
.sl.ay{background:#CA6F1E;box-shadow:0 0 12px rgba(202,111,30,.6)}
.sl.ag{background:#27AE60;box-shadow:0 0 12px rgba(39,174,96,.6)}

/* =============================================
   SCORES
   ============================================= */
.sg{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:1rem}
.sb{
  background:var(--s2);border-radius:10px;padding:1rem;
  border:.5px solid var(--b);
  position:relative;overflow:hidden;
}
.sb::after{
  content:'';
  position:absolute;
  top:0;right:0;
  width:60px;height:60px;
  background:radial-gradient(circle at top right,rgba(26,107,60,.05),transparent);
}
.snum{
  font-family:'Instrument Serif',Georgia,serif;font-size:36px;line-height:1;
  margin-bottom:8px;transition:color .3s;
}
.mtr{
  height:6px;background:var(--b);border-radius:4px;
  overflow:hidden;margin-bottom:8px;
}
.mf{height:100%;border-radius:4px;transition:width .5s cubic-bezier(.4,0,.2,1),background .3s}

/* =============================================
   BADGES
   ============================================= */
.badge{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:600;padding:3px 10px;border-radius:20px}
.bd{background:var(--dl);color:var(--dn)}
.bw{background:var(--wl);color:var(--wn)}
.bo{background:var(--ol);color:var(--ok)}
.bi{background:var(--il);color:var(--in)}
.bg_{background:var(--gl);color:var(--g)}
.bgold{background:#FBF5E6;color:var(--goldd)}

/* =============================================
   URGÊNCIA BAR
   ============================================= */
.urgbar{
  height:12px;
  background:linear-gradient(to right,#27AE60 0%,#27AE60 33%,#CA6F1E 33%,#CA6F1E 66%,#CB4335 66%,#CB4335 100%);
  border-radius:6px;margin:8px 0;position:relative;
}
.urgmark{
  position:absolute;top:-5px;
  width:22px;height:22px;
  background:#fff;border:2.5px solid var(--t);border-radius:50%;
  transform:translateX(-50%);
  transition:left .5s cubic-bezier(.4,0,.2,1);
  box-shadow:var(--sh);
}
.urglabs{display:flex;justify-content:space-between;font-size:10px;color:var(--f)}

/* =============================================
   FACTORES DE RISCO — EXPANDÍVEL ENRIQUECIDO
   ============================================= */
.fr-item{
  border:.5px solid var(--b);
  border-radius:10px;
  margin-bottom:8px;
  overflow:hidden;
  transition:box-shadow .2s;
}
.fr-item:hover{box-shadow:var(--sh)}
.fr-item:last-child{margin-bottom:0}

.fr-header{
  display:flex;align-items:center;gap:10px;
  padding:10px 14px;cursor:pointer;
  background:var(--s);
  transition:background .15s;
  user-select:none;
}
.fr-header:hover{background:var(--s2)}

.fr-impact{
  width:8px;height:8px;border-radius:50%;flex-shrink:0;
}
.fr-high{background:var(--dm)}
.fr-med{background:var(--wm)}
.fr-low{background:var(--om)}

.fr-name{font-size:13px;font-weight:500;flex:1}
.fr-evidence{font-size:10px;font-weight:600;padding:2px 8px;border-radius:12px;white-space:nowrap}
.ev-A{background:#E4F0EB;color:#0F3D22}
.ev-B{background:#E4EDF5;color:#0F2D42}
.ev-C{background:#FBF0E0;color:#4A2A00}
.fr-pts{font-size:12px;font-weight:700;color:var(--g);min-width:36px;text-align:right}
.fr-arrow{font-size:12px;color:var(--f);transition:transform .2s;flex-shrink:0}
.fr-arrow.open{transform:rotate(180deg)}

.fr-body{
  display:none;
  padding:0 14px 14px;
  background:var(--s2);
  border-top:.5px solid var(--b);
}
.fr-body.show{display:block}

.fr-explanation{font-size:12px;color:var(--m);line-height:1.7;margin-bottom:8px;padding-top:10px}
.fr-patient-context{
  background:var(--gl);border:.5px solid rgba(26,107,60,.2);
  border-radius:7px;padding:8px 12px;font-size:12px;color:var(--g);
  margin-bottom:8px;line-height:1.6;
}
.fr-patient-context strong{font-weight:600;display:block;margin-bottom:2px}
.fr-ref{font-size:10px;color:var(--f);font-style:italic;margin-top:4px}
.fr-explain-btn{
  font-size:11px;background:var(--il);color:var(--ac);
  border:.5px solid rgba(27,63,92,.2);border-radius:6px;
  padding:4px 10px;cursor:pointer;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;
  transition:all .15s;
}
.fr-explain-btn:hover{background:var(--ac);color:#fff}

/* =============================================
   CONDUTA ENRIQUECIDA
   ============================================= */
.cd-item{
  border:.5px solid var(--b);border-radius:10px;
  margin-bottom:8px;overflow:hidden;
}
.cd-item:last-child{margin-bottom:0}

.cd-header{
  display:flex;align-items:center;gap:10px;padding:10px 14px;
  background:var(--s);cursor:pointer;
}
.cd-header:hover{background:var(--s2)}

.cd-check{
  width:20px;height:20px;border-radius:5px;
  border:2px solid var(--bs);background:transparent;
  display:flex;align-items:center;justify-content:center;
  cursor:pointer;flex-shrink:0;transition:all .2s;
}
.cd-check.done{background:var(--g);border-color:var(--g)}
.cd-check.done::after{content:'✓';color:#fff;font-size:11px;font-weight:700}

.cd-urgency{
  font-size:9px;font-weight:700;padding:2px 8px;border-radius:12px;
  text-transform:uppercase;letter-spacing:.06em;white-space:nowrap;
}
.urg-imediato{background:#FAE8E8;color:#7A1F1F}
.urg-urgente{background:#FBF0E0;color:#6B4A0E}
.urg-eletivo{background:#E4F0EB;color:#0F3D22}
.urg-continuo{background:#E4EDF5;color:#0F2D42}

.cd-text{font-size:13px;font-weight:500;flex:1}
.cd-arrow{font-size:12px;color:var(--f);transition:transform .2s;flex-shrink:0}
.cd-arrow.open{transform:rotate(180deg)}

.cd-body{display:none;padding:0 14px 14px;background:var(--s2);border-top:.5px solid var(--b)}
.cd-body.show{display:block}
.cd-detail{font-size:12px;color:var(--m);line-height:1.7;padding-top:10px;margin-bottom:8px}
.cd-protocol{
  background:#0F3D22;color:#A8D8BC;
  border-radius:7px;padding:10px 14px;
  font-family:'JetBrains Mono','SF Mono','Fira Code',Menlo,monospace;font-size:11px;line-height:1.8;
  margin-bottom:8px;
}
.cd-protocol-title{color:#4CD691;font-weight:500;margin-bottom:4px;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:11px}
.cd-guideline{font-size:10px;color:var(--f);font-style:italic}

/* =============================================
   ASSISTENTE IA
   ============================================= */
.ai-chat{
  display:flex;flex-direction:column;
  height:360px;
  border:.5px solid var(--b);border-radius:10px;
  overflow:hidden;background:var(--s);
}
.ai-messages{
  flex:1;overflow-y:auto;padding:1rem;
  display:flex;flex-direction:column;gap:10px;
  background:var(--s2);
}
.ai-msg{display:flex;gap:8px;align-items:flex-start}
.ai-msg.user{flex-direction:row-reverse}
.ai-avatar{
  width:28px;height:28px;border-radius:50%;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  font-size:12px;font-weight:600;
}
.ai-av-ai{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff}
.ai-av-user{background:var(--ac);color:#fff}
.ai-bubble{
  max-width:80%;padding:8px 12px;border-radius:10px;
  font-size:12px;line-height:1.6;
}
.ai-msg.ai .ai-bubble{background:var(--s);border:.5px solid var(--b);color:var(--t)}
.ai-msg.user .ai-bubble{background:linear-gradient(135deg,var(--g),var(--g2));color:#fff}
.ai-typing{display:flex;gap:4px;padding:12px 16px;align-items:center}
.ai-dot{width:6px;height:6px;border-radius:50%;background:var(--f);animation:blink 1.2s infinite}
.ai-dot:nth-child(2){animation-delay:.2s}
.ai-dot:nth-child(3){animation-delay:.4s}
@keyframes blink{0%,80%,100%{opacity:.3}40%{opacity:1}}
.ai-input-row{display:flex;gap:8px;padding:.75rem;border-top:.5px solid var(--b);background:var(--s)}
.ai-input{
  flex:1;padding:8px 12px;border:.5px solid var(--bs);border-radius:var(--rs);
  font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:13px;
  background:var(--s2);color:var(--t);
}
.ai-input:focus{outline:none;border-color:var(--g)}
.ai-send{
  background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;
  border:none;border-radius:var(--rs);padding:8px 16px;
  font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:12px;font-weight:500;cursor:pointer;
}
.ai-quick{display:flex;gap:6px;flex-wrap:wrap;padding:.5rem .75rem;border-top:.5px solid var(--b);background:var(--s)}
.ai-quick-btn{
  background:var(--gl);color:var(--g);border:.5px solid rgba(26,107,60,.2);
  border-radius:16px;padding:4px 10px;font-size:11px;cursor:pointer;
  font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;transition:all .15s;
}
.ai-quick-btn:hover{background:var(--g);color:#fff}

/* =============================================
   RELATÓRIO CLÍNICO
   ============================================= */
.report-box{
  font-family:'JetBrains Mono','SF Mono','Fira Code',Menlo,monospace;
  font-size:12px;line-height:1.8;
  background:var(--s2);
  border:.5px solid var(--b);
  border-radius:10px;
  padding:1.25rem;
  color:var(--t);
  white-space:pre-wrap;
  min-height:200px;
}
.report-header-text{color:var(--g);font-weight:500}

/* =============================================
   SEGUIMENTO
   ============================================= */
.follow-item{
  display:flex;align-items:center;gap:12px;
  padding:10px 14px;
  border:.5px solid var(--b);border-radius:10px;
  margin-bottom:8px;background:var(--s);
  transition:all .2s;
}
.follow-item:hover{box-shadow:var(--sh)}
.follow-date{
  font-family:'Instrument Serif',Georgia,serif;font-size:18px;
  color:var(--g);min-width:60px;text-align:center;
}
.follow-month{font-size:10px;color:var(--m);text-align:center;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.follow-info{flex:1}
.follow-type{font-size:13px;font-weight:500}
.follow-detail{font-size:11px;color:var(--m);margin-top:1px}

/* =============================================
   ENSAIOS CLÍNICOS
   ============================================= */
.trial-item{
  border:.5px solid var(--b);border-radius:10px;
  padding:1rem;margin-bottom:8px;
  background:var(--s);transition:all .2s;
}
.trial-item:hover{box-shadow:var(--sh);border-color:var(--bs)}
.trial-header{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;margin-bottom:8px}
.trial-name{font-size:13px;font-weight:600;color:var(--t)}
.trial-status{font-size:10px;font-weight:600;padding:2px 8px;border-radius:12px}
.ts-open{background:var(--gl);color:var(--g)}
.ts-closed{background:var(--dl);color:var(--dn)}
.ts-review{background:var(--wl);color:var(--wn)}
.trial-criteria{font-size:12px;color:var(--m);line-height:1.6;margin-bottom:8px}
.trial-match{
  display:flex;align-items:center;gap:6px;
  font-size:12px;font-weight:600;
}
.trial-match.yes{color:var(--g)}
.trial-match.partial{color:var(--wm)}
.trial-match.no{color:var(--dn)}

/* =============================================
   MISC
   ============================================= */
.disc{background:var(--wl);border:.5px solid #E8C080;border-radius:var(--rs);padding:10px 14px;font-size:11px;color:var(--wn);line-height:1.6;margin-top:1rem}
.infonote{background:var(--il);border:.5px solid #A0BCDA;border-radius:var(--rs);padding:10px 14px;font-size:12px;color:var(--in);line-height:1.6;margin-bottom:1rem}
.gnote{background:var(--gl);border:.5px solid rgba(26,107,60,.2);border-radius:var(--rs);padding:10px 14px;font-size:12px;color:var(--g);line-height:1.6;margin-bottom:1rem}
.gnote strong{font-weight:600;display:block;margin-bottom:2px}
.pnote{background:var(--wl);border:.5px solid #E0B060;border-radius:var(--rs);padding:10px 14px;font-size:12px;color:var(--wn);line-height:1.6}
.pnote strong{font-weight:600;display:block;margin-bottom:2px}

.sc{background:var(--s);border:.5px solid var(--b);border-radius:10px;padding:1rem;text-align:center;box-shadow:var(--sh)}
.scc{font-family:'Instrument Serif',Georgia,serif;font-size:28px}
.scl{font-size:10px;color:var(--m);text-transform:uppercase;letter-spacing:.07em;font-weight:600;margin-top:2px}

.nomo-row{display:flex;align-items:center;gap:8px;margin-bottom:6px}
.nomo-label{font-size:11px;color:var(--m);width:130px;flex-shrink:0;text-align:right}
.nomo-track{flex:1;height:8px;background:var(--b);border-radius:4px;position:relative;overflow:visible}
.nomo-fill{height:100%;border-radius:4px;transition:width .4s}
.nomo-marker{position:absolute;top:-4px;width:16px;height:16px;background:#fff;border:2px solid var(--g);border-radius:50%;transform:translateX(-50%);transition:left .4s;z-index:2;box-shadow:var(--sh)}
.nomo-pts{font-size:11px;font-weight:600;color:var(--g);width:36px;text-align:left;flex-shrink:0}

.shap-bar{display:flex;align-items:center;gap:8px;margin-bottom:5px}
.shap-lbl{font-size:11px;color:var(--m);width:140px;text-align:right;flex-shrink:0}
.shap-track{flex:1;height:20px;background:var(--b);border-radius:4px;position:relative;overflow:hidden}
.shap-pos{position:absolute;left:50%;height:100%;background:rgba(184,50,50,.65);border-radius:0 4px 4px 0;transition:width .4s}
.shap-neg{position:absolute;right:50%;height:100%;background:rgba(39,174,96,.65);border-radius:4px 0 0 4px;transition:width .4s}
.shap-zero{position:absolute;left:50%;top:0;width:1px;height:100%;background:var(--bs)}
.shap-val{font-size:11px;font-weight:600;width:36px;flex-shrink:0}

.urgbar2{height:12px;background:linear-gradient(to right,#27AE60,#CA6F1E,#CB4335);border-radius:6px;margin:8px 0;position:relative}
.urgmark2{position:absolute;top:-5px;width:22px;height:22px;background:#fff;border:2.5px solid var(--t);border-radius:50%;transform:translateX(-50%);transition:left .5s;box-shadow:var(--sh)}
.urglabs2{display:flex;justify-content:space-between;font-size:10px;color:var(--f)}

.plist{display:flex;flex-direction:column;gap:8px;max-height:340px;overflow-y:auto}
.pi{background:var(--s2);border:.5px solid var(--b);border-radius:10px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;gap:8px;transition:all .2s}
.pi:hover{border-color:var(--bs)}
.pdel{background:none;border:none;color:var(--f);cursor:pointer;font-size:16px;padding:2px 6px;border-radius:4px}
.pdel:hover{color:var(--dn);background:var(--dl)}
.empty{text-align:center;padding:2rem;color:var(--f);font-size:13px;border:.5px dashed var(--bs);border-radius:10px}

.dt{width:100%;border-collapse:collapse;font-size:12px}
.dt th{text-align:left;font-size:10px;text-transform:uppercase;letter-spacing:.07em;color:var(--m);padding:6px 8px;border-bottom:.5px solid var(--b);font-weight:600;background:var(--s2)}
.dt td{padding:7px 8px;border-bottom:.5px solid var(--b);vertical-align:middle}
.dt tr:last-child td{border-bottom:none}
.dt tr:hover td{background:var(--s2)}

/* Modal */
.mo{display:none;position:fixed;inset:0;background:rgba(10,16,10,.5);z-index:1000;align-items:center;justify-content:center;backdrop-filter:blur(2px)}
.mo.on{display:flex}
.md{background:var(--s);border-radius:var(--r);padding:1.75rem;max-width:540px;width:90%;box-shadow:0 16px 48px rgba(0,0,0,.2)}
.md h3{font-family:'Instrument Serif',Georgia,serif;font-size:20px;font-weight:400;margin-bottom:.5rem;color:var(--g)}
.md p{font-size:13px;line-height:1.7;color:var(--m);margin-bottom:.75rem}
.mclose{margin-top:1rem;background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;border:none;border-radius:var(--rs);padding:9px 22px;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:13px;font-weight:500;cursor:pointer}

footer{max-width:1160px;margin:0 auto 2rem;padding:0 1.5rem;position:relative;z-index:1}
.fc{background:var(--s);border:.5px solid var(--b);border-radius:var(--r);padding:1.25rem;display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;box-shadow:var(--sh)}
.fcopy,.frefs{font-size:11px;color:var(--f);line-height:1.8}
.fcopy strong,.frefs strong{display:block;color:var(--m);font-size:12px;margin-bottom:4px;font-weight:600}

@media(max-width:760px){
  .g2,.g3,.g4,.fg2,.fg3,.sg,.fc{grid-template-columns:1fr}
  .hbar{flex-direction:column;text-align:center}
  .hlogo{height:52px}
  .g4{grid-template-columns:1fr 1fr}
}
</style>
</head>
<body>

<!-- ============================================================
     HEADER
     ============================================================ -->
<header>
  <div class="hbar">
    <img src="data:image/png;base64,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" alt="UEM — Faculdade de Medicina" class="hlogo">
    <div class="hcenter">
      <h1 class="htitle">TNBC Predictor — HCM</h1>
      <p class="hsub">Predição Inteligente · Apoio à Decisão Clínica · Versão 12.0 — ESMO 2024 · NCCN 2025</p>
    </div>
    <div class="hactions noprint">
      <button id="dark-btn" onclick="toggleDark()" class="btn-dark">🌙 Escuro</button>
      <button class="btn-hdr" onclick="openM('mpesos')">Pesos</button>
      <button class="btn-hdr" onclick="openM('meusoma')">EUSOMA</button>
      <button class="btn-hdr-gold btn-hdr" onclick="window.print()">Imprimir</button>
    </div>
  </div>
  <div class="hmeta">
    <div class="mi"><strong>Desenvolvedor:</strong>Abudala Sualé</div>
    <div class="mi"><strong>Inst.:</strong>UEM — Faculdade de Medicina</div>
    <div class="mi"><strong>Local:</strong>Hospital Central de Maputo</div>
    <div class="mi"><strong>2026</strong></div>
  </div>
</header>

<!-- TABS -->
<div class="tabs noprint">
  <button class="tb on"  onclick="T('t1',this)">Simulação</button>
  <button class="tb"     onclick="T('t2',this)">Nomograma &amp; SHAP</button>
  <button class="tb"     onclick="T('t3',this)">Calculadora pCR</button>
  <button class="tb"     onclick="T('t4',this)">Curva KM</button>
  <button class="tb"     onclick="T('t5',this)">Protocolo Rápido</button>
  <button class="tb"     onclick="T('t6',this)">Relatório Clínico</button>
  <button class="tb"     onclick="T('t7',this)">Seguimento</button>
  <button class="tb"     onclick="T('t8',this)">Ensaios Clínicos</button>
  <button class="tb"     onclick="T('t9',this)">Análise Populacional</button>
  <button class="tb"     onclick="T('t10',this)">Comparação Modelos</button>
<button class="tb"     onclick="T('t11',this)">📷 Atlas Clínico</button>
<button class="tb"     onclick="T('t12',this)">🎯 Modo Apresentação</button>
<button class="tb"     onclick="T('t13',this)">⚖ Comparar Perfis</button>
<button class="tb"     onclick="T('t14',this)">⏱ Timer Clínico</button>
<button class="tb"     onclick="T('t15',this)">🇲🇿 Dados HCM</button>
<button class="tb"     onclick="T('t16',this)">🏥 MDT Board</button>
<button class="tb"     onclick="T('t17',this)">🧬 BRCA &amp; Genética</button>
</div>

<!-- ============================================================
     TAB 1 — SIMULAÇÃO
     ============================================================ -->
<div id="t1" class="tc on"><main>
<div class="g2">

<!-- COL ESQUERDA — INPUTS -->
<div class="col">
  <div class="card card-accent">
    <p class="ct"><span class="ct-icon cti-g">👤</span>Identificação &amp; Dados demográficos</p>
    <div class="fg3">
      <div class="f"><label>ID paciente</label><input type="text" id="pid" value="HCM_001"></div>
      <div class="f"><label>Idade <span class="rt">OR 2.13 &lt;40</span></label><input type="number" id="idade" value="35" min="15" max="90" oninput="calc()"></div>
      <div class="f"><label>Paridade</label><input type="number" id="par" value="2" min="0" max="20" oninput="calc()"></div>
    </div>
    <div class="fg3">
      <div class="f"><label>Peso (kg)</label><input type="number" id="peso" value="68" min="30" max="200" oninput="calc()"></div>
      <div class="f"><label>Altura (cm)</label><input type="number" id="alt" value="160" min="100" max="220" oninput="calc()"></div>
      <div class="f"><label>Menopausa <span class="rt">67% TNBC pré</span></label>
        <select id="men" onchange="calc()"><option value="1">Pré-menopausa</option><option value="0">Pós-menopausa</option></select>
      </div>
    </div>
    <div class="fg2">
      <div class="f"><label>História familiar</label>
        <select id="hfam" onchange="calc()"><option value="0">Não</option><option value="1">Sim (1º grau)</option></select>
      </div>
      <div class="f"><label>Resposta a hormonoterapia</label>
        <select id="hor" onchange="calc()"><option value="0">Não fez / Não respondeu</option><option value="1">Respondeu</option></select>
      </div>
    </div>
  </div>

  <div class="card card-accent">
    <p class="ct"><span class="ct-icon cti-r">🔬</span>Dados do tumor <span style="font-size:10px;color:var(--f);font-weight:400;margin-left:6px">EUSOMA D16 D42 I06 I10 I67</span></p>
    <div class="fg3">
      <div class="f"><label>Tamanho (cm) <span class="rt">RR 1.67 &gt;5</span></label><input type="number" id="tam" value="5.5" min="0.1" max="30" step="0.1" oninput="calc()"></div>
      <div class="f"><label>Crescimento (meses)</label><input type="number" id="cr" value="4" min="1" max="120" oninput="calc()"></div>
      <div class="f"><label>Gânglios N (D20)</label>
        <select id="gan" onchange="calc()"><option value="1">N+ (positivos)</option><option value="0">N0 (negativos)</option></select>
      </div>
    </div>
    <div class="fg3">
      <div class="f"><label>Grau hist. (D42)</label>
        <select id="grau" onchange="calc()"><option value="1">Grau I (baixo)</option><option value="2">Grau II (médio)</option><option value="3" selected>Grau III (alto)</option></select>
      </div>
      <div class="f"><label>Tipo hist. (I06)</label>
        <select id="hist" onchange="calc()"><option value="1" selected>Ductal NST</option><option value="3">Medular</option><option value="2">Lobular</option><option value="4">Outro</option></select>
      </div>
      <div class="f"><label>Estadiamento TNM</label>
        <select id="est" onchange="calc()"><option value="1">I</option><option value="2">II</option><option value="3" selected>III</option><option value="4">IV</option></select>
      </div>
    </div>
    <div class="fg3">
      <div class="f"><label>Ulceração (D13A)</label>
        <select id="ulc" onchange="calc()"><option value="0">Não</option><option value="1">Sim</option></select>
      </div>
      <div class="f"><label>Invasão vasc. (I10)</label>
        <select id="inv" onchange="calc()"><option value="0">Não vista</option><option value="1">Presente</option><option value="2">Incerta</option></select>
      </div>
      <div class="f"><label>Ki-67 % (I67) <span class="rt">0=N/D</span></label><input type="number" id="ki" value="0" min="0" max="100" oninput="calc()"></div>
    </div>
  </div>

  <div class="card card-info">
    <p class="ct"><span class="ct-icon cti-b">🩸</span>Marcadores inflamatórios (hemograma)</p>
    <div class="gnote"><strong>Exclusivo neste modelo — AUC 87.7%</strong>NLR &amp; PLR do hemograma simples disponível no HCM. Br J Surg 2024. 0 = não disponível.</div>
    <div class="fg3">
      <div class="f"><label>Neutrófilos (×10⁹/L)</label><input type="number" id="neut" value="0" min="0" max="30" step="0.1" oninput="calc()"></div>
      <div class="f"><label>Linfócitos (×10⁹/L)</label><input type="number" id="linf" value="0" min="0" max="15" step="0.1" oninput="calc()"></div>
      <div class="f"><label>Plaquetas (×10⁹/L)</label><input type="number" id="plaq" value="0" min="0" max="800" oninput="calc()"></div>
    </div>
    <div class="fg2" style="margin-top:.75rem">
      <div class="f"><label>HIV status <span class="rt">Moza-BC: HIV+ → 33% TNBC</span></label>
        <select id="hiv" onchange="calc()">
          <option value="0">Negativo / Desconhecido</option>
          <option value="1">HIV positivo (confirmado)</option>
        </select>
      </div>
      <div class="f"><label>ECOG Performance Status <span class="rt">decisão terapêutica</span></label>
        <select id="ecog" onchange="calc()">
          <option value="0">0 — Activo sem restrições</option>
          <option value="1">1 — Restrito em actividade intensa</option>
          <option value="2">2 — Ambulatório, incapaz de trabalho</option>
          <option value="3">3 — Limitado autocuidado</option>
        </select>
      </div>
    </div>
        <div id="nlr-row" style="display:none;background:var(--il);border:.5px solid #A0BCDA;border-radius:10px;padding:10px 14px;margin-top:.5rem">
      <div style="display:flex;gap:20px">
        <div><p style="font-size:10px;color:var(--in);font-weight:600;text-transform:uppercase;letter-spacing:.07em">NLR</p><p style="font-family:'Instrument Serif',Georgia,serif;font-size:24px;color:var(--ac)" id="nlrv">—</p></div>
        <div><p style="font-size:10px;color:var(--in);font-weight:600;text-transform:uppercase;letter-spacing:.07em">PLR</p><p style="font-family:'Instrument Serif',Georgia,serif;font-size:24px;color:var(--ac)" id="plrv">—</p></div>
        <div style="flex:1"><p style="font-size:10px;color:var(--in);font-weight:600;text-transform:uppercase;letter-spacing:.07em">Interpretação</p><p style="font-size:12px;color:var(--m);margin-top:4px" id="nlrint">—</p></div>
      </div>
    </div>
  </div>

  <button style="background:var(--ac);color:#fff;border:none;border-radius:var(--rs);padding:9px 20px;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:12px;font-weight:500;cursor:pointer;width:100%;margin-bottom:6px;transition:background .15s" onclick="printScoreSheet()">🖨 Score sheet</button>
<button class="btnadd" style="background:var(--g);color:#fff;border-color:var(--g)" onclick="printGuiaTriagem()">📋 Guia de Triagem</button>
<button class="btnadd" onclick="addPatient()">
    <span style="font-size:20px;font-weight:300">+</span>Adicionar à análise populacional
  </button>
</div>

<!-- COL DIREITA — RESULTADOS -->
<div class="col">

  <div class="card card-gold">
    <p class="ct"><span class="ct-icon cti-gold">⚡</span>Avaliação de risco</p>
    <div class="sem">
      <div class="sll"><div class="sl" id="sr"></div><div class="sl" id="sy"></div><div class="sl" id="sg2"></div></div>
      <div style="flex:1">
        <p style="font-size:16px;font-weight:500;color:var(--t)" id="stit">—</p>
        <p style="font-size:12px;color:var(--m)" id="ssub">Preencha os dados clínicos</p>
      </div>
    </div>

    <div class="sg">
      <div class="sb">
        <p style="font-size:10px;color:var(--m);font-weight:600;text-transform:uppercase;letter-spacing:.07em;margin-bottom:5px">Obj. 1 — Probabilidade TNBC</p>
        <p class="snum" id="ptn">—</p>
        <div class="mtr"><div class="mf" id="mtn" style="width:0%"></div></div>
        <div style="display:flex;align-items:center;gap:6px;margin-top:4px;flex-wrap:wrap">
          <span id="btn">—</span>
          <span id="tnbc-ci" style="font-size:10px;color:var(--f)">IC 95%: —</span>
        </div>
        <span id="completeness-badge" class="badge bi" style="font-size:10px;margin-top:4px;display:inline-block">—</span>
      </div>
      <div class="sb">
        <p style="font-size:10px;color:var(--m);font-weight:600;text-transform:uppercase;letter-spacing:.07em;margin-bottom:5px">Obj. 2 — Risco prognóstico</p>
        <p class="snum" id="ppr">—</p>
        <div class="mtr"><div class="mf" id="mpr" style="width:0%"></div></div>
        <span id="bpr">—</span>
      </div>
    </div>

    <div style="margin-bottom:1rem">
      <p style="font-size:10px;color:var(--m);font-weight:600;text-transform:uppercase;letter-spacing:.07em;margin-bottom:6px">Score de urgência — encaminhamento IHQ (Joanesburgo)</p>
      <div class="urgbar"><div class="urgmark" id="umark" style="left:20%"></div></div>
      <div class="urglabs"><span>Não urgente</span><span>Moderado</span><span>Urgente</span></div>
      <p style="font-size:12px;color:var(--m);margin-top:6px;font-weight:500" id="urgtext">—</p>
    </div>

    <div style="display:flex;gap:10px;margin-bottom:1rem">
      <div style="flex:1;background:var(--s2);border:.5px solid var(--b);border-radius:10px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center">
        <div><p style="font-size:10px;color:var(--m);text-transform:uppercase;font-weight:600;letter-spacing:.07em">IMC</p><p style="font-size:22px;font-family:'Instrument Serif',Georgia,serif" id="imc">—</p></div>
        <span id="bmi">—</span>
      </div>
      <div style="flex:1;background:var(--il);border:.5px solid #A0BCDA;border-radius:10px;padding:10px 14px">
        <p style="font-size:10px;color:var(--in);text-transform:uppercase;font-weight:600;letter-spacing:.07em;margin-bottom:4px">Sobrevivência estimada SSA</p>
        <div style="display:flex;gap:12px">
          <div style="text-align:center"><p style="font-family:'Instrument Serif',Georgia,serif;font-size:20px;color:var(--ac)" id="s3">—</p><p style="font-size:9px;color:var(--in);font-weight:600;text-transform:uppercase">3 anos</p></div>
          <div style="text-align:center"><p style="font-family:'Instrument Serif',Georgia,serif;font-size:20px;color:var(--ac)" id="s5">—</p><p style="font-size:9px;color:var(--in);font-weight:600;text-transform:uppercase">5 anos</p></div>
        </div>
      </div>
    </div>

    <div class="disc" style="margin-top:0">⚠ Ferramenta de apoio à decisão clínica. Não substitui avaliação especializada nem IHQ. Em validação com dados reais HCM Jan/2023–Mar/2026.</div>
  </div>

  <!-- FACTORES ENRIQUECIDOS -->
  <div class="card card-accent">
    <p class="ct">
      <span class="ct-icon cti-r">⚠</span>Factores de risco identificados
      <span style="margin-left:auto;font-size:10px;color:var(--f);font-weight:400;text-transform:none;letter-spacing:0">Clica para expandir</span>
    </p>
    <div id="flist-enriched"><p style="font-size:13px;color:var(--f)">Preencha os dados clínicos para ver os factores.</p></div>
  </div>

  <!-- CONDUTA ENRIQUECIDA -->
  <div class="card card-accent">
    <p class="ct">
      <span class="ct-icon cti-g">✓</span>Conduta sugerida
      <span style="margin-left:auto;font-size:10px;color:var(--f);font-weight:400;text-transform:none;letter-spacing:0">Clica para expandir · marcar como feito</span>
    </p>
    <div id="clist-enriched"><p style="font-size:13px;color:var(--f)">Preencha os dados clínicos.</p></div>
  </div>

</div>
</div>
</main></div>

<!-- ============================================================
     TAB 2 — NOMOGRAMA & SHAP
     ============================================================ -->
<div id="t2" class="tc"><main>
<div class="g2">
  <div class="card card-accent">
    <p class="ct"><span class="ct-icon cti-g">📊</span>Nomograma visual interactivo</p>
    <div class="infonote">Cada barra representa a contribuição da variável ao score TNBC. Actualiza em tempo real.</div>
    <div id="nomo-rows"></div>
    <div style="margin-top:1rem;padding-top:1rem;border-top:.5px solid var(--b);display:flex;justify-content:space-between;align-items:center">
      <p style="font-size:12px;color:var(--m)">Score total TNBC</p>
      <p style="font-family:'Instrument Serif',Georgia,serif;font-size:28px;color:var(--g)" id="nomo-total">—</p>
    </div>
  </div>
  <div class="card card-info">
    <p class="ct"><span class="ct-icon cti-b">🧠</span>SHAP values — impacto individual</p>
    <div class="infonote">Inspirado em SHapley Additive exPlanations (XGBoost 2025). Vermelho = aumenta risco. Verde = diminui risco.</div>
    <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--f);margin-bottom:8px"><span>← Diminui risco TNBC</span><span>Baseline</span><span>Aumenta risco →</span></div>
    <div id="shap-rows"></div>
    <div class="pnote" style="margin-top:1rem"><strong>Nota metodológica</strong>SHAP values exactos serão calculados pelo modelo Python treinado com dados reais do HCM.</div>
  </div>
</div>
</main></div>

<!-- ============================================================
     TAB 3 — pCR
     ============================================================ -->
<div id="t3" class="tc"><main>
<div class="g2">
  <div class="card card-info">
    <p class="ct"><span class="ct-icon cti-b">💊</span>Calculadora pCR — QT neoadjuvante</p>
    <div class="gnote"><strong>AUC 87.7% — Br J Surg 2024</strong>Predição de resposta patológica completa em TNBC estádio II/III. Inclui NLR, PLR e variação após 1º ciclo.</div>
    <div class="f"><label>NLR pré-tratamento</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="pcr-nlr" min="0.5" max="15" step="0.1" value="3" oninput="calcPCR()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="pnv">3.0</span></div></div>
    <div class="f"><label>PLR pré-tratamento</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="pcr-plr" min="50" max="500" step="5" value="150" oninput="calcPCR()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="ppv">150</span></div></div>
    <div class="f"><label>Variação PLR após 1º ciclo (%)</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="pcr-dplr" min="-80" max="80" step="5" value="0" oninput="calcPCR()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="pdv">0%</span></div></div>
    <div class="fg2">
      <div class="f"><label>Estadiamento</label><select id="pcr-est" onchange="calcPCR()"><option value="2">Estádio II</option><option value="3" selected>Estádio III</option></select></div>
      <div class="f"><label>Tamanho (cm)</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="pcr-tam" min="1" max="12" step="0.5" value="5.5" oninput="calcPCR()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="ptv">5.5</span></div></div>
    </div>
  </div>
  <div class="col">
    <div class="card card-gold">
      <p class="ct"><span class="ct-icon cti-gold">🎯</span>Probabilidade de pCR</p>
      <div style="text-align:center;padding:1rem 0">
        <p style="font-family:'Instrument Serif',Georgia,serif;font-size:60px;line-height:1;margin-bottom:8px" id="pcr-val">—</p>
        <span id="pcr-badge">—</span>
      </div>
      <div class="mtr" style="height:10px;margin-bottom:1rem"><div class="mf" id="pcr-bar" style="width:0%;height:10px"></div></div>
      <div id="pcr-interp" style="font-size:12px;color:var(--m);line-height:1.6"></div>
    </div>
    <div class="card card-accent">
      <p class="ct"><span class="ct-icon cti-g">✓</span>Conduta baseada em pCR</p>
      <ul class="cl" id="pcr-conduct" style="list-style:none"></ul>
    </div>
  </div>
</div>


<!-- DOSE CALCULATOR SECTION inside t3 -->
<div class="g2" style="margin-top:1.25rem">
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">💊</span>Calculadora de dose QT — BSA &amp; protocolo</p>
    <div class="infonote">Calcula doses de quimioterapia para esta paciente com base no peso/altura (BSA — Mosteller). Exclusivo neste modelo.</div>
    <div class="fg3">
      <div class="f"><label>Peso (kg)</label><input type="number" id="dose-peso" value="68" min="30" max="200" oninput="calcDose()"></div>
      <div class="f"><label>Altura (cm)</label><input type="number" id="dose-alt" value="160" min="100" max="220" oninput="calcDose()"></div>
      <div class="f"><label>Protocolo QT</label>
        <select id="dose-prot" onchange="calcDose()">
          <option value="act">AC-T (Standard TNBC)</option>
          <option value="ac">AC (Antraciclina)</option>
          <option value="carbo">Carboplatina + Paclitaxel</option>
          <option value="cmf">CMF (alternativo)</option>
          <option value="pal">Capecitabina (paliativa)</option>
        </select>
      </div>
    </div>
    <div style="background:var(--gl);border:.5px solid var(--g);border-radius:var(--rs);padding:12px;margin-bottom:1rem">
      <p style="font-size:10px;color:var(--m);font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:4px">BSA calculada — Fórmula Mosteller</p>
      <p style="font-family:'Instrument Serif',Georgia,serif;font-size:32px;color:var(--g)" id="bsa-val">— m²</p>
    </div>
    <div id="dose-drugs-list"></div>
    <div class="disc">⚠ Doses indicativas — ajustar conforme toxicidade, comorbilidades e disponibilidade HCM.</div>
  </div>

  <!-- VALIDAÇÃO CAMPOS - Card resumo -->
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">✅</span>Validação do perfil clínico</p>
    <div class="infonote">Verificação automática da consistência clínica dos dados introduzidos.</div>
    <div id="validation-results"></div>
    <div style="margin-top:1rem;padding-top:1rem;border-top:.5px solid var(--b)">
      <p class="ct" style="margin-bottom:.75rem"><span class="ct-icon cti-g">💾</span>Exportar dados da sessão</p>
      <button class="btn-g" style="width:100%;padding:9px;margin-bottom:6px" onclick="exportJSON()">Exportar JSON completo</button>
      <button class="btn-go" style="width:100%;padding:9px" onclick="exportCSV()">Exportar CSV pacientes</button>
    </div>
  </div>
</div>
</main></div>

<!-- ============================================================
     TAB 4 — CURVA KM
     ============================================================ -->
<div id="t4" class="tc"><main>
<div class="g2">
  <div class="card card-info">
    <p class="ct"><span class="ct-icon cti-b">📈</span>Parâmetros da curva Kaplan-Meier</p>
    <div class="infonote">Curva simulada com base em dados populacionais SSA. Fins ilustrativos e de apoio à decisão clínica.</div>
    <div class="f"><label>Score TNBC</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="km-tnbc" min="0" max="100" value="65" oninput="renderKM()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="kt-v">65%</span></div></div>
    <div class="f"><label>Score prognóstico</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="km-prog" min="0" max="100" value="70" oninput="renderKM()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="kp-v">70%</span></div></div>
    <div class="fg2">
      <div class="f"><label>Recebeu QT</label><select id="km-qt" onchange="renderKM()"><option value="1">Sim</option><option value="0">Não</option></select></div>
      <div class="f"><label>Estadiamento</label><select id="km-est" onchange="renderKM()"><option value="1">I</option><option value="2">II</option><option value="3" selected>III</option><option value="4">IV</option></select></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:1rem">
      <div class="sc"><p class="scc" id="km1">—</p><p class="scl">1 ano</p></div>
      <div class="sc"><p class="scc" id="km3">—</p><p class="scl">3 anos</p></div>
      <div class="sc"><p class="scc" id="km5">—</p><p class="scl">5 anos</p></div>
    </div>
  </div>
  <div class="card card-accent">
    <p class="ct"><span class="ct-icon cti-g">📉</span>Curva de Kaplan-Meier simulada</p>
    <canvas id="km-chart" style="max-height:300px"></canvas>
    <div style="display:flex;gap:16px;margin-top:12px;flex-wrap:wrap">
      <div style="display:flex;align-items:center;gap:6px"><span style="width:20px;height:3px;background:#CB4335;display:inline-block"></span><span style="font-size:11px;color:var(--m)">Esta paciente</span></div>
      <div style="display:flex;align-items:center;gap:6px"><span style="width:20px;height:0;border-top:2px dashed #CA6F1E;display:inline-block"></span><span style="font-size:11px;color:var(--m)">TNBC médio SSA</span></div>
      <div style="display:flex;align-items:center;gap:6px"><span style="width:20px;height:0;border-top:2px dashed #27AE60;display:inline-block"></span><span style="font-size:11px;color:var(--m)">Não-TNBC SSA</span></div>
    </div>
    <div class="disc">⚠ Curva simulada — não é individual real. Fins de apoio à decisão.</div>
  </div>
</div>
</main></div>

<!-- ============================================================
     TAB 5 — ASSISTENTE IA
     ============================================================ -->
<div id="t5" class="tc"><main>
<div class="infonote">Protocolo de decisão clínica passo-a-passo baseado nos dados da paciente actual. Clica em cada etapa para ver orientação detalhada.</div>
<div class="g2">
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">⚡</span>Decisão rápida — sem IHQ (contexto HCM)</p>
    <div id="decision-flow-output"></div>
    <button class="btn-g" style="width:100%;margin-top:1rem;padding:10px" onclick="buildDecisionFlow()">Gerar protocolo para esta paciente</button>
  </div>
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">📋</span>Guidelines ESMO adaptadas ao HCM</p>
    <div style="font-size:12px;line-height:1.8;color:var(--m)">
      <div style="background:var(--gl);border-radius:var(--rs);padding:10px 14px;margin-bottom:8px">
        <p style="font-weight:700;color:var(--g);margin-bottom:4px">Estádio II–III (operável)</p>
        <p>→ QT neoadjuvante primeiro (AC-T × 8 ciclos)<br>→ Cirurgia 3–6 semanas após QT<br>→ Se pCR: observação<br>→ Se não pCR: Capecitabina adj.</p>
      </div>
      <div style="background:var(--wl);border-radius:var(--rs);padding:10px 14px;margin-bottom:8px">
        <p style="font-weight:700;color:var(--wn);margin-bottom:4px">Estádio IV (metastático)</p>
        <p>→ QT paliativa (Capecitabina ou Gencitabina)<br>→ Carboplatina se BRCA1/2 suspeito<br>→ Cuidados de suporte obrigatórios<br>→ Sobrev. mediana HCM: 10–13 meses</p>
      </div>
      <div style="background:var(--il);border-radius:var(--rs);padding:10px 14px">
        <p style="font-weight:700;color:var(--in);margin-bottom:4px">Sem IHQ disponível (HCM)</p>
        <p>→ Tratar como TNBC se Score ≥70%<br>→ Não dar tamoxifeno sem IHQ<br>→ Enviar biópsia para Joanesburgo se possível<br>→ Reavaliação com IHQ altera conduta em ~30% dos casos</p>
      </div>
    </div>
    <p style="font-size:10px;color:var(--f);margin-top:8px;font-style:italic">Fonte: ESMO Clinical Practice Guidelines 2024 · Adaptado para HCM por A. Sualé</p>
  </div>
</div>
<div class="card" style="margin-top:1.25rem">
  <p class="ct"><span class="ct-icon cti-g">💊</span>Fármacos disponíveis vs não disponíveis — HCM 2026</p>
  <div id="drug-availability-table"></div>
</div>
</main></div>

<div id="t6" class="tc"><main>
<div class="g2">
  <div class="card card-accent">
    <p class="ct"><span class="ct-icon cti-g">📄</span>Gerador de relatório clínico</p>
    <div class="infonote">Gera automaticamente um texto médico formal em português para arquivar no processo clínico do HCM. Baseado nos dados inseridos e nos scores calculados.</div>
    <div class="f"><label>Médico responsável</label><input type="text" id="rep-medico" value="Dr. " placeholder="Nome do médico"></div>
    <div class="fg2">
      <div class="f"><label>Serviço / Enfermaria</label><input type="text" id="rep-servico" value="Oncologia — HCM" placeholder="Serviço"></div>
      <div class="f"><label>Data do relatório</label><input type="date" id="rep-data"></div>
    </div>
    <div class="f"><label>Observações adicionais</label><textarea id="rep-obs" style="width:100%;padding:8px 11px;border:.5px solid var(--bs);border-radius:var(--rs);font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:13px;height:80px;resize:vertical;background:var(--s);color:var(--t);" placeholder="Observações clínicas adicionais..."></textarea></div>
    <div style="display:flex;gap:8px;margin-top:.5rem">
      <button class="btn-g" onclick="generateReport()">Gerar relatório</button>
      <button class="btn-go" onclick="copyReport()">Copiar texto</button>
      <button class="btn-go" onclick="window.print()">Imprimir</button>
    </div>
  </div>

  <div class="card card-gold">
    <p class="ct"><span class="ct-icon cti-gold">📋</span>Relatório gerado</p>
    <div class="report-box" id="report-box">O relatório será gerado aqui após clicar em "Gerar relatório"...</div>
  </div>
</div>
</main></div>

<!-- ============================================================
     TAB 7 — SEGUIMENTO
     ============================================================ -->
<div id="t7" class="tc"><main>
<div class="g2">
  <div class="card card-accent">
    <p class="ct"><span class="ct-icon cti-g">📅</span>Calculadora de seguimento</p>
    <div class="infonote">Define automaticamente as datas das próximas consultas com base no risco clínico calculado. Baseado em guidelines de oncologia e protocolos HCM.</div>
    <div class="f"><label>Data do diagnóstico / 1ª consulta</label><input type="date" id="fu-start" onchange="calcFollowUp()"></div>
    <div class="f"><label>Plano terapêutico escolhido</label>
      <select id="fu-plan" onchange="calcFollowUp()">
        <option value="qt-neo">QT neoadjuvante (AC-T)</option>
        <option value="qt-adj">QT adjuvante</option>
        <option value="cir-rt">Cirurgia + RT</option>
        <option value="paliat">Paliativo / Estádio IV</option>
        <option value="std">Protocolo standard</option>
      </select>
    </div>
    <div class="f"><label>Frequência de seguimento</label>
      <select id="fu-freq" onchange="calcFollowUp()">
        <option value="quinz">Quinzenal (alto risco)</option>
        <option value="mens">Mensal (risco moderado)</option>
        <option value="bim">Bimensal (baixo risco)</option>
      </select>
    </div>
    <div class="gnote" style="margin-top:.75rem"><strong>Calendário gerado automaticamente</strong>Baseado no perfil de risco e plano terapêutico seleccionado.</div>
  </div>

  <div class="card card-gold">
    <p class="ct"><span class="ct-icon cti-gold">🗓</span>Calendário de consultas</p>
    <div id="follow-list"><p style="font-size:13px;color:var(--f)">Selecciona a data de início e o plano.</p></div>
  </div>
</div>
</main></div>

<!-- ============================================================
     TAB 8 — ENSAIOS CLÍNICOS
     ============================================================ -->
<div id="t8" class="tc"><main>
  <div class="infonote">Avaliação automática de elegibilidade para ensaios clínicos activos em África e contextos de baixos recursos. O sistema compara o perfil da paciente com os critérios de inclusão.</div>
  <div class="g4" id="trial-stats" style="margin-bottom:1.25rem"></div>
  <div id="trial-list"></div>
</main></div>

<!-- ============================================================
     TAB 9 — ANÁLISE POPULACIONAL
     ============================================================ -->
<div id="t9" class="tc"><main>
  <div class="card" style="margin-bottom:1.25rem">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;flex-wrap:wrap;gap:8px">
      <div style="display:flex;align-items:center;gap:8px;font-size:13px;color:var(--m)">Pacientes registadas: <span style="background:linear-gradient(135deg,var(--g),var(--g2));color:#fff;font-size:12px;font-weight:600;padding:2px 10px;border-radius:20px" id="cbdg">0</span></div>
      <div style="display:flex;gap:8px">
        <button class="btn-go" onclick="exportCSV()">Exportar CSV</button>
        <button style="background:transparent;color:var(--dn);border:.5px solid var(--dm);border-radius:var(--rs);padding:8px 16px;font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;font-size:12px;cursor:pointer" onclick="clearAll()">Limpar tudo</button>
      </div>
    </div>
    <div id="plist-empty" class="empty">Adicione pacientes no separador "Simulação".</div>
    <div class="plist" id="plist" style="display:none"></div>
  </div>
  <div id="pop-section" style="display:none">
    <div class="g4" id="pop-stats" style="margin-bottom:1.25rem"></div>
    <div class="g2" style="margin-bottom:1.25rem">
      <div class="card"><p class="ct"><span class="dot" style="width:6px;height:6px;border-radius:50%;background:var(--g);display:inline-block"></span>Distribuição risco TNBC</p><canvas id="ch-tnbc" style="max-height:200px"></canvas></div>
      <div class="card"><p class="ct"><span class="dot" style="width:6px;height:6px;border-radius:50%;background:var(--g);display:inline-block"></span>Score TNBC × Idade</p><canvas id="ch-sc" style="max-height:200px"></canvas></div>
    </div>
    <div class="g2" style="margin-bottom:1.25rem">
      <div class="card"><p class="ct"><span class="dot" style="width:6px;height:6px;border-radius:50%;background:var(--g);display:inline-block"></span>Score por grau histológico</p><canvas id="ch-gr" style="max-height:200px"></canvas></div>
      <div class="card"><p class="ct"><span class="dot" style="width:6px;height:6px;border-radius:50%;background:var(--g);display:inline-block"></span>NLR × Score prognóstico</p><canvas id="ch-nlr" style="max-height:200px"></canvas></div>
    </div>
    <div class="card" style="margin-bottom:1.25rem">
      <p class="ct"><span class="dot" style="width:6px;height:6px;border-radius:50%;background:var(--g);display:inline-block"></span>Padrões clínicos — alto risco TNBC</p>
      <div id="patterns"></div>
    </div>
    <div class="card">
      <p class="ct"><span class="dot" style="width:6px;height:6px;border-radius:50%;background:var(--g);display:inline-block"></span>Tabela individual</p>
      <div style="overflow-x:auto"><table class="dt"><thead><tr><th>ID</th><th>Idade</th><th>Grau</th><th>Est.</th><th>Tumor</th><th>Ki-67</th><th>NLR</th><th>TNBC%</th><th>Prog%</th><th>Conduta</th></tr></thead><tbody id="pop-tbody"></tbody></table></div>
    </div>
  </div>
</main></div>

<!-- ============================================================
     TAB 10 — COMPARAÇÃO MODELOS
     ============================================================ -->
<div id="t10" class="tc"><main>
  <div class="infonote">Ajusta o perfil da paciente com os sliders e vê como cada modelo internacional classificaria aquela paciente em tempo real.</div>
  <div class="g2">
    <div class="card card-accent">
      <p class="ct"><span class="ct-icon cti-g">🎛</span>Perfil — ajusta para comparar</p>
      <div class="f"><label>Idade</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="c-idade" min="20" max="80" value="35" oninput="calcCmp()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="c-iv">35</span></div></div>
      <div class="f"><label>Tamanho (cm)</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="c-tam" min="1" max="12" step="0.5" value="5.5" oninput="calcCmp()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="c-tv">5.5</span></div></div>
      <div class="f"><label>Grau histológico</label><select id="c-grau" onchange="calcCmp()"><option value="1">I</option><option value="2">II</option><option value="3" selected>III</option></select></div>
      <div class="f"><label>Estadiamento</label><select id="c-est" onchange="calcCmp()"><option value="1">I</option><option value="2">II</option><option value="3" selected>III</option><option value="4">IV</option></select></div>
      <div class="f"><label>Gânglios positivos</label><select id="c-gan" onchange="calcCmp()"><option value="1">Sim</option><option value="0">Não</option></select></div>
      <div class="f"><label>Pré-menopausa</label><select id="c-men" onchange="calcCmp()"><option value="1">Sim</option><option value="0">Não</option></select></div>
      <div class="f"><label>Ki-67 (%)</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="c-ki" min="0" max="100" value="55" oninput="calcCmp()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="c-kv">55%</span></div></div>
      <div class="f"><label>NLR</label><div style="display:flex;align-items:center;gap:10px"><input type="range" id="c-nlr" min="0.5" max="15" step="0.5" value="3" oninput="calcCmp()" style="flex:1"><span style="font-size:13px;font-weight:600;color:var(--g);min-width:40px;text-align:right" id="c-nv">3.0</span></div></div>
      <div style="background:var(--il);border:.5px solid #A0BCDA;border-radius:10px;padding:10px 14px;margin-top:.75rem">
        <p style="font-size:12px;font-weight:600;color:var(--in);margin-bottom:8px">Simular IHQ disponível</p>
        <div class="fg2">
          <div class="f"><label style="font-size:11px">ER status</label><select id="c-er" onchange="calcCmp()"><option value="nd" selected>N/D (sem IHQ)</option><option value="neg">ER negativo</option><option value="pos">ER positivo</option></select></div>
          <div class="f"><label style="font-size:11px">HER2 status</label><select id="c-her2" onchange="calcCmp()"><option value="nd" selected>N/D (sem IHQ)</option><option value="neg">HER2 negativo</option><option value="pos">HER2 positivo</option></select></div>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card card-gold">
        <p class="ct"><span class="ct-icon cti-gold">⚖</span>Classificação em tempo real</p>
        <div id="cmp-bars"></div>
      </div>
      <div class="card card-info">
        <p class="ct"><span class="ct-icon cti-b">🕸</span>Radar — comparação multidimensional</p>
        <canvas id="ch-radar" style="max-height:280px"></canvas>
      </div>
    </div>
  </div>
</main></div>

<!-- FOOTER -->

<!-- ===== TAB 11: ATLAS CLÍNICO ===== -->
<div id="t11" class="tc"><main>
<div style="margin-bottom:1rem">
  <div class="infonote">Galeria de referência clínica e imagiológica do cancro da mama. Clica em cada imagem para ampliar e ver detalhes. Útil para correlacionar o caso actual com padrões conhecidos.</div>
</div>

<!-- SELECTOR DE CATEGORIA -->
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:1.5rem">
  <button class="tb on" onclick="filterAtlas('all',this)">Todas</button>
  <button class="tb" onclick="filterAtlas('macro',this)">Macroscopia</button>
  <button class="tb" onclick="filterAtlas('micro',this)">Histologia</button>
  <button class="tb" onclick="filterAtlas('img',this)">Imagiologia</button>
  <button class="tb" onclick="filterAtlas('tnbc',this)">Específico TNBC</button>
  <button class="tb" onclick="filterAtlas('stages',this)">Estadiamento</button>
</div>

<div id="atlas-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1.25rem"></div>

<!-- LIGHTBOX -->
<div id="lightbox" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:2000;align-items:center;justify-content:center;flex-direction:column;padding:2rem" onclick="closeLB(event)">
  <div style="max-width:800px;width:100%;text-align:center">
    <div id="lb-img-wrap" style="margin-bottom:1rem"></div>
    <h3 id="lb-title" style="font-family:'Instrument Serif',Georgia,serif;font-size:20px;color:#fff;margin-bottom:6px"></h3>
    <p id="lb-desc" style="font-size:13px;color:rgba(255,255,255,.75);line-height:1.7;max-width:600px;margin:0 auto 1rem"></p>
    <div id="lb-tags" style="display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin-bottom:1rem"></div>
    <button onclick="closeLB()" style="background:rgba(255,255,255,.15);color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:8px;padding:8px 20px;cursor:pointer;font-size:13px">Fechar</button>
  </div>
</div>
</main></div>

<!-- ===== TAB 12: MODO APRESENTAÇÃO ===== -->
<div id="t12" class="tc"><main>
<div class="card" style="max-width:800px;margin:0 auto">
  <p class="ct"><span class="dot"></span>Modo Apresentação — para mostrar a médicos e comité</p>
  <div class="infonote">Resume os resultados da paciente actual num formato limpo, sem campos técnicos. Ideal para apresentar em reunião clínica ou ao próprio comité de ética.</div>
  <div id="present-output"></div>
  <button class="btn-g" style="width:100%;margin-top:1rem;padding:11px" onclick="renderPresent()">Gerar apresentação</button>
</div>
</main></div>


<!-- ===== TAB 13: COMPARAÇÃO DE PERFIS ===== -->
<div id="t13" class="tc"><main>
<div class="infonote">Compara dois perfis clínicos lado a lado. Útil para comparar a paciente actual com um caso de referência ou para avaliar como mudanças nos dados afectam o score.</div>

<div class="g2">
  <!-- Perfil A -->
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g" style="background:rgba(26,107,60,.15)">A</span>Perfil A — Paciente actual</p>
    <div id="compare-A-summary"></div>
    <button class="btn-g" style="width:100%;margin-top:.75rem;padding:8px" onclick="loadCompareA()">Carregar perfil actual</button>
  </div>
  <!-- Perfil B -->
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g" style="background:rgba(27,63,92,.15)">B</span>Perfil B — Perfil de comparação</p>
    <div class="fg3" style="margin-bottom:.75rem">
      <div class="f"><label>Idade</label><input type="number" id="cmp-b-idade" value="45" min="15" max="90" oninput="updateCompareB()"></div>
      <div class="f"><label>Tumor (cm)</label><input type="number" id="cmp-b-tam" value="3.5" min="0.1" max="20" step="0.1" oninput="updateCompareB()"></div>
      <div class="f"><label>Grau</label>
        <select id="cmp-b-grau" onchange="updateCompareB()"><option value="1">I</option><option value="2" selected>II</option><option value="3">III</option></select>
      </div>
    </div>
    <div class="fg3">
      <div class="f"><label>Estadiamento</label>
        <select id="cmp-b-est" onchange="updateCompareB()"><option value="1">I</option><option value="2" selected>II</option><option value="3">III</option><option value="4">IV</option></select>
      </div>
      <div class="f"><label>Gânglios</label>
        <select id="cmp-b-gan" onchange="updateCompareB()"><option value="0" selected>N0</option><option value="1">N+</option></select>
      </div>
      <div class="f"><label>Menopausa</label>
        <select id="cmp-b-men" onchange="updateCompareB()"><option value="1">Pré</option><option value="0" selected>Pós</option></select>
      </div>
    </div>
    <div id="compare-B-summary"></div>
  </div>
</div>

<!-- Resultado comparação -->
<div class="card" style="margin-top:1.25rem" id="compare-result-card">
  <p class="ct"><span class="ct-icon cti-g">📊</span>Comparação lado a lado</p>
  <div id="compare-result"></div>
</div>
</main></div>

<!-- ===== TAB 14: TIMER CLÍNICO ===== -->
<div id="t14" class="tc"><main>
<div class="g2">
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">⏱</span>Timer clínico — alertas de tempo</p>
    <div class="infonote">Ferramenta de apoio à gestão do tempo em contexto clínico. Define alertas para acções urgentes desta paciente.</div>

    <!-- Contagem decrescente urgência -->
    <div style="text-align:center;padding:1.5rem 0;border-bottom:.5px solid var(--b);margin-bottom:1rem">
      <p style="font-size:9px;color:var(--m);text-transform:uppercase;font-weight:700;letter-spacing:.1em;margin-bottom:8px">Tempo desde apresentação</p>
      <p style="font-family:'Instrument Serif',Georgia,serif;font-size:48px;color:var(--g);line-height:1" id="elapsed-time">00:00:00</p>
      <p style="font-size:11px;color:var(--f);margin-top:4px">Sessão clínica actual</p>
      <div style="display:flex;gap:8px;justify-content:center;margin-top:1rem">
        <button class="btn-g" onclick="startTimer()" id="timer-start">Iniciar</button>
        <button class="btn-go" onclick="resetTimer()">Reset</button>
      </div>
    </div>

    <!-- Alertas por acção -->
    <p style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--m);margin-bottom:.75rem">Lembretes de acção — baseados no perfil actual</p>
    <div id="action-reminders"></div>
  </div>

  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">📆</span>Próximas consultas — agendamento rápido</p>
    <div class="f"><label>Data de hoje / 1ª consulta</label><input type="date" id="timer-start-date" value="" onchange="calcQuickSchedule()"></div>
    <div id="quick-schedule"></div>

    <div style="margin-top:1.25rem;padding-top:1.25rem;border-top:.5px solid var(--b)">
      <p class="ct" style="margin-bottom:.75rem"><span class="ct-icon cti-g">🔔</span>Janela de máximo risco de recorrência</p>
      <div id="recurrence-window"></div>
    </div>
  </div>
</div>
</main></div>


<!-- ===== TAB 15: PAINEL MOZA-BC ===== -->
<div id="t15" class="tc"><main>
<div class="infonote"><strong>Base de evidência local</strong> — Único estudo com dados reais de sobrevivência por subtipo molecular em Moçambique. Incorporados directamente no modelo de predição.</div>

<!-- Reference card -->
<div class="card" style="margin-bottom:1.25rem;border-left:4px solid var(--g)">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem">
    <div style="flex:1">
      <p style="font-family:'Instrument Serif',Georgia,serif;font-size:16px;color:var(--g);margin-bottom:4px">Brandão M. et al. — ESMO Open 2020;5:e000829</p>
      <p style="font-size:12px;color:var(--m);margin-bottom:4px"><em>Breast cancer in Mozambique: retrospective analysis of subtypes, immunohistochemical profile and prognosis</em></p>
      <p style="font-size:11px;color:var(--f)">Hospital Central de Maputo · Universidade Eduardo Mondlane · Jan 2015 – Ago 2017 · n=210 · doi:10.1136/esmoopen-2020-000829</p>
    </div>
    <span class="badge bo" style="font-size:12px;padding:6px 14px">CC BY-NC 4.0</span>
  </div>
</div>

<!-- Stats grid -->
<div class="g4" style="margin-bottom:1.25rem">
  <div class="sc"><p class="scc" style="color:var(--g)">210</p><p class="scl">Pacientes total</p></div>
  <div class="sc"><p class="scc" style="color:var(--dm)">25%</p><p class="scl">TNBC (52/210)</p></div>
  <div class="sc"><p class="scc" style="color:var(--wm)">74%</p><p class="scl">Estádio III/IV</p></div>
  <div class="sc"><p class="scc" style="color:var(--ac)">2%</p><p class="scl">Taxa de pCR</p></div>
</div>

<div class="g2" style="margin-bottom:1.25rem">
  <!-- Survival chart canvas -->
  <div class="card">
    <p class="ct"><span class="dot"></span>Sobrevivência OS 3 anos por subtipo (Moza-BC)</p>
    <canvas id="moza-os-chart" style="max-height:220px"></canvas>
    <p style="font-size:10px;color:var(--f);margin-top:8px;font-style:italic">HR morte TNBC vs ER+/HER2−: 3.10 (IC 95%: 1.81–5.31) · p&lt;0.001</p>
  </div>
  <!-- Key findings -->
  <div class="card">
    <p class="ct"><span class="dot"></span>Achados principais — contexto HCM</p>
    <div style="font-size:12px;line-height:1.8">
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:.5px solid var(--b)">
        <span style="color:var(--m)">Prevalência TNBC</span>
        <strong>25% (52/210)</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:.5px solid var(--b)">
        <span style="color:var(--m)">OS 3 anos — TNBC</span>
        <strong style="color:var(--dm)">31.9%</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:.5px solid var(--b)">
        <span style="color:var(--m)">DFS 3 anos — TNBC</span>
        <strong style="color:var(--dm)">26.7%</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:.5px solid var(--b)">
        <span style="color:var(--m)">OS 3 anos — ER+</span>
        <strong style="color:var(--om)">61.1%</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:.5px solid var(--b)">
        <span style="color:var(--m)">Estádio III/IV à apresentação</span>
        <strong>74%</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:.5px solid var(--b)">
        <span style="color:var(--m)">Mastectomia total</span>
        <strong>92%</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:.5px solid var(--b)">
        <span style="color:var(--m)">HIV positivo (TNBC)</span>
        <strong>33% <span style="font-weight:400;font-size:10px">vs 20% HIV-</span></strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:.5px solid var(--b)">
        <span style="color:var(--m)">Taxa pCR (ypT0/is N0)</span>
        <strong style="color:var(--dm)">2% apenas</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0">
        <span style="color:var(--m)">Sobrepeso/obesas</span>
        <strong>62%</strong>
      </div>
    </div>
  </div>
</div>

<!-- Implication for this model -->
<div class="card" style="margin-bottom:1.25rem">
  <p class="ct"><span class="dot"></span>Como estes dados calibram o nosso modelo</p>
  <div class="g3">
    <div style="background:var(--gl);border-radius:var(--rs);padding:12px 14px">
      <p style="font-size:11px;font-weight:700;color:var(--g);margin-bottom:4px">Score TNBC</p>
      <p style="font-size:12px;color:var(--m)">Prevalência de 25% no HCM justifica threshold de 45% para triagem — captura a maioria sem excesso de falsos positivos.</p>
    </div>
    <div style="background:var(--dl);border-radius:var(--rs);padding:12px 14px">
      <p style="font-size:11px;font-weight:700;color:var(--dn);margin-bottom:4px">Score Prognóstico</p>
      <p style="font-size:12px;color:var(--m)">OS 3a de 31.9% calibra a estimativa de sobrevivência. HR 3.10 vs ER+ explica por que o score >70% activa conduta urgente.</p>
    </div>
    <div style="background:var(--wl);border-radius:var(--rs);padding:12px 14px">
      <p style="font-size:11px;font-weight:700;color:var(--wn);margin-bottom:4px">pCR de apenas 2%</p>
      <p style="font-size:12px;color:var(--m)">A baixíssima taxa de pCR no HCM reforça a necessidade de identificação precoce — o tratamento actualmente iniciado tarde demais.</p>
    </div>
  </div>
</div>

<!-- What's missing -->
<div class="card">
  <p class="ct"><span class="dot dot-y"></span>Lacunas — o que este projecto quer preencher</p>
  <div style="font-size:12px;line-height:1.8;color:var(--m)">
    <p style="margin-bottom:8px">O estudo Moza-BC demonstra o problema mas não resolve o diagnóstico precoce. As principais lacunas que este modelo aborda:</p>
    <div style="display:grid;gap:6px">
      <div style="background:var(--s2);border-radius:var(--rs);padding:8px 12px;display:flex;gap:10px">
        <span style="font-size:16px;flex-shrink:0">🔬</span>
        <div><strong>IHQ ausente localmente</strong> — 100% dos diagnósticos TNBC em Moza-BC dependeram de IHQ enviada fora. Este modelo prevê TNBC sem IHQ com variáveis clínicas disponíveis no HCM.</div>
      </div>
      <div style="background:var(--s2);border-radius:var(--rs);padding:8px 12px;display:flex;gap:10px">
        <span style="font-size:16px;flex-shrink:0">⏱</span>
        <div><strong>Diagnóstico tardio</strong> — 74% em estádio III/IV. A ferramenta de urgência IHQ prioriza encaminhamento antes da perda de janela cirúrgica.</div>
      </div>
      <div style="background:var(--s2);border-radius:var(--rs);padding:8px 12px;display:flex;gap:10px">
        <span style="font-size:16px;flex-shrink:0">🧪</span>
        <div><strong>NLR não usado</strong> — Nenhum estudo africano incorporou NLR do hemograma simples como preditor. Este modelo é o primeiro no contexto HCM a fazê-lo.</div>
      </div>
      <div style="background:var(--s2);border-radius:var(--rs);padding:8px 12px;display:flex;gap:10px">
        <span style="font-size:16px;flex-shrink:0">📊</span>
        <div><strong>Dados locais insuficientes</strong> — Moza-BC tem n=210. Objectivo: recolher ≥300 casos HCM para recalibrar os pesos do modelo com dados reais.</div>
      </div>
    </div>
  </div>
</div>
</main></div>


<!-- ===== TAB 16: MDT TUMOR BOARD ===== -->
<div id="t16" class="tc"><main>
<div class="infonote">Checklist de tumor board multidisciplinar (MDT). Replica a discussão que deve acontecer em comité oncológico antes de definir o plano terapêutico. Baseado nas recomendações ESMO 2024 e protocolos HCM.</div>

<div class="g2">
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">📋</span>Checklist MDT — paciente actual</p>
    <div id="mdt-checklist"></div>
    <button class="btn-g" style="width:100%;margin-top:1rem;padding:9px" onclick="buildMDTChecklist()">Gerar checklist para esta paciente</button>
  </div>

  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">👥</span>Especialistas necessários — equipa MDT</p>
    <div id="mdt-team"></div>
    <div style="margin-top:1rem;padding-top:1rem;border-top:.5px solid var(--b)">
      <p class="ct" style="margin-bottom:.75rem"><span class="ct-icon cti-g">⚠</span>Pontos de discussão obrigatórios</p>
      <div id="mdt-discussion"></div>
    </div>
  </div>
</div>

<div class="card" style="margin-top:1.25rem">
  <p class="ct"><span class="dot"></span>Decisão MDT — registo</p>
  <div class="fg3">
    <div class="f"><label>Data da reunião MDT</label><input type="date" id="mdt-date"></div>
    <div class="f"><label>Decisão tomada</label>
      <select id="mdt-decision">
        <option>QT neoadjuvante → cirurgia</option>
        <option>Cirurgia primária → QT adj.</option>
        <option>QT paliativa</option>
        <option>Cuidados paliativos exclusivos</option>
        <option>Encaminhar para estudo / ensaio</option>
        <option>Aguardar IHQ antes de decidir</option>
      </select>
    </div>
    <div class="f"><label>Próximo passo urgente</label>
      <select id="mdt-next">
        <option>Carta referência IHQ — urgente</option>
        <option>Iniciar QT — esta semana</option>
        <option>Estadiamento completo</option>
        <option>Consulta paliativos</option>
        <option>Cirurgia programada</option>
      </select>
    </div>
  </div>
  <button class="btn-g" style="padding:9px 20px;margin-top:.5rem" onclick="printMDT()">🖨 Imprimir acta MDT</button>
</div>
</main></div>

<!-- ===== TAB 17: BRCA & GENÉTICA ===== -->
<div id="t17" class="tc"><main>
<div class="infonote">Calculadora de probabilidade BRCA1/2 e implicações terapêuticas. Baseado no modelo Tyrer-Cuzick simplificado e nas recomendações ESMO 2024. TNBC é o subtipo com maior prevalência de mutações BRCA1/2 (~20%).</div>

<div class="g2">
  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">🧬</span>Score de probabilidade BRCA1/2</p>
    <div class="gnote"><strong>Porquê avaliar BRCA em TNBC?</strong>ESMO 2024 recomenda teste gBRCA1/2 em todos os TNBC HER2-negativos. ~20% têm mutação. Se positivo: PARP inibidores (olaparib) são opção terapêutica eficaz.</div>

    <div class="f"><label>História familiar cancro mama (1º grau)</label>
      <select id="brca-hfam" onchange="calcBRCA()">
        <option value="0">Sem história</option>
        <option value="1">1 familiar</option>
        <option value="2">2+ familiares</option>
      </select>
    </div>
    <div class="f"><label>História familiar cancro ovário</label>
      <select id="brca-ovario" onchange="calcBRCA()">
        <option value="0">Não</option>
        <option value="1">Sim</option>
      </select>
    </div>
    <div class="f"><label>Cancro mama bilateral ou múltiplo</label>
      <select id="brca-bi" onchange="calcBRCA()">
        <option value="0">Não</option>
        <option value="1">Sim</option>
      </select>
    </div>
    <div class="f"><label>Origem étnica africana subsariana</label>
      <select id="brca-etnia" onchange="calcBRCA()">
        <option value="1" selected>Sim (prevalência BRCA1 aumentada)</option>
        <option value="0">Não / Mista</option>
      </select>
    </div>
    <div class="f"><label>Histotipo medular (BRCA1 associado)</label>
      <select id="brca-med" onchange="calcBRCA()">
        <option value="0">Não</option>
        <option value="1">Sim</option>
      </select>
    </div>
    <div class="f"><label>Cancro mama em familiar masculino</label>
      <select id="brca-masc" onchange="calcBRCA()">
        <option value="0">Não</option>
        <option value="1">Sim (fortemente BRCA2)</option>
      </select>
    </div>

    <!-- Result -->
    <div style="text-align:center;padding:1.5rem 0;border-top:.5px solid var(--b);margin-top:.75rem">
      <p style="font-size:9px;color:var(--m);text-transform:uppercase;font-weight:700;letter-spacing:.1em;margin-bottom:8px">Probabilidade estimada gBRCA1/2</p>
      <p style="font-family:'Instrument Serif',Georgia,serif;font-size:52px;line-height:1;margin-bottom:8px" id="brca-prob">—</p>
      <span id="brca-badge" class="badge">—</span>
    </div>
    <div id="brca-interp" style="font-size:12px;color:var(--m);line-height:1.7;margin-top:.75rem"></div>
  </div>

  <div class="card">
    <p class="ct"><span class="ct-icon cti-g">💊</span>Implicações terapêuticas BRCA</p>
    <div id="brca-therapy"></div>

    <div style="margin-top:1.25rem;padding-top:1.25rem;border-top:.5px solid var(--b)">
      <p class="ct" style="margin-bottom:.75rem"><span class="dot"></span>Onde testar em Moçambique</p>
      <div style="font-size:12px;line-height:1.8;color:var(--m)">
        <div style="background:var(--s2);border-radius:var(--rs);padding:10px 12px;margin-bottom:6px">
          <p style="font-weight:600;color:var(--t)">NHLS — National Health Laboratory Service (SA)</p>
          <p>→ Joanesburgo, África do Sul · Aceita amostras FFPE</p>
          <p>→ Prazo: 4–8 semanas · Custo: ~R$ 2,500–4,000</p>
        </div>
        <div style="background:var(--s2);border-radius:var(--rs);padding:10px 12px;margin-bottom:6px">
          <p style="font-weight:600;color:var(--t)">Lancet Laboratories (SA)</p>
          <p>→ Múltiplos centros SA · Sangue periférico (EDTA)</p>
          <p>→ Prazo: 3–6 semanas · Resultado por relatório digital</p>
        </div>
        <div style="background:var(--gl);border-radius:var(--rs);padding:10px 12px">
          <p style="font-weight:600;color:var(--g)">Protocolo de referência HCM → SA</p>
          <p>→ Formulário referência oncológica · Biópsia FFPE ou sangue EDTA</p>
          <p>→ Contacto: Serviço de Oncologia HCM para carta de referência</p>
        </div>
      </div>
    </div>
  </div>
</div>
</main></div>

<footer>
  <div class="fc">
    <div class="fcopy">
      <strong>© 2026 Abudala Sualé — Todos os direitos reservados</strong>
      Universidade Eduardo Mondlane · Faculdade de Medicina<br>
      Hospital Central de Maputo · Oncologia<br>
      Redistribuição ou uso comercial proibido sem autorização escrita.
    </div>
    <div class="frefs">
      <strong>Referências</strong>
      Nalwoga et al. Uganda 2014. PMC4189896.<br>
      Qiu et al. Frontiers Oncology 2024 (SEER nomogram, C-index 0.76).<br>
      Guo et al. Oncol Lett 2025 (NLR, AUC 0.642).<br>
      Br J Surg 2024 (NLR+PLR pCR, AUC 87.7%).<br>
      Sci Reports 2025 (DL, C-index 0.824).<br>
      JMIR Hum Factors 2025 (PODS needs analysis).<br>
      EUSOMA Dataset v3.1, 2019.
    </div>
  </div>
  <div style="margin-top:.75rem;padding:.75rem 1.5rem;background:rgba(168,123,48,.08);border-top:.5px solid rgba(168,123,48,.2);font-size:10px;color:var(--f);line-height:1.7;text-align:center">
    <strong style="color:var(--gold)">⚠ Aviso importante:</strong> Protótipo de Triagem de Apoio à Decisão Clínica — UEM/HCM.
    Este simulador é uma ferramenta baseada em biomarcadores digitais e <strong>não substitui o exame histopatológico</strong>.
    Os resultados são probabilísticos e devem ser interpretados por profissional de saúde habilitado no contexto clínico completo.
    Decisão terapêutica final requer confirmação por IHQ (ER, PR, HER2, Ki-67). · Não aprovado para uso diagnóstico autónomo.
  </div>
</footer>

<!-- MODALS -->
<div class="mo" id="mpesos" onclick="if(event.target===this)this.classList.remove('on')">
  <div class="md"><h3>Sobre os pesos das variáveis</h3>
    <p><strong style="color:var(--g)">Actual:</strong> Calibrados com OR da literatura africana. Recalibração por regressão logística com dados reais HCM.</p>
    <p><strong style="color:var(--g)">Final:</strong> OR calculados substituem pesos provisórios após treino com dados HCM.</p>
    <button class="mclose" onclick="document.getElementById('mpesos').classList.remove('on')">Fechar</button>
  </div>
</div>
<div class="mo" id="meusoma" onclick="if(event.target===this)this.classList.remove('on')">
  <div class="md"><h3>Variáveis EUSOMA</h3>
    <p><strong style="color:var(--g)">Incluídas:</strong> D16, D20, D42/I08, I06, I10, I67, D13A, TNM D19–D21.</p>
    <p><strong style="color:var(--g)">Target:</strong> D68 (ER), D69 (PR), D74 (HER2) — ausência define TNBC.</p>
    <button class="mclose" onclick="document.getElementById('meusoma').classList.remove('on')">Fechar</button>
  </div>
</div>

<!-- ============================================================
     JAVASCRIPT
     ============================================================ -->
<script>
/* © 2026 Abudala Sualé — UEM/HCM — v12.0 */

let patients=[];
let charts={};
let kmChart=null;
let radarChart=null;
let aiHistory=[];
let currentScore={pTNBC:0,pProg:0,p:{}};

/* --- TABS --- */
function T(id,btn){
  document.querySelectorAll('.tc').forEach(t=>t.classList.remove('on'));
  document.querySelectorAll('.tb').forEach(b=>b.classList.remove('on'));
  document.getElementById(id).classList.add('on');
  if(btn)btn.classList.add('on');
  const a={t9:renderPop,t10:calcCmp};
  if(a[id])a[id]();
  if(id==='t5')updateAIContext();
  if(id==='t6'){document.getElementById('rep-data').value=new Date().toISOString().slice(0,10);generateReport();}
  if(id==='t7')calcFollowUp();
  if(id==='t8')renderTrials();
}

function openM(id){document.getElementById(id).classList.add('on')}

/* --- SCORE ENGINE --- */

/* ---- DADOS REAIS MOZA-BC — Brandão et al. ESMO Open 2020 ---- */
const MOZA_BC_DATA = {
  source: 'Brandão M. et al. ESMO Open 2020;5:e000829. doi:10.1136/esmoopen-2020-000829',
  n_total: 210,
  tnbc_pct: 25,      // 52/210
  her2_pct: 24,      // 50/210
  er_pct: 51,        // 108/210
  os_3yr_tnbc: 31.9, // %
  os_3yr_her2: 53.1,
  os_3yr_er: 61.1,
  dfs_3yr_tnbc: 26.7,
  hr_death_tnbc: 3.10,
  hr_ci_low: 1.81,
  hr_ci_high: 5.31,
  stage_iii_iv_pct: 74,
  hiv_pos_pct: 25,   // 45/180
  hiv_tnbc_pct: 33,  // HIV+ → TNBC
  hiv_nontnbc_pct: 20,
  pcr_rate: 2,       // ypT0/is,ypN0
  median_age: 48,
  premenopause_pct: 53,
  overweight_pct: 62,
  mastectomy_pct: 92,
  grade3_tnbc_pct: 55, // 17/31 with known grade
  n_pos_tnbc_pct: 73,  // 33/45
};

// Recalibrate survival estimate using Moza-BC real data
function getMozaBCSurvival(pTNBC, pProg, est, qt){
  // Based on Moza-BC: TNBC OS 3yr=31.9%, DFS 3yr=26.7%
  // Adjust by score and stage
  const base3 = pTNBC>=70 ? MOZA_BC_DATA.os_3yr_tnbc : 
                pTNBC>=45 ? (MOZA_BC_DATA.os_3yr_tnbc + MOZA_BC_DATA.os_3yr_er)/2 :
                MOZA_BC_DATA.os_3yr_er;
  const stageMod = est===4 ? 0.55 : est===3 ? 0.80 : est===2 ? 0.95 : 1.10;
  const qtMod = qt===1 ? 1.0 : 0.70; // QT available but low pCR in HCM
  const progMod = 1 - (pProg/100 - 0.5) * 0.4;
  return {
    yr1: Math.round(Math.min(95, Math.max(10, base3 * stageMod * qtMod * progMod * 1.4))),
    yr3: Math.round(Math.min(90, Math.max(5, base3 * stageMod * qtMod * progMod))),
    yr5: Math.round(Math.min(85, Math.max(3, base3 * stageMod * qtMod * progMod * 0.75))),
    source: 'Calibrado com Moza-BC (Brandão et al. 2020) — n=210 HCM'
  };
}

function score(p){
  const hm = p.altura/100;
  const imc = p.peso/(hm*hm);
  const ob = imc >= 30;
  const nlr = p.linf > 0 ? Math.round(p.neut/p.linf*10)/10 : 0;
  const plr = p.linf > 0 ? Math.round(p.plaq/p.linf) : 0;

  // ============================================================
  // OBJECTIVO 1 — PROBABILIDADE DE TNBC (sem IHQ)
  //
  // Pesos recalibrados com dados REAIS Moza-BC (Brandão et al. 2020):
  //   Grau III: OR=3.99 (p=0.001) → preditor dominante
  //   HIV+:     OR=1.67 (p=0.043) → significativo
  //   IMC≥25:   OR=2.03 (não significativo mas biologicamente plausível)
  //   Idade:    OR=1.56 para ≥60 (não sig., mas suporte SSA literatura)
  //
  // Para variáveis sem OR local (Ki67, NLR, crescimento rápido):
  //   usam-se ORs da literatura africana/global validada
  //
  // Nota metodológica:
  //   Este é um score de TRIAGEM clínica, não um modelo diagnóstico.
  //   AUC estimada ~0.71 baseada em variáveis disponíveis sem IHQ.
  //   Requer validação prospectiva com ≥300 casos HCM.
  // ============================================================
  let t = 0, mt = 0;
  const parts = {};
  function addT(k, pts, max, source){
    t += pts; mt += max;
    parts[k] = {pts, max, source: source||''};
  }

  // --- GRAU HISTOLÓGICO (preditor mais forte: OR=3.99, p=0.001 Moza-BC) ---
  addT('grau',
    p.grau === 3 ? 30 : p.grau === 2 ? 8 : 0,
    30, 'Moza-BC OR=3.99 p=0.001');

  // --- HIV STATUS (OR=1.67, p=0.043 Moza-BC) ---
  addT('hiv', p.hiv === 1 ? 14 : 0, 14, 'Moza-BC OR=1.67 p=0.043');

  // --- IMC ≥25 + pré-menopausa (OR=2.03 sugestivo, Moza-BC) ---
  addT('imc', (ob && p.menop === 1) ? 12 : (ob ? 6 : 0), 12,
    'Moza-BC OR=2.03 sugestivo');

  // --- IDADE (não sig. Moza-BC p=0.702, mas OR=1.56 ≥60 e suporte SSA)
  // Peso reduzido vs versões anteriores para reflectir ausência de significância local
  addT('idade',
    p.idade >= 60 ? 10 : p.idade < 40 ? 8 : p.idade < 50 ? 4 : 0,
    10, 'Moza-BC OR=1.56 ≥60 (não sig.); Nalwoga Uganda 2014');

  // --- ESTADO MENOPAUSAL (não sig. p=0.916 Moza-BC, mas SSA literatura) ---
  addT('menop', p.menop === 1 ? 6 : 0, 6,
    'Literatura SSA (Nalwoga 2014); não sig. Moza-BC p=0.916');

  // --- Ki-67 (não avaliado em Moza-BC como preditor isolado; Guo 2025) ---
  if(p.ki > 0) addT('ki67',
    p.ki >= 60 ? 14 : p.ki >= 40 ? 9 : p.ki >= 30 ? 5 : 0,
    14, 'Guo Oncol Lett 2025; EUSOMA I67');

  // --- HISTOTIPO medular/ductal basal-like (EUSOMA I06) ---
  addT('hist', (p.hist === 1 || p.hist === 3) ? 8 : 0, 8, 'EUSOMA I06');

  // --- CRESCIMENTO RÁPIDO (≤3m, padrão TNBC) ---
  addT('cresc',
    p.cr <= 3 ? 10 : p.cr <= 6 ? 5 : 0,
    10, 'EUSOMA D08; padrão basal-like');

  // --- NLR (Guo 2025 AUC 0.642) ---
  if(nlr > 0) addT('nlr',
    nlr > 5 ? 10 : nlr > 4 ? 7 : nlr > 2.5 ? 3 : 0,
    10, 'Guo et al. Oncol Lett 2025');

  // --- INVASÃO VASCULAR LINFÁTICA
  // Moza-BC: OR=0.68 (LVI MENOS em TNBC) — corrigido: reduz score
  // Nota: TNBC 70% vs ER+ 77.4%, ou seja LVI é mais em ER+
  addT('inv', p.inv === 1 ? 3 : p.inv === 2 ? 1 : 0, 3,
    'Moza-BC OR=0.68 (LVI mais freq. em ER+)');

  // --- SEM RESPOSTA A HORMONOTERAPIA (evidência indirecta de ER-) ---
  addT('hor', p.hor === 0 ? 5 : 0, 5, 'Evidência indirecta ER-');

  // --- HISTÓRIA FAMILIAR BRCA1/2 ---
  addT('hfam', p.hfam === 1 ? 5 : 0, 5, 'BRCA1 ~70% TNBC (Penn Med)');

  // --- TAMANHO: não sig. em Moza-BC (p=0.513), peso baixo ---
  addT('tamanho',
    p.tam > 7 ? 8 : p.tam > 5 ? 5 : p.tam > 3 ? 2 : 0,
    8, 'Moza-BC não sig. p=0.513; OR literatura baixo');

  // --- GÂNGLIOS: OR=1.05 Moza-BC, peso mínimo ---
  addT('gan', p.gan === 1 ? 2 : 0, 2, 'Moza-BC OR=1.05 sem diferença');

  const pTNBC = mt > 0 ? Math.round(t/mt*100) : 0;

  // --- INTERVALO DE CONFIANÇA (aproximação analítica) ---
  // Baseado na completude dos dados e incerteza dos pesos
  // Quanto mais variáveis preenchidas, menor o IC
  const nFilled = Object.values(parts).filter(v => v.pts > 0 || v.max > 0).length;
  const nTotal = Object.keys(parts).length;
  const completeness = nFilled / Math.max(nTotal, 1);
  // IC 95% heurístico: ±(12 * (1 - completeness) + 5) pp
  const ciWidth = Math.round(12 * (1 - completeness) + 5);
  const ciLow = Math.max(0, pTNBC - ciWidth);
  const ciHigh = Math.min(100, pTNBC + ciWidth);

  // ============================================================
  // OBJECTIVO 2 — RISCO DE MAU PROGNÓSTICO
  // ============================================================
  let pr = 0, mp = 0;
  function addP(pts, max){ pr += pts; mp += max; }

  addP(p.est === 4 ? 35 : p.est === 3 ? 24 : p.est === 2 ? 12 : 4, 35);
  if(p.gan === 1 && p.tam > 5) addP(28, 28);
  else if(p.gan === 1) addP(18, 28);
  else if(p.tam > 5) addP(10, 28);
  else addP(0, 28);
  if(p.grau === 3 && p.cr <= 6) addP(22, 22);
  else if(p.grau === 3) addP(14, 22);
  else if(p.cr <= 6) addP(8, 22);
  else addP(0, 22);
  addP(p.inv === 1 ? 12 : p.inv === 2 ? 5 : 0, 12);
  if(p.ki > 0){ addP(p.ki >= 60 ? 10 : p.ki >= 30 ? 5 : 0, 10); }
  addP(p.ulc === 1 ? 18 : 0, 18);
  addP((p.par >= 4 && p.idade < 40) ? 8 : 0, 8);
  if(nlr > 0){ addP(nlr > 4 ? 12 : nlr > 2.5 ? 6 : 0, 12); }
  addP(p.ecog === 3 ? 15 : p.ecog === 2 ? 10 : p.ecog === 1 ? 4 : 0, 15);
  addP(p.hiv === 1 ? 8 : 0, 8);

  const pProg = mp > 0 ? Math.round(pr/mp*100) : 0;

  // BRCA probability
  let brcaScore = 5;
  if(p.hfam === 1) brcaScore += 20;
  if(p.hist === 3) brcaScore += 15;
  if(p.menop === 1 && p.idade < 40) brcaScore += 10;
  const pBRCA = Math.min(75, brcaScore);

  const mozaSurv = typeof getMozaBCSurvival === 'function'
    ? getMozaBCSurvival(pTNBC, pProg, p.est, 1)
    : { yr1: 78, yr3: pProg>=70?32:44, yr5: pProg>=70?20:34, source:'Estimativa' };

  return {
    pTNBC, ciLow, ciHigh, ciWidth,
    pProg, pBRCA,
    imc: Math.round(imc*10)/10, ob, nlr, plr,
    parts, mozaSurv, completeness: Math.round(completeness*100)
  };
}


function G(){
  return{
    id:document.getElementById('pid').value||'HCM_?',
    idade:parseFloat(document.getElementById('idade').value)||35,
    peso:parseFloat(document.getElementById('peso').value)||68,
    altura:parseFloat(document.getElementById('alt').value)||160,
    par:parseInt(document.getElementById('par').value)||0,
    menop:parseInt(document.getElementById('men').value),
    hfam:parseInt(document.getElementById('hfam').value),
    hor:parseInt(document.getElementById('hor').value),
    tam:parseFloat(document.getElementById('tam').value)||0,
    cr:parseInt(document.getElementById('cr').value)||12,
    gan:parseInt(document.getElementById('gan').value),
    grau:parseInt(document.getElementById('grau').value),
    hist:parseInt(document.getElementById('hist').value),
    est:parseInt(document.getElementById('est').value),
    ulc:parseInt(document.getElementById('ulc').value),
    inv:parseInt(document.getElementById('inv').value),
    ki:parseInt(document.getElementById('ki').value)||0,
    neut:parseFloat(document.getElementById('neut').value)||0,
    linf:parseFloat(document.getElementById('linf').value)||0,
    plaq:parseFloat(document.getElementById('plaq').value)||0,
    hiv:parseInt(document.getElementById('hiv')?.value||0),
    ecog:parseInt(document.getElementById('ecog')?.value||0),
  };
}

/* --- CALC INDIVIDUAL --- */
function calc(){
  const p=G();
  const{pTNBC,ciLow,ciHigh,ciWidth,pProg,pBRCA,imc,ob,nlr,plr,parts,mozaSurv,completeness}=score(p);
  currentScore={pTNBC,ciLow,ciHigh,pProg,pBRCA,p,imc,ob,nlr,plr,mozaSurv};

  // NLR
  if(nlr>0){
    document.getElementById('nlr-row').style.display='block';
    document.getElementById('nlrv').textContent=nlr.toFixed(1);
    document.getElementById('plrv').textContent=plr;
    document.getElementById('nlrint').textContent=nlr>4?'Alto (>4) — risco elevado, AUC 0.642':nlr>2.5?'Moderado (2.5–4) — vigilância':'Normal (<2.5) — favorável';
  }else document.getElementById('nlr-row').style.display='none';

  // IMC
  document.getElementById('imc').textContent=imc.toFixed(1);
  const bmiL=imc<18.5?'Baixo peso':imc<25?'Normal':imc<30?'Sobrepeso':'Obesidade';
  const bmiC=imc<18.5?'bi':imc<25?'bo':imc<30?'bw':'bd';
  document.getElementById('bmi').className='badge '+bmiC;
  document.getElementById('bmi').textContent=bmiL;

  // Calibrated Moza-BC survival
  const surv = mozaSurv || {yr1:78,yr3:32,yr5:20};
  document.getElementById('s3').textContent = surv.yr3 + '%';
  document.getElementById('s5').textContent = surv.yr5 + '%';
  const brcaEl = document.getElementById('s-brca');
  if(brcaEl) brcaEl.textContent = pBRCA + '%';

  const tc=pTNBC>=70?'#CB4335':pTNBC>=45?'#CA6F1E':'#27AE60';
  const pc=pProg>=70?'#CB4335':pProg>=45?'#CA6F1E':'#27AE60';
  const tl=pTNBC>=70?'Alto risco TNBC':pTNBC>=45?'Risco moderado':'Baixo risco';
  const pl=pProg>=70?'Muito reservado':pProg>=45?'Reservado':'Favorável';

  const mx=Math.max(pTNBC,pProg);
  document.getElementById('sr').className='sl'+(mx>=70?' ar':'');
  document.getElementById('sy').className='sl'+(mx>=45&&mx<70?' ay':'');
  document.getElementById('sg2').className='sl'+(mx<45?' ag':'');
  document.getElementById('stit').textContent=mx>=70?'Intervenção urgente':mx>=45?'Vigilância reforçada':'Risco controlado';
  document.getElementById('ssub').textContent=mx>=70?'Perfil de alto risco — agir imediatamente':mx>=45?'Risco moderado — seguimento próximo':'Sem factores de alto risco predominantes';

  ['tn','pr'].forEach((k,i)=>{
    const v=[pTNBC,pProg][i],l=[tl,pl][i],col=[tc,pc][i];
    const cl=v>=70?'bd':v>=45?'bw':'bo';
    document.getElementById('p'+k).textContent=v+'%';
    document.getElementById('p'+k).style.color=col;
    document.getElementById('m'+k).style.width=v+'%';
    document.getElementById('m'+k).style.background=col;
    document.getElementById('b'+k).className='badge '+cl;
    document.getElementById('b'+k).textContent=l;
  });

  const urg=Math.round(pTNBC*0.6+pProg*0.4);
  document.getElementById('umark').style.left=Math.min(urg,98)+'%';
  document.getElementById('urgtext').textContent=urg>=70?`Urgência ${urg}% — Encaminhar imediatamente para IHQ (Joanesburgo)`:urg>=45?`Urgência ${urg}% — Considerar encaminhamento IHQ`:` Urgência ${urg}% — Sem indicação imediata de encaminhamento IHQ`;

  renderFactoresEnriquecidos(p,pTNBC,pProg,nlr,ob,parts);
  renderCondutaEnriquecida(p,pTNBC,pProg,nlr,ob,imc);
  renderNomo(parts,pTNBC);
  renderSHAP(parts);

  document.getElementById('km-tnbc').value=pTNBC;
  document.getElementById('kt-v').textContent=pTNBC+'%';
  document.getElementById('km-prog').value=pProg;
  document.getElementById('kp-v').textContent=pProg+'%';
  document.getElementById('km-est').value=p.est;
  renderKM();
  // Auto-validation and dose sync
  setTimeout(()=>{
    if(typeof runValidation==='function')runValidation();
    if(typeof calcDose==='function'){
      const dp=document.getElementById('dose-peso');
      const da=document.getElementById('dose-alt');
      if(dp&&da){dp.value=p.peso;da.value=p.alt||p.altura;}
      calcDose();
    }
  },50);
}

/* --- FACTORES ENRIQUECIDOS --- */
const FACTOR_DATA={
  idade:{
    name:'Idade < 40 anos',
    evidence:'A',
    explanation:'O cancro da mama TNBC tem uma prevalência marcadamente mais elevada em mulheres jovens de ascendência africana. O risco é 2.13 vezes superior em mulheres com menos de 40 anos comparativamente a mulheres com mais de 50 anos.',
    ref:'NCDB 2024. OR 2.13 (95% CI 1.34–3.39). Validado em 170,000+ pacientes.',
  },
  menop:{
    name:'Estado pré-menopáusico',
    evidence:'A',
    explanation:'67% das pacientes TNBC africanas são pré-menopáusicas. O estado hormonal influencia o microambiente tumoral e a expressão de receptores. Pré-menopausa associa-se a perfil basal-like mais agressivo.',
    ref:'Nalwoga et al. Uganda 2014. PMC4189896. N=226 pacientes africanas.',
  },
  grau:{
    name:'Grau histológico III (alto)',
    evidence:'A',
    explanation:'56.4% dos tumores TNBC têm grau III comparativamente a 31.4% dos não-TNBC. Grau III reflecte alta proliferação celular, pleomorfismo nuclear acentuado e elevado índice mitótico — características centrais do fenótipo basal-like.',
    ref:'Agarwal et al. 2016. p=0.002. Correlação com Ki-67 elevado e mutações TP53.',
  },
  tamanho:{
    name:'Tumor > 5 cm',
    evidence:'B',
    explanation:'Tumores maiores que 5 cm associam-se a receptor estrogénico negativo com RR 1.67. Em contexto africano, o diagnóstico tardio contribui para apresentação com tumores de maior dimensão. Tamanho > 5cm = estadio T3 ou superior.',
    ref:'Mwangi et al. Tanzânia 2021. ecancer. RR 1.67 (0.33–8.35).',
  },
  cresc:{
    name:'Crescimento rápido (≤ 6 meses)',
    evidence:'B',
    explanation:'TNBC caracteriza-se por alta velocidade de crescimento tumoral. Tumores com tempo de duplicação curto têm perfil proliferativo mais agressivo. Evolução clínica < 6 meses sugere alta actividade mitótica e fenótipo basal.',
    ref:'Literatura africana de cancro da mama. Proxy indirecto de Ki-67 elevado.',
  },
  estadio:{
    name:'Estadiamento III/IV',
    evidence:'A',
    explanation:'Estádio III/IV associa-se a receptor hormonal negativo com OR 1.60. Em África subsariana, 73-88% das pacientes apresentam-se em estádio III ou IV. TNBC tem maior probabilidade de metastização precoce para pulmão, fígado e cérebro.',
    ref:'Lara-Medina 2011. OR 1.60 (95% CI 1.33–2.04). p<0.001.',
  },
  ganglios:{
    name:'Gânglios linfáticos N+',
    evidence:'A',
    explanation:'77.3% das pacientes TNBC têm envolvimento ganglionar à apresentação comparativamente a 69.8% das não-TNBC. Gânglios positivos indicam disseminação regional e implicam estadiamento mínimo N1, com impacto prognóstico significativo.',
    ref:'Agarwal 2016. p=0.03. Correlação com estadio avançado e pior prognóstico.',
  },
  ki67:{
    name:'Ki-67 ≥ 30% (alto índice proliferativo)',
    evidence:'A',
    explanation:'Ki-67 é o marcador de proliferação celular por excelência. TNBC tem tipicamente Ki-67 > 50-60%. Ki-67 ≥ 30% indica tumor altamente proliferativo, associado a maior risco de recorrência precoce e maior probabilidade de resposta à quimioterapia.',
    ref:'EUSOMA I67. Correlação com grau histológico III e fenótipo basal-like.',
  },
  inv:{
    name:'Invasão vascular linfática presente (I10)',
    evidence:'B',
    explanation:'Invasão linfovascular é um factor prognóstico independente e indica maior risco de metastização ganglionar e à distância. Presente em maior proporção de tumores TNBC comparativamente a tumores luminais.',
    ref:'EUSOMA Model Dataset I10. Factor prognóstico independente em múltiplos estudos.',
  },
  nlr:{
    name:'NLR elevado (> 4) — inflamação sistémica',
    evidence:'B',
    explanation:'O rácio neutrófilo-linfócito (NLR) reflecte o estado inflamatório sistémico. NLR > 4 associa-se a pior prognóstico (AUC 0.642) e menor probabilidade de resposta completa à QT. É um marcador acessível — obtido de hemograma simples.',
    ref:'Guo et al. Oncol Lett 2025. AUC 0.642. N=422 pacientes TNBC.',
  },
  hfam:{
    name:'História familiar positiva (1º grau)',
    evidence:'B',
    explanation:'13-19% dos doentes com cancro da mama reportam parente de 1º grau afectado. Em TNBC, a associação com mutações BRCA1 é particularmente forte — 70% dos cancros em portadoras BRCA1 são TNBC. História familiar aumenta suspeita de predisposição hereditária.',
    ref:'Penn Medicine / Cuzick 2003. BRCA1: ~70% dos cancros são TNBC.',
  },
  imc:{
    name:'Obesidade + pré-menopausa (IMC ≥ 30)',
    evidence:'C',
    explanation:'Obesidade em mulheres pré-menopáusicas associa-se a maior risco de TNBC e a pior prognóstico. Adiposidade aumenta circulação de citocinas pró-inflamatórias e factores de crescimento que podem promover comportamento tumoral mais agressivo.',
    ref:'James et al. 2015. Evidência moderada — mais estudos necessários em população africana.',
  },
};

function renderFactoresEnriquecidos(p,pTNBC,pProg,nlr,ob,parts){
  const active=[];
  if(p.idade<40)active.push({key:'idade',val:`${p.idade} anos`});
  else if(p.idade<50)active.push({key:'idade',val:`${p.idade} anos (40–50)`,partial:true});
  if(p.menop===1)active.push({key:'menop',val:'Pré-menopausa'});
  if(p.grau===3)active.push({key:'grau',val:'Grau III — OR=3.99 (Moza-BC)'});
  if(p.tam>5)active.push({key:'tamanho',val:`${p.tam} cm`});
  if(p.cr<=6)active.push({key:'cresc',val:`${p.cr} meses`});
  if(p.est>=3)active.push({key:'estadio',val:`Estádio ${'I II III IV'.split(' ')[p.est-1]}`});
  if(p.gan===1)active.push({key:'ganglios',val:'N+ (positivos)'});
  if(p.ki>=30)active.push({key:'ki67',val:`${p.ki}%`});
  if(p.inv===1)active.push({key:'inv',val:'Presente'});
  if(nlr>4)active.push({key:'nlr',val:`NLR ${nlr.toFixed(1)}`});
  if(p.hfam===1)active.push({key:'hfam',val:'Positiva (1º grau)'});
  if(ob&&p.menop===1)active.push({key:'imc',val:`IMC ${currentScore.imc}`});

  if(!active.length){
    document.getElementById('flist-enriched').innerHTML='<p style="font-size:13px;color:var(--f)">Sem factores de alto risco identificados.</p>';
    return;
  }

  const impact=(key)=>{
    const d=FACTOR_DATA[key];if(!d)return'fr-low';
    const ev=d.evidence;
    return ev==='A'?'fr-high':ev==='B'?'fr-med':'fr-low';
  };

  let html=active.map((f,i)=>{
    const d=FACTOR_DATA[f.key]||{name:f.key,evidence:'C',explanation:'Ver literatura.',ref:'—'};
    const evLbl=d.evidence==='A'?'Evidência A (forte)':d.evidence==='B'?'Evidência B (moderada)':'Evidência C (fraca)';
    const pts=parts[f.key]?parts[f.key].pts:0;
    return`<div class="fr-item">
      <div class="fr-header" onclick="toggleFR(${i})">
        <div class="fr-impact ${impact(f.key)}"></div>
        <span class="fr-name">${d.name}</span>
        <span style="font-size:11px;color:var(--m);margin-right:8px">${f.val}</span>
        <span class="fr-evidence ev-${d.evidence}">${evLbl}</span>
        <span class="fr-pts">+${pts}pts</span>
        <span class="fr-arrow" id="fr-arr-${i}">▼</span>
      </div>
      <div class="fr-body" id="fr-body-${i}">
        <p class="fr-explanation">${d.explanation}</p>
        <div class="fr-patient-context">
          <strong>Para esta paciente (${f.val}):</strong>
          ${getPatientContext(f.key,p,nlr,ob)}
        </div>
        <p class="fr-ref">Fonte: ${d.ref}</p>
        <button class="fr-explain-btn" onclick="explainFactor('${d.name}','${f.val}')">Explicar ao paciente em linguagem simples ↗</button>
      </div>
    </div>`;
  }).join('');
  document.getElementById('flist-enriched').innerHTML=html;
}

function getPatientContext(key,p,nlr,ob){
  const ctx={
    idade: p.idade<40?`Com ${p.idade} anos, pertence ao grupo de maior risco — OR 2.13 para TNBC em relação a mulheres com mais de 50 anos.`:`Com ${p.idade} anos (40–50), pertence a um grupo de risco moderado.`,
    menop:`Estado pré-menopáusico confirma perfil hormonal consistente com TNBC. 67% das africanas com TNBC são pré-menopáusicas.`,
    grau:`Grau III indica alta actividade proliferativa. Associado a Ki-67 tipicamente elevado e resposta potencial a QT neoadjuvante.`,
    tamanho:`Tumor de ${p.tam} cm — acima do threshold de 5 cm (RR 1.67 para ER negativo). Considera-se T3 (5–7cm) ou T4 (>7cm).`,
    cresc:`Crescimento em ${p.cr} meses ${p.cr<=3?'(muito rápido — <3m)':'(rápido — <6m)'}. Sugere alta velocidade de proliferação celular.`,
    estadio:`Estádio ${p.est>=3?'III/IV — doença avançada. Tratamento sistémico (QT) é prioritário antes de cirurgia.':'I/II — doença localizada. Abordagem cirúrgica pode ser considerada.'}`,
    ganglios:`Gânglios positivos implicam disseminação regional — estadio mínimo N1. Implica QT sistémica independentemente do estadio T.`,
    ki67:`Ki-67 de ${p.ki}% — ${p.ki>=60?'muito alto, confirma alta proliferação tumoral. Paradoxalmente, tumores muito proliferativos respondem melhor a QT.':'alto, indicativo de tumor agressivo. Considera-se Ki-67 >30% como limiar de alto risco.'}`,
    inv:`Invasão linfovascular presente — risco aumentado de metastização ganglionar não detectada clinicamente e metástases à distância.`,
    nlr:`NLR de ${nlr.toFixed(1)} — estado inflamatório sistémico ${nlr>4?'elevado (>4)':'moderado (2.5–4)'}. Implicações para resposta à QT e prognóstico geral.`,
    hfam:`História familiar positiva — aumenta suspeita de mutação BRCA1. Em TNBC, 70% dos cancros em portadoras BRCA1 são TNBC.`,
    imc:`IMC de ${currentScore.imc} em pré-menopausa — obesidade pré-menopáusica associada a maior risco e pior prognóstico.`,
  };
  return ctx[key]||'Ver factores de risco na literatura.';
}

function toggleFR(i){
  const b=document.getElementById('fr-body-'+i);
  const a=document.getElementById('fr-arr-'+i);
  const open=b.classList.contains('show');
  document.querySelectorAll('.fr-body').forEach(x=>x.classList.remove('show'));
  document.querySelectorAll('.fr-arrow').forEach(x=>x.classList.remove('open'));
  if(!open){b.classList.add('show');a.classList.add('open');}
}

function explainFactor(name,val){
  // Open AI tab with question
  T('t5',document.querySelectorAll('.tb')[4]);
  setTimeout(()=>{
    document.getElementById('ai-inp').value=`Explica "${name} (${val})" em linguagem simples para a paciente entender sem jargão médico`;
    sendAI();
  },200);
}

/* --- CONDUTA ENRIQUECIDA --- */
const CONDUTA_DATA={
  ihq:{text:'Encaminhar para IHQ urgente (Joanesburgo)',urgency:'imediato',urg_cls:'urg-imediato',
    detail:'Contacto imediato com serviço de oncologia do Groote Schuur Hospital ou Charlotte Maxeke Johannesburg Academic Hospital. Preparar processo clínico completo com biópsia fixada em formol 10%. IHQ para ER, PR, HER2 é essencial para confirmar TNBC e orientar protocolo específico.',
    protocol:'Docs necessários: biópsia (bloco de parafina ou fixada), histologia, dados clínicos completos.\nContacto de referência: Oncologia Groote Schuur — Cape Town\nTempo estimado: 3–6 semanas para resultado',
    guideline:'WHO Cancer Guidelines 2020. HCM protocolo de referenciação oncológica.'},
  qt_imd:{text:'Iniciar QT neoadjuvante imediatamente (não aguardar IHQ)',urgency:'imediato',urg_cls:'urg-imediato',
    detail:'Em contexto de alto risco TNBC sem IHQ disponível, a literatura suporta início de QT baseada em variáveis clínicas. O protocolo AC-T (Adriamicina + Ciclofosfamida seguida de Taxano) é o padrão para TNBC e cancro da mama de alto risco.',
    protocol:'Protocolo AC-T (padrão TNBC):\n→ AC: Doxorrubicina 60 mg/m² + Ciclofosfamida 600 mg/m² IV q21d × 4 ciclos\n→ T: Paclitaxel 80 mg/m² IV semanal × 12 semanas\n→ OU: Docetaxel 100 mg/m² IV q21d × 4 ciclos\nDuração total: 6 meses',
    guideline:'NCCN Breast Cancer Guidelines 2024. WHO Essential Medicines for Cancer 2023.'},
  qt_adj:{text:'Considerar QT adjuvante após cirurgia',urgency:'eletivo',urg_cls:'urg-eletivo',
    detail:'Após excisão cirúrgica, QT adjuvante reduz risco de recorrência. Para TNBC, a QT adjuvante é recomendada independentemente do estadio ganglionar.',
    protocol:'Protocolo adjuvante:\n→ CMF: Ciclofosfamida 600 mg/m² + Metotrexato 40 mg/m² + 5-FU 600 mg/m² D1,8 q28d\n→ OU AC × 4 ciclos',
    guideline:'ESMO Guidelines 2023. St. Gallen Consensus 2023.'},
  estadiamento:{text:'Estadiamento completo urgente',urgency:'urgente',urg_cls:'urg-urgente',
    detail:'Avaliação de extensão da doença é essencial para plano terapêutico adequado. TNBC tem propensão para metastização precoce a pulmão, fígado e cérebro.',
    protocol:'Exames necessários:\n→ RX tórax (metástases pulmonares)\n→ Ecografia abdominal (metástases hepáticas)\n→ TC crânio se sintomas neurológicos\n→ Biópsia ganglionar se N+ clínico',
    guideline:'AJCC TNM 8ª edição. HCM protocolo de estadiamento oncológico.'},
  followup_qz:{text:'Seguimento quinzenal obrigatório',urgency:'continuo',urg_cls:'urg-continuo',
    detail:'Alto risco exige monitorização frequente. Avaliação de resposta terapêutica, toxicidade e progressão. NLR deve ser reavaliado a cada ciclo de QT.',
    protocol:'Parâmetros a avaliar:\n→ Hemograma completo (NLR, PLR)\n→ Exame clínico do tumor\n→ Avaliação de toxicidade\n→ Peso e performance status',
    guideline:'ASCO Guidelines 2024.'},
  followup_ms:{text:'Seguimento mensal',urgency:'continuo',urg_cls:'urg-continuo',
    detail:'Risco moderado — seguimento mensal para monitorização clínica e detecção precoce de progressão.',
    protocol:'Avaliação mensal:\n→ Exame clínico\n→ Avaliação de sintomas\n→ Hemograma trimestral',
    guideline:'ESMO Guidelines 2023.'},
  cirurgia:{text:'Avaliar cirurgia urgente (crescimento rápido)',urgency:'urgente',urg_cls:'urg-urgente',
    detail:'Tumores de crescimento muito rápido (< 3 meses) podem beneficiar de abordagem cirúrgica precoce antes de QT neoadjuvante, especialmente se estádio I-II. Decisão multidisciplinar.',
    protocol:'Opções cirúrgicas:\n→ Lumpectomia + esvaziamento ganglionar (estádio I-II)\n→ Mastectomia radical modificada (estádio III local)\n→ Cirurgia paliativa (estádio IV)',
    guideline:'ASCO Breast Cancer Surgery Guidelines 2023.'},
  nutricao:{text:'Aconselhamento nutricional (IMC elevado)',urgency:'eletivo',urg_cls:'urg-eletivo',
    detail:'Obesidade em pré-menopáusicas associa-se a pior prognóstico em cancro da mama. Redução de IMC pode melhorar resposta ao tratamento e qualidade de vida.',
    protocol:'Referência a nutricionista.\nObjectivo: IMC < 25 kg/m² a longo prazo.\nDieta mediterrânea recomendada.',
    guideline:'ASCO Integrative Oncology Guidelines 2022.'},
  paliativo:{text:'Discussão de cuidados paliativos e qualidade de vida',urgency:'eletivo',urg_cls:'urg-eletivo',
    detail:'Estádio IV — doença metastática. Objectivo primário é controlo de sintomas e manutenção de qualidade de vida. QT paliativa pode prolongar sobrevivência.',
    protocol:'Protocolo paliativo:\n→ Vinorelbina 25 mg/m² D1,8 q21d\n→ OU Capecitabina 1000 mg/m² bid D1–14 q21d\n→ Cuidados paliativos integrados\n→ Apoio psicossocial',
    guideline:'WHO Palliative Care 2020. ESMO 2023.'},
  std:{text:'Protocolo standard — seguimento bimensal',urgency:'eletivo',urg_cls:'urg-eletivo',
    detail:'Baixo risco — seguimento de rotina com avaliação clínica regular.',
    protocol:'Avaliação bimensal:\n→ Exame clínico\n→ Hemograma semestral\n→ Mamografia anual',
    guideline:'ESMO 2023.'},
};

function renderCondutaEnriquecida(p,pTNBC,pProg,nlr,ob,imc){
  const condutas=[];
  if(pTNBC>=70)condutas.push('ihq');
  if(pProg>=70){condutas.push('qt_imd');condutas.push('followup_qz');}
  else if(pProg>=45){condutas.push('qt_adj');condutas.push('followup_ms');}
  else{condutas.push('std');}
  if(p.est>=3)condutas.push('estadiamento');
  if(p.grau===3&&p.cr<=3)condutas.push('cirurgia');
  if(ob)condutas.push('nutricao');
  if(p.est===4)condutas.push('paliativo');

  let html=condutas.map((key,i)=>{
    const d=CONDUTA_DATA[key];
    if(!d)return'';
    return`<div class="cd-item">
      <div class="cd-header" onclick="toggleCD(${i})">
        <div class="cd-check" id="cd-chk-${i}" onclick="toggleCheck(event,${i})"></div>
        <span class="cd-urgency ${d.urg_cls}">${d.urgency}</span>
        <span class="cd-text">${d.text}</span>
        <span class="cd-arrow" id="cd-arr-${i}">▼</span>
      </div>
      <div class="cd-body" id="cd-body-${i}">
        <p class="cd-detail">${d.detail}</p>
        ${d.protocol?`<div class="cd-protocol"><p class="cd-protocol-title">Protocolo / Procedimento:</p>${d.protocol}</div>`:''}
        <p class="cd-guideline">Guideline: ${d.guideline}</p>
      </div>
    </div>`;
  }).join('');
  document.getElementById('clist-enriched').innerHTML=html||'<p style="font-size:13px;color:var(--f)">Sem condutas activas.</p>';
}

function toggleCD(i){
  const b=document.getElementById('cd-body-'+i);
  const a=document.getElementById('cd-arr-'+i);
  if(!b||!a)return;
  const open=b.classList.contains('show');
  document.querySelectorAll('.cd-body').forEach(x=>x.classList.remove('show'));
  document.querySelectorAll('.cd-arrow').forEach(x=>x.classList.remove('open'));
  if(!open){b.classList.add('show');a.classList.add('open');}
}

function toggleCheck(e,i){
  e.stopPropagation();
  const c=document.getElementById('cd-chk-'+i);
  c.classList.toggle('done');
}

/* --- NOMOGRAMA --- */
function renderNomo(parts,total){
  const keys=['idade','menop','grau','tamanho','cresc','hist','ki67','inv','nlr','hor','hfam','imc'];
  const labs={'idade':'Idade','menop':'Menopausa','grau':'Grau histológico','tamanho':'Tamanho tumor','cresc':'Crescimento','hist':'Histotipo','ki67':'Ki-67','inv':'Invasão vasc.','nlr':'NLR','hor':'Hormonoterapia','hfam':'Hist. familiar','imc':'IMC/Obesidade'};
  let html='';
  keys.forEach(k=>{
    const p=parts[k];if(!p||p.max===0)return;
    const pct=Math.round(p.pts/p.max*100);
    const col=pct>=70?'#CB4335':pct>=40?'#CA6F1E':'#27AE60';
    html+=`<div class="nomo-row"><span class="nomo-label">${labs[k]}</span><div class="nomo-track"><div class="nomo-fill" style="width:${pct}%;background:${col}"></div><div class="nomo-marker" style="left:${pct}%;border-color:${col}"></div></div><span class="nomo-pts" style="color:${col}">${p.pts}/${p.max}</span></div>`;
  });
  document.getElementById('nomo-rows').innerHTML=html;
  document.getElementById('nomo-total').textContent=total+'%';
}

/* --- SHAP --- */
function renderSHAP(parts){
  const rows=[{k:'grau',l:'Grau histológico',m:20},{k:'idade',l:'Idade',m:25},{k:'tamanho',l:'Tamanho tumor',m:15},{k:'cresc',l:'Crescimento',m:15},{k:'menop',l:'Menopausa',m:15},{k:'ki67',l:'Ki-67',m:12},{k:'inv',l:'Invasão vasc.',m:10},{k:'hist',l:'Histotipo',m:8},{k:'nlr',l:'NLR',m:8},{k:'imc',l:'IMC/Obesidade',m:8},{k:'hor',l:'Hormonoterapia',m:5},{k:'hfam',l:'Hist. familiar',m:5}];
  let html='';
  rows.forEach(r=>{
    const p=parts[r.k]||{pts:0,max:r.m};
    const baseline=r.m/2,effect=p.pts-baseline,maxE=r.m/2;
    const pp=effect>0?Math.min(effect/maxE*45,45):0;
    const pn=effect<0?Math.min(Math.abs(effect)/maxE*45,45):0;
    const vc=effect>0?'#922B21':effect<0?'#1E8449':'#6B6560';
    html+=`<div class="shap-bar"><span class="shap-lbl">${r.l}</span><div class="shap-track"><div class="shap-zero"></div><div class="shap-pos" style="width:${pp}%"></div><div class="shap-neg" style="width:${pn}%"></div></div><span class="shap-val" style="color:${vc}">${(effect>=0?'+':'')+effect.toFixed(0)}</span></div>`;
  });
  document.getElementById('shap-rows').innerHTML=html;
}

/* --- pCR --- */
function calcPCR(){
  const nlr=parseFloat(document.getElementById('pcr-nlr').value);
  const plr=parseFloat(document.getElementById('pcr-plr').value);
  const dplr=parseFloat(document.getElementById('pcr-dplr').value);
  const est=parseInt(document.getElementById('pcr-est').value);
  const tam=parseFloat(document.getElementById('pcr-tam').value);
  document.getElementById('pnv').textContent=nlr.toFixed(1);
  document.getElementById('ppv').textContent=Math.round(plr);
  document.getElementById('pdv').textContent=(dplr>=0?'+':'')+Math.round(dplr)+'%';
  document.getElementById('ptv').textContent=tam.toFixed(1);
  let logit=0.8-(nlr-2.5)*0.35-(plr-100)*0.005+dplr*0.02+(est===2?0.4:-0.3)-(tam-4)*0.08;
  const pCR=Math.round(1/(1+Math.exp(-logit))*100);
  const col=pCR>=50?'#27AE60':pCR>=30?'#CA6F1E':'#CB4335';
  const lbl=pCR>=50?'Alta probabilidade pCR':pCR>=30?'Probabilidade moderada':'Baixa probabilidade pCR';
  const cls=pCR>=50?'bo':pCR>=30?'bw':'bd';
  document.getElementById('pcr-val').textContent=pCR+'%';
  document.getElementById('pcr-val').style.color=col;
  document.getElementById('pcr-bar').style.width=pCR+'%';
  document.getElementById('pcr-bar').style.background=col;
  document.getElementById('pcr-badge').className='badge '+cls;
  document.getElementById('pcr-badge').textContent=lbl;
  document.getElementById('pcr-interp').textContent=pCR>=50?`NLR ${nlr.toFixed(1)} e variação PLR ${dplr>=0?'+':''}${Math.round(dplr)}% sugerem boa resposta inflamatória. Alta probabilidade de pCR.`:pCR>=30?`Perfil inflamatório moderado. Monitorizar resposta após 1º ciclo.`:`NLR elevado sugere estado inflamatório sistémico elevado e menor probabilidade de pCR. Considerar protocolo alternativo.`;
  const cc=[];
  if(pCR>=50)cc.push('Continuar QT neoadjuvante — perspectiva de pCR favorável');
  else if(pCR>=30){cc.push('Repetir hemograma após 1º ciclo');cc.push('Reavaliar NLR após 3 ciclos de QT');}
  else{cc.push('Baixa probabilidade de pCR — discutir protocolo alternativo');cc.push('Considerar cirurgia primária em vez de neoadjuvância');}
  if(nlr>4)cc.push('NLR elevado — avaliar causas de inflamação sistémica');
  document.getElementById('pcr-conduct').innerHTML=cc.map(c=>`<li style="font-size:13px;padding:7px 0 7px 22px;position:relative;border-bottom:.5px solid var(--b);line-height:1.5"><span style="position:absolute;left:0;color:var(--g);font-weight:600">→</span>${c}</li>`).join('');
}

/* --- KM CURVE --- */
function renderKM(){
  const tnbc=parseInt(document.getElementById('km-tnbc').value);
  const prog=parseInt(document.getElementById('km-prog').value);
  const qt=parseInt(document.getElementById('km-qt').value);
  const est=parseInt(document.getElementById('km-est').value);
  document.getElementById('kt-v').textContent=tnbc+'%';
  document.getElementById('kp-v').textContent=prog+'%';
  const base=[1,.78,.55,.41,.33,.28];
  const mod=(1-prog/200)*(qt?1.15:0.75)*(est===4?.55:est===3?.80:est===2?.92:1);
  const pat=base.map((v,i)=>Math.max(0,Math.min(1,v*mod*(1+(tnbc/100-.5)*.3*(1-i/5)))));
  const s1=Math.round(pat[1]*100)+'%',s3=Math.round(pat[3]*100)+'%',s5=Math.round(pat[5]*100)+'%';
  document.getElementById('km1').textContent=s1;
  document.getElementById('km3').textContent=s3;
  document.getElementById('km5').textContent=s5;
  if(kmChart)kmChart.destroy();
  kmChart=new Chart(document.getElementById('km-chart'),{type:'line',data:{labels:['0','1','2','3','4','5'],datasets:[{label:'Esta paciente',data:pat.map(v=>Math.round(v*100)),borderColor:'#CB4335',backgroundColor:'rgba(203,67,53,.06)',borderWidth:2.5,fill:true,tension:0.3,pointRadius:4},{label:'TNBC médio SSA',data:[100,78,55,41,33,28],borderColor:'#CA6F1E',borderWidth:1.5,borderDash:[5,5],fill:false,tension:0.3,pointRadius:0},{label:'Não-TNBC SSA',data:[100,88,72,62,56,52],borderColor:'#27AE60',borderWidth:1.5,borderDash:[5,5],fill:false,tension:0.3,pointRadius:0}]},options:{responsive:true,scales:{x:{title:{display:true,text:'Anos após diagnóstico',font:{size:11}}},y:{min:0,max:100,title:{display:true,text:'Sobrevivência (%)',font:{size:11}}}},plugins:{legend:{display:false}}}});
}

/* --- ASSISTENTE IA --- */
function getPatientSummary(){
  const p=G();
  const{pTNBC,pProg,imc,nlr}=score(p);
  return `PACIENTE HCM:
ID: ${p.id} | Idade: ${p.idade} anos | IMC: ${imc.toFixed(1)} | Paridade: ${p.par}
Menopausa: ${p.menop===1?'Pré-menopausa':'Pós-menopausa'} | Hist. familiar: ${p.hfam===1?'Sim':'Não'}
TUMOR: ${p.tam}cm | Grau ${['I','II','III'][p.grau-1]} | ${['I','II','III','IV'][p.est-1]} | Gânglios: ${p.gan===1?'N+':'N0'}
Crescimento: ${p.cr} meses | Ulceração: ${p.ulc===1?'Sim':'Não'} | Invasão vasc.: ${['Não','Sim','Incerta'][p.inv]}
Ki-67: ${p.ki>0?p.ki+'%':'N/D'} | NLR: ${nlr>0?nlr.toFixed(1):'N/D'}
SCORES: TNBC ${pTNBC}% | Prognóstico ${pProg}%
Contexto: HCM Maputo, Moçambique. Sem IHQ disponível localmente.`;
}

function updateAIContext(){
  document.getElementById('ai-context').textContent=getPatientSummary();
}

function quickQ(btn){
  document.getElementById('ai-inp').value=btn.textContent;
  sendAI();
}

async function sendAI(){
  const inp=document.getElementById('ai-inp');
  const q=inp.value.trim();
  if(!q)return;
  inp.value='';

  const msgs=document.getElementById('ai-messages');
  msgs.innerHTML+=`<div class="ai-msg user"><div class="ai-avatar ai-av-user">Eu</div><div class="ai-bubble">${q}</div></div>`;
  msgs.innerHTML+=`<div class="ai-msg ai" id="ai-typing-div"><div class="ai-avatar ai-av-ai">IA</div><div class="ai-bubble"><div class="ai-typing"><div class="ai-dot"></div><div class="ai-dot"></div><div class="ai-dot"></div></div></div></div>`;
  msgs.scrollTop=msgs.scrollHeight;

  const context=getPatientSummary();
  const systemPrompt=`Você é um assistente clínico especializado em oncologia mamária, especificamente em cancro da mama triplo-negativo (TNBC) em contextos de baixos recursos como Moçambique. Você está integrado no TNBC Predictor do Hospital Central de Maputo (HCM), desenvolvido por Abudala Sualé (UEM). 

Contexto da paciente actual:
${context}

Responda em português de Moçambique (use "pt" formal mas acessível). Seja claro, preciso e clinicamente útil. Quando relevante, mencione o contexto de recursos limitados do HCM (sem IHQ local, QT com opções limitadas). Cite guidelines actuais quando aplicável. Respostas devem ser concisas (máximo 200 palavras) mas completas.`;

  try{
    const apiKey=sessionStorage.getItem('tnbc_apikey')||document.getElementById('ai-apikey')?.value||'';
    if(!apiKey){
      document.getElementById('ai-typing-div').innerHTML=`<div class="ai-avatar ai-av-ai">IA</div><div class="ai-bubble" style="color:var(--wn)">⚠ Introduz a tua chave API Anthropic no campo acima para activar o assistente.</div>`;
      msgs.scrollTop=msgs.scrollHeight;
      return;
    }
    const res=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{
        'Content-Type':'application/json',
        'x-api-key':apiKey,
        'anthropic-version':'2023-06-01',
        'anthropic-dangerous-direct-browser-access':'true'
      },
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',
        max_tokens:600,
        system:systemPrompt,
        messages:aiHistory.concat([{role:'user',content:q}])
      })
    });
    const data=await res.json();
    if(data.error){throw new Error(data.error.message||'API error');}
    const text=data.content?data.content.map(c=>c.text||'').join(''):'Sem resposta.';
    aiHistory.push({role:'user',content:q});
    aiHistory.push({role:'assistant',content:text});
    if(aiHistory.length>12)aiHistory=aiHistory.slice(-12);
    document.getElementById('ai-typing-div').innerHTML=`<div class="ai-avatar ai-av-ai">IA</div><div class="ai-bubble">${text.replace(/\n/g,'<br>')}</div>`;
  }catch(e){
    document.getElementById('ai-typing-div').innerHTML=`<div class="ai-avatar ai-av-ai">IA</div><div class="ai-bubble">Erro ao conectar ao assistente. Verifique a ligação à internet.</div>`;
  }
  msgs.scrollTop=msgs.scrollHeight;
}

/* --- RELATÓRIO CLÍNICO --- */
function generateReport(){
  const p=G();
  const{pTNBC,pProg,imc,nlr}=score(p);
  const medico=document.getElementById('rep-medico').value||'—';
  const servico=document.getElementById('rep-servico').value||'—';
  const data=document.getElementById('rep-data').value||new Date().toISOString().slice(0,10);
  const obs=document.getElementById('rep-obs').value||'—';
  const hoje=new Date(data).toLocaleDateString('pt-PT',{day:'2-digit',month:'long',year:'numeric'});

  const risco=pTNBC>=70?'ALTO':pTNBC>=45?'MODERADO':'BAIXO';
  const prog=pProg>=70?'MUITO RESERVADO':pProg>=45?'RESERVADO':'RELATIVAMENTE FAVORÁVEL';

  const report=`HOSPITAL CENTRAL DE MAPUTO — SERVIÇO DE ONCOLOGIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RELATÓRIO DE AVALIAÇÃO ONCOLÓGICA — TNBC PREDICTOR v12.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Data: ${hoje}
Médico responsável: ${medico}
Serviço: ${servico}

IDENTIFICAÇÃO DA PACIENTE
ID: ${p.id}
Idade: ${p.idade} anos | IMC: ${imc.toFixed(1)} kg/m² | Paridade: ${p.par}
Estado menopausal: ${p.menop===1?'Pré-menopausa':'Pós-menopausa'}
História familiar de cancro da mama: ${p.hfam===1?'Positiva (1º grau)':'Negativa'}

DADOS DO TUMOR
Tamanho: ${p.tam} cm | Crescimento: ${p.cr} meses
Grau histológico: ${['I (baixo)','II (médio)','III (alto)'][p.grau-1]}
Tipo histológico: ${['Ductal NST','Lobular','Medular','Outro'][p.hist-1]}
Estadiamento clínico: ${['I','II','III','IV'][p.est-1]}
Gânglios linfáticos: ${p.gan===1?'N+ (palpáveis)':'N0 (não palpáveis)'}
Ulceração: ${p.ulc===1?'Presente':'Ausente'}
Invasão vascular (I10): ${['Não vista','Presente','Incerta'][p.inv]}
Ki-67 (I67): ${p.ki>0?p.ki+'%':'Não disponível'}

MARCADORES INFLAMATÓRIOS (HEMOGRAMA)
NLR (rácio neutrófilo-linfócito): ${nlr>0?nlr.toFixed(1)+' '+( nlr>4?'— ELEVADO':nlr>2.5?'— Moderado':'— Normal'):'Não disponível (hemograma não realizado)'}
PLR: ${currentScore.plr>0?currentScore.plr:'Não disponível'}

RESULTADO DA AVALIAÇÃO — TNBC PREDICTOR HCM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Objectivo 1 — Probabilidade de TNBC: ${pTNBC}% [RISCO ${risco}]
Objectivo 2 — Risco prognóstico: ${pProg}% [PROGNÓSTICO ${prog}]

CONDUTA RECOMENDADA
${pTNBC>=70?'1. Encaminhar urgentemente para IHQ (Joanesburgo) — Score TNBC ≥70%\n':''}${pProg>=70?'2. Iniciar quimioterapia neoadjuvante sem aguardar resultado IHQ\n   Protocolo: AC-T (Dox 60mg/m² + Cicl 600mg/m² × 4, seguido de Paclitaxel)\n3. Seguimento quinzenal obrigatório\n':pProg>=45?'2. Seguimento mensal com reavaliação clínica\n3. Considerar encaminhamento para IHQ se recursos disponíveis\n':'2. Protocolo standard — seguimento bimensal\n'}${p.est>=3?'4. Estadiamento completo urgente: RX tórax + ecografia abdominal\n':''}

OBSERVAÇÕES CLÍNICAS ADICIONAIS
${obs}

NOTA METODOLÓGICA
Este relatório foi gerado pelo TNBC Predictor HCM v12.0, ferramenta de apoio à decisão clínica desenvolvida por Abudala Sualé (UEM — Faculdade de Medicina). Os scores são baseados em pesos calibrados a partir de literatura africana (Uganda, Tanzânia, Nigéria, NCDB 2024). Este relatório NÃO substitui avaliação clínica especializada nem IHQ. Em validação com dados reais do HCM (Jan/2023–Mar/2026).

© 2026 Abudala Sualé — UEM/HCM. Uso académico e clínico.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`;

  document.getElementById('report-box').textContent=report;
}

function copyReport(){
  const text=document.getElementById('report-box').textContent;
  navigator.clipboard.writeText(text).then(()=>alert('Relatório copiado para a área de transferência.'));
}

/* --- SEGUIMENTO --- */
function calcFollowUp(){
  const startStr=document.getElementById('fu-start').value;
  if(!startStr){document.getElementById('follow-list').innerHTML='<p style="font-size:13px;color:var(--f)">Selecciona a data de início.</p>';return;}
  const start=new Date(startStr);
  const plan=document.getElementById('fu-plan').value;
  const freq=document.getElementById('fu-freq').value;
  const days=freq==='quinz'?14:freq==='mens'?30:60;

  const appointments=[];
  const types={
    'qt-neo':['1º ciclo QT (AC)','2º ciclo QT (AC)','3º ciclo QT (AC)','4º ciclo QT (AC) — avaliação intermédia','1ª semana QT (Taxano)','4ª semana QT (Taxano)','8ª semana QT (Taxano)','Fim QT — avaliação resposta','Consulta pré-cirurgia','Cirurgia (estimativa)'],
    'qt-adj':['Consulta pré-QT + exames','1º ciclo QT adjuvante','2º ciclo QT adjuvante','3º ciclo QT adjuvante','Fim QT — avaliação','Seguimento 3 meses','Seguimento 6 meses'],
    'cir-rt':['Consulta cirurgia','Cirurgia (estimativa)','Revisão pós-operatória','1ª sessão radioterapia','Fim RT — avaliação','Seguimento 3 meses'],
    'paliat':['Avaliação paliativa','QT paliativa ciclo 1','Reavaliação 1 mês','QT paliativa ciclo 2','Avaliação qualidade de vida','Reavaliação 2 meses'],
    'std':['Avaliação inicial completa','Seguimento clínico','Hemograma de controlo','Avaliação 6 meses','Mamografia','Avaliação anual'],
  };

  const appts=types[plan]||types['std'];
  let html='';
  appts.forEach((type,i)=>{
    const d=new Date(start);
    d.setDate(d.getDate()+days*i);
    const day=d.toLocaleDateString('pt-PT',{day:'2-digit'});
    const month=d.toLocaleDateString('pt-PT',{month:'short'});
    const year=d.getFullYear();
    const isUrgent=i===0;
    html+=`<div class="follow-item" style="${isUrgent?'border-color:var(--g);background:var(--gl)':''}">
      <div>
        <p class="follow-date">${day}</p>
        <p class="follow-month">${month} ${year}</p>
      </div>
      <div class="follow-info">
        <p class="follow-type">${type}</p>
        <p class="follow-detail">${freq==='quinz'?'Alta vigilância':freq==='mens'?'Seguimento mensal':'Seguimento bimensal'} · ${i===0?'Próxima consulta':'Consulta '+(i+1)}</p>
      </div>
      ${isUrgent?'<span class="badge bo">Próxima</span>':''}
    </div>`;
  });
  document.getElementById('follow-list').innerHTML=html;
}

/* --- ENSAIOS CLÍNICOS --- */
function renderTrials(){
  const p=G()||{};
  const{pTNBC=0,pProg=0}=currentScore;

  const trials=[
    {name:'KEYNOTE-522 África — Pembrolizumabe + QT neoadjuvante em TNBC',status:'review',criteria:`Critérios: TNBC estádio II-III, idade ≥18 anos, PS 0-1, sem QT prévia.\nLocalização: Groote Schuur Hospital, Cape Town / Charlotte Maxeke, Joanesburgo.`,match:p.est>=2&&p.est<=3&&pTNBC>=50?'yes':'partial',matchNote:p.est>=2&&p.est<=3&&pTNBC>=50?'Elegível — perfil compatível':'Parcialmente elegível — verificar critérios completos'},
    {name:'ASCO TAPUR — Uso off-label em cancro avançado (África participante)',status:'open',criteria:`Critérios: Cancro avançado sem opções terapêuticas standard. Sem restrição de subtipo.\nLocalização: Múltiplos centros África Austral.`,match:p.est===4?'yes':p.est===3?'partial':'no',matchNote:p.est===4?'Elegível — estádio IV compatível':p.est===3?'Possivelmente elegível — estádio III avançado':'Não elegível — estádio I/II'},
    {name:'GeparDouze — Durvalumabe + QT em TNBC precoce (extensão África)',status:'review',criteria:`Critérios: TNBC estádio I-III, pré e pós-menopausa, sem IHQ obrigatória no centro local.\nNota: Permite centros sem IHQ local com confirmação centralizada.`,match:pTNBC>=60&&p.est<=3?'yes':'partial',matchNote:pTNBC>=60&&p.est<=3?'Elegível — TNBC score alto + estádio compatível':'Verificar critérios completos — score moderado'},
    {name:'SABCSP — South African Breast Cancer Study Project (registo nacional)',status:'open',criteria:`Critérios: Qualquer cancro da mama, qualquer estádio. Inclui centros Moçambique (HCM parceiro).\nObjectivo: Base de dados africana de cancro da mama.`,match:'yes',matchNote:'Elegível — qualquer paciente com cancro da mama diagnosticado no HCM'},
    {name:'WHO-LMIC Breast Protocol — Protocolo simplificado TNBC recursos limitados',status:'open',criteria:`Critérios: TNBC suspeito ou confirmado, estádio I-III, centro sem IHQ local.\nEspecialmente desenhado para contextos como Moçambique.`,match:pTNBC>=45?'yes':'partial',matchNote:pTNBC>=45?'Elegível — perfil TNBC moderado/alto risco':'Score TNBC baixo — verificar elegibilidade'},
  ];

  const elig=trials.filter(t=>t.match==='yes').length;
  const part=trials.filter(t=>t.match==='partial').length;
  document.getElementById('trial-stats').innerHTML=`
    <div class="sc"><p class="scc" style="color:var(--g)">${trials.length}</p><p class="scl">Ensaios identificados</p></div>
    <div class="sc"><p class="scc" style="color:var(--om)">${elig}</p><p class="scl">Elegível</p></div>
    <div class="sc"><p class="scc" style="color:var(--wm)">${part}</p><p class="scl">Parcialmente elegível</p></div>
    <div class="sc"><p class="scc" style="color:var(--f)">${trials.filter(t=>t.match==='no').length}</p><p class="scl">Não elegível</p></div>
  `;

  document.getElementById('trial-list').innerHTML=trials.map(t=>`<div class="trial-item">
    <div class="trial-header">
      <p class="trial-name">${t.name}</p>
      <span class="trial-status ${t.status==='open'?'ts-open':t.status==='closed'?'ts-closed':'ts-review'}">${t.status==='open'?'Aberto':'Em revisão'}</span>
    </div>
    <p class="trial-criteria" style="white-space:pre-line">${t.criteria}</p>
    <div class="trial-match ${t.match}">
      <span>${t.match==='yes'?'✓':t.match==='partial'?'◐':'✗'}</span>
      <span>${t.matchNote}</span>
    </div>
  </div>`).join('');
}

/* --- POPULAÇÃO --- */
function addPatient(){
  const p=G();const{pTNBC,pProg,imc,ob,nlr,plr}=score(p);
  if(patients.find(x=>x.id===p.id)){alert('ID "'+p.id+'" já registado.');return;}
  patients.push({...p,pTNBC,pProg,imc,ob,nlr,plr});
  const cur=document.getElementById('pid').value;
  const m=cur.match(/(\D*)(\d+)$/);
  if(m)document.getElementById('pid').value=m[1]+(parseInt(m[2])+1).toString().padStart(3,'0');
  updateList();
  const b=document.querySelector('.btnadd');
  b.textContent='✓ Adicionada com sucesso!';b.style.background='#27AE60';
  setTimeout(()=>{b.innerHTML='<span style="font-size:20px;font-weight:300">+</span>Adicionar à análise populacional';b.style.background='';},1500);
}

function delPat(id){patients=patients.filter(p=>p.id!==id);updateList();}
function clearAll(){if(!patients.length||!confirm('Apagar todas?'))return;patients=[];updateList();destroyCharts();document.getElementById('pop-section').style.display='none';}

function updateList(){
  const n=patients.length;
  document.getElementById('cbdg').textContent=n;
  const pl=document.getElementById('plist'),em=document.getElementById('plist-empty');
  if(!n){em.style.display='block';pl.style.display='none';return;}
  em.style.display='none';pl.style.display='flex';
  pl.innerHTML=patients.map(p=>{
    const tb=p.pTNBC>=70?'#FDEDEC':p.pTNBC>=45?'#FEF5E7':'#EAFAF1';
    const tt=p.pTNBC>=70?'#922B21':p.pTNBC>=45?'#7E5109':'#1E8449';
    const pb=p.pProg>=70?'#FDEDEC':p.pProg>=45?'#FEF5E7':'#EAFAF1';
    const pt=p.pProg>=70?'#922B21':p.pProg>=45?'#7E5109':'#1E8449';
    return`<div class="pi"><div style="flex:1"><p style="font-size:13px;font-weight:500">${p.id}</p><p style="font-size:11px;color:var(--m)">${p.idade}a · Grau ${['I','II','III'][p.grau-1]} · Est.${'I II III IV'.split(' ')[p.est-1]} · ${p.tam}cm${p.nlr>0?' · NLR '+p.nlr:''}</p></div><div style="display:flex;gap:8px;align-items:center"><span style="background:${tb};color:${tt};padding:2px 10px;border-radius:20px;font-size:11px;font-weight:600">TNBC ${p.pTNBC}%</span><span style="background:${pb};color:${pt};padding:2px 10px;border-radius:20px;font-size:11px;font-weight:600">P ${p.pProg}%</span><button class="pdel" onclick="delPat('${p.id}')">×</button></div></div>`;
  }).join('');
}

function destroyCharts(){Object.values(charts).forEach(c=>{if(c)c.destroy()});charts={};}

function renderPop(){
  const n=patients.length;
  if(n<2){document.getElementById('pop-section').style.display='none';return;}
  document.getElementById('pop-section').style.display='block';
  const aT=patients.filter(p=>p.pTNBC>=70).length,aP=patients.filter(p=>p.pProg>=70).length;
  const ms=Math.round(patients.reduce((a,p)=>a+p.pTNBC,0)/n);
  document.getElementById('pop-stats').innerHTML=`<div class="sc"><p class="scc" style="color:var(--g)">${n}</p><p class="scl">Total</p></div><div class="sc"><p class="scc" style="color:#CB4335">${aT}</p><p class="scl">Alto risco TNBC</p></div><div class="sc"><p class="scc" style="color:#CA6F1E">${aP}</p><p class="scl">Mau prognóstico</p></div><div class="sc"><p class="scc">${ms}%</p><p class="scl">Score médio</p></div>`;
  destroyCharts();
  const co=['#CB4335','#CA6F1E','#27AE60'];
  charts.tn=new Chart(document.getElementById('ch-tnbc'),{type:'doughnut',data:{labels:['Alto','Moderado','Baixo'],datasets:[{data:[patients.filter(p=>p.pTNBC>=70).length,patients.filter(p=>p.pTNBC>=45&&p.pTNBC<70).length,patients.filter(p=>p.pTNBC<45).length],backgroundColor:co,borderWidth:2,borderColor:'#fff'}]},options:{responsive:true,cutout:'55%',plugins:{legend:{position:'bottom',labels:{font:{size:11},padding:10}}}}});
  charts.sc=new Chart(document.getElementById('ch-sc'),{type:'scatter',data:{datasets:[{data:patients.map(p=>({x:p.idade,y:p.pTNBC})),backgroundColor:patients.map(p=>p.pTNBC>=70?'rgba(203,67,53,.7)':p.pTNBC>=45?'rgba(202,111,30,.7)':'rgba(39,174,96,.7)'),pointRadius:7}]},options:{responsive:true,scales:{x:{title:{display:true,text:'Idade',font:{size:11}}},y:{min:0,max:100,title:{display:true,text:'Score TNBC',font:{size:11}}}},plugins:{legend:{display:false}}}});
  const gd=[1,2,3].map(i=>{const g=patients.filter(p=>p.grau===i);return g.length?Math.round(g.reduce((a,p)=>a+p.pTNBC,0)/g.length):0;});
  charts.gr=new Chart(document.getElementById('ch-gr'),{type:'bar',data:{labels:['Grau I','Grau II','Grau III'],datasets:[{data:gd,backgroundColor:co.slice().reverse(),borderRadius:4}]},options:{responsive:true,scales:{y:{min:0,max:100}},plugins:{legend:{display:false}}}});
  const nlrP=patients.filter(p=>p.nlr>0);
  if(nlrP.length>0)charts.nlr=new Chart(document.getElementById('ch-nlr'),{type:'scatter',data:{datasets:[{data:nlrP.map(p=>({x:p.nlr,y:p.pProg})),backgroundColor:'rgba(27,63,92,.65)',pointRadius:7}]},options:{responsive:true,scales:{x:{title:{display:true,text:'NLR',font:{size:11}}},y:{min:0,max:100,title:{display:true,text:'Score Progn.',font:{size:11}}}},plugins:{legend:{display:false}}}});
  const hr=patients.filter(p=>p.pTNBC>=70);
  document.getElementById('patterns').innerHTML=hr.length
    ?[['idade<40',hr.filter(p=>p.idade<40).length],['pré-menop.',hr.filter(p=>p.menop===1).length],['grau III',hr.filter(p=>p.grau===3).length],['tumor>5cm',hr.filter(p=>p.tam>5).length],['Ki-67≥30%',hr.filter(p=>p.ki>=30).length]].filter(x=>x[1]>0).map(x=>`<div style="background:var(--s2);border:.5px solid var(--b);border-radius:10px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;font-size:12px;gap:8px;margin-bottom:6px"><span>${x[1]}/${hr.length} de alto risco com ${x[0]}</span><span class="badge bi">${Math.round(x[1]/hr.length*100)}%</span></div>`).join('')
    :'<p style="font-size:13px;color:var(--f)">Sem alto risco TNBC nesta amostra.</p>';
  document.getElementById('pop-tbody').innerHTML=patients.map(p=>{
    const tb=p.pTNBC>=70?'#FDEDEC':p.pTNBC>=45?'#FEF5E7':'#EAFAF1',tt=p.pTNBC>=70?'#922B21':p.pTNBC>=45?'#7E5109':'#1E8449';
    const pb=p.pProg>=70?'#FDEDEC':p.pProg>=45?'#FEF5E7':'#EAFAF1',pt=p.pProg>=70?'#922B21':p.pProg>=45?'#7E5109':'#1E8449';
    const cd=p.pTNBC>=70&&p.pProg>=70?'IHQ+QT urgente':p.pTNBC>=70?'Priorizar IHQ':p.pProg>=70?'QT imediata':'Standard';
    return`<tr><td><strong>${p.id}</strong></td><td>${p.idade}</td><td>${['I','II','III'][p.grau-1]}</td><td>${'I II III IV'.split(' ')[p.est-1]}</td><td>${p.tam}</td><td>${p.ki>0?p.ki+'%':'N/D'}</td><td>${p.nlr>0?p.nlr:'N/D'}</td><td><span style="background:${tb};color:${tt};padding:2px 8px;border-radius:20px;font-size:11px;font-weight:600">${p.pTNBC}%</span></td><td><span style="background:${pb};color:${pt};padding:2px 8px;border-radius:20px;font-size:11px;font-weight:600">${p.pProg}%</span></td><td style="font-size:11px;color:var(--m)">${cd}</td></tr>`;
  }).join('');
}

/* --- COMPARAÇÃO INTERACTIVA --- */
function calcCmp(){
  const idade=parseInt(document.getElementById('c-idade').value);
  const tam=parseFloat(document.getElementById('c-tam').value);
  const grau=parseInt(document.getElementById('c-grau').value);
  const est=parseInt(document.getElementById('c-est').value);
  const gan=parseInt(document.getElementById('c-gan').value);
  const men=parseInt(document.getElementById('c-men').value);
  const ki=parseInt(document.getElementById('c-ki').value);
  const nlr=parseFloat(document.getElementById('c-nlr').value);
  const er=document.getElementById('c-er').value;
  const her2=document.getElementById('c-her2').value;

  document.getElementById('c-iv').textContent=idade;
  document.getElementById('c-tv').textContent=tam.toFixed(1);
  document.getElementById('c-kv').textContent=ki+'%';
  document.getElementById('c-nv').textContent=nlr.toFixed(1);

  const ours=Math.min(100,Math.round(((idade<40?25:idade<50?10:0)+(men===1?15:0)+(grau===3?20:grau===2?5:0)+(tam>5?15:tam>3?7:0)+(ki>=60?12:ki>=30?7:0)+(nlr>4?8:nlr>2.5?4:0))/0.9));
  const seer=Math.min(100,Math.round((est===4?35:est===3?25:est===2?15:5)+(grau===3?20:grau===2?10:0)+(gan===1?15:0)+(tam>5?15:tam>3?10:0)+(idade<50?10:0)));
  const mayo=Math.min(100,Math.round((tam>5?30:tam>3?20:10)+(gan===1?25:0)+(ki>=60?25:ki>=30?15:0)+(grau===3?15:0)));
  const est_tn=Math.min(100,Math.round((est===4?40:est===3?30:est===2?20:10)+(tam>5?20:10)+(gan===1?20:0)+(grau===3?10:0)));

  const models=[
    {name:'TNBC Predictor HCM',val:ours,col:'#1A6B3C',ours:true,note:'Contexto africano + NLR'},
    {name:'Nomograma SEER 2024',val:seer,col:'#1B4F72',note:'23,394 pac. EUA'},
    {name:'Mayo Clinic Calculator',val:mayo,col:'#7B3F00',note:'605 pac.'},
    {name:'ESTIMATE-TN',val:est_tn,col:'#4A235A',note:'37,293 pac. SEER'},
  ];

  let html='';
  models.forEach(m=>{
    const col=m.val>=70?'#CB4335':m.val>=45?'#CA6F1E':'#27AE60';
    html+=`<div style="background:${m.ours?'var(--gl)':'var(--s2)'};border:${m.ours?'1px solid var(--g)':'.5px solid var(--b)'};border-radius:10px;padding:10px 14px;margin-bottom:8px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
        <div><span style="font-size:12px;font-weight:600;color:${m.ours?'var(--g)':'var(--t)'}">${m.name}</span>${m.ours?'<span style="background:var(--g);color:#fff;font-size:10px;padding:1px 6px;border-radius:20px;margin-left:6px">Este modelo</span>':''}<p style="font-size:10px;color:var(--f);margin-top:1px">${m.note}</p></div>
        <span style="font-family:DM Serif Display,serif;font-size:22px;color:${col}">${m.val}%</span>
      </div>
      <div class="mtr"><div class="mf" style="width:${m.val}%;background:${col}"></div></div>
    </div>`;
  });
  document.getElementById('cmp-bars').innerHTML=html;

  if(radarChart)radarChart.destroy();
  radarChart=new Chart(document.getElementById('ch-radar'),{type:'radar',data:{labels:['Contexto África','Sem IHQ','NLR incluído','Custo HCM','Dados locais','Precisão'],datasets:[{label:'HCM Predictor',data:[90,90,85,80,85,75],borderColor:'#1A6B3C',backgroundColor:'rgba(26,107,60,.15)',borderWidth:2,pointRadius:4},{label:'SEER 2024',data:[20,10,15,10,15,76],borderColor:'#1B4F72',backgroundColor:'rgba(27,79,114,.1)',borderWidth:1.5,pointRadius:3},{label:'Mayo',data:[15,10,50,10,15,73],borderColor:'#7B3F00',backgroundColor:'rgba(123,63,0,.1)',borderWidth:1.5,pointRadius:3}]},options:{responsive:true,scales:{r:{min:0,max:100,ticks:{stepSize:20,font:{size:9}},pointLabels:{font:{size:10}}}},plugins:{legend:{position:'bottom',labels:{font:{size:11},padding:10}}}}});
}

function exportCSV(){
  if(!patients.length){alert('Sem pacientes.');return;}
  const h='ID,Idade,IMC,Par,Menop,Grau,Est,Tumor,Ganglios,Ki67,NLR,PLR,ScoreTNBC,ScoreProg\n';
  const r=patients.map(p=>`${p.id},${p.idade},${p.imc},${p.par},${p.menop===1?'Pre':'Pos'},${['I','II','III'][p.grau-1]},${'I II III IV'.split(' ')[p.est-1]},${p.tam},${p.gan===1?'Sim':'Nao'},${p.ki>0?p.ki:'ND'},${p.nlr>0?p.nlr:'ND'},${p.plr>0?p.plr:'ND'},${p.pTNBC}%,${p.pProg}%`).join('\n');
  const blob=new Blob(['\ufeff'+h+r],{type:'text/csv;charset=utf-8'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=`tnbc_hcm_${new Date().toISOString().slice(0,10)}.csv`;a.click();
}

/* INIT */
document.getElementById('fu-start').value=new Date().toISOString().slice(0,10);
calc();
calcPCR();
renderKM();
calcCmp();
renderTrials();


/* ---- ATLAS CLÍNICO ---- */
const ATLAS_DATA = [
  // ---- HISTOLOGIA ----
  {
    cat:'micro', 
    title:'TNBC basal-like — histopatologia clássica (H&E 200×)',
    desc:'Carcinoma ductal invasivo subtipo basal-like (TNBC). Células com pleomorfismo nuclear marcado, nucléolos proeminentes (seta amarela), necrose central e infiltrado linfocítico estromal (TILs). ~80% dos TNBC são basal-like. Crescimento sólido/difuso sem formação tubular — padrão de Grau III.',
    tags:['Histologia','Basal-like','TNBC','H&E','TILs','200×'],
    img:'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMzAwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCI+CiAgPHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiNGOUVFRjAiLz4KICA8IS0tIEJhY2tncm91bmQgdGlzc3VlIC0tPgogIDxyZWN0IHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIiBmaWxsPSIjRkJFRUY1Ii8+CiAgPCEtLSBTdHJvbWEgLSBwaW5rIGVvc2lub3BoaWxpYyAtLT4KICA8ZWxsaXBzZSBjeD0iMjAwIiBjeT0iMTUwIiByeD0iMTkwIiByeT0iMTQwIiBmaWxsPSIjRThCNEM4IiBvcGFjaXR5PSIwLjMiLz4KICA8IS0tIERlbnNlIGNlbGwgbmVzdHMgLSB0eXBpY2FsIFROQkMgc29saWQgZ3Jvd3RoIHBhdHRlcm4gLS0+CiAgPCEtLSBDZWxsIG5lc3QgMSAtLT4KICA8ZWxsaXBzZSBjeD0iMTAwIiBjeT0iMTAwIiByeD0iNTUiIHJ5PSI0NSIgZmlsbD0iI0M4NzA5MCIgb3BhY2l0eT0iMC43Ii8+CiAgPGVsbGlwc2UgY3g9IjEwMCIgY3k9IjEwMCIgcng9IjQ1IiByeT0iMzUiIGZpbGw9IiNEMDgwQTAiIG9wYWNpdHk9IjAuOCIvPgogIDwhLS0gSW5kaXZpZHVhbCB0dW1vciBjZWxscyAtLT4KICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjkwIiByPSI5IiBmaWxsPSIjNzA0MEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iODAiIGN5PSI5MCIgcj0iNSIgZmlsbD0iIzkwNjBDMCIgb3BhY2l0eT0iMC42Ii8+CiAgPGNpcmNsZSBjeD0iOTQiIGN5PSI4NSIgcj0iMTAiIGZpbGw9IiM2MDMwQTAiIG9wYWNpdHk9IjAuODUiLz4KICA8Y2lyY2xlIGN4PSI5NCIgY3k9Ijg1IiByPSI2IiBmaWxsPSIjODA1MEMwIiBvcGFjaXR5PSIwLjYiLz4KICA8Y2lyY2xlIGN4PSIxMTAiIGN5PSI4OCIgcj0iOSIgZmlsbD0iIzcwNDBBMCIgb3BhY2l0eT0iMC44NSIvPgogIDxjaXJjbGUgY3g9IjExMCIgY3k9Ijg4IiByPSI1IiBmaWxsPSIjOTA2MEMwIiBvcGFjaXR5PSIwLjYiLz4KICA8Y2lyY2xlIGN4PSI4NSIgY3k9IjEwMyIgcj0iMTAiIGZpbGw9IiM2MDMwQTAiIG9wYWNpdHk9IjAuODUiLz4KICA8Y2lyY2xlIGN4PSI4NSIgY3k9IjEwMyIgcj0iNiIgZmlsbD0iIzgwNTBDMCIgb3BhY2l0eT0iMC42Ii8+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTA4IiByPSI5IiBmaWxsPSIjNzA0MEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMTAwIiBjeT0iMTA4IiByPSI1IiBmaWxsPSIjOTA2MEMwIiBvcGFjaXR5PSIwLjYiLz4KICA8Y2lyY2xlIGN4PSIxMTUiIGN5PSIxMDMiIHI9IjEwIiBmaWxsPSIjNjAzMEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMTE1IiBjeT0iMTAzIiByPSI2IiBmaWxsPSIjODA1MEMwIiBvcGFjaXR5PSIwLjYiLz4KICA8IS0tIE1pdG90aWMgZmlndXJlIChhcnJvdy1saWtlKSAtLT4KICA8ZWxsaXBzZSBjeD0iMTA1IiBjeT0iNzIiIHJ4PSIxMiIgcnk9IjYiIGZpbGw9IiM0MDIwQzAiIG9wYWNpdHk9IjAuOSIgdHJhbnNmb3JtPSJyb3RhdGUoLTMwIDEwNSA3MikiLz4KICA8IS0tIENlbGwgbmVzdCAyIC0tPgogIDxlbGxpcHNlIGN4PSIyNzAiIGN5PSI5MCIgcng9IjYwIiByeT0iNTAiIGZpbGw9IiNDODcwOTAiIG9wYWNpdHk9IjAuNyIvPgogIDxjaXJjbGUgY3g9IjI1MiIgY3k9IjgwIiByPSIxMCIgZmlsbD0iIzYwMzBBMCIgb3BhY2l0eT0iMC44NSIvPgogIDxjaXJjbGUgY3g9IjI1MiIgY3k9IjgwIiByPSI2IiBmaWxsPSIjODA1MEMwIiBvcGFjaXR5PSIwLjYiLz4KICA8Y2lyY2xlIGN4PSIyNjgiIGN5PSI3NiIgcj0iMTEiIGZpbGw9IiM1MDIwQTAiIG9wYWNpdHk9IjAuODUiLz4KICA8Y2lyY2xlIGN4PSIyNjgiIGN5PSI3NiIgcj0iNyIgZmlsbD0iIzcwNDBDMCIgb3BhY2l0eT0iMC42Ii8+CiAgPGNpcmNsZSBjeD0iMjg0IiBjeT0iODMiIHI9IjEwIiBmaWxsPSIjNjAzMEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMjg0IiBjeT0iODMiIHI9IjYiIGZpbGw9IiM4MDUwQzAiIG9wYWNpdHk9IjAuNiIvPgogIDxjaXJjbGUgY3g9IjI1OCIgY3k9Ijk2IiByPSI5IiBmaWxsPSIjNzA0MEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMjU4IiBjeT0iOTYiIHI9IjUiIGZpbGw9IiM5MDYwQzAiIG9wYWNpdHk9IjAuNiIvPgogIDxjaXJjbGUgY3g9IjI3NCIgY3k9IjEwMCIgcj0iMTAiIGZpbGw9IiM2MDMwQTAiIG9wYWNpdHk9IjAuODUiLz4KICA8Y2lyY2xlIGN4PSIyNzQiIGN5PSIxMDAiIHI9IjYiIGZpbGw9IiM4MDUwQzAiIG9wYWNpdHk9IjAuNiIvPgogIDxjaXJjbGUgY3g9IjI4OCIgY3k9Ijk0IiByPSI5IiBmaWxsPSIjNzA0MEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPCEtLSBCaWcgbnVjbGVvbHVzID0gcHJvbWluZW50IChUTkJDIGZlYXR1cmUpIC0tPgogIDxjaXJjbGUgY3g9IjI2OCIgY3k9Ijc2IiByPSIzIiBmaWxsPSIjRkZGRkZGIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSIyNTIiIGN5PSI4MCIgcj0iMi41IiBmaWxsPSIjRkZGRkZGIiBvcGFjaXR5PSIwLjciLz4KICA8IS0tIENlbGwgbmVzdCAzIC0gbGFyZ2VyLCBjZW50cmFsIG5lY3Jvc2lzIGFyZWEgLS0+CiAgPGVsbGlwc2UgY3g9IjE4MCIgY3k9IjIxMCIgcng9Ijc1IiByeT0iNTUiIGZpbGw9IiNDODcwOTAiIG9wYWNpdHk9IjAuNyIvPgogIDxlbGxpcHNlIGN4PSIxODAiIGN5PSIyMTAiIHJ4PSIzMCIgcnk9IjIyIiBmaWxsPSIjRThDODkwIiBvcGFjaXR5PSIwLjgiLz4KICA8dGV4dCB4PSIxODAiIHk9IjIxNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI5IiBmaWxsPSIjQTA2MDMwIiBmb250LWZhbWlseT0ic2VyaWYiPm5lY3Jvc2U8L3RleHQ+CiAgPCEtLSBDZWxscyBhcm91bmQgbmVjcm9zaXMgLS0+CiAgPGNpcmNsZSBjeD0iMTMwIiBjeT0iMjAwIiByPSIxMCIgZmlsbD0iIzYwMzBBMCIgb3BhY2l0eT0iMC44NSIvPgogIDxjaXJjbGUgY3g9IjEzMCIgY3k9IjIwMCIgcj0iNiIgZmlsbD0iIzgwNTBDMCIgb3BhY2l0eT0iMC42Ii8+CiAgPGNpcmNsZSBjeD0iMTQ1IiBjeT0iMTkwIiByPSI5IiBmaWxsPSIjNzA0MEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMTQ1IiBjeT0iMTkwIiByPSI1IiBmaWxsPSIjOTA2MEMwIiBvcGFjaXR5PSIwLjYiLz4KICA8Y2lyY2xlIGN4PSIyMjAiIGN5PSIyMDAiIHI9IjEwIiBmaWxsPSIjNjAzMEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMjIwIiBjeT0iMjAwIiByPSI2IiBmaWxsPSIjODA1MEMwIiBvcGFjaXR5PSIwLjYiLz4KICA8Y2lyY2xlIGN4PSIyMDUiIGN5PSIxOTUiIHI9IjkiIGZpbGw9IiM3MDQwQTAiIG9wYWNpdHk9IjAuODUiLz4KICA8Y2lyY2xlIGN4PSIxNzUiIGN5PSIyMzUiIHI9IjEwIiBmaWxsPSIjNjAzMEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMTkwIiBjeT0iMjMzIiByPSI5IiBmaWxsPSIjNzA0MEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPCEtLSBMeW1waG9jeXRpYyBpbmZpbHRyYXRlIChUSUxzKSAtIHNtYWxsIGRhcmsgbHltcGhvY3l0ZXMgaW4gc3Ryb21hIC0tPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNjAiIHI9IjUiIGZpbGw9IiMzMDIwQTAiIG9wYWNpdHk9IjAuOSIvPgogIDxjaXJjbGUgY3g9IjYwIiBjeT0iNzAiIHI9IjQiIGZpbGw9IiMzMDIwQTAiIG9wYWNpdHk9IjAuOSIvPgogIDxjaXJjbGUgY3g9IjQ1IiBjeT0iNzUiIHI9IjUiIGZpbGw9IiMzMDIwQTAiIG9wYWNpdHk9IjAuOSIvPgogIDxjaXJjbGUgY3g9IjE2MCIgY3k9IjQ1IiByPSI0IiBmaWxsPSIjMzAyMEEwIiBvcGFjaXR5PSIwLjkiLz4KICA8Y2lyY2xlIGN4PSIxNzAiIGN5PSI1NSIgcj0iNSIgZmlsbD0iIzMwMjBBMCIgb3BhY2l0eT0iMC45Ii8+CiAgPGNpcmNsZSBjeD0iMTU1IiBjeT0iNjAiIHI9IjQiIGZpbGw9IiMzMDIwQTAiIG9wYWNpdHk9IjAuOSIvPgogIDxjaXJjbGUgY3g9IjM0MCIgY3k9IjE1MCIgcj0iNSIgZmlsbD0iIzMwMjBBMCIgb3BhY2l0eT0iMC45Ii8+CiAgPGNpcmNsZSBjeD0iMzUwIiBjeT0iMTYwIiByPSI0IiBmaWxsPSIjMzAyMEEwIiBvcGFjaXR5PSIwLjkiLz4KICA8Y2lyY2xlIGN4PSIzMzUiIGN5PSIxNjUiIHI9IjUiIGZpbGw9IiMzMDIwQTAiIG9wYWNpdHk9IjAuOSIvPgogIDxjaXJjbGUgY3g9IjM2MCIgY3k9IjE0NSIgcj0iNCIgZmlsbD0iIzMwMjBBMCIgb3BhY2l0eT0iMC45Ii8+CiAgPCEtLSBTdHJvbWEgZmlicm91cyBzdHJhbmRzIC0tPgogIDxwYXRoIGQ9Ik0zMCAxNTAgUSAxMDAgMTMwIDE3MCAxNTUgUSAyNDAgMTc1IDMxMCAxNjAiIHN0cm9rZT0iI0QwOTBCMCIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIiBvcGFjaXR5PSIwLjUiLz4KICA8cGF0aCBkPSJNNTAgMjAwIFEgMTMwIDE4NSAyMDAgMjAwIFEgMjcwIDIxNSAzNTAgMTk1IiBzdHJva2U9IiNEMDkwQjAiIGZpbGw9Im5vbmUiIHN0cm9rZS13aWR0aD0iMiIgb3BhY2l0eT0iMC41Ii8+CiAgPCEtLSBMYWJlbHMgLS0+CiAgPHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjQwMCIgaGVpZ2h0PSIxOCIgZmlsbD0icmdiYSgxMDAsMjAsNjAsMC44NSkiLz4KICA8dGV4dCB4PSI4IiB5PSIxMyIgZm9udC1zaXplPSIxMCIgZmlsbD0id2hpdGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iYm9sZCI+SCZhbXA7RSDCtyBDYXJjaW5vbWEgYmFzYWwtbGlrZSAoVE5CQykgwrcgR3JhdSBJSUkgwrcgMjAww5c8L3RleHQ+CiAgPCEtLSBBbm5vdGF0aW9ucyAtLT4KICA8bGluZSB4MT0iMTA1IiB5MT0iNzUiIHgyPSIxMjUiIHkyPSI1NSIgc3Ryb2tlPSIjRkZDQzAwIiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDx0ZXh0IHg9IjEyNyIgeT0iNTIiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iI0ZGQ0MwMCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPm1pdG9zZTwvdGV4dD4KICA8bGluZSB4MT0iMzQwIiB5MT0iMTU1IiB4Mj0iMzYwIiB5Mj0iMTM1IiBzdHJva2U9IiNGRkNDMDAiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPHRleHQgeD0iMzEwIiB5PSIxMzIiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iI0ZGQ0MwMCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPlRJTHM8L3RleHQ+CiAgPGxpbmUgeDE9IjE4MCIgeTE9IjIxMyIgeDI9IjE1MCIgeTI9IjI0NSIgc3Ryb2tlPSIjRkZDQzAwIiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDx0ZXh0IHg9IjEwMCIgeT0iMjU4IiBmb250LXNpemU9IjgiIGZpbGw9IiNGRkNDMDAiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5uZWNyb3NlIGNlbnRyYWw8L3RleHQ+CiAgPGxpbmUgeDE9IjI2OCIgeTE9Ijc2IiB4Mj0iMjk1IiB5Mj0iNjAiIHN0cm9rZT0iI0ZGQ0MwMCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8dGV4dCB4PSIyOTYiIHk9IjU4IiBmb250LXNpemU9IjgiIGZpbGw9IiNGRkNDMDAiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5udWNsw6lvbG8gcHJvbWluZW50ZTwvdGV4dD4KICA8IS0tIFNjYWxlIGJhciAtLT4KICA8cmVjdCB4PSIzMjAiIHk9IjI4MCIgd2lkdGg9IjUwIiBoZWlnaHQ9IjMiIGZpbGw9IndoaXRlIi8+CiAgPHRleHQgeD0iMzIwIiB5PSIyOTUiIGZvbnQtc2l6ZT0iOCIgZmlsbD0id2hpdGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj41MCDOvG08L3RleHQ+Cjwvc3ZnPg==',
    credit:'Ilustração clínica TNBC Predictor HCM · A. Sualé / UEM 2026 · Baseado em: Nephron (Wikimedia CC BY-SA 4.0) · PathologyOutlines TNBC',
    color:'#6C3483',emoji:'🔬',
    facts:[{l:'Subtipo molecular',v:'Basal-like (~80%'},{l:'TILs',v:'Frequentes'},{l:'Grau típico',v:'III (8–9)'}]
  },
  {
    cat:'micro',
    title:'Grau III — pleomorfismo nuclear marcado, mitoses ↑ (H&E 400×)',
    desc:'Alta magnificação (400×): células com núcleos grandes e irregulares, nucléolos proeminentes (bisnucleolados), figuras mitóticas (seta). Score de Elston-Ellis: 8–9 (Grau III). >20 mitoses/10 HPF. Padrão diagnóstico de TNBC ductal NST de alto grau — presente em 55% dos TNBC no HCM (Moza-BC).',
    tags:['H&E 400×','Grau III','Mitoses','Nucléolos','Pleomorfismo'],
    img:'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMzAwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCI+CiAgPHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiNGQkYwRjQiLz4KICA8IS0tIFBpbmsgY3l0b3BsYXNtIGJhY2tncm91bmQgLS0+CiAgPHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiNGMEQ4RTQiIG9wYWNpdHk9IjAuNSIvPgogIDwhLS0gTGFyZ2UgcGxlb21vcnBoaWMgY2VsbHMgLSBHcmF1IElJSSAtLT4KICA8IS0tIFJvdyAxIC0tPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNjAiIHI9IjI4IiBmaWxsPSIjRDA5MEIwIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSI1MCIgY3k9IjYwIiByPSIyMiIgZmlsbD0iIzMwMjBBMCIgb3BhY2l0eT0iMC44NSIvPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNjAiIHI9IjgiIGZpbGw9IiNGRkZGRkYiIG9wYWNpdHk9IjAuNSIvPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNjAiIHI9IjQiIGZpbGw9IiNGRjQwODAiIG9wYWNpdHk9IjAuOSIvPgogIAogIDxjaXJjbGUgY3g9IjExNSIgY3k9IjU1IiByPSIzMiIgZmlsbD0iI0QwOTBCMCIgb3BhY2l0eT0iMC43Ii8+CiAgPGNpcmNsZSBjeD0iMTE1IiBjeT0iNTUiIHI9IjI2IiBmaWxsPSIjNDAzMEIwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMTE1IiBjeT0iNTUiIHI9IjEwIiBmaWxsPSIjRkZGRkZGIiBvcGFjaXR5PSIwLjUiLz4KICA8Y2lyY2xlIGN4PSIxMTUiIGN5PSI1NSIgcj0iNSIgZmlsbD0iI0ZGNDA4MCIgb3BhY2l0eT0iMC45Ii8+CiAgCiAgPGNpcmNsZSBjeD0iMTg1IiBjeT0iNjUiIHI9IjI2IiBmaWxsPSIjRDA5MEIwIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSIxODUiIGN5PSI2NSIgcj0iMjAiIGZpbGw9IiMzMDIwQTAiIG9wYWNpdHk9IjAuODUiLz4KICA8Y2lyY2xlIGN4PSIxODUiIGN5PSI2NSIgcj0iNyIgZmlsbD0iI0ZGRkZGRiIgb3BhY2l0eT0iMC41Ii8+CiAgPGNpcmNsZSBjeD0iMTg1IiBjeT0iNjUiIHI9IjMuNSIgZmlsbD0iI0ZGNDA4MCIgb3BhY2l0eT0iMC45Ii8+CiAgCiAgPGNpcmNsZSBjeD0iMjUwIiBjeT0iNTUiIHI9IjMwIiBmaWxsPSIjRDA5MEIwIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSIyNTAiIGN5PSI1NSIgcj0iMjQiIGZpbGw9IiM1MDQwQzAiIG9wYWNpdHk9IjAuODUiLz4KICA8Y2lyY2xlIGN4PSIyNTAiIGN5PSI1NSIgcj0iOSIgZmlsbD0iI0ZGRkZGRiIgb3BhY2l0eT0iMC41Ii8+CiAgPGNpcmNsZSBjeD0iMjUwIiBjeT0iNTUiIHI9IjQuNSIgZmlsbD0iI0ZGNDA4MCIgb3BhY2l0eT0iMC45Ii8+CiAgCiAgPCEtLSBNaXRvdGljIGZpZ3VyZSBpbiBkaXZpc2lvbiAtLT4KICA8ZWxsaXBzZSBjeD0iMzIwIiBjeT0iNjAiIHJ4PSIyMCIgcnk9IjEyIiBmaWxsPSIjMjAyMEEwIiBvcGFjaXR5PSIwLjkiIHRyYW5zZm9ybT0icm90YXRlKC0yMCAzMjAgNjApIi8+CiAgPGVsbGlwc2UgY3g9IjM0MCIgY3k9IjcwIiByeD0iMjAiIHJ5PSIxMiIgZmlsbD0iIzIwMjBBMCIgb3BhY2l0eT0iMC45IiB0cmFuc2Zvcm09InJvdGF0ZSgtMjAgMzQwIDcwKSIvPgogIDxsaW5lIHgxPSIzMjAiIHkxPSI2MCIgeDI9IjM0MCIgeTI9IjcwIiBzdHJva2U9IiM2MDYwRDAiIHN0cm9rZS13aWR0aD0iMiIvPgogIAogIDwhLS0gUm93IDIgLS0+CiAgPGNpcmNsZSBjeD0iNzUiIGN5PSIxNDUiIHI9IjMwIiBmaWxsPSIjRDA5MEIwIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSI3NSIgY3k9IjE0NSIgcj0iMjQiIGZpbGw9IiMzMDIwQTAiIG9wYWNpdHk9IjAuODUiLz4KICA8Y2lyY2xlIGN4PSI3NSIgY3k9IjE0NSIgcj0iOSIgZmlsbD0iI0ZGRkZGRiIgb3BhY2l0eT0iMC41Ii8+CiAgPGNpcmNsZSBjeD0iNzUiIGN5PSIxNDUiIHI9IjQuNSIgZmlsbD0iI0ZGNDA4MCIgb3BhY2l0eT0iMC45Ii8+CiAgCiAgPGNpcmNsZSBjeD0iMTQ4IiBjeT0iMTM1IiByPSIyOCIgZmlsbD0iI0QwOTBCMCIgb3BhY2l0eT0iMC43Ii8+CiAgPGNpcmNsZSBjeD0iMTQ4IiBjeT0iMTM1IiByPSIyMiIgZmlsbD0iIzQwMzBCMCIgb3BhY2l0eT0iMC44NSIvPgogIDxjaXJjbGUgY3g9IjE0OCIgY3k9IjEzNSIgcj0iOCIgZmlsbD0iI0ZGRkZGRiIgb3BhY2l0eT0iMC41Ii8+CiAgPGNpcmNsZSBjeD0iMTQ4IiBjeT0iMTM1IiByPSI0IiBmaWxsPSIjRkY0MDgwIiBvcGFjaXR5PSIwLjkiLz4KICAKICA8Y2lyY2xlIGN4PSIyMjAiIGN5PSIxNDgiIHI9IjMyIiBmaWxsPSIjRDA5MEIwIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSIyMjAiIGN5PSIxNDgiIHI9IjI2IiBmaWxsPSIjNTA0MEIwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMjIwIiBjeT0iMTQ4IiByPSIxMCIgZmlsbD0iI0ZGRkZGRiIgb3BhY2l0eT0iMC41Ii8+CiAgPGNpcmNsZSBjeD0iMjIwIiBjeT0iMTQ4IiByPSI1IiBmaWxsPSIjRkY0MDgwIiBvcGFjaXR5PSIwLjkiLz4KICAKICA8Y2lyY2xlIGN4PSIyOTUiIGN5PSIxNDAiIHI9IjI2IiBmaWxsPSIjRDA5MEIwIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSIyOTUiIGN5PSIxNDAiIHI9IjIwIiBmaWxsPSIjMzAyMEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMjk1IiBjeT0iMTQwIiByPSI3IiBmaWxsPSIjRkZGRkZGIiBvcGFjaXR5PSIwLjUiLz4KICA8Y2lyY2xlIGN4PSIyOTUiIGN5PSIxNDAiIHI9IjMuNSIgZmlsbD0iI0ZGNDA4MCIgb3BhY2l0eT0iMC45Ii8+CiAgCiAgPCEtLSBBcG9wdG90aWMgY2VsbCAtIHNocmlua2FnZSAtLT4KICA8Y2lyY2xlIGN4PSIzNjAiIGN5PSIxNDAiIHI9IjE0IiBmaWxsPSIjQTA3MDkwIiBvcGFjaXR5PSIwLjYiLz4KICA8Y2lyY2xlIGN4PSIzNjAiIGN5PSIxNDAiIHI9IjEwIiBmaWxsPSIjODA0MDYwIiBvcGFjaXR5PSIwLjciLz4KICAKICA8IS0tIFJvdyAzIC0tPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iMjM1IiByPSIyOCIgZmlsbD0iI0QwOTBCMCIgb3BhY2l0eT0iMC43Ii8+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSIyMzUiIHI9IjIyIiBmaWxsPSIjMzAyMEEwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSIyMzUiIHI9IjgiIGZpbGw9IiNGRkZGRkYiIG9wYWNpdHk9IjAuNSIvPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iMjM1IiByPSI0IiBmaWxsPSIjRkY0MDgwIiBvcGFjaXR5PSIwLjkiLz4KICAKICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSIyMjUiIHI9IjMwIiBmaWxsPSIjRDA5MEIwIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSIyMjUiIHI9IjI0IiBmaWxsPSIjNDAzMEIwIiBvcGFjaXR5PSIwLjg1Ii8+CiAgPGNpcmNsZSBjeD0iMTIwIiBjeT0iMjI1IiByPSI5IiBmaWxsPSIjRkZGRkZGIiBvcGFjaXR5PSIwLjUiLz4KICA8Y2lyY2xlIGN4PSIxMjAiIGN5PSIyMjUiIHI9IjQuNSIgZmlsbD0iI0ZGNDA4MCIgb3BhY2l0eT0iMC45Ii8+CiAgCiAgPGNpcmNsZSBjeD0iMTk1IiBjeT0iMjM4IiByPSIyNyIgZmlsbD0iI0QwOTBCMCIgb3BhY2l0eT0iMC43Ii8+CiAgPGNpcmNsZSBjeD0iMTk1IiBjeT0iMjM4IiByPSIyMSIgZmlsbD0iIzUwNDBCMCIgb3BhY2l0eT0iMC44NSIvPgogIDxjaXJjbGUgY3g9IjE5NSIgY3k9IjIzOCIgcj0iOCIgZmlsbD0iI0ZGRkZGRiIgb3BhY2l0eT0iMC41Ii8+CiAgPGNpcmNsZSBjeD0iMTk1IiBjeT0iMjM4IiByPSI0IiBmaWxsPSIjRkY0MDgwIiBvcGFjaXR5PSIwLjkiLz4KICAKICA8IS0tIE1pdG90aWMgZmlndXJlIGRpdmlkaW5nIC0tPgogIDxlbGxpcHNlIGN4PSIyODUiIGN5PSIyMjgiIHJ4PSIyNCIgcnk9IjEwIiBmaWxsPSIjMTAxMEEwIiBvcGFjaXR5PSIwLjkiLz4KICA8ZWxsaXBzZSBjeD0iMzE1IiBjeT0iMjQ0IiByeD0iMjQiIHJ5PSIxMCIgZmlsbD0iIzEwMTBBMCIgb3BhY2l0eT0iMC45Ii8+CiAgCiAgPCEtLSBIZWFkZXIgLS0+CiAgPHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjQwMCIgaGVpZ2h0PSIxOCIgZmlsbD0icmdiYSgxMDAsMjAsNjAsMC44NSkiLz4KICA8dGV4dCB4PSI4IiB5PSIxMyIgZm9udC1zaXplPSIxMCIgZmlsbD0id2hpdGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iYm9sZCI+SCZhbXA7RSA0MDDDlyDCtyBHcmF1IElJSSDCtyBQbGVvbW9yZmlzbW8gbnVjbGVhciBtYXJjYWRvIMK3IE1pdG9zZXMg4oaRPC90ZXh0PgogIDwhLS0gQW5ub3RhdGlvbnMgd2l0aCBhcnJvd3MgLS0+CiAgPGxpbmUgeDE9IjExNSIgeTE9IjQwIiB4Mj0iMTMwIiB5Mj0iMjAiIHN0cm9rZT0iI0ZGQ0MwMCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8cG9seWdvbiBwb2ludHM9IjEzMCwyMCAxMjQsMjYgMTM2LDI2IiBmaWxsPSIjRkZDQzAwIi8+CiAgPHRleHQgeD0iMTMyIiB5PSIxNyIgZm9udC1zaXplPSI4IiBmaWxsPSIjRkZDQzAwIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+bnVjbMOpb2xvIHByb2VtaW5lbnRlPC90ZXh0PgogIDxsaW5lIHgxPSIzMjIiIHkxPSI1NSIgeDI9IjM1MCIgeTI9IjM4IiBzdHJva2U9IiNGRkNDMDAiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPHRleHQgeD0iMjkwIiB5PSIzNSIgZm9udC1zaXplPSI4IiBmaWxsPSIjRkZDQzAwIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+ZmlndXJhIG1pdMOzdGljYTwvdGV4dD4KICA8IS0tIFNjYWxlIC0tPgogIDxyZWN0IHg9IjM0MCIgeT0iMjgwIiB3aWR0aD0iNDAiIGhlaWdodD0iMiIgZmlsbD0id2hpdGUiLz4KICA8dGV4dCB4PSIzNDAiIHk9IjI5NSIgZm9udC1zaXplPSI4IiBmaWxsPSJ3aGl0ZSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPjIwIM68bTwvdGV4dD4KPC9zdmc+',
    credit:'Ilustração clínica TNBC Predictor HCM · A. Sualé / UEM 2026 · Baseado em: Nephron (Wikimedia CC BY-SA 3.0)',
    color:'#922B21',emoji:'🔬',
    facts:[{l:'Grau Elston-Ellis',v:'8–9 (III)'},{l:'Mitoses/10 HPF',v:'>20'},{l:'TNBC HCM',v:'55% Grau III (Moza-BC)'}]
  },
  {
    cat:'micro',
    title:'TILs — infiltrado linfocítico tumoral intenso (H&E)',
    desc:'Infiltrado linfocítico tumoral (TILs) intenso (~60%): linfócitos densos no estroma e infiltrando o tumor. Score segundo Salgado et al. 2015. TILs altos associam-se a maior probabilidade de pCR à QT neoadjuvante. Marcador prognóstico emergente — ausente no painel HCM actual mas com impacto clínico directo.',
    tags:['TILs','H&E','Imunohistoquímica','pCR','Prognóstico'],
    img:'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMzAwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCI+CiAgPHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiNGQkYwRjQiLz4KICA8cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjE4IiBmaWxsPSJyZ2JhKDI2LDEwNyw2MCwwLjkpIi8+CiAgPHRleHQgeD0iOCIgeT0iMTMiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IndoaXRlIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC13ZWlnaHQ9ImJvbGQiPkgmYW1wO0UgwrcgSW5maWx0cmFkbyBsaW5mb2PDrXRpY28gdHVtb3JhbCAoVElMcykgaW50ZW5zbyDigJQgVE5CQyBmYXZvcsOhdmVsPC90ZXh0PgogIDwhLS0gU3Ryb21hIHdpdGggbHltcGhvY3l0ZXMgLS0+CiAgPCEtLSBUdW1vciBjZWxscyAtIGNsdXN0ZXJlZCAtLT4KICA8ZWxsaXBzZSBjeD0iMjAwIiBjeT0iMTUwIiByeD0iODAiIHJ5PSI2NSIgZmlsbD0iI0UwQTBCOCIgb3BhY2l0eT0iMC42Ii8+CiAgPCEtLSBUdW1vciBjZWxscyAtLT4KICA8Y2lyY2xlIGN4PSIxNzUiIGN5PSIxMzUiIHI9IjE2IiBmaWxsPSIjQzg3MEEwIi8+CiAgPGNpcmNsZSBjeD0iMTc1IiBjeT0iMTM1IiByPSIxMCIgZmlsbD0iIzUwMzBBMCIvPgogIDxjaXJjbGUgY3g9IjE3NSIgY3k9IjEzNSIgcj0iNCIgZmlsbD0id2hpdGUiIG9wYWNpdHk9IjAuNiIvPgogIDxjaXJjbGUgY3g9IjE3NSIgY3k9IjEzNSIgcj0iMiIgZmlsbD0iI0ZGNDA4MCIgb3BhY2l0eT0iMC44Ii8+CiAgCiAgPGNpcmNsZSBjeD0iMjEwIiBjeT0iMTMwIiByPSIxOCIgZmlsbD0iI0M4NzBBMCIvPgogIDxjaXJjbGUgY3g9IjIxMCIgY3k9IjEzMCIgcj0iMTIiIGZpbGw9IiM0MDIwQTAiLz4KICA8Y2lyY2xlIGN4PSIyMTAiIGN5PSIxMzAiIHI9IjUiIGZpbGw9IndoaXRlIiBvcGFjaXR5PSIwLjYiLz4KICA8Y2lyY2xlIGN4PSIyMTAiIGN5PSIxMzAiIHI9IjIuNSIgZmlsbD0iI0ZGNDA4MCIgb3BhY2l0eT0iMC44Ii8+CiAgCiAgPGNpcmNsZSBjeD0iMTk1IiBjeT0iMTY1IiByPSIxNiIgZmlsbD0iI0M4NzBBMCIvPgogIDxjaXJjbGUgY3g9IjE5NSIgY3k9IjE2NSIgcj0iMTAiIGZpbGw9IiM1MDMwQTAiLz4KICA8Y2lyY2xlIGN4PSIxOTUiIGN5PSIxNjUiIHI9IjQiIGZpbGw9IndoaXRlIiBvcGFjaXR5PSIwLjYiLz4KICAKICA8Y2lyY2xlIGN4PSIyMjgiIGN5PSIxNTgiIHI9IjE1IiBmaWxsPSIjQzg3MEEwIi8+CiAgPGNpcmNsZSBjeD0iMjI4IiBjeT0iMTU4IiByPSI5IiBmaWxsPSIjNDAyMEEwIi8+CiAgPGNpcmNsZSBjeD0iMjI4IiBjeT0iMTU4IiByPSIzLjUiIGZpbGw9IndoaXRlIiBvcGFjaXR5PSIwLjYiLz4KICAKICA8Y2lyY2xlIGN4PSIxNjgiIGN5PSIxNjMiIHI9IjE0IiBmaWxsPSIjQzg3MEEwIi8+CiAgPGNpcmNsZSBjeD0iMTY4IiBjeT0iMTYzIiByPSI4IiBmaWxsPSIjNTAzMEEwIi8+CiAgCiAgPCEtLSBEZW5zZSBseW1waG9jeXRlcyBhcm91bmQgYW5kIGJldHdlZW4gdHVtb3IgY2VsbHMgLSBUSUxzIC0tPgogIDwhLS0gVmVyeSBkZW5zZSAtIGhpZ2ggVElMIHNjb3JlIC0tPgogIDxnIGZpbGw9IiMxQTMwOTAiIG9wYWNpdHk9IjAuOSI+CiAgICA8Y2lyY2xlIGN4PSI5NSIgY3k9IjkwIiByPSI1LjUiLz48Y2lyY2xlIGN4PSIxMDgiIGN5PSI4MCIgcj0iNSIvPjxjaXJjbGUgY3g9IjgyIiBjeT0iODAiIHI9IjUuNSIvPgogICAgPGNpcmNsZSBjeD0iNzAiIGN5PSI5NSIgcj0iNSIvPjxjaXJjbGUgY3g9IjEyMCIgY3k9Ijk1IiByPSI1LjUiLz48Y2lyY2xlIGN4PSI5NSIgY3k9IjExMCIgcj0iNSIvPgogICAgPGNpcmNsZSBjeD0iNjAiIGN5PSIxMTUiIHI9IjUuNSIvPjxjaXJjbGUgY3g9Ijc1IiBjeT0iMTI1IiByPSI1Ii8+PGNpcmNsZSBjeD0iMTEwIiBjeT0iMTE1IiByPSI1Ii8+CiAgICA8Y2lyY2xlIGN4PSI1NSIgY3k9IjE0MCIgcj0iNS41Ii8+PGNpcmNsZSBjeD0iNjgiIGN5PSIxNTUiIHI9IjUiLz48Y2lyY2xlIGN4PSI4MCIgY3k9IjE2NSIgcj0iNS41Ii8+CiAgICA8Y2lyY2xlIGN4PSIzMDAiIGN5PSI5MCIgcj0iNS41Ii8+PGNpcmNsZSBjeD0iMzE1IiBjeT0iODAiIHI9IjUiLz48Y2lyY2xlIGN4PSIyODUiIGN5PSI4MiIgcj0iNS41Ii8+CiAgICA8Y2lyY2xlIGN4PSIzMzAiIGN5PSI5OCIgcj0iNSIvPjxjaXJjbGUgY3g9IjI3NSIgY3k9IjEwMCIgcj0iNS41Ii8+PGNpcmNsZSBjeD0iMzIwIiBjeT0iMTE1IiByPSI1Ii8+CiAgICA8Y2lyY2xlIGN4PSIzNDAiIGN5PSIxMzAiIHI9IjUuNSIvPjxjaXJjbGUgY3g9IjMyOCIgY3k9IjE1MCIgcj0iNSIvPjxjaXJjbGUgY3g9IjMxMCIgY3k9IjE2NSIgcj0iNSIvPgogICAgPGNpcmNsZSBjeD0iMjk1IiBjeT0iMTgwIiByPSI1LjUiLz48Y2lyY2xlIGN4PSIyODAiIGN5PSIxNzUiIHI9IjUiLz4KICAgIDxjaXJjbGUgY3g9IjEzMCIgY3k9Ijg1IiByPSI1Ii8+PGNpcmNsZSBjeD0iMTQ4IiBjeT0iNzgiIHI9IjUuNSIvPjxjaXJjbGUgY3g9IjE0MiIgY3k9IjEwMCIgcj0iNSIvPgogICAgPGNpcmNsZSBjeD0iMjY1IiBjeT0iODgiIHI9IjUuNSIvPjxjaXJjbGUgY3g9IjI1MiIgY3k9IjgwIiByPSI1Ii8+PGNpcmNsZSBjeD0iMjYwIiBjeT0iMTA0IiByPSI1Ii8+CiAgICA8Y2lyY2xlIGN4PSIxNDAiIGN5PSIxOTUiIHI9IjUiLz48Y2lyY2xlIGN4PSIxNTUiIGN5PSIyMTAiIHI9IjUuNSIvPjxjaXJjbGUgY3g9IjE3MCIgY3k9IjIyMCIgcj0iNSIvPgogICAgPGNpcmNsZSBjeD0iMjAwIiBjeT0iMjI1IiByPSI1LjUiLz48Y2lyY2xlIGN4PSIyMjUiIGN5PSIyMTgiIHI9IjUiLz48Y2lyY2xlIGN4PSIyNDUiIGN5PSIyMDgiIHI9IjUuNSIvPgogICAgPGNpcmNsZSBjeD0iMjYwIiBjeT0iMTk1IiByPSI1Ii8+PGNpcmNsZSBjeD0iMTIwIiBjeT0iMTgwIiByPSI1LjUiLz48Y2lyY2xlIGN4PSIxMDgiIGN5PSIxOTUiIHI9IjUiLz4KICAgIDwhLS0gSW50cmF0dW1vcmFsIGx5bXBob2N5dGVzIC0gaW5maWx0cmF0aW5nIC0tPgogICAgPGNpcmNsZSBjeD0iMTg4IiBjeT0iMTQ4IiByPSI0LjUiIG9wYWNpdHk9IjAuOCIvPgogICAgPGNpcmNsZSBjeD0iMjE3IiBjeT0iMTQzIiByPSI0IiBvcGFjaXR5PSIwLjgiLz4KICAgIDxjaXJjbGUgY3g9IjIwNSIgY3k9IjE1NyIgcj0iNC41IiBvcGFjaXR5PSIwLjgiLz4KICAgIDxjaXJjbGUgY3g9IjE4MyIgY3k9IjE3OCIgcj0iNCIgb3BhY2l0eT0iMC44Ii8+CiAgICA8Y2lyY2xlIGN4PSIyMjAiIGN5PSIxNzUiIHI9IjQuNSIgb3BhY2l0eT0iMC44Ii8+CiAgPC9nPgogIDwhLS0gVElMIHNjb3JlIGluZGljYXRvciAtLT4KICA8cmVjdCB4PSIxMiIgeT0iMjQwIiB3aWR0aD0iMTc1IiBoZWlnaHQ9IjUwIiBmaWxsPSJyZ2JhKDI2LDEwNyw2MCwwLjg1KSIgcng9IjYiLz4KICA8dGV4dCB4PSI5OSIgeT0iMjYwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSJ3aGl0ZSIgZm9udC13ZWlnaHQ9ImJvbGQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5TY29yZSBUSUxzIChTYWxnYWRvIDIwMTUpPC90ZXh0PgogIDx0ZXh0IHg9Ijk5IiB5PSIyNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0id2hpdGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5USUxzIGVzdHJvbWFpczogfjYwJSDihpIgQUxUTzwvdGV4dD4KICA8dGV4dCB4PSI5OSIgeT0iMjg3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjkiIGZpbGw9IiM5MEZGQjAiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj7ihpEgcmVzcG9zdGEgUVQgbmVvYWRqdXZhbnRlPC90ZXh0PgogIDwhLS0gTGVnZW5kIC0tPgogIDxyZWN0IHg9IjIxNSIgeT0iMjQwIiB3aWR0aD0iMTc1IiBoZWlnaHQ9IjUwIiBmaWxsPSJyZ2JhKDAsMCwwLDAuMDgpIiByeD0iNiIgc3Ryb2tlPSJyZ2JhKDAsMCwwLDAuMTUpIiBzdHJva2Utd2lkdGg9IjAuNSIvPgogIDxjaXJjbGUgY3g9IjIyOCIgY3k9IjI1NSIgcj0iNSIgZmlsbD0iIzFBMzA5MCIvPgogIDx0ZXh0IHg9IjIzNyIgeT0iMjU4IiBmb250LXNpemU9IjkiIGZpbGw9IiM0NDQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5MaW5mw7NjaXRvIChUSUwpPC90ZXh0PgogIDxjaXJjbGUgY3g9IjIyOCIgY3k9IjI3MCIgcj0iOCIgZmlsbD0iI0M4NzBBMCIvPgogIDxjaXJjbGUgY3g9IjIyOCIgY3k9IjI3MCIgcj0iNSIgZmlsbD0iIzUwMzBBMCIvPgogIDx0ZXh0IHg9IjIzNyIgeT0iMjczIiBmb250LXNpemU9IjkiIGZpbGw9IiM0NDQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5Dw6lsdWxhIHR1bW9yYWwgKFROQkMpPC90ZXh0Pgo8L3N2Zz4=',
    credit:'Ilustração clínica TNBC Predictor HCM · A. Sualé / UEM 2026 · Baseado em: Salgado et al. 2015, TIL guidelines',
    color:'#1A6B3C',emoji:'🔬',
    facts:[{l:'TILs >50% → pCR',v:'↑ significativo'},{l:'Score (Salgado 2015)',v:'% linfócitos estroma'},{l:'Status HCM',v:'Não avaliado rotina'}]
  },
  // ---- IMAGIOLOGIA ----
  {
    cat:'img',
    title:'Mamografia CC — massa espiculada BI-RADS 5',
    desc:'Massa densa com bordos espiculados e irregulares, sem calcificações associadas — padrão típico de carcinoma ductal invasivo de alto grau. TNBC apresenta-se como massa não-calcificada com margens ill-defined ou espiculadas em 63% dos casos (AJR 2011). BI-RADS 5: VPP >95%. Sensibilidade TNBC: 75–85%.',
    tags:['Mamografia','BI-RADS 5','Espiculada','TNBC','CC'],
    img:'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMzAwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCI+CiAgPHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiMwQTBBMEEiLz4KICA8IS0tIEJyZWFzdCB0aXNzdWUgLSBncmV5IGRlbnNpdGllcyAtLT4KICA8ZWxsaXBzZSBjeD0iMjAwIiBjeT0iMTYwIiByeD0iMTcwIiByeT0iMTMwIiBmaWxsPSIjMkEyQTJBIi8+CiAgPCEtLSBEZW5zZSBwYXJlbmNoeW1hIC0tPgogIDxlbGxpcHNlIGN4PSIxNjAiIGN5PSIxNDAiIHJ4PSI4MCIgcnk9IjYwIiBmaWxsPSIjNDA0MDQwIiBvcGFjaXR5PSIwLjgiLz4KICA8ZWxsaXBzZSBjeD0iMjIwIiBjeT0iMTIwIiByeD0iNjAiIHJ5PSI0MCIgZmlsbD0iIzM1MzUzNSIgb3BhY2l0eT0iMC43Ii8+CiAgPCEtLSBTcGljdWxhdGVkIG1hc3MgLSBUTkJDIHR5cGljYWwgLS0+CiAgPGVsbGlwc2UgY3g9IjE5NSIgY3k9IjE1NSIgcng9IjI4IiByeT0iMjIiIGZpbGw9IiM4MDgwODAiLz4KICA8ZWxsaXBzZSBjeD0iMTk1IiBjeT0iMTU1IiByeD0iMjIiIHJ5PSIxNyIgZmlsbD0iIzkwOTA5MCIvPgogIDxlbGxpcHNlIGN4PSIxOTUiIGN5PSIxNTUiIHJ4PSIxNiIgcnk9IjEyIiBmaWxsPSIjQTBBMEEwIi8+CiAgPCEtLSBTcGljdWxlcyByYWRpYXRpbmcgb3V0d2FyZCAtLT4KICA8bGluZSB4MT0iMTk1IiB5MT0iMTMzIiB4Mj0iMTk1IiB5Mj0iMTA1IiBzdHJva2U9IiM2MDYwNjAiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPGxpbmUgeDE9IjIwOCIgeTE9IjEzNyIgeDI9IjIyOCIgeTI9IjExMiIgc3Ryb2tlPSIjNjA2MDYwIiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDxsaW5lIHgxPSIyMTgiIHkxPSIxNDgiIHgyPSIyNDgiIHkyPSIxNDAiIHN0cm9rZT0iIzYwNjA2MCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8bGluZSB4MT0iMjIwIiB5MT0iMTYyIiB4Mj0iMjUyIiB5Mj0iMTY4IiBzdHJva2U9IiM2MDYwNjAiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPGxpbmUgeDE9IjIxMCIgeTE9IjE3MyIgeDI9IjIyOCIgeTI9IjE5NSIgc3Ryb2tlPSIjNjA2MDYwIiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDxsaW5lIHgxPSIxOTUiIHkxPSIxNzgiIHgyPSIxOTAiIHkyPSIyMDUiIHN0cm9rZT0iIzYwNjA2MCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8bGluZSB4MT0iMTgwIiB5MT0iMTczIiB4Mj0iMTYyIiB5Mj0iMTk1IiBzdHJva2U9IiM2MDYwNjAiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPGxpbmUgeDE9IjE3MCIgeTE9IjE2MiIgeDI9IjE0NSIgeTI9IjE3MCIgc3Ryb2tlPSIjNjA2MDYwIiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDxsaW5lIHgxPSIxNzIiIHkxPSIxNDgiIHgyPSIxNDUiIHkyPSIxNDIiIHN0cm9rZT0iIzYwNjA2MCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8bGluZSB4MT0iMTc4IiB5MT0iMTM3IiB4Mj0iMTYyIiB5Mj0iMTE4IiBzdHJva2U9IiM2MDYwNjAiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPCEtLSBTa2luIGxpbmUgLS0+CiAgPHBhdGggZD0iTTMwIDMwIFEgMjAwIDEwIDM3MCAzNSBMIDM4MCAzMDAgUSAyMDAgMzEwIDIwIDMwMCBaIiBmaWxsPSJub25lIiBzdHJva2U9IiM1NTUiIHN0cm9rZS13aWR0aD0iMiIvPgogIDwhLS0gTmlwcGxlIC0tPgogIDxjaXJjbGUgY3g9IjIwMCIgY3k9IjI3MCIgcj0iNSIgZmlsbD0iIzQ0NCIvPgogIDwhLS0gUGVjdG9yYWwgbXVzY2xlIC0tPgogIDxwYXRoIGQ9Ik0zMzAgMzAgTCAzODAgMzAgTCAzODAgMjIwIFEgMzYwIDI0MCAzMzAgMjUwIFoiIGZpbGw9IiMxQTFBMUEiLz4KICA8IS0tIEJJLVJBRFMgbGFiZWwgLS0+CiAgPHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjQwMCIgaGVpZ2h0PSIxOCIgZmlsbD0icmdiYSgwLDAsMCwwLjg1KSIvPgogIDx0ZXh0IHg9IjgiIHk9IjEzIiBmb250LXNpemU9IjEwIiBmaWxsPSJ3aGl0ZSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSJib2xkIj5NYW1vZ3JhZmlhIENDIMK3IE1hc3NhIGVzcGljdWxhZGEgwrcgQkktUkFEUyA1PC90ZXh0PgogIDwhLS0gQW5ub3RhdGlvbnMgLS0+CiAgPGNpcmNsZSBjeD0iMTk1IiBjeT0iMTU1IiByPSIzNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjRkZDQzAwIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWRhc2hhcnJheT0iNCAzIi8+CiAgPHRleHQgeD0iMjM1IiB5PSIxMDgiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iI0ZGQ0MwMCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPm1hc3NhPC90ZXh0PgogIDx0ZXh0IHg9IjIzNSIgeT0iMTE5IiBmb250LXNpemU9IjkiIGZpbGw9IiNGRkNDMDAiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5lc3BpY3VsYWRhPC90ZXh0PgogIDx0ZXh0IHg9IjIzNSIgeT0iMTMwIiBmb250LXNpemU9IjkiIGZpbGw9IiNGRkNDMDAiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj4zLjIgY208L3RleHQ+CiAgPCEtLSBTY2FsZSAtLT4KICA8cmVjdCB4PSIxNSIgeT0iMjc1IiB3aWR0aD0iNDAiIGhlaWdodD0iMiIgZmlsbD0id2hpdGUiLz4KICA8dGV4dCB4PSIxNSIgeT0iMjkxIiBmb250LXNpemU9IjgiIGZpbGw9IndoaXRlIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+MiBjbTwvdGV4dD4KPC9zdmc+',
    credit:'Ilustração clínica TNBC Predictor HCM · A. Sualé / UEM 2026 · Baseado em: AJR 2011 TNBC imaging characteristics',
    color:'#1B4F72',emoji:'🩻',
    facts:[{l:'BI-RADS',v:'5 (VPP >95%)'},{l:'Calcificações',v:'Ausentes (58% TNBC)'},{l:'Sensibilidade',v:'75–85%'}]
  },
  {
    cat:'img',
    title:'Ecografia mamária — nódulo hipoecogénico U5 (EUSOMA D06)',
    desc:'Nódulo sólido hipoecogénico 3.8×2.9cm, forma irregular, bordos angulares, sombra acústica posterior. Classificação U5 (altamente suspeito). Ecografia é 1ª linha no HCM por custo-efectividade e disponibilidade. EUSOMA D06/D07. Permite biópsia guiada. TNBC pode ter margens circunscritas (~30%) — aspecto "enganador".',
    tags:['Ecografia','U5','Hipoecogénico','EUSOMA D06','Sombra acústica'],
    img:'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMzAwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCI+CiAgPHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiMwRDFBMkEiLz4KICA8IS0tIFVTIHRpc3N1ZSBiYWNrZ3JvdW5kIC0gc3BlY2tsZSBwYXR0ZXJuIC0tPgogIDxyZWN0IHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIiBmaWxsPSIjMUEyQTNBIi8+CiAgPCEtLSBTa2luIGxpbmUgLS0+CiAgPHJlY3QgeD0iMCIgeT0iMzAiIHdpZHRoPSI0MDAiIGhlaWdodD0iNCIgZmlsbD0iIzdBQUFCQiIvPgogIDwhLS0gU3ViY3V0YW5lb3VzIGZhdCAtIGh5cGVyZWNob2ljIC0tPgogIDxyZWN0IHg9IjAiIHk9IjM0IiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjM1IiBmaWxsPSIjNEE2QTdBIiBvcGFjaXR5PSIwLjYiLz4KICA8IS0tIEJyZWFzdCBwYXJlbmNoeW1hIC0gbWl4ZWQgZWNob2dlbmljaXR5IC0tPgogIDxyZWN0IHg9IjAiIHk9IjY5IiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0iIzJBNEE1QSIvPgogIDwhLS0gRmlicm9nbGFuZHVsYXIgdGlzc3VlIHBhdGNoZXMgLS0+CiAgPGVsbGlwc2UgY3g9IjEwMCIgY3k9IjEyMCIgcng9IjcwIiByeT0iMzAiIGZpbGw9IiM1QThBOUEiIG9wYWNpdHk9IjAuNCIvPgogIDxlbGxpcHNlIGN4PSIzMDAiIGN5PSIxNDAiIHJ4PSI2MCIgcnk9IjI1IiBmaWxsPSIjNEE3QThBIiBvcGFjaXR5PSIwLjQiLz4KICA8ZWxsaXBzZSBjeD0iMjAwIiBjeT0iMjQwIiByeD0iODAiIHJ5PSIyMCIgZmlsbD0iIzRBN0E4QSIgb3BhY2l0eT0iMC4zIi8+CiAgPCEtLSBIeXBvZWNob2ljIG1hc3MgLSBUTkJDIHR5cGljYWwgLS0+CiAgPGVsbGlwc2UgY3g9IjIwMCIgY3k9IjE2NSIgcng9IjU1IiByeT0iNDIiIGZpbGw9IiMwQTE1MjAiIG9wYWNpdHk9IjAuOTUiLz4KICA8ZWxsaXBzZSBjeD0iMjAwIiBjeT0iMTY1IiByeD0iNTAiIHJ5PSIzOCIgZmlsbD0iIzBEMUEyNSIvPgogIDwhLS0gQW5ndWxhciBib3JkZXJzIHR5cGljYWwgb2YgbWFsaWduYW5jeSAtLT4KICA8cGF0aCBkPSJNMTQ4IDE1MCBMMTU1IDEzOCBMMTcwIDEzMCBMMTk1IDEyNyBMMjIwIDEzMCBMMjM4IDE0MCBMMjQ1IDE1NSBMMjQ4IDE3MCBMMjQyIDE4MyBMMjMwIDE5MiBMMjEwIDE5NiBMMTkwIDE5NiBMMTcwIDE5MiBMMTU4IDE4MyBMMTUwIDE3MCBaIiBmaWxsPSIjMEExNTIwIiBzdHJva2U9IiMxQTMwNDAiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPCEtLSBQb3N0ZXJpb3IgYWNvdXN0aWMgc2hhZG93aW5nIC0tPgogIDxwYXRoIGQ9Ik0xNDggMTk4IEwxMzUgMzAwIE0yNTIgMTk4IEwyNjUgMzAwIiBzdHJva2U9IiMwNTBEMTgiIHN0cm9rZS13aWR0aD0iMTUiIG9wYWNpdHk9IjAuNiIvPgogIDwhLS0gSW50ZXJuYWwgbG93LWxldmVsIGVjaG9lcyAtLT4KICA8Y2lyY2xlIGN4PSIxODUiIGN5PSIxNTUiIHI9IjIiIGZpbGw9IiMxQTMwNDAiIG9wYWNpdHk9IjAuOCIvPgogIDxjaXJjbGUgY3g9IjIwMCIgY3k9IjE2MCIgcj0iMiIgZmlsbD0iIzFBMzA0MCIgb3BhY2l0eT0iMC44Ii8+CiAgPGNpcmNsZSBjeD0iMjE1IiBjeT0iMTU4IiByPSIxLjUiIGZpbGw9IiMxQTMwNDAiIG9wYWNpdHk9IjAuOCIvPgogIDxjaXJjbGUgY3g9IjE5MiIgY3k9IjE3MiIgcj0iMiIgZmlsbD0iIzFBMzA0MCIgb3BhY2l0eT0iMC44Ii8+CiAgPCEtLSBEZXB0aCBtYXJrZXJzIC0tPgogIDx0ZXh0IHg9IjgiIHk9IjQ1IiBmb250LXNpemU9IjgiIGZpbGw9IiM1QUFBQkIiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiPjAuNTwvdGV4dD4KICA8dGV4dCB4PSI4IiB5PSI4NSIgZm9udC1zaXplPSI4IiBmaWxsPSIjNUFBQUJCIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIj4xLjA8L3RleHQ+CiAgPHRleHQgeD0iOCIgeT0iMTM1IiBmb250LXNpemU9IjgiIGZpbGw9IiM1QUFBQkIiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiPjIuMDwvdGV4dD4KICA8dGV4dCB4PSI4IiB5PSIxODUiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iIzVBQUFCQiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSI+My4wPC90ZXh0PgogIDx0ZXh0IHg9IjgiIHk9IjIzNSIgZm9udC1zaXplPSI4IiBmaWxsPSIjNUFBQUJCIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIj40LjA8L3RleHQ+CiAgPCEtLSBDYWxsaXBlcnMgLS0+CiAgPGxpbmUgeDE9IjE0OCIgeTE9IjEzMCIgeDI9IjI0OCIgeTI9IjEzMCIgc3Ryb2tlPSIjRkZGRjAwIiBzdHJva2Utd2lkdGg9IjEiLz4KICA8bGluZSB4MT0iMTQ4IiB5MT0iMTMwIiB4Mj0iMTQ4IiB5Mj0iMTM1IiBzdHJva2U9IiNGRkZGMDAiIHN0cm9rZS13aWR0aD0iMiIvPgogIDxsaW5lIHgxPSIyNDgiIHkxPSIxMzAiIHgyPSIyNDgiIHkyPSIxMzUiIHN0cm9rZT0iI0ZGRkYwMCIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHRleHQgeD0iMTc1IiB5PSIxMjUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iI0ZGRkYwMCIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSI+My44IGNtPC90ZXh0PgogIDxsaW5lIHgxPSIyNjUiIHkxPSIxMzAiIHgyPSIyNjUiIHkyPSIyMDAiIHN0cm9rZT0iI0ZGRkYwMCIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgPGxpbmUgeDE9IjI2MCIgeTE9IjEzMCIgeDI9IjI3MCIgeTI9IjEzMCIgc3Ryb2tlPSIjRkZGRjAwIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8bGluZSB4MT0iMjYwIiB5MT0iMjAwIiB4Mj0iMjcwIiB5Mj0iMjAwIiBzdHJva2U9IiNGRkZGMDAiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjI2OCIgeT0iMTY4IiBmb250LXNpemU9IjkiIGZpbGw9IiNGRkZGMDAiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiPjIuOWNtPC90ZXh0PgogIDwhLS0gSGVhZGVyIC0tPgogIDxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSI0MDAiIGhlaWdodD0iMTgiIGZpbGw9InJnYmEoMCwwLDAsMC44NSkiLz4KICA8dGV4dCB4PSI4IiB5PSIxMyIgZm9udC1zaXplPSIxMCIgZmlsbD0id2hpdGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iYm9sZCI+RWNvZ3JhZmlhIG1hbcOhcmlhIMK3IE7Ds2R1bG8gaGlwb2Vjb2fDqW5pY28gaXJyZWd1bGFyIMK3IFU1PC90ZXh0PgogIDwhLS0gQW5ub3RhdGlvbnMgLS0+CiAgPHRleHQgeD0iMjU1IiB5PSIxNjAiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iI0ZGQUEwMCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPmJvcmRvczwvdGV4dD4KICA8dGV4dCB4PSIyNTUiIHk9IjE3MCIgZm9udC1zaXplPSI4IiBmaWxsPSIjRkZBQTAwIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+aXJyZWd1bGFyZXM8L3RleHQ+CiAgPHRleHQgeD0iMTQ4IiB5PSIyMjUiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iIzg4OTlBQSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPnNvbWJyYSBhY8O6c3RpY2E8L3RleHQ+Cjwvc3ZnPg==',
    credit:'Ilustração clínica TNBC Predictor HCM · A. Sualé / UEM 2026 · Baseado em: EUSOMA D06/D07, AJR 2011',
    color:'#1A6B3C',emoji:'🩻',
    facts:[{l:'Classificação',v:'U5 — altamente suspeito'},{l:'EUSOMA',v:'D06 / D07'},{l:'Disponível HCM',v:'✓ Sim'}]
  },
  // ---- ESPECÍFICO TNBC ----
  {
    cat:'tnbc',
    title:'Dados reais HCM — Moza-BC Cohort (Brandão et al. ESMO Open 2020)',
    desc:'Dados reais do único estudo de sobrevivência por subtipo de cancro da mama em Moçambique: 210 pacientes HCM (Jan 2015–Ago 2017). TNBC: 25% (52/210). OS 3 anos TNBC: 31.9%. DFS 3 anos: 26.7%. HR de morte TNBC vs ER+: 3.10 (IC 95%: 1.81–5.31, p<0.001). 74% estadio III/IV. 92% mastectomia. pCR: apenas 2%.',
    tags:['Moza-BC','HCM','Dados reais','OS 31.9%','Moçambique'],
    img:'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMzAwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCI+CiAgPHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiNGMkY0RjAiLz4KICA8IS0tIFRpdGxlIC0tPgogIDxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSI0MDAiIGhlaWdodD0iMjAiIGZpbGw9IiMxQTZCM0MiLz4KICA8dGV4dCB4PSIyMDAiIHk9IjE0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjExIiBmaWxsPSJ3aGl0ZSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSJib2xkIj5Nb3phLUJDIOKAlCBIQ00gTW/Dp2FtYmlxdWUgwrcgQnJhbmTDo28gZXQgYWwuIEVTTU8gT3BlbiAyMDIwPC90ZXh0PgogIDwhLS0gU3VidGl0bGUgLS0+CiAgPHRleHQgeD0iMjAwIiB5PSIzNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI5IiBmaWxsPSIjNTU1IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+bj0yMTAgcGFjaWVudGVzIMK3IEphbiAyMDE14oCTQWdvIDIwMTcgwrcgSG9zcGl0YWwgQ2VudHJhbCBkZSBNYXB1dG88L3RleHQ+CiAgPCEtLSBDaGFydCBhcmVhIC0tPgogIDxsaW5lIHgxPSI2MCIgeTE9IjI1MCIgeDI9IjM4MCIgeTI9IjI1MCIgc3Ryb2tlPSIjOTk5IiBzdHJva2Utd2lkdGg9IjEiLz4KICA8bGluZSB4MT0iNjAiIHkxPSI1MCIgeDI9IjYwIiB5Mj0iMjUwIiBzdHJva2U9IiM5OTkiIHN0cm9rZS13aWR0aD0iMSIvPgogIDwhLS0gWSBheGlzIGxhYmVscyAtLT4KICA8dGV4dCB4PSI1NSIgeT0iMjU0IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjgiIGZpbGw9IiM2NjYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj4wJTwvdGV4dD4KICA8dGV4dCB4PSI1NSIgeT0iMjA0IiB0ZXh0LWFuY2hvcj0iZW5kIiBmb250LXNpemU9IjgiIGZpbGw9IiM2NjYiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj4yNSU8L3RleHQ+CiAgPHRleHQgeD0iNTUiIHk9IjE1NCIgdGV4dC1hbmNob3I9ImVuZCIgZm9udC1zaXplPSI4IiBmaWxsPSIjNjY2IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+NTAlPC90ZXh0PgogIDx0ZXh0IHg9IjU1IiB5PSIxMDQiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iIzY2NiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPjc1JTwvdGV4dD4KICA8dGV4dCB4PSI1NSIgeT0iNTQiIHRleHQtYW5jaG9yPSJlbmQiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iIzY2NiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPjEwMCU8L3RleHQ+CiAgPCEtLSBHcmlkbGluZXMgLS0+CiAgPGxpbmUgeDE9IjYwIiB5MT0iMjAwIiB4Mj0iMzgwIiB5Mj0iMjAwIiBzdHJva2U9IiNEREQiIHN0cm9rZS13aWR0aD0iMC41IiBzdHJva2UtZGFzaGFycmF5PSIzIDMiLz4KICA8bGluZSB4MT0iNjAiIHkxPSIxNTAiIHgyPSIzODAiIHkyPSIxNTAiIHN0cm9rZT0iI0RERCIgc3Ryb2tlLXdpZHRoPSIwLjUiIHN0cm9rZS1kYXNoYXJyYXk9IjMgMyIvPgogIDxsaW5lIHgxPSI2MCIgeTE9IjEwMCIgeDI9IjM4MCIgeTI9IjEwMCIgc3Ryb2tlPSIjREREIiBzdHJva2Utd2lkdGg9IjAuNSIgc3Ryb2tlLWRhc2hhcnJheT0iMyAzIi8+CiAgPCEtLSBCYXIgMTogT1MgM3lyIFROQkMgPSAzMS45JSAtLT4KICA8cmVjdCB4PSI3NSIgeT0iMTIyIiB3aWR0aD0iNDAiIGhlaWdodD0iMTI4IiBmaWxsPSIjQzAzOTJCIiBvcGFjaXR5PSIwLjg1IiByeD0iMyIvPgogIDx0ZXh0IHg9Ijk1IiB5PSIxMTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiNDMDM5MkIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iYm9sZCI+MzEuOSU8L3RleHQ+CiAgPHRleHQgeD0iOTUiIHk9IjI2NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI4IiBmaWxsPSIjNDQ0IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+T1MgM2E8L3RleHQ+CiAgPHRleHQgeD0iOTUiIHk9IjI3NCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI4IiBmaWxsPSIjNDQ0IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+VE5CQzwvdGV4dD4KICA8IS0tIEJhciAyOiBERlMgM3lyIFROQkMgPSAyNi43JSAtLT4KICA8cmVjdCB4PSIxMzAiIHk9IjE0MyIgd2lkdGg9IjQwIiBoZWlnaHQ9IjEwNyIgZmlsbD0iI0U3NEMzQyIgb3BhY2l0eT0iMC44NSIgcng9IjMiLz4KICA8dGV4dCB4PSIxNTAiIHk9IjEzOSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZmlsbD0iI0U3NEMzQyIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSJib2xkIj4yNi43JTwvdGV4dD4KICA8dGV4dCB4PSIxNTAiIHk9IjI2NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI4IiBmaWxsPSIjNDQ0IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+REZTIDNhPC90ZXh0PgogIDx0ZXh0IHg9IjE1MCIgeT0iMjc0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjgiIGZpbGw9IiM0NDQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5UTkJDPC90ZXh0PgogIDwhLS0gQmFyIDM6IE9TIDN5ciBIRVIyKyA9IDUzLjElIC0tPgogIDxyZWN0IHg9IjE4NSIgeT0iODgiIHdpZHRoPSI0MCIgaGVpZ2h0PSIxNjIiIGZpbGw9IiNFNjdFMjIiIG9wYWNpdHk9IjAuODUiIHJ4PSIzIi8+CiAgPHRleHQgeD0iMjA1IiB5PSI4NCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZmlsbD0iI0U2N0UyMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtd2VpZ2h0PSJib2xkIj41My4xJTwvdGV4dD4KICA8dGV4dCB4PSIyMDUiIHk9IjI2NSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI4IiBmaWxsPSIjNDQ0IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+T1MgM2E8L3RleHQ+CiAgPHRleHQgeD0iMjA1IiB5PSIyNzQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iIzQ0NCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPkhFUjIrPC90ZXh0PgogIDwhLS0gQmFyIDQ6IE9TIDN5ciBFUisgPSA2MS4xJSAtLT4KICA8cmVjdCB4PSIyNDAiIHk9IjY2IiB3aWR0aD0iNDAiIGhlaWdodD0iMTg0IiBmaWxsPSIjMjdBRTYwIiBvcGFjaXR5PSIwLjg1IiByeD0iMyIvPgogIDx0ZXh0IHg9IjI2MCIgeT0iNjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiMyN0FFNjAiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iYm9sZCI+NjEuMSU8L3RleHQ+CiAgPHRleHQgeD0iMjYwIiB5PSIyNjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iIzQ0NCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPk9TIDNhPC90ZXh0PgogIDx0ZXh0IHg9IjI2MCIgeT0iMjc0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjgiIGZpbGw9IiM0NDQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5FUis8L3RleHQ+CiAgPCEtLSBCYXIgNTogVE5CQyBwY3QgPSAyNSUgLS0+CiAgPHJlY3QgeD0iMzE1IiB5PSIxNTAiIHdpZHRoPSI0MCIgaGVpZ2h0PSIxMDAiIGZpbGw9IiM4RTQ0QUQiIG9wYWNpdHk9IjAuODUiIHJ4PSIzIi8+CiAgPHRleHQgeD0iMzM1IiB5PSIxNDYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTAiIGZpbGw9IiM4RTQ0QUQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iYm9sZCI+MjUlPC90ZXh0PgogIDx0ZXh0IHg9IjMzNSIgeT0iMjY1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjgiIGZpbGw9IiM0NDQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5UTkJDICU8L3RleHQ+CiAgPHRleHQgeD0iMzM1IiB5PSIyNzQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iIzQ0NCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPnRvdGFsPC90ZXh0PgogIDwhLS0gSFIgYW5ub3RhdGlvbiAtLT4KICA8cmVjdCB4PSI2NSIgeT0iMjgyIiB3aWR0aD0iMzMwIiBoZWlnaHQ9IjE0IiBmaWxsPSIjRkZGM0NEIiByeD0iMiIvPgogIDx0ZXh0IHg9IjIzMCIgeT0iMjkyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjgiIGZpbGw9IiM4NTY0MDQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5IUiBtb3J0ZSBUTkJDIHZzIEVSKzogMy4xMCAoSUMgOTUlOiAxLjgx4oCTNS4zMSkgwrcgcCZsdDswLjAwMTwvdGV4dD4KPC9zdmc+',
    credit:'Brandão M. et al. ESMO Open 2020;5:e000829. doi:10.1136/esmoopen-2020-000829 · CC BY-NC 4.0 · HCM/UEM',
    color:'#1A6B3C',emoji:'📊',
    facts:[{l:'TNBC HCM',v:'25% (52/210)'},{l:'OS 3a TNBC',v:'31.9%'},{l:'HR morte',v:'3.10 (p<0.001)'}]
  },
  // ---- ESTADIAMENTO ----
  {
    cat:'stages',
    title:'Estadiamento TNM — distribuição real Moza-BC HCM',
    desc:'Distribuição de estadiamento na coorte Moza-BC do HCM: ~3% Estádio I, ~23% Estádio II, ~51% Estádio III, ~23% Estádio IV. 74% dos casos em estadio III/IV reflecte o diagnóstico tardio em Moçambique — ausência de rastreio organizado. Prognóstico por estadiamento baseado em Moza-BC e literatura SSA.',
    tags:['Estadiamento','TNM','Moza-BC','Diagnóstico tardio','HCM'],
    img:'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMzAwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCI+CiAgPHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiNGNUY1RjUiLz4KICA8cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjIwIiBmaWxsPSIjMUI0RjcyIi8+CiAgPHRleHQgeD0iMjAwIiB5PSIxNCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMSIgZmlsbD0id2hpdGUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXdlaWdodD0iYm9sZCI+RXN0YWRpYW1lbnRvIFROTSDigJQgZGlzdHJpYnVpw6fDo28gTW96YS1CQyBIQ00gKG49MjEwKTwvdGV4dD4KICA8IS0tIDQgc3RhZ2UgYm94ZXMgLS0+CiAgPCEtLSBTdGFnZSBJIC0tPgogIDxyZWN0IHg9IjE1IiB5PSIzNSIgd2lkdGg9IjgwIiBoZWlnaHQ9IjIyMCIgZmlsbD0iI0U4RjVFOSIgcng9IjYiIHN0cm9rZT0iIzRDQUY1MCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8dGV4dCB4PSI1NSIgeT0iNTIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZpbGw9IiMxQTZCM0MiIGZvbnQtd2VpZ2h0PSJib2xkIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+STwvdGV4dD4KICA8IS0tIFNtYWxsIGJyZWFzdCB3aXRoIHNtYWxsIHR1bW9yIC0tPgogIDxlbGxpcHNlIGN4PSI1NSIgY3k9IjExMCIgcng9IjI1IiByeT0iMjAiIGZpbGw9IiNGRkI2QzEiIHN0cm9rZT0iI0ZGOEZBMCIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgPGNpcmNsZSBjeD0iNTUiIGN5PSIxMDQiIHI9IjUiIGZpbGw9IiNDMDM5MkIiLz4KICA8dGV4dCB4PSI1NSIgeT0iMTQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjkiIGZpbGw9IiM1NTUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5UMSBOMCBNMDwvdGV4dD4KICA8dGV4dCB4PSI1NSIgeT0iMTU3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjkiIGZpbGw9IiM1NTUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj50dW1vciDiiaQyY208L3RleHQ+CiAgPHRleHQgeD0iNTUiIHk9IjE2OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI5IiBmaWxsPSIjNTU1IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+c2VtIGfDom5nbGlvczwvdGV4dD4KICA8IS0tIEhDTSBwZXJjZW50YWdlIC0tPgogIDxyZWN0IHg9IjIwIiB5PSIxODUiIHdpZHRoPSI3MCIgaGVpZ2h0PSIyMiIgZmlsbD0iIzRDQUY1MCIgcng9IjQiLz4KICA8dGV4dCB4PSI1NSIgeT0iMTk5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEwIiBmaWxsPSJ3aGl0ZSIgZm9udC13ZWlnaHQ9ImJvbGQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5+MyUgSENNPC90ZXh0PgogIDx0ZXh0IHg9IjU1IiB5PSIyMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iIzFBNkIzQyIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPlNvYnJldi4gNWE8L3RleHQ+CiAgPHRleHQgeD0iNTUiIHk9IjIzNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzFBNkIzQyIgZm9udC13ZWlnaHQ9ImJvbGQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5+ODUlPC90ZXh0PgogIDwhLS0gU3RhZ2UgSUkgLS0+CiAgPHJlY3QgeD0iMTA1IiB5PSIzNSIgd2lkdGg9IjgwIiBoZWlnaHQ9IjIyMCIgZmlsbD0iI0ZGRjhFMSIgcng9IjYiIHN0cm9rZT0iI0ZGQzEwNyIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8dGV4dCB4PSIxNDUiIHk9IjUyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmaWxsPSIjRTY1MTAwIiBmb250LXdlaWdodD0iYm9sZCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPklJPC90ZXh0PgogIDxlbGxpcHNlIGN4PSIxNDUiIGN5PSIxMTAiIHJ4PSIyNSIgcnk9IjIwIiBmaWxsPSIjRkZCNkMxIiBzdHJva2U9IiNGRjhGQTAiIHN0cm9rZS13aWR0aD0iMSIvPgogIDxjaXJjbGUgY3g9IjE0NSIgY3k9IjEwMyIgcj0iOSIgZmlsbD0iI0MwMzkyQiIvPgogIDwhLS0gU21hbGwgbm9kZSAtLT4KICA8Y2lyY2xlIGN4PSIxNjMiIGN5PSI5OCIgcj0iNSIgZmlsbD0iI0MwMzkyQiIgb3BhY2l0eT0iMC42Ii8+CiAgPHRleHQgeD0iMTQ1IiB5PSIxNDUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iIzU1NSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPlQyIE4wLTEgTTA8L3RleHQ+CiAgPHRleHQgeD0iMTQ1IiB5PSIxNTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iIzU1NSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPjLigJM1Y20gb3U8L3RleHQ+CiAgPHRleHQgeD0iMTQ1IiB5PSIxNjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iIzU1NSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPmfDom5nbC4gTjE8L3RleHQ+CiAgPHJlY3QgeD0iMTEwIiB5PSIxODUiIHdpZHRoPSI3MCIgaGVpZ2h0PSIyMiIgZmlsbD0iI0ZGQzEwNyIgcng9IjQiLz4KICA8dGV4dCB4PSIxNDUiIHk9IjE5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZmlsbD0id2hpdGUiIGZvbnQtd2VpZ2h0PSJib2xkIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+fjIzJSBIQ008L3RleHQ+CiAgPHRleHQgeD0iMTQ1IiB5PSIyMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iI0U2NTEwMCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPlNvYnJldi4gNWE8L3RleHQ+CiAgPHRleHQgeD0iMTQ1IiB5PSIyMzciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiIGZpbGw9IiNFNjUxMDAiIGZvbnQtd2VpZ2h0PSJib2xkIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+fjYwJTwvdGV4dD4KICA8IS0tIFN0YWdlIElJSSAtLT4KICA8cmVjdCB4PSIxOTUiIHk9IjM1IiB3aWR0aD0iODAiIGhlaWdodD0iMjIwIiBmaWxsPSIjRkZGM0UwIiByeD0iNiIgc3Ryb2tlPSIjRkY1NzIyIiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDx0ZXh0IHg9IjIzNSIgeT0iNTIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTMiIGZpbGw9IiNCRjM2MEMiIGZvbnQtd2VpZ2h0PSJib2xkIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+SUlJPC90ZXh0PgogIDxlbGxpcHNlIGN4PSIyMzUiIGN5PSIxMDgiIHJ4PSIyOCIgcnk9IjIzIiBmaWxsPSIjRkZCNkMxIiBzdHJva2U9IiNGRjhGQTAiIHN0cm9rZS13aWR0aD0iMSIvPgogIDxjaXJjbGUgY3g9IjIzNSIgY3k9IjEwMCIgcj0iMTQiIGZpbGw9IiNDMDM5MkIiLz4KICA8IS0tIE11bHRpcGxlIG5vZGVzIC0tPgogIDxjaXJjbGUgY3g9IjI1OCIgY3k9IjkzIiByPSI2IiBmaWxsPSIjQzAzOTJCIiBvcGFjaXR5PSIwLjciLz4KICA8Y2lyY2xlIGN4PSIyNjMiIGN5PSIxMDUiIHI9IjUiIGZpbGw9IiNDMDM5MkIiIG9wYWNpdHk9IjAuNiIvPgogIDx0ZXh0IHg9IjIzNSIgeT0iMTQ4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjkiIGZpbGw9IiM1NTUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5UMyBvdSBOMi9OMyBNMDwvdGV4dD4KICA8dGV4dCB4PSIyMzUiIHk9IjE2MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI5IiBmaWxsPSIjNTU1IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+Jmd0OzVjbSBvdTwvdGV4dD4KICA8dGV4dCB4PSIyMzUiIHk9IjE3MiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI5IiBmaWxsPSIjNTU1IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+TjIvTjM8L3RleHQ+CiAgPHJlY3QgeD0iMjAwIiB5PSIxODUiIHdpZHRoPSI3MCIgaGVpZ2h0PSIyMiIgZmlsbD0iI0ZGNTcyMiIgcng9IjQiLz4KICA8dGV4dCB4PSIyMzUiIHk9IjE5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZmlsbD0id2hpdGUiIGZvbnQtd2VpZ2h0PSJib2xkIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+fjUxJSBIQ008L3RleHQ+CiAgPHRleHQgeD0iMjM1IiB5PSIyMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iI0JGMzYwQyIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPlNvYnJldi4gNWE8L3RleHQ+CiAgPHRleHQgeD0iMjM1IiB5PSIyMzciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMTIiIGZpbGw9IiNCRjM2MEMiIGZvbnQtd2VpZ2h0PSJib2xkIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+fjMyJTwvdGV4dD4KICA8IS0tIFN0YWdlIElWIC0tPgogIDxyZWN0IHg9IjI4NSIgeT0iMzUiIHdpZHRoPSIxMDAiIGhlaWdodD0iMjIwIiBmaWxsPSIjRkZFQkVFIiByeD0iNiIgc3Ryb2tlPSIjQjcxQzFDIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSIzMzUiIHk9IjUyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjEzIiBmaWxsPSIjN0IwMDAwIiBmb250LXdlaWdodD0iYm9sZCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPklWPC90ZXh0PgogIDxlbGxpcHNlIGN4PSIzMTUiIGN5PSIxMDgiIHJ4PSIyNCIgcnk9IjIwIiBmaWxsPSIjRkZCNkMxIiBzdHJva2U9IiNGRjhGQTAiIHN0cm9rZS13aWR0aD0iMSIvPgogIDxjaXJjbGUgY3g9IjMxNSIgY3k9IjEwMiIgcj0iMTMiIGZpbGw9IiM4QjAwMDAiLz4KICA8IS0tIERpc3RhbnQgbWV0cyAtLT4KICA8Y2lyY2xlIGN4PSIzNTAiIGN5PSI3OCIgcj0iNyIgZmlsbD0iI0MwMzkyQiIgb3BhY2l0eT0iMC43Ii8+CiAgPGNpcmNsZSBjeD0iMzY1IiBjeT0iOTUiIHI9IjUiIGZpbGw9IiNDMDM5MkIiIG9wYWNpdHk9IjAuNiIvPgogIDxjaXJjbGUgY3g9IjM1OCIgY3k9IjExMCIgcj0iNiIgZmlsbD0iI0MwMzkyQiIgb3BhY2l0eT0iMC42NSIvPgogIDxsaW5lIHgxPSIzMjgiIHkxPSIxMDAiIHgyPSIzNDYiIHkyPSI4MSIgc3Ryb2tlPSIjQzAzOTJCIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjIgMiIvPgogIDxsaW5lIHgxPSIzMjgiIHkxPSIxMDUiIHgyPSIzNjEiIHkyPSI5NyIgc3Ryb2tlPSIjQzAzOTJCIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjIgMiIvPgogIDx0ZXh0IHg9IjMzNSIgeT0iMTQ1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXNpemU9IjkiIGZpbGw9IiM1NTUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5UNCBvdSBNMTwvdGV4dD4KICA8dGV4dCB4PSIzMzUiIHk9IjE1NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSI5IiBmaWxsPSIjNTU1IiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+bWV0w6FzdGFzZXM8L3RleHQ+CiAgPHRleHQgeD0iMzM1IiB5PSIxNjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iIzU1NSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPsOgIGRpc3TDom5jaWE8L3RleHQ+CiAgPHJlY3QgeD0iMjkyIiB5PSIxODUiIHdpZHRoPSI4NiIgaGVpZ2h0PSIyMiIgZmlsbD0iI0I3MUMxQyIgcng9IjQiLz4KICA8dGV4dCB4PSIzMzUiIHk9IjE5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMCIgZmlsbD0id2hpdGUiIGZvbnQtd2VpZ2h0PSJib2xkIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiI+fjIzJSBIQ008L3RleHQ+CiAgPHRleHQgeD0iMzM1IiB5PSIyMjUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOSIgZmlsbD0iIzdCMDAwMCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPlNvYnJldi4gbWVkLjwvdGV4dD4KICA8dGV4dCB4PSIzMzUiIHk9IjIzNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzdCMDAwMCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIj5+MTFtPC90ZXh0PgogIDwhLS0gU291cmNlIG5vdGUgLS0+CiAgPHRleHQgeD0iMjAwIiB5PSIyODgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iIzg4OCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPkZvbnRlOiBCcmFuZMOjbyBldCBhbC4gRVNNTyBPcGVuIDIwMjAgwrcgSENNIE1vw6dhbWJpcXVlIChuPTIxMCkgwrcgVmFsb3JlcyBhcHJveGltYWRvczwvdGV4dD4KPC9zdmc+',
    credit:'Ilustração clínica TNBC Predictor HCM · A. Sualé / UEM 2026 · Dados: Brandão et al. ESMO Open 2020',
    color:'#C0392B',emoji:'📈',
    facts:[{l:'Estadio III/IV',v:'74% (Moza-BC)'},{l:'Estadio I',v:'<3%'},{l:'vs Europa',v:'Estadio I ~20%'}]
  },
];

window.ATLAS_DATA = ATLAS_DATA;

function filterAtlas(cat, btn){
  document.querySelectorAll('#t11 .tb').forEach(b=>b.classList.remove('on'));
  if(btn) btn.classList.add('on');
  renderAtlas(cat);
}

function renderAtlas(cat='all'){
  const data = cat==='all' ? ATLAS_DATA : ATLAS_DATA.filter(d=>d.cat===cat);
  const grid = document.getElementById('atlas-grid');
  if(!grid) return;
  grid.innerHTML = data.map((item,i)=>{
    const idx_real = ATLAS_DATA.indexOf(item);
    const hasImg = item.img;
    const imgHtml = hasImg
      ? `<img src="${item.img}" alt="${item.title}" style="width:100%;height:160px;object-fit:cover;display:block" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'" loading="lazy">
         <div style="display:none;height:160px;background:linear-gradient(135deg,${item.color}22,${item.color}44);align-items:center;justify-content:center;font-size:48px">${item.emoji}</div>`
      : `<div style="height:160px;background:linear-gradient(135deg,${item.color}22,${item.color}44);display:flex;align-items:center;justify-content:center;font-size:56px">${item.img_placeholder||item.emoji}</div>`;
    return `<div onclick="openLB(${idx_real})" style="background:var(--s);border:.5px solid var(--b);border-radius:var(--r);overflow:hidden;cursor:pointer;transition:transform .2s,box-shadow .2s;box-shadow:var(--shadow)" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.transform='';this.style.boxShadow='var(--shadow)'">
      ${imgHtml}
      <div style="padding:12px 14px">
        <p style="font-size:12px;font-weight:600;color:var(--t);margin-bottom:4px;line-height:1.4">${item.title}</p>
        <p style="font-size:11px;color:var(--m);line-height:1.5;margin-bottom:6px">${item.desc.substring(0,90)}...</p>
        <div style="display:flex;gap:4px;flex-wrap:wrap">
          ${item.tags.slice(0,2).map(t=>`<span style="background:${item.color}18;color:${item.color};border:.5px solid ${item.color}30;border-radius:20px;padding:2px 7px;font-size:10px;font-weight:600">${t}</span>`).join('')}
        </div>
      </div>
    </div>`;
  }).join('');
}

function openLB(i){
  const item = ATLAS_DATA[i];
  document.getElementById('lb-title').textContent = item.title;
  document.getElementById('lb-desc').textContent = item.desc;
  document.getElementById('lb-tags').innerHTML = item.tags.map(t=>`<span style="background:rgba(255,255,255,.15);color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:20px;padding:3px 10px;font-size:11px">${t}</span>`).join('');

  const statsHtml = item.facts.map(f=>`<div style="background:rgba(255,255,255,.1);border-radius:6px;padding:8px 12px;text-align:center"><p style="font-size:10px;color:rgba(255,255,255,.65);text-transform:uppercase;font-weight:600;letter-spacing:.06em;margin-bottom:3px">${f.l}</p><p style="font-family:'Instrument Serif',Georgia,serif;font-size:16px;color:#fff">${f.v}</p></div>`).join('');

  const imgUrl = item.img_full || item.img;
  const imgContent = imgUrl
    ? `<div id="lb-zoom-wrap" style="position:relative;overflow:hidden;border-radius:12px;background:#000;cursor:grab;max-height:380px;user-select:none" onmousedown="startPan(event)" onmousemove="doPan(event)" onmouseup="endPan()" onmouseleave="endPan()" onwheel="doZoom(event)">
        <img id="lb-img" src="${imgUrl}" alt="${item.title}" style="width:100%;height:auto;display:block;transition:none;transform-origin:center center;max-height:380px;object-fit:contain" onerror="this.closest('#lb-zoom-wrap').innerHTML='<div style=\'min-height:200px;display:flex;align-items:center;justify-content:center;font-size:72px\'>${item.emoji}</div>'">
        <div style="position:absolute;bottom:8px;right:8px;display:flex;gap:4px;z-index:10">
          <button onclick="event.stopPropagation();zoomIn()" style="background:rgba(0,0,0,.5);color:#fff;border:none;border-radius:6px;padding:5px 10px;cursor:pointer;font-size:14px">+</button>
          <button onclick="event.stopPropagation();zoomOut()" style="background:rgba(0,0,0,.5);color:#fff;border:none;border-radius:6px;padding:5px 10px;cursor:pointer;font-size:14px">−</button>
          <button onclick="event.stopPropagation();resetZoom()" style="background:rgba(0,0,0,.5);color:#fff;border:none;border-radius:6px;padding:5px 10px;cursor:pointer;font-size:11px">↺</button>
          <a href="${imgUrl}" target="_blank" onclick="event.stopPropagation()" style="background:rgba(0,0,0,.5);color:#fff;border:none;border-radius:6px;padding:5px 10px;cursor:pointer;font-size:11px;text-decoration:none;display:inline-block">↗</a>
        </div>
      </div>`
    : `<div style="min-height:180px;background:linear-gradient(135deg,${item.color}40,${item.color}80);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:72px">${item.img_placeholder||item.emoji}</div>`;

  document.getElementById('lb-img-wrap').innerHTML = `
    ${imgContent}
    <p style="font-size:10px;color:rgba(255,255,255,.5);margin-top:6px;text-align:center;font-style:italic">${item.credit} ${imgUrl?'· Roda para zoom · Arrasta para mover':''}</p>
    <div style="display:grid;grid-template-columns:repeat(${item.facts.length},1fr);gap:8px;margin-top:10px">${statsHtml}</div>`;

  // Reset zoom state
  window._zoomScale = 1; window._panX = 0; window._panY = 0; window._panning = false;

  const lb = document.getElementById('lightbox');
  lb.style.display = 'flex';
  lb.style.alignItems = 'center';
  lb.style.justifyContent = 'center';
}

/* ---- PAN & ZOOM ---- */
window._zoomScale=1;window._panX=0;window._panY=0;window._panning=false;window._lastX=0;window._lastY=0;

function applyTransform(){
  const img=document.getElementById('lb-img');
  if(img) img.style.transform=`scale(${window._zoomScale}) translate(${window._panX/window._zoomScale}px,${window._panY/window._zoomScale}px)`;
}
function zoomIn(){window._zoomScale=Math.min(window._zoomScale*1.3,8);applyTransform();}
function zoomOut(){window._zoomScale=Math.max(window._zoomScale/1.3,0.5);applyTransform();}
function resetZoom(){window._zoomScale=1;window._panX=0;window._panY=0;applyTransform();}
function doZoom(e){
  e.preventDefault();
  if(e.deltaY<0)zoomIn();else zoomOut();
}
function startPan(e){
  if(window._zoomScale<=1)return;
  window._panning=true;window._lastX=e.clientX;window._lastY=e.clientY;
  e.currentTarget.style.cursor='grabbing';
}
function doPan(e){
  if(!window._panning)return;
  window._panX+=e.clientX-window._lastX;window._panY+=e.clientY-window._lastY;
  window._lastX=e.clientX;window._lastY=e.clientY;
  applyTransform();
}
function endPan(){
  window._panning=false;
  const w=document.getElementById('lb-zoom-wrap');
  if(w)w.style.cursor='grab';
}

function closeLB(e){
  if(!e || e.target.id==='lightbox' || e.target.tagName==='BUTTON'){
    document.getElementById('lightbox').style.display='none';
  }
}

// Initialize atlas on first render
document.addEventListener('DOMContentLoaded', ()=>{
  if(document.getElementById('atlas-grid')) renderAtlas();
});

/* ---- MODO APRESENTAÇÃO ---- */
function renderPresent(){
  const s = currentScore || {};
  const p = s.p || {};
  const pTNBC = s.pTNBC || 0;
  const pProg = s.pProg || 0;

  if(!p.id){
    document.getElementById('present-output').innerHTML = '<p style="color:var(--m)">Preenche primeiro os dados no separador Simulação.</p>';
    return;
  }

  const riskColor = pTNBC>=70?'#C0392B':pTNBC>=45?'#BE6B15':'#239B52';
  const riskLabel = pTNBC>=70?'ALTO RISCO':pTNBC>=45?'RISCO MODERADO':'BAIXO RISCO';
  const progColor = pProg>=70?'#C0392B':pProg>=45?'#BE6B15':'#239B52';
  const progLabel = pProg>=70?'MUITO RESERVADO':pProg>=45?'RESERVADO':'FAVORÁVEL';
  const urgLabel = Math.max(pTNBC,pProg)>=70?'URGENTE — Agir imediatamente':Math.max(pTNBC,pProg)>=45?'PRIORITÁRIO — Esta semana':'ROTINA — Protocolo standard';
  const urgColor = Math.max(pTNBC,pProg)>=70?'#C0392B':Math.max(pTNBC,pProg)>=45?'#BE6B15':'#239B52';

  document.getElementById('present-output').innerHTML = `
    <div style="border:.5px solid var(--b);border-radius:var(--r);overflow:hidden;margin-top:1rem">

      <!-- Header apresentação -->
      <div style="background:var(--g);color:#fff;padding:1.5rem;text-align:center">
        <p style="font-size:10px;opacity:.7;text-transform:uppercase;letter-spacing:.1em;margin-bottom:6px">Hospital Central de Maputo · Serviço de Oncologia</p>
        <h2 style="font-family:'Instrument Serif',Georgia,serif;font-size:22px;font-weight:400;margin-bottom:4px">Avaliação de Risco TNBC</h2>
        <p style="font-size:14px;opacity:.85">Paciente ${p.id} · ${p.idade} anos · ${new Date().toLocaleDateString('pt-PT')}</p>
      </div>

      <!-- Indicador de urgência -->
      <div style="background:${urgColor};color:#fff;text-align:center;padding:.75rem;font-size:14px;font-weight:700;letter-spacing:.05em">
        ${urgLabel}
      </div>

      <!-- Scores principais -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0">
        <div style="padding:1.5rem;text-align:center;border-right:.5px solid var(--b)">
          <p style="font-size:10px;color:var(--m);text-transform:uppercase;font-weight:700;letter-spacing:.1em;margin-bottom:8px">Probabilidade de TNBC</p>
          <p style="font-family:'Instrument Serif',Georgia,serif;font-size:56px;line-height:1;color:${riskColor};margin-bottom:8px">${pTNBC}%</p>
          <span style="background:${riskColor}22;color:${riskColor};border:.5px solid ${riskColor}44;border-radius:20px;padding:4px 14px;font-size:12px;font-weight:700">${riskLabel}</span>
        </div>
        <div style="padding:1.5rem;text-align:center">
          <p style="font-size:10px;color:var(--m);text-transform:uppercase;font-weight:700;letter-spacing:.1em;margin-bottom:8px">Risco Prognóstico</p>
          <p style="font-family:'Instrument Serif',Georgia,serif;font-size:56px;line-height:1;color:${progColor};margin-bottom:8px">${pProg}%</p>
          <span style="background:${progColor}22;color:${progColor};border:.5px solid ${progColor}44;border-radius:20px;padding:4px 14px;font-size:12px;font-weight:700">${progLabel}</span>
        </div>
      </div>

      <!-- Perfil resumido -->
      <div style="padding:1.25rem;border-top:.5px solid var(--b);background:var(--s2)">
        <p style="font-size:10px;color:var(--m);text-transform:uppercase;font-weight:700;letter-spacing:.1em;margin-bottom:10px">Perfil clínico</p>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">
          ${[
            {l:'Idade',v:p.idade+' anos'},
            {l:'Tumor',v:p.tam+' cm'},
            {l:'Grau',v:['I','II','III'][p.grau-1]||'—'},
            {l:'Estádio',v:'I II III IV'.split(' ')[p.est-1]||'—'},
            {l:'Gânglios',v:p.gan===1?'N+ positivos':'N0'},
            {l:'Ki-67',v:p.ki>0?p.ki+'%':'N/D'},
          ].map(f=>`<div style="background:var(--s);border:.5px solid var(--b);border-radius:8px;padding:8px;text-align:center"><p style="font-size:9px;color:var(--m);font-weight:600;text-transform:uppercase;margin-bottom:3px">${f.l}</p><p style="font-size:15px;font-weight:600;color:var(--t)">${f.v}</p></div>`).join('')}
        </div>
      </div>

      <!-- Conduta resumida -->
      <div style="padding:1.25rem;border-top:.5px solid var(--b)">
        <p style="font-size:10px;color:var(--m);text-transform:uppercase;font-weight:700;letter-spacing:.1em;margin-bottom:10px">Conduta recomendada</p>
        ${pTNBC>=70?`<div style="background:#FDEDEC;border:.5px solid #C0392B;border-radius:8px;padding:10px 14px;margin-bottom:8px"><p style="font-weight:600;color:#8B2118">1. Encaminhamento urgente para IHQ (Joanesburgo)</p></div>`:''}
        ${pProg>=70?`<div style="background:#FDEDEC;border:.5px solid #C0392B;border-radius:8px;padding:10px 14px;margin-bottom:8px"><p style="font-weight:600;color:#8B2118">2. Iniciar quimioterapia sem aguardar IHQ</p></div>`:''}
        ${p.est>=3?`<div style="background:#FEF3E2;border:.5px solid #BE6B15;border-radius:8px;padding:10px 14px;margin-bottom:8px"><p style="font-weight:600;color:#7A4E08">3. Estadiamento completo urgente (RX tórax + eco abdominal)</p></div>`:''}
        ${pProg<70&&pProg<45?`<div style="background:#EAFAF1;border:.5px solid #239B52;border-radius:8px;padding:10px 14px"><p style="font-weight:600;color:#1A6B3C">Protocolo standard — seguimento bimensal</p></div>`:''}
      </div>

      <!-- Rodapé -->
      <div style="padding:.75rem 1.25rem;background:var(--s2);border-top:.5px solid var(--b);display:flex;justify-content:space-between;align-items:center">
        <p style="font-size:10px;color:var(--f)">TNBC Predictor HCM v12.0 · © 2026 Abudala Sualé · UEM/HCM</p>
        <div style="display:flex;gap:8px">
          <button class="btn-g" onclick="window.print()" style="padding:6px 12px;font-size:11px">Imprimir</button>
        </div>
      </div>
    </div>`;
}


/* ---- MODO ESCURO ---- */
function toggleDark(){
  const d=document.documentElement;
  const isDark=d.getAttribute('data-theme')==='dark';
  d.setAttribute('data-theme',isDark?'light':'dark');
  const btn=document.getElementById('dark-btn');
  if(btn)btn.textContent=isDark?'🌙 Escuro':'☀️ Claro';
  // Redraw charts for new theme
  if(typeof renderKM==='function')renderKM();
}

/* ---- CALCULADORA DOSE QT ---- */
function calcDose(){
  const peso = parseFloat(document.getElementById('dose-peso')?.value) || 68;
  const alt = parseFloat(document.getElementById('dose-alt')?.value) || 160;
  const prot = document.getElementById('dose-prot')?.value || 'act';
  
  const bsa = Math.round(Math.sqrt(peso * alt / 3600) * 100) / 100;
  const bsaEl = document.getElementById('bsa-val');
  if(bsaEl) bsaEl.textContent = bsa.toFixed(2) + ' m²';

  const protocols = {
    act:{name:'AC-T Neoadjuvante (Standard TNBC)',drugs:[
      {n:'Doxorrubicina (Adriamicina)',d:60,u:'mg/m²',f:'Ciclo 21d × 4',r:'IV'},
      {n:'Ciclofosfamida',d:600,u:'mg/m²',f:'Ciclo 21d × 4',r:'IV'},
      {n:'Paclitaxel (fase T)',d:80,u:'mg/m²',f:'Semanal × 12',r:'IV'},
    ]},
    ac:{name:'AC (Antraciclina + Ciclofosfamida)',drugs:[
      {n:'Doxorrubicina',d:60,u:'mg/m²',f:'Ciclo 21d × 4',r:'IV'},
      {n:'Ciclofosfamida',d:600,u:'mg/m²',f:'Ciclo 21d × 4',r:'IV'},
    ]},
    carbo:{name:'Carboplatina + Paclitaxel',drugs:[
      {n:'Carboplatina',d:'AUC×6',u:'(calculado)',f:'Ciclo 21d × 6',r:'IV'},
      {n:'Paclitaxel',d:175,u:'mg/m²',f:'Ciclo 21d × 6',r:'IV'},
    ]},
    cmf:{name:'CMF (alternativo)',drugs:[
      {n:'Ciclofosfamida (oral)',d:100,u:'mg/m²',f:'D1-14, ciclo 28d',r:'VO'},
      {n:'Metotrexato',d:40,u:'mg/m²',f:'D1+D8, ciclo 28d',r:'IV'},
      {n:'5-Fluorouracilo',d:600,u:'mg/m²',f:'D1+D8, ciclo 28d',r:'IV'},
    ]},
    pal:{name:'Capecitabina (paliativa)',drugs:[
      {n:'Capecitabina',d:1250,u:'mg/m² bid',f:'D1-14, ciclo 21d',r:'VO'},
    ]},
  };

  const p = protocols[prot] || protocols.act;
  const dEl = document.getElementById('dose-drugs-list');
  if(!dEl) return;
  dEl.innerHTML = `<p style="font-size:11px;font-weight:700;color:var(--g);text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px">${p.name}</p>` +
    p.drugs.map(d => {
      const total = d.d === 'AUC×6' ? 'Ver protocolo' : Math.round(parseFloat(d.d) * bsa) + ' mg';
      return `<div style="background:var(--s2);border:.5px solid var(--b);border-radius:var(--rs);padding:10px 12px;margin-bottom:6px">
        <p style="font-size:12px;font-weight:600;color:var(--t);margin-bottom:5px">${d.n}</p>
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px">
          <div><p style="font-size:9px;color:var(--m);font-weight:600;text-transform:uppercase">Dose/m²</p><p style="font-size:12px;font-weight:700;color:var(--g);font-family:'JetBrains Mono','SF Mono','Fira Code',Menlo,monospace">${d.d} ${d.u}</p></div>
          <div><p style="font-size:9px;color:var(--m);font-weight:600;text-transform:uppercase">Dose total</p><p style="font-size:12px;font-weight:700;color:var(--g);font-family:'JetBrains Mono','SF Mono','Fira Code',Menlo,monospace">${total}</p></div>
          <div><p style="font-size:9px;color:var(--m);font-weight:600;text-transform:uppercase">Via/Freq.</p><p style="font-size:12px;font-weight:600;color:var(--t)">${d.r} · ${d.f}</p></div>
        </div>
      </div>`;
    }).join('');
}

/* ---- VALIDAÇÃO CLÍNICA ---- */
function runValidation(){
  const p = G ? G() : {};
  const warnings = [];
  const ok = [];

  if(p.idade < 20 || p.idade > 85) warnings.push({t:'Idade fora do intervalo esperado',d:'Verificar dado (15–85 anos para TNBC)'});
  else ok.push('Idade plausível para TNBC');

  if(p.tam <= 0 || p.tam > 20) warnings.push({t:'Tamanho tumoral inválido',d:'Revisar medição ecográfica/mamográfica'});
  else if(p.tam > 10) warnings.push({t:'Tumor muito grande (>10cm)',d:'Confirmar medição — pode indicar T4'});
  else ok.push('Tamanho tumoral dentro do esperado');

  if(p.cr > 60) warnings.push({t:'Crescimento >5 anos parece improvável',d:'Rever história clínica — possivelmente tumor negligenciado'});
  else ok.push('Tempo de crescimento plausível');

  if(p.ki > 0 && p.ki < 5) warnings.push({t:'Ki-67 muito baixo (<5%) — incomum em TNBC',d:'Verificar se é TNBC ou outro subtipo'});
  if(p.ki > 90) warnings.push({t:'Ki-67 extremamente alto (>90%)',d:'Confirmar leitura — pode indicar tumor muito agressivo'});

  if(p.gan === 1 && p.est === 1) warnings.push({t:'Inconsistência: N+ com Estádio I',d:'N+ normalmente implica estádio II ou superior'});
  else ok.push('Estadiamento e gânglios consistentes');

  if(p.neut > 0 && p.linf === 0) warnings.push({t:'Neutrófilos sem linfócitos',d:'Preencher linfócitos para calcular NLR'});
  if(p.neut > 15) warnings.push({t:'Neutrófilos muito elevados (>15)',d:'Excluir infecção activa antes de atribuir ao tumor'});

  const vEl = document.getElementById('validation-results');
  if(!vEl) return;

  let html = '';
  if(warnings.length > 0){
    html += warnings.map(w=>`<div style="display:flex;gap:8px;align-items:flex-start;padding:7px 0;border-bottom:.5px solid var(--b)"><span style="font-size:14px;flex-shrink:0">⚠️</span><div><p style="font-size:12px;font-weight:600;color:var(--wn)">${w.t}</p><p style="font-size:11px;color:var(--m)">${w.d}</p></div></div>`).join('');
  }
  if(ok.length > 0){
    html += `<div style="margin-top:8px">${ok.map(o=>`<div style="display:flex;gap:8px;align-items:center;padding:4px 0"><span style="color:var(--g);font-size:12px">✓</span><p style="font-size:11px;color:var(--m)">${o}</p></div>`).join('')}</div>`;
  }
  if(!warnings.length && !ok.length) html = '<p style="font-size:13px;color:var(--f)">Preencha os dados para validar.</p>';
  vEl.innerHTML = html;
}

/* ---- EXPORT JSON ---- */
function exportJSON(){
  const data = {
    metadata:{
      tool:'TNBC Predictor HCM v12.0',
      author:'Abudala Sualé — UEM/HCM',
      date:new Date().toISOString(),
      version:'8.0'
    },
    currentPatient: currentScore && currentScore.p ? {...currentScore.p, scores:{pTNBC:currentScore.pTNBC, pProg:currentScore.pProg, nlr:currentScore.nlr, imc:currentScore.imc}} : null,
    population: typeof patients !== 'undefined' ? patients : []
  };
  const blob = new Blob([JSON.stringify(data,null,2)],{type:'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `tnbc_hcm_${new Date().toISOString().slice(0,10)}.json`;
  a.click();
}

/* ---- COMPARAÇÃO DE PERFIS ---- */
let profileA = null, profileB = null;

function loadCompareA(){
  if(!currentScore || !currentScore.p){
    alert('Preenche os dados no separador Simulação primeiro.');
    return;
  }
  profileA = {...currentScore};
  renderCompareA();
  renderCompareSideBySide();
}

function renderCompareA(){
  if(!profileA){document.getElementById('compare-A-summary').innerHTML='<p style="color:var(--f);font-size:13px">Clica em "Carregar perfil actual"</p>';return;}
  const p=profileA.p;
  document.getElementById('compare-A-summary').innerHTML=`
    <div style="background:var(--gl);border:.5px solid var(--gll);border-radius:var(--rs);padding:10px 12px">
      <p style="font-size:13px;font-weight:600;color:var(--g);margin-bottom:6px">${p.id} · ${p.idade} anos</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:11px;color:var(--m)">
        <span>TNBC: <strong style="color:var(--g)">${profileA.pTNBC}%</strong></span>
        <span>Prog: <strong style="color:var(--g)">${profileA.pProg}%</strong></span>
        <span>Tumor: ${p.tam}cm</span>
        <span>Grau: ${['I','II','III'][p.grau-1]}</span>
      </div>
    </div>`;
}

function updateCompareB(){
  const p={
    idade:parseInt(document.getElementById('cmp-b-idade')?.value)||45,
    tam:parseFloat(document.getElementById('cmp-b-tam')?.value)||3.5,
    grau:parseInt(document.getElementById('cmp-b-grau')?.value)||2,
    est:parseInt(document.getElementById('cmp-b-est')?.value)||2,
    gan:parseInt(document.getElementById('cmp-b-gan')?.value)||0,
    menop:parseInt(document.getElementById('cmp-b-men')?.value)||0,
    peso:68,altura:160,par:2,hfam:0,hor:0,cr:12,hist:1,ulc:0,inv:0,ki:0,neut:0,linf:0,plaq:0
  };
  const s = score(p);
  profileB = {...s, p};
  const sumEl = document.getElementById('compare-B-summary');
  if(sumEl) sumEl.innerHTML=`
    <div style="background:var(--acl);border:.5px solid #B2C8D8;border-radius:var(--rs);padding:10px 12px;margin-top:.75rem">
      <p style="font-size:13px;font-weight:600;color:var(--ac);margin-bottom:6px">Perfil B · ${p.idade} anos</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:11px;color:var(--m)">
        <span>TNBC: <strong style="color:var(--ac)">${s.pTNBC}%</strong></span>
        <span>Prog: <strong style="color:var(--ac)">${s.pProg}%</strong></span>
        <span>Tumor: ${p.tam}cm</span>
        <span>Grau: ${['I','II','III'][p.grau-1]}</span>
      </div>
    </div>`;
  renderCompareSideBySide();
}

function renderCompareSideBySide(){
  const el = document.getElementById('compare-result');
  if(!el) return;
  if(!profileA && !profileB){el.innerHTML='<p style="color:var(--f);font-size:13px">Carrega pelo menos um perfil.</p>';return;}

  const A = profileA || {pTNBC:0,pProg:0,p:{id:'—',idade:'—',tam:'—',grau:1,est:1}};
  const B = profileB || {pTNBC:0,pProg:0,p:{id:'—',idade:'—',tam:'—',grau:1,est:1}};

  const metrics=[
    {l:'Score TNBC',a:A.pTNBC+'%',b:B.pTNBC+'%',better:A.pTNBC<=B.pTNBC?'A':'B'},
    {l:'Score Prognóstico',a:A.pProg+'%',b:B.pProg+'%',better:A.pProg<=B.pProg?'A':'B'},
    {l:'Idade',a:(A.p.idade||'—')+(A.p.idade?'a':''),b:(B.p.idade||'—')+(B.p.idade?'a':''),better:null},
    {l:'Tumor',a:(A.p.tam||'—')+'cm',b:(B.p.tam||'—')+'cm',better:null},
    {l:'IMC',a:A.imc?A.imc.toFixed(1):'—',b:B.imc?B.imc.toFixed(1):'—',better:null},
  ];

  el.innerHTML=`<div style="display:grid;grid-template-columns:2fr 1fr 1fr;gap:0">
    <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--m);padding:8px 0;border-bottom:.5px solid var(--b)">Métrica</div>
    <div style="font-size:11px;font-weight:700;color:var(--g);text-align:center;padding:8px 0;border-bottom:.5px solid var(--b);background:rgba(26,107,60,.05)">Perfil A</div>
    <div style="font-size:11px;font-weight:700;color:var(--ac);text-align:center;padding:8px 0;border-bottom:.5px solid var(--b);background:rgba(27,63,92,.05)">Perfil B</div>
    ${metrics.map(m=>`
    <div style="font-size:12px;color:var(--m);padding:8px 0;border-bottom:.5px solid var(--b)">${m.l}</div>
    <div style="font-size:13px;font-weight:600;color:${m.better==='A'?'var(--g)':'var(--t)'};text-align:center;padding:8px 0;border-bottom:.5px solid var(--b);background:rgba(26,107,60,.05)">${m.a}${m.better==='A'?' ✓':''}</div>
    <div style="font-size:13px;font-weight:600;color:${m.better==='B'?'var(--ac)':'var(--t)'};text-align:center;padding:8px 0;border-bottom:.5px solid var(--b);background:rgba(27,63,92,.05)">${m.b}${m.better==='B'?' ✓':''}</div>`).join('')}
  </div>`;
}

function initCompare(){
  renderCompareA();
  updateCompareB();
}

/* ---- TIMER CLÍNICO ---- */
let timerInterval = null;
let timerStart = null;
let timerRunning = false;

function startTimer(){
  const btn = document.getElementById('timer-start');
  if(timerRunning){
    clearInterval(timerInterval);
    timerRunning = false;
    if(btn) btn.textContent = 'Retomar';
  } else {
    if(!timerStart) timerStart = Date.now();
    else timerStart = Date.now() - (timerStart - 0); // resume
    timerInterval = setInterval(updateTimerDisplay, 1000);
    timerRunning = true;
    if(btn) btn.textContent = 'Pausar';
  }
}

function resetTimer(){
  clearInterval(timerInterval);
  timerRunning = false;
  timerStart = null;
  const el = document.getElementById('elapsed-time');
  if(el) el.textContent = '00:00:00';
  const btn = document.getElementById('timer-start');
  if(btn) btn.textContent = 'Iniciar';
}

function updateTimerDisplay(){
  if(!timerStart) return;
  const elapsed = Math.floor((Date.now() - timerStart) / 1000);
  const h = Math.floor(elapsed / 3600).toString().padStart(2,'0');
  const m = Math.floor((elapsed % 3600) / 60).toString().padStart(2,'0');
  const s = (elapsed % 60).toString().padStart(2,'0');
  const el = document.getElementById('elapsed-time');
  if(el) el.textContent = h+':'+m+':'+s;
}

function calcQuickSchedule(){
  const dateEl = document.getElementById('timer-start-date');
  if(!dateEl || !dateEl.value) return;
  
  const start = new Date(dateEl.value);
  const pTNBC = (currentScore && currentScore.pTNBC) || 50;
  const pProg = (currentScore && currentScore.pProg) || 50;
  
  const isHighRisk = Math.max(pTNBC, pProg) >= 70;
  const intervals = isHighRisk ? [14,28,42,84,168] : [30,60,90,180,365];
  const labels = isHighRisk ? ['2 semanas','1 mês','6 semanas','3 meses','6 meses'] : ['1 mês','2 meses','3 meses','6 meses','1 ano'];

  const scheduleEl = document.getElementById('quick-schedule');
  if(!scheduleEl) return;

  scheduleEl.innerHTML = `<p style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--m);margin-bottom:.75rem;margin-top:.75rem">Calendário de consultas — ${isHighRisk?'Alto risco':'Risco moderado/baixo'}</p>` +
    intervals.map((days,i)=>{
      const d = new Date(start);
      d.setDate(d.getDate() + days);
      const dateStr = d.toLocaleDateString('pt-PT');
      const color = i<2?'var(--dl)':i<3?'var(--wl)':'var(--ol)';
      const textColor = i<2?'var(--dn)':i<3?'var(--wn)':'var(--ok)';
      return `<div style="display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:.5px solid var(--b)">
        <span style="font-size:12px;color:var(--m)">${labels[i]}</span>
        <span style="background:${color};color:${textColor};padding:3px 10px;border-radius:20px;font-size:11px;font-weight:600">${dateStr}</span>
      </div>`;
    }).join('');

  // Recurrence window
  const rwEl = document.getElementById('recurrence-window');
  if(rwEl){
    const peak3 = new Date(start);peak3.setFullYear(peak3.getFullYear()+3);
    rwEl.innerHTML=`
      <div style="background:var(--dl);border:.5px solid var(--dm);border-radius:var(--rs);padding:10px 14px;margin-bottom:6px">
        <p style="font-size:12px;font-weight:600;color:var(--dn);margin-bottom:3px">⚠ Janela de alto risco (0–3 anos)</p>
        <p style="font-size:11px;color:var(--dn)">Até ${peak3.toLocaleDateString('pt-PT')} — seguimento intensivo. TNBC recorre preferencialmente neste período.</p>
      </div>
      <div style="background:var(--wl);border:.5px solid var(--wm);border-radius:var(--rs);padding:10px 14px">
        <p style="font-size:12px;font-weight:600;color:var(--wn);margin-bottom:3px">Sites de metástase mais frequentes em TNBC</p>
        <p style="font-size:11px;color:var(--wn)">Pulmão (40%) · Cérebro (34%) · Fígado (25%) · Raramente osso (vs subtipos HR+)</p>
      </div>`;
  }
}

function initTimerTab(){
  // Set today's date
  const dateEl = document.getElementById('timer-start-date');
  if(dateEl && !dateEl.value) {
    dateEl.value = new Date().toISOString().slice(0,10);
    calcQuickSchedule();
  }
  // Show action reminders based on current profile
  const remEl = document.getElementById('action-reminders');
  if(!remEl) return;
  const pTNBC = (currentScore && currentScore.pTNBC) || 0;
  const pProg = (currentScore && currentScore.pProg) || 0;
  const p = (currentScore && currentScore.p) || {};

  const reminders=[];
  if(pTNBC>=70)reminders.push({t:'Carta de referência para IHQ',u:'Hoje',col:'var(--dl)',tc:'var(--dn)'});
  if(pProg>=70)reminders.push({t:'Iniciar protocolo QT',u:'Esta semana',col:'var(--dl)',tc:'var(--dn)'});
  if(p.est>=3)reminders.push({t:'Pedir RX tórax + eco abdominal',u:'Hoje',col:'var(--wl)',tc:'var(--wn)'});
  if((currentScore&&currentScore.nlr)>4)reminders.push({t:'Repetir hemograma (NLR elevado)',u:'Próxima semana',col:'var(--wl)',tc:'var(--wn)'});
  reminders.push({t:'Actualizar registo na base de dados HCM',u:'Esta consulta',col:'var(--ol)',tc:'var(--ok)'});

  remEl.innerHTML = reminders.map(r=>`
    <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:.5px solid var(--b)">
      <span style="font-size:12px;color:var(--t)">${r.t}</span>
      <span style="background:${r.col};color:${r.tc};padding:3px 10px;border-radius:20px;font-size:11px;font-weight:600">${r.u}</span>
    </div>`).join('');
}

/* ---- API KEY MANAGEMENT ---- */
function saveKey(){
  const k=document.getElementById('ai-apikey')?.value;
  if(k&&k.startsWith('sk-ant')){
    sessionStorage.setItem('tnbc_apikey',k);
    const btn=document.querySelector('[onclick="saveKey()"]');
    if(btn){btn.textContent='✓ Guardada';btn.style.background='var(--g)';setTimeout(()=>{btn.textContent='Guardar';},2000);}
  }else{
    alert('Chave inválida. Deve começar com sk-ant-...');
  }
}
// Auto-load saved key
window.addEventListener('load',()=>{
  const saved=sessionStorage.getItem('tnbc_apikey');
  const inp=document.getElementById('ai-apikey');
  if(saved&&inp)inp.value=saved;
});

/* ---- SCORE SHEET IMPRIMÍVEL ---- */
function printScoreSheet(){
  const p = G ? G() : {};
  const s = currentScore || {};
  const pTNBC = s.pTNBC || 0;
  const pProg = s.pProg || 0;
  const nlr = s.nlr || 0;
  const imc = s.imc || 0;

  const grauStr = ['I','II','III'][(p.grau||1)-1];
  const estStr = ['I','II','III','IV'][(p.est||1)-1];
  const riskCol = pTNBC>=70?'#C0392B':pTNBC>=45?'#BE6B15':'#239B52';
  const progCol = pProg>=70?'#C0392B':pProg>=45?'#BE6B15':'#239B52';

  const win = window.open('','_blank','width=800,height=900');
  win.document.write(`<!DOCTYPE html><html><head>
    <meta charset="UTF-8">
    <title>Score Sheet — ${p.id||'HCM'} — TNBC Predictor</title>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
      body{font-family:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Helvetica,Arial,sans-serif;margin:0;padding:20px;color:#1A180F;font-size:13px}
      h1{font-family:'Instrument Serif',Georgia,serif;font-size:22px;font-weight:400;color:#1A6B3C;margin:0 0 4px}
      .header{border-bottom:3px solid #1A6B3C;padding-bottom:12px;margin-bottom:16px}
      .grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}
      .card{border:.5px solid #DDD;border-radius:8px;padding:12px}
      .score-big{font-family:'Instrument Serif',Georgia,serif;font-size:52px;line-height:1}
      .label{font-size:9px;text-transform:uppercase;font-weight:700;letter-spacing:.1em;color:#666;margin-bottom:4px}
      .row{display:flex;justify-content:space-between;padding:4px 0;border-bottom:.5px solid #EEE}
      .row:last-child{border:none}
      .badge{display:inline-block;padding:2px 10px;border-radius:20px;font-size:11px;font-weight:700}
      .footer{margin-top:16px;padding-top:8px;border-top:.5px solid #DDD;font-size:10px;color:#999;text-align:center}
      @media print{body{padding:10px}}
    </style>
  </head><body>
    <div class="header">
      <h1>TNBC Predictor HCM — Score Sheet</h1>
      <p style="font-size:11px;color:#666;margin:0">Hospital Central de Maputo · © 2026 Abudala Sualé · UEM</p>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;background:#F5F5F0;border-radius:8px;padding:10px 14px;margin-bottom:14px">
      <div><p class="label">Paciente</p><p style="font-size:16px;font-weight:600">${p.id||'—'}</p></div>
      <div><p class="label">Idade</p><p style="font-size:16px;font-weight:600">${p.idade||'—'} anos</p></div>
      <div><p class="label">Data</p><p style="font-size:14px;font-weight:600">${new Date().toLocaleDateString('pt-PT')}</p></div>
      <div><p class="label">IMC</p><p style="font-size:14px;font-weight:600">${imc?imc.toFixed(1):'—'} kg/m²</p></div>
    </div>
    <div class="grid">
      <div class="card" style="border-color:${riskCol}22">
        <p class="label">Objectivo 1 — Probabilidade TNBC</p>
        <p class="score-big" style="color:${riskCol}">${pTNBC}%</p>
        <div style="height:6px;background:#EEE;border-radius:3px;margin:8px 0"><div style="width:${pTNBC}%;height:100%;background:${riskCol};border-radius:3px"></div></div>
        <span class="badge" style="background:${riskCol}22;color:${riskCol}">${pTNBC>=70?'ALTO RISCO':pTNBC>=45?'MODERADO':'BAIXO RISCO'}</span>
      </div>
      <div class="card" style="border-color:${progCol}22">
        <p class="label">Objectivo 2 — Risco Prognóstico</p>
        <p class="score-big" style="color:${progCol}">${pProg}%</p>
        <div style="height:6px;background:#EEE;border-radius:3px;margin:8px 0"><div style="width:${pProg}%;height:100%;background:${progCol};border-radius:3px"></div></div>
        <span class="badge" style="background:${progCol}22;color:${progCol}">${pProg>=70?'MUITO RESERVADO':pProg>=45?'RESERVADO':'FAVORÁVEL'}</span>
      </div>
    </div>
    <div class="grid">
      <div class="card">
        <p class="label">Dados do tumor</p>
        <div class="row"><span>Tamanho</span><span>${p.tam||'—'} cm</span></div>
        <div class="row"><span>Grau hist.</span><span>Grau ${grauStr}</span></div>
        <div class="row"><span>Estadiamento</span><span>Est. ${estStr}</span></div>
        <div class="row"><span>Gânglios</span><span>${p.gan===1?'N+ (positivos)':'N0'}</span></div>
        <div class="row"><span>Invasão vasc.</span><span>${['Não vista','Presente','Incerta'][p.inv||0]}</span></div>
        <div class="row"><span>Ki-67</span><span>${p.ki>0?p.ki+'%':'N/D'}</span></div>
      </div>
      <div class="card">
        <p class="label">Dados clínicos</p>
        <div class="row"><span>Menopausa</span><span>${p.menop===1?'Pré':'Pós'}-menopausa</span></div>
        <div class="row"><span>NLR</span><span style="color:${nlr>4?'#C0392B':nlr>2.5?'#BE6B15':'#239B52'}">${nlr>0?nlr.toFixed(1):'N/D'}${nlr>4?' ⚠':''}</span></div>
        <div class="row"><span>Crescimento</span><span>${p.cr||'—'} meses</span></div>
        <div class="row"><span>Histotipo</span><span>${['','Ductal NST','Lobular','Medular','Outro'][p.hist||1]}</span></div>
        <div class="row"><span>Hist. familiar</span><span>${p.hfam===1?'Sim (1º grau)':'Não'}</span></div>
        <div class="row"><span>Ulceração</span><span>${p.ulc===1?'Sim':'Não'}</span></div>
      </div>
    </div>
    <div class="card" style="margin-bottom:14px;border-color:${pTNBC>=70?'#C0392B':'#1A6B3C'}">
      <p class="label">Conduta recomendada</p>
      ${pTNBC>=70?'<p style="color:#C0392B;font-weight:600;margin:4px 0">▶ Encaminhamento urgente para IHQ (Joanesburgo)</p>':''}
      ${pProg>=70?'<p style="color:#C0392B;font-weight:600;margin:4px 0">▶ Iniciar quimioterapia sem aguardar IHQ</p>':''}
      ${p.est>=3?'<p style="color:#BE6B15;margin:4px 0">▶ Estadiamento completo urgente</p>':''}
      ${pTNBC<45&&pProg<45?'<p style="color:#239B52;margin:4px 0">▶ Protocolo standard — seguimento bimensal</p>':''}
      <p style="font-size:10px;color:#999;margin-top:6px">Baseado em guidelines ESMO 2024 adaptadas ao contexto HCM</p>
    </div>
    <div class="footer">
      TNBC Predictor HCM v10.0 · © 2026 Abudala Sualé · UEM — Faculdade de Medicina · HCM Maputo<br>
      ⚠ Ferramenta de apoio à decisão. Não substitui IHQ nem avaliação especializada.<br>
      Calibrado com dados reais Moza-BC: Brandão et al. ESMO Open 2020;5:e000829.
    </div>
    <script>window.onload=()=>{window.print();}<\/script>
  </body></html>`);
  win.document.close();
}

/* ---- PROTOCOLO DE DECISÃO RÁPIDA ---- */
function buildDecisionFlow(){
  const p = G ? G() : {};
  const s = currentScore || {};
  const pTNBC = s.pTNBC || 0;
  const pProg = s.pProg || 0;
  const el = document.getElementById('decision-flow-output');
  if(!el) return;

  const steps = [];

  // Step 1: IHQ urgency
  if(pTNBC >= 70){
    steps.push({
      icon:'🔴', urgent:true,
      title:'Passo 1 — Encaminhar para IHQ urgente',
      body:'Score TNBC ' + pTNBC + '% → alta probabilidade. Enviar biópsia para Joanesburgo (NHLS ou Lancet). Incluir carta de referência com dados clínicos. Prazo esperado: 2–4 semanas.',
      action:'Redigir carta de referência'
    });
  } else if(pTNBC >= 45) {
    steps.push({
      icon:'🟡', urgent:false,
      title:'Passo 1 — Considerar IHQ se disponível',
      body:'Score TNBC ' + pTNBC + '% → risco moderado. IHQ recomendada mas não urgente. Se não disponível nos próximos 30 dias, tratar empiricamente.',
      action:'Avaliar disponibilidade de recursos'
    });
  } else {
    steps.push({
      icon:'🟢', urgent:false,
      title:'Passo 1 — IHQ electiva',
      body:'Score TNBC ' + pTNBC + '% → baixo risco. IHQ quando disponível. Enquanto aguarda, protocolo hormonoterapia empírica pode ser considerado.',
      action:'Protocolo standard'
    });
  }

  // Step 2: Staging
  steps.push({
    icon: p.est >= 3 ? '🔴' : '🟡',
    urgent: p.est >= 3,
    title: 'Passo 2 — Estadiamento completo',
    body: p.est >= 3
      ? 'Estádio ' + ['I','II','III','IV'][(p.est||1)-1] + ' → estadiamento urgente: RX tórax PA + perfil · Ecografia abdominopélvica · Cintilografia óssea se dores. Em HCM disponível nos 7–14 dias.'
      : 'Estádio ' + ['I','II','III','IV'][(p.est||1)-1] + ' → RX tórax de rotina. Ecografia abdominal. Sem urgência de TC.',
    action: p.est >= 3 ? 'Pedir exames urgentes' : 'Pedir exames de rotina'
  });

  // Step 3: QT decision
  if(pProg >= 70 && p.est <= 3){
    steps.push({
      icon:'🔴', urgent:true,
      title:'Passo 3 — Iniciar QT neoadjuvante (não adiar)',
      body:'Score prognóstico ' + pProg + '% + Estádio ' + ['I','II','III','IV'][(p.est||1)-1] + ' → QT neoadjuvante obrigatória. Protocolo: AC (Doxorrubicina 60mg/m² + Ciclofosfamida 600mg/m² × 4 ciclos) → Paclitaxel 80mg/m² semanal × 12. Calcular BSA e doses (ver separador pCR).',
      action:'Calcular doses QT →'
    });
  } else if(p.est === 4) {
    steps.push({
      icon:'🟡', urgent:false,
      title:'Passo 3 — QT paliativa + suporte',
      body:'Estádio IV → objectivo paliativo. Capecitabina 1250mg/m² bid D1-14 ciclo 21d ou Gencitabina 1000mg/m² D1+D8 ciclo 21d. Iniciar cuidados de suporte: analgesia, nutrição, psicologia.',
      action:'Referenciar oncologia + paliativos'
    });
  } else {
    steps.push({
      icon:'🟢', urgent:false,
      title:'Passo 3 — Tratamento cirúrgico primário',
      body:'Score favorável → avaliar elegibilidade cirúrgica. Mastectomia total (92% em HCM) ou conservadora se tumor ≤4cm e sem envolvimento axilar extenso. Programar para 3–4 semanas.',
      action:'Programar cirurgia'
    });
  }

  // Step 4: Follow-up
  const fuInterval = pProg >= 70 ? '15 dias' : pProg >= 45 ? '30 dias' : '60 dias';
  steps.push({
    icon:'📅', urgent:false,
    title:'Passo 4 — Agendamento de seguimento',
    body:'Risco ' + (pProg>=70?'alto':'moderado') + ' → consulta de seguimento em ' + fuInterval + '. Incluir: peso, PA, exame mama, toxicidade QT se em tratamento, hemograma (NLR). Registar no sistema HCM.',
    action:'Agendar em ' + fuInterval
  });

  // NLR specific
  if(s.nlr > 4){
    steps.push({
      icon:'🧪', urgent:true,
      title:'Passo adicional — NLR elevado (>' + s.nlr.toFixed(1) + ')',
      body:'NLR > 4 detectado. Excluir causas infecciosas/inflamatórias antes de atribuir ao tumor: hemograma completo + PCR + urina. Se infecção activa, tratar antes de iniciar QT.',
      action:'Hemograma completo + PCR'
    });
  }

  el.innerHTML = steps.map((s,i) => `
    <div style="border:.5px solid ${s.urgent?'var(--dm)':'var(--b)'};border-radius:var(--rs);margin-bottom:8px;overflow:hidden">
      <div style="display:flex;align-items:center;gap:10px;padding:10px 14px;background:${s.urgent?'var(--dl)':'var(--s2)'};cursor:pointer" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">
        <span style="font-size:18px">${s.icon}</span>
        <span style="font-size:13px;font-weight:600;color:${s.urgent?'var(--dn)':'var(--t)'};flex:1">${s.title}</span>
        <span style="font-size:11px;background:${s.urgent?'var(--dm)':'var(--bs)'};color:#fff;padding:2px 8px;border-radius:20px;flex-shrink:0">${s.action}</span>
      </div>
      <div style="padding:10px 14px;font-size:12px;color:var(--m);line-height:1.7;display:none">${s.body}</div>
    </div>`).join('');
}

/* ---- DRUG AVAILABILITY TABLE ---- */
function buildDrugTable(){
  const el = document.getElementById('drug-availability-table');
  if(!el) return;
  const drugs = [
    {name:'Doxorrubicina (Adriamicina)',avail:true,use:'1ª linha QT (AC)'},
    {name:'Ciclofosfamida',avail:true,use:'1ª linha QT (AC)'},
    {name:'Paclitaxel',avail:true,use:'2ª fase AC-T'},
    {name:'Carboplatina',avail:'parcial',use:'Alternativa, BRCA+'},
    {name:'Capecitabina',avail:true,use:'Paliativa / não-pCR'},
    {name:'Gencitabina',avail:'parcial',use:'Paliativa 2ª linha'},
    {name:'Pembrolizumab',avail:false,use:'PD-L1+ (não disponível HCM)'},
    {name:'Olaparib (PARP-i)',avail:false,use:'BRCA1/2 mutado (não HCM)'},
    {name:'Sacituzumab gov.',avail:false,use:'3ª linha mTNBC (não HCM)'},
    {name:'Tamoxifeno',avail:true,use:'Só se ER+ confirmado'},
    {name:'Metotrexato',avail:true,use:'CMF alternativo'},
  ];
  el.innerHTML = `<table class="dt"><thead><tr>
    <th>Fármaco</th><th>Disponível HCM</th><th>Uso em TNBC</th>
  </tr></thead><tbody>` + drugs.map(d => `
    <tr>
      <td style="font-weight:500">${d.name}</td>
      <td>${d.avail===true?'<span class="badge bo">✓ Sim</span>':d.avail==='parcial'?'<span class="badge bw">⚡ Parcial</span>':'<span class="badge bd">✗ Não</span>'}</td>
      <td style="font-size:11px;color:var(--m)">${d.use}</td>
    </tr>`).join('') + '</tbody></table>';
}

// Auto-build on tab load
const _origT = T;
T = function(id, btn){
  _origT(id, btn);
  if(id === 't5'){
    buildDecisionFlow();
    buildDrugTable();
  }
};
// Also build on first render
setTimeout(() => {
  if(typeof buildDrugTable === 'function') buildDrugTable();
}, 200);

/* ---- MOZA-BC CHART ---- */
let mozaChart = null;
function renderMozaChart(){
  const el = document.getElementById('moza-os-chart');
  if(!el) return;
  if(mozaChart) mozaChart.destroy();
  const isDark = document.documentElement.getAttribute('data-theme')==='dark';
  const tc = isDark ? '#9EA89E' : '#6B6560';
  mozaChart = new Chart(el, {
    type: 'bar',
    data: {
      labels: ['TNBC', 'HER2+', 'ER+/HER2-', 'Média geral'],
      datasets: [
        {
          label: 'OS 3 anos (%)',
          data: [31.9, 53.1, 61.1, 52.4],
          backgroundColor: ['#C0392B','#E67E22','#27AE60','#1B4F72'],
          borderWidth: 0,
          borderRadius: 5
        },
        {
          label: 'DFS 3 anos (%)',
          data: [26.7, 45.2, 54.8, 45.0],
          backgroundColor: ['#E8786A','#F0A060','#70CC90','#4A7FAA'],
          borderWidth: 0,
          borderRadius: 5
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          min: 0, max: 80,
          title: { display: true, text: 'Sobrevivência (%)', font:{size:11}, color:tc },
          ticks: { color: tc }
        },
        x: { ticks: { color: tc } }
      },
      plugins: {
        legend: { position: 'bottom', labels: { font:{size:11}, padding:10, color:tc }},
        tooltip: {
          callbacks: {
            afterLabel: ctx => ctx.datasetIndex===0 && ctx.dataIndex===0 ? 'HR morte vs ER+: 3.10 (p<0.001)' : ''
          }
        }
      }
    }
  });
}

/* ---- MDT TUMOR BOARD ---- */
function buildMDTChecklist(){
  const p = G ? G() : {};
  const s = currentScore || {};
  const pTNBC = s.pTNBC || 0;
  const pProg = s.pProg || 0;
  const pBRCA = s.pBRCA || 0;
  const nlr = s.nlr || 0;

  const items = [
    {done:false, cat:'Diagnóstico', text:'Biópsia core realizada com resultado histológico', req:true},
    {done:false, cat:'Diagnóstico', text:'Grau histológico determinado (Elston-Ellis)', req:true},
    {done:false, cat:'Diagnóstico', text:'IHQ realizada ou enviada (ER, PR, HER2, Ki-67)', req:true},
    {done:p.ki>0, cat:'Diagnóstico', text:'Ki-67 avaliado: '+( p.ki>0?p.ki+'%':'pendente'), req:false},
    {done:false, cat:'Estadiamento', text:'Estadiamento clínico TNM completo', req:true},
    {done:p.est>=1, cat:'Estadiamento', text:'RX tórax PA + Perfil: '+(p.est>=3?'urgente':'rotina'), req:p.est>=3},
    {done:false, cat:'Estadiamento', text:'Ecografia abdomino-pélvica', req:p.est>=3},
    {done:false, cat:'Estadiamento', text:'Cintilografia óssea (se dores ósseas ou est. III/IV)', req:p.est>=3},
    {done:false, cat:'Clínico', text:'ECOG performance status documentado: '+(['0 — Totalmente activo','1','2','3','4'][p.ecog||0]), req:true},
    {done:false, cat:'Clínico', text:'Estado HIV documentado: '+(p.hiv===1?'Positivo — considerar ARV e interacções':'Negativo'), req:true},
    {done:false, cat:'Clínico', text:'Avaliação nutricional (IMC '+( s.imc?s.imc.toFixed(1):'?')+')', req:false},
    {done:false, cat:'Clínico', text:'Discussão fertilidade (se pré-menopausa + jovem)', req:p.menop===1&&p.idade<40},
    {done:false, cat:'Tratamento', text:'Plano QT definido e farmácia consultada sobre disponibilidade', req:pProg>=45},
    {done:false, cat:'Tratamento', text:'Cálculo BSA e doses QT validado por médico sénior', req:pProg>=70},
    {done:false, cat:'Tratamento', text:'Referência IHQ Joanesburgo enviada', req:pTNBC>=70},
    {done:pBRCA>=20, cat:'Genética', text:'Probabilidade BRCA1/2 avaliada: '+pBRCA+'%', req:true},
    {done:false, cat:'Genética', text:'Teste BRCA1/2 solicitado (se indicação)', req:pBRCA>=20||p.hfam===1},
    {done:false, cat:'Comunicação', text:'Paciente informada do diagnóstico e plano terapêutico', req:true},
    {done:false, cat:'Comunicação', text:'Consentimento informado assinado', req:true},
    {done:false, cat:'Comunicação', text:'Consulta paliativos/suporte (se ECOG≥2 ou Est.IV)', req:p.ecog>=2||p.est===4},
  ].filter(i=>i.req||i.done);

  const cats = [...new Set(items.map(i=>i.cat))];
  const el = document.getElementById('mdt-checklist');
  if(!el) return;

  el.innerHTML = cats.map(cat=>`
    <p style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--m);margin:8px 0 4px">${cat}</p>
    ${items.filter(i=>i.cat===cat).map((item,idx)=>`
      <div style="display:flex;align-items:flex-start;gap:8px;padding:5px 0;border-bottom:.5px solid var(--b)">
        <div onclick="this.classList.toggle('checked');this.innerHTML=this.classList.contains('checked')?'✓':'';this.style.background=this.classList.contains('checked')?'var(--g)':'transparent'" 
             style="width:18px;height:18px;border-radius:3px;border:1.5px solid ${item.req?'var(--dm)':'var(--bs)'};flex-shrink:0;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:11px;color:#fff;transition:all .15s;background:${item.done?'var(--g)':'transparent'}">${item.done?'✓':''}</div>
        <span style="font-size:12px;color:var(--t);flex:1">${item.text}</span>
        ${item.req?'<span style="font-size:9px;background:var(--dl);color:var(--dn);padding:1px 6px;border-radius:20px;flex-shrink:0;font-weight:700">REQ</span>':''}
      </div>`).join('')}`).join('');

  // Team
  const teamEl = document.getElementById('mdt-team');
  if(teamEl){
    const team = [
      {role:'Oncologista médico', req:true, note:'Decisão QT e protocolo'},
      {role:'Cirurgião oncológico', req:true, note:'Planeamento cirúrgico'},
      {role:'Anatomia patológica', req:true, note:'Interpretação biópsia e IHQ'},
      {role:'Radiologista', req:p.est>=3, note:'Interpretação imagiologia'},
      {role:'Radioterapeuta', req:p.est>=2, note:'Plano RT pós-cirurgia'},
      {role:'Enfermagem oncológica', req:true, note:'Cuidados e monitorização QT'},
      {role:'Paliativos', req:p.est===4||p.ecog>=2, note:'Suporte sintomático'},
      {role:'Psicólogo/Assistente social', req:p.idade<40||p.menop===1, note:'Suporte psicossocial'},
    ].filter(t=>t.req);
    teamEl.innerHTML = team.map(t=>`
      <div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-bottom:.5px solid var(--b)">
        <span style="font-size:12px;font-weight:500;color:var(--t)">${t.role}</span>
        <span style="font-size:10px;color:var(--m)">${t.note}</span>
      </div>`).join('');
  }

  // Discussion points
  const discEl = document.getElementById('mdt-discussion');
  if(discEl){
    const disc = [];
    if(pTNBC>=70) disc.push({text:'IHQ urgente vs iniciar QT empírica imediatamente?',priority:'alta'});
    if(p.est>=3) disc.push({text:'Ressecabilidade tumoral — cirurgia imediata vs neoadjuvância?',priority:'alta'});
    if(p.hiv===1) disc.push({text:'Interacções QT ↔ ARV — manter ou suspender ARV durante QT?',priority:'alta'});
    if(pBRCA>=20) disc.push({text:'Solicitar teste BRCA — implicação para olaparib adj. (se disponível)?',priority:'mod'});
    if(p.ecog>=2) disc.push({text:'ECOG '+(p.ecog)+' — paciente tolera QT intensiva? Reduzir doses?',priority:'alta'});
    if(p.menop===1&&p.idade<40) disc.push({text:'Preservação fertilidade antes da QT?',priority:'mod'});
    disc.push({text:'Protocolo de monitorização e gestão de toxicidades',priority:'rot'});
    discEl.innerHTML = disc.map(d=>`
      <div style="display:flex;gap:8px;padding:5px 0;border-bottom:.5px solid var(--b)">
        <span class="badge ${d.priority==='alta'?'bd':d.priority==='mod'?'bw':'bi'}" style="flex-shrink:0;font-size:10px">${d.priority==='alta'?'Urgente':'Discutir'}</span>
        <span style="font-size:12px;color:var(--m)">${d.text}</span>
      </div>`).join('');
  }
}

function printMDT(){
  const p = G ? G() : {};
  const s = currentScore || {};
  const date = document.getElementById('mdt-date')?.value || new Date().toISOString().slice(0,10);
  const dec = document.getElementById('mdt-decision')?.value || '—';
  const next = document.getElementById('mdt-next')?.value || '—';
  const win = window.open('','_blank','width=700,height=600');
  win.document.write(`<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Acta MDT — ${p.id}</title>
    <style>body{font-family:sans-serif;margin:20px;font-size:13px}h2{color:#1A6B3C}table{width:100%;border-collapse:collapse}td,th{border:.5px solid #CCC;padding:6px 10px;text-align:left}@media print{body{margin:10px}}
/* ── Dark mode button ── */
.btn-dark{
  background:rgba(255,255,255,.1);
  border:.5px solid rgba(255,255,255,.2);
  border-radius:var(--rs);
  padding:6px 12px;
  font-family:-apple-system,BlinkMacSystemFont,'Inter',sans-serif;
  font-size:12px;
  color:rgba(255,255,255,.9);
  cursor:pointer;
  transition:background .15s;
  letter-spacing:.01em;
}
.btn-dark:hover{background:rgba(255,255,255,.18)}

/* ── Body background - enhanced ── */
body::before{
  content:'';
  position:fixed;inset:0;
  background:
    radial-gradient(ellipse 70% 55% at 8% 15%, rgba(26,107,60,.09) 0%, transparent 55%),
    radial-gradient(ellipse 50% 40% at 92% 85%, rgba(27,63,92,.07) 0%, transparent 55%),
    radial-gradient(ellipse 60% 60% at 50% 50%, rgba(168,123,48,.04) 0%, transparent 70%);
  pointer-events:none;z-index:0;
}
</style>
    </head><body>
    <h2>Acta Reunião MDT — Hospital Central de Maputo</h2>
    <p><strong>Data:</strong> ${date} | <strong>Paciente:</strong> ${p.id||'—'} | <strong>Idade:</strong> ${p.idade||'—'} anos</p>
    <table><tr><th>Score TNBC</th><th>Score Prognóstico</th><th>Estádio</th><th>ECOG</th></tr>
    <tr><td>${s.pTNBC||'—'}%</td><td>${s.pProg||'—'}%</td><td>${['I','II','III','IV'][(p.est||1)-1]}</td><td>${p.ecog||0}</td></tr></table>
    <p style="margin-top:12px"><strong>Decisão MDT:</strong> ${dec}</p>
    <p><strong>Próximo passo:</strong> ${next}</p>
    <p style="margin-top:20px;font-size:10px;color:#888">TNBC Predictor HCM v12 · © 2026 Abudala Sualé · UEM/HCM</p>
    <script>window.onload=()=>{window.print();}<\/script></body></html>`);
  win.document.close();
}

/* ---- BRCA CALCULATOR ---- */
function calcBRCA(){
  const hfam = parseInt(document.getElementById('brca-hfam')?.value||0);
  const ovario = parseInt(document.getElementById('brca-ovario')?.value||0);
  const bi = parseInt(document.getElementById('brca-bi')?.value||0);
  const etnia = parseInt(document.getElementById('brca-etnia')?.value||1);
  const med = parseInt(document.getElementById('brca-med')?.value||0);
  const masc = parseInt(document.getElementById('brca-masc')?.value||0);

  // Tyrer-Cuzick simplified + African adjustment
  let prob = 5; // baseline TNBC BRCA prevalence ~20% but starting conservative
  if(hfam===1) prob += 20;
  if(hfam===2) prob += 38;
  if(ovario===1) prob += 25;
  if(bi===1) prob += 20;
  if(etnia===1) prob += 5; // SSA slightly higher BRCA1 founder variants
  if(med===1) prob += 15; // medullary BRCA1 association
  if(masc===1) prob += 30; // male BC ~ always BRCA2

  prob = Math.min(90, Math.round(prob));

  const probEl = document.getElementById('brca-prob');
  const badgeEl = document.getElementById('brca-badge');
  const interpEl = document.getElementById('brca-interp');
  const therapyEl = document.getElementById('brca-therapy');

  if(!probEl) return;

  const col = prob>=40?'var(--dm)':prob>=20?'var(--wm)':'var(--om)';
  const cls = prob>=40?'bd':prob>=20?'bw':'bo';
  const lbl = prob>=40?'Risco elevado — teste recomendado':prob>=20?'Risco moderado — considerar teste':'Risco baixo';

  probEl.textContent = prob + '%';
  probEl.style.color = col;
  badgeEl.className = 'badge ' + cls;
  badgeEl.textContent = lbl;

  if(interpEl) interpEl.innerHTML = prob>=40
    ? '<p>Probabilidade elevada de mutação gBRCA1/2. Encaminhar para aconselhamento genético e teste. Resultado terá impacto terapêutico directo: PARP inibidores em caso de mutação confirmada.</p>'
    : prob>=20
    ? '<p>Risco moderado. Teste deve ser considerado, especialmente se a paciente estará a receber QT adjuvante ou tem perspectiva de recidiva. Discutir em MDT.</p>'
    : '<p>Risco baixo baseado na história disponível. Se TNBC confirmado por IHQ, o teste BRCA ainda pode revelar mutação em ~10–15% dos casos sem história familiar.</p>';

  if(therapyEl) therapyEl.innerHTML = `
    <div style="font-size:12px;line-height:1.8">
      <div style="background:var(--s2);border-radius:var(--rs);padding:10px 12px;margin-bottom:8px">
        <p style="font-weight:600;margin-bottom:4px">Se BRCA1/2 positivo + Estádio precoce (II–III)</p>
        <p style="color:var(--m)">→ Olaparib 300mg bid × 1 ano após QT+cirurgia (OlympiA trial, DFS HR 0.58)</p>
        <p style="color:var(--m)">→ Redução de 42% no risco de recidiva</p>
        <p style="color:var(--wn);font-size:10px">⚠ Não disponível no HCM — referenciar para centro com acesso</p>
      </div>
      <div style="background:var(--s2);border-radius:var(--rs);padding:10px 12px;margin-bottom:8px">
        <p style="font-weight:600;margin-bottom:4px">Se BRCA1/2 positivo + Estádio IV (metastático)</p>
        <p style="color:var(--m)">→ Olaparib 300mg bid ou Talazoparib 1mg/d (EMBRACA trial)</p>
        <p style="color:var(--m)">→ PFS melhorado vs QT standard: 7.0 vs 4.2 meses</p>
      </div>
      <div style="background:var(--s2);border-radius:var(--rs);padding:10px 12px">
        <p style="font-weight:600;margin-bottom:4px">Se BRCA1/2 negativo — opções HCM</p>
        <p style="color:var(--m)">→ QT standard: AC-T (disponível HCM)</p>
        <p style="color:var(--m)">→ Capecitabina adj. se residual (CREATE-X)</p>
        <p style="color:var(--m)">→ Carboplatina + Paclitaxel se disponível</p>
      </div>
    </div>`;
}

// Fix T() for t16, t17
const _T_old = T;
T = function(id, btn){
  _T_old(id, btn);
  if(id==='t16'){ buildMDTChecklist(); }
  if(id==='t17'){ calcBRCA(); }
};

// Init BRCA on first load
setTimeout(()=>{ if(typeof calcBRCA==='function') calcBRCA(); }, 300);

/* ============================================================
   GUIA DE TRIAGEM — impressão clínica formal
   Baseado em: Brandão et al. ESMO Open 2020 + literatura SSA
   ============================================================ */
function printGuiaTriagem(){
  const p = G ? G() : {};
  const s = currentScore || {};
  const pTNBC = s.pTNBC || 0;
  const pProg = s.pProg || 0;
  const ciLow = s.ciLow || 0;
  const ciHigh = s.ciHigh || 100;
  const pBRCA = s.pBRCA || 0;
  const nlr = s.nlr || 0;
  const imc = s.imc || 0;
  const today = new Date().toLocaleDateString('pt-PT');

  // Semaphore
  const urgColor = pTNBC>=70?'#C0392B':pTNBC>=45?'#E67E22':'#1A6B3C';
  const urgLabel = pTNBC>=70?'ALTO — encaminhar IHQ urgente':
                   pTNBC>=45?'MODERADO — considerar IHQ':'BAIXO — protocolo standard';

  // Key predictors from parts
  const parts = (s.parts && typeof s.parts === 'object') ? s.parts : {};
  const activePredictors = Object.entries(parts)
    .filter(([k,v]) => v.pts > 0)
    .sort((a,b) => b[1].pts - a[1].pts)
    .slice(0,6);

  const predHTML = activePredictors.map(([k,v]) => {
    const labels = {
      grau:'Grau Histológico III', hiv:'HIV Positivo',
      imc:'Obesidade/Sobrepeso', ki67:'Ki-67 elevado',
      idade:'Idade', menop:'Pré-menopausa',
      nlr:'NLR elevado', hist:'Histotipo',
      cresc:'Crescimento rápido', hor:'Sem resposta a hormonoterapia',
      hfam:'História familiar', tamanho:'Tamanho tumoral', inv:'Invasão vascular',
    };
    return `<tr>
      <td style="padding:4px 8px;border:.5px solid #CCC">${labels[k]||k}</td>
      <td style="padding:4px 8px;border:.5px solid #CCC;text-align:center">${v.pts}/${v.max}</td>
      <td style="padding:4px 8px;border:.5px solid #CCC;font-size:11px;color:#555">${v.source||'—'}</td>
    </tr>`;
  }).join('');

  // Recommendation
  const recList = [];
  if(pTNBC>=70) recList.push('<li><strong>Encaminhar biópsia para IHQ urgente</strong> — laboratório Joanesburgo (NHLS/Lancet Labs). Carta de referência com dados clínicos.</li>');
  if(pTNBC>=45) recList.push('<li>Considerar QT neoadjuvante empírica AC×4 → Paclitaxel×12 se IHQ não disponível nos próximos 30 dias</li>');
  if(pBRCA>=20) recList.push('<li>Probabilidade BRCA1/2: ' + pBRCA + '% — considerar teste genético (Lancet Labs SA)</li>');
  if(p.hiv===1) recList.push('<li><strong>HIV positivo</strong> — verificar interacções ARV↔QT (especialmente efavirenz). Manter ARV durante QT.</li>');
  if(nlr>4) recList.push('<li>NLR ' + nlr.toFixed(1) + ' (>4) — excluir infecção activa antes de iniciar QT. Pedir PCR.</li>');
  if(p.ecog>=2) recList.push('<li>ECOG ' + (p.ecog||0) + ' — avaliar tolerância a QT intensiva. Considerar redução de dose.</li>');
  recList.push('<li>Discussão em MDT (Tumor Board) antes de iniciar tratamento</li>');

  const win = window.open('','_blank','width=740,height=900');
  win.document.write(`<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="UTF-8">
<title>Guia de Triagem TNBC — HCM</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif;font-size:13px;color:#1C1814;background:#fff;padding:28px 32px}
  h1{font-size:18px;font-weight:700;color:#0D3D22;margin-bottom:2px}
  h2{font-size:13px;font-weight:700;color:#1A6B3C;text-transform:uppercase;letter-spacing:.06em;margin:16px 0 6px;padding-bottom:4px;border-bottom:1.5px solid #1A6B3C}
  .header{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:12px;border-bottom:2px solid #0D3D22;margin-bottom:16px}
  .header-left p{font-size:11px;color:#666;margin-top:3px}
  .score-box{text-align:center;background:#F0F7F3;border-radius:10px;padding:14px 20px;border:1.5px solid #1A6B3C}
  .score-big{font-size:42px;font-weight:700;color:${urgColor};line-height:1}
  .score-ci{font-size:11px;color:#555;margin-top:3px}
  .score-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:#888;margin-top:4px}
  .urgency{display:inline-block;padding:5px 14px;border-radius:20px;font-size:12px;font-weight:700;color:#fff;background:${urgColor};margin:8px 0}
  table{width:100%;border-collapse:collapse;margin-bottom:8px}
  th{background:#F5F5F5;padding:5px 8px;border:.5px solid #CCC;font-size:11px;text-align:left;font-weight:600}
  td{padding:4px 8px;border:.5px solid #CCC;font-size:12px}
  .rec-list{padding-left:16px}
  .rec-list li{margin-bottom:5px;font-size:12px;line-height:1.5}
  .disclaimer{margin-top:20px;padding:10px 14px;background:#FFF8E1;border:.5px solid #F0C040;border-radius:6px;font-size:10px;color:#5A4A00;line-height:1.6}
  .footer{margin-top:16px;padding-top:10px;border-top:.5px solid #CCC;font-size:10px;color:#888;text-align:center}
  .two-col{display:grid;grid-template-columns:1fr 1fr;gap:16px}
  @media print{body{padding:14px 18px}.score-box{break-inside:avoid}}
</style>
</head>
<body>
<div class="header">
  <div class="header-left">
    <h1>Guia de Triagem TNBC</h1>
    <p>Hospital Central de Maputo · Oncologia</p>
    <p>Paciente: <strong>${p.id||'—'}</strong> · Data: <strong>${today}</strong></p>
    <p>Idade: ${p.idade||'—'} anos · ECOG: ${p.ecog||0}</p>
  </div>
  <div class="score-box">
    <div class="score-big">${pTNBC}%</div>
    <div class="score-ci">IC 95%: ${ciLow}%–${ciHigh}%</div>
    <div class="score-label">Probabilidade TNBC</div>
    <div class="urgency">${urgLabel}</div>
  </div>
</div>

<div class="two-col">
  <div>
    <h2>Scores sumário</h2>
    <table>
      <tr><td>Probabilidade TNBC</td><td><strong>${pTNBC}%</strong> (IC 95%: ${ciLow}–${ciHigh}%)</td></tr>
      <tr><td>Risco prognóstico</td><td><strong>${pProg}%</strong></td></tr>
      <tr><td>Probabilidade BRCA1/2</td><td><strong>${pBRCA}%</strong></td></tr>
      <tr><td>NLR</td><td>${nlr>0?nlr.toFixed(1):'não avaliado'}</td></tr>
      <tr><td>IMC</td><td>${imc>0?imc.toFixed(1)+' kg/m²':'—'} ${imc>=30?'(obesa)':imc>=25?'(sobrepeso)':''}</td></tr>
      <tr><td>HIV</td><td>${p.hiv===1?'<strong style="color:#C0392B">Positivo</strong>':'Negativo/Desconhecido'}</td></tr>
      <tr><td>Estádio</td><td>${['I','II','III','IV'][(p.est||1)-1]}</td></tr>
    </table>
  </div>
  <div>
    <h2>Preditores activos</h2>
    <table>
      <tr><th>Factor</th><th>Pts</th><th>Fonte</th></tr>
      ${predHTML||'<tr><td colspan="3">Nenhum factor activado</td></tr>'}
    </table>
  </div>
</div>

<h2>Recomendações clínicas</h2>
<ul class="rec-list">${recList.join('')}</ul>

<h2>Metodologia</h2>
<p style="font-size:11px;color:#555;line-height:1.6">
  Score de triagem clínica baseado em regressão logística com pesos derivados de:
  Brandão et al. ESMO Open 2020 (n=210 HCM, Grau III OR=3.99 p=0.001; HIV+ OR=1.67 p=0.043) ·
  Nalwoga et al. Uganda 2014 · Guo et al. Oncol Lett 2025 (NLR AUC=0.642) ·
  EUSOMA Dataset v3.1 2019.
  Estimativa de IC 95% heurística baseada na completude de dados.
  AUC estimada ~0.71 (não validada prospectivamente).
</p>

<div class="disclaimer">
  <strong>⚠ Aviso importante:</strong> Este é um Protótipo de Triagem de Apoio à Decisão Clínica — UEM/HCM.
  Este simulador é uma ferramenta de triagem baseada em biomarcadores digitais e <strong>não substitui o exame histopatológico (IHQ)</strong>.
  Os resultados são probabilísticos e devem ser interpretados no contexto clínico completo por profissional de saúde habilitado.
  Decisão terapêutica final requer confirmação por IHQ (ER, PR, HER2, Ki-67).
  Versão 14.0 — Não aprovada para uso diagnóstico autónomo.
</div>

<div class="footer">
  TNBC Predictor HCM v14.0 · Desenvolvido por Abudala Sualé · UEM — Faculdade de Medicina · Hospital Central de Maputo · 2026<br>
  Baseado em: Brandão et al. ESMO Open 2020;5:e000829 · Moza-BC Cohort (n=210)
</div>

<script>window.onload=()=>{window.print()}<\/script>
</body></html>`);
  win.document.close();
}
</script>
</body>
</html>
