# ✅ BRIEFING: QA/Procesos Agent
## Proyecto Stayva - 3 Nuevas Páginas

### CONTEXTO
- **Objetivo QA**: Validar que 3 nuevas páginas son funcionales, optimizadas y listas para producción
- **Criterio Blocking**: 0 errores críticos antes de launch
- **Audiencia Testing**: Desktop users, Mobile users, Accessibility users

---

## 🎯 CHECKLIST QA FUNCIONAL

### PÁGINA: `/apartamentos`

#### Funcionalidad
- [ ] Página carga correctamente (sin errores console)
- [ ] Imagen hero visible
- [ ] Filters (Zona, Tamaño, Ordenar) funcionan individualmente
- [ ] Filtros combinados no generan resultados vacíos
- [ ] Cards de apartamento mostran correctamente:
  - [ ] Imágenes cargan
  - [ ] Títulos visibles
  - [ ] Stats (ocupación, ingresos, rating) correctos
  - [ ] Amenities tags se muestran
- [ ] CTA "Ver detalles" clickeable y funciona
- [ ] CTA final "¿Tu piso aquí?" links a `/contacto`
- [ ] Social Proof section render correcto

#### Responsividad
- [ ] Desktop (1920x1080): Sin overflow, layout correcto
- [ ] Tablet (768x1024): Elementos stacked, legible
- [ ] Mobile (375x812): Single column, CTAs above fold, no pinch zoom needed
- [ ] Font sizes lógicos en cada breakpoint

#### Performance
- [ ] Load time: < 2.5s (Lighthouse audit)
- [ ] LCP < 2s
- [ ] Imágenes optimizadas (WebP o comprimidas)
- [ ] No 404s en console

---

### PÁGINA: `/calculadora`

#### Funcionalidad (CRÍTICO)
- [ ] Página carga
- [ ] Form inputs accesibles:
  - [ ] Dropdown Zona: mostrar opciones, seleccionar funciona
  - [ ] Radio buttons Tamaño: solo 1 seleccionable
  - [ ] Radio buttons Tipo: solo 1 seleccionable
- [ ] Submit button clickeable
- [ ] **Cálculos correctos** (validar 5 combinaciones):
  ```
  Caso 1: Madrid, Estudio → ~1.050€/mes
  Caso 2: Madrid, 2hab → ~1.800€/mes
  Caso 3: Medellín, Estudio → ~600€/mes
  Caso 4: Madrid, 3hab → ~2.400€/mes
  Caso 5: Cancún, 1hab → ~1.200€/mes
  ```
- [ ] Output dinámico muestra en la misma página (no redirect)
- [ ] Números destacados correctos
- [ ] Breakdown cards muestran: mensual, anual, comparativa
- [ ] CTA "Quiero valoración" funciona
- [ ] Pre-rellena email si viene de otro funnel
- [ ] Form validation: No submits si campos vacíos

#### Responsividad
- [ ] Desktop: Form + Output side by side o stacked legible
- [ ] Tablet: Elementos centrados
- [ ] Mobile: Single column, inputs grandes (min 48px height para accesibilidad)
- [ ] Output números legibles en mobile

#### Performance
- [ ] Load time: < 2.5s
- [ ] Cálculos procesan < 1s
- [ ] No lag en interactions

---

### PÁGINA: `/sobre-nosotros`

#### Funcionalidad
- [ ] Hero section carga:
  - [ ] Headline visible
  - [ ] Subheader visible
  - [ ] Background image o video loads
- [ ] Video embeds (si hay):
  - [ ] Play button funciona
  - [ ] Video no autoplay (molesto para UX)
  - [ ] Responsive (no overflow YouTube player)
- [ ] Valores section:
  - [ ] 4 cards visible
  - [ ] Texto legible
  - [ ] Iconos cargan
- [ ] Equipo section:
  - [ ] Photos cargan
  - [ ] Nombres y roles visibles
  - [ ] Hover state funciona (si hay)
- [ ] Timeline section:
  - [ ] 4-5 items en orden cronológico
  - [ ] Responsive (no line overlap en mobile)
- [ ] Stats block:
  - [ ] 4 numbers visible
  - [ ] Counters animate (o static, pero claros)
  - [ ] Labels bajo números
- [ ] CTAs funcionales:
  - [ ] "Habla con nosotros" links a `/contacto`
  - [ ] Navigation links a `/apartamentos` y `/calculadora` funcionan

#### Responsividad
- [ ] Desktop: Multi-column layouts correcto
- [ ] Tablet: 2-column donde corresponda
- [ ] Mobile: Single column, legible, sin overflow
- [ ] Timeline readable en mobile (no cruzamiento de líneas)
- [ ] Team cards grid responsive

#### Performance
- [ ] Load time: < 2.5s
- [ ] Images optimized
- [ ] Video lazy loaded

---

## 📋 CHECKLIST TÉCNICO GENERAL

### SEO & Meta
- [ ] Title tags presentes y correctos (< 60 chars)
- [ ] Meta descriptions presentes (< 160 chars)
- [ ] Canonical URLs set
- [ ] og:tags presentes (Open Graph)
- [ ] Structured data (JSON-LD) valida con schema.org validator
- [ ] H1 único por página (no múltiples H1s)
- [ ] H2-H3 jeraraquía lógica

### Accessibility
- [ ] WCAG 2.1 AA compliant (minimum)
- [ ] Images tienen alt text descriptivo
- [ ] Links tienen aria-labels si necesario
- [ ] Form labels asociados a inputs (<label for="">)
- [ ] Color contrast > 4.5:1 para texto
- [ ] Focus states visible (keyboard navigation)
- [ ] No focus trap

### Security
- [ ] No mixed content (http/https)
- [ ] Forms HTTPS only
- [ ] Turnstile/hCaptcha (si hay en contacto) funciona
- [ ] No secrets en client-side code

### Cross-browser
- [ ] Chrome: OK
- [ ] Firefox: OK
- [ ] Safari: OK
- [ ] Edge: OK

### Performance (Lighthouse Audit)
- [ ] Performance score: > 85/100
- [ ] Accessibility: > 90/100
- [ ] Best Practices: > 90/100
- [ ] SEO: > 90/100

---

## 🔗 USER JOURNEY TESTING

### Journey 1: "Inspiración a Contacto"
```
Homepage 
→ Click "Nuestros apartamentos"
→ Browse `/apartamentos` page
→ See social proof
→ Click "¿Tu piso aquí?"
→ Land on `/contacto` form
→ Form works, submits successfully
```
**Expected**: Smooth flow, no 404s, CTAs clear

### Journey 2: "Calculadora a Valoración"
```
Homepage
→ Click "Calcula cuánto ganas"
→ Land on `/calculadora`
→ Fill form (zona, tamaño, tipo)
→ Click Calculate
→ See resultado
→ Click "Quiero valoración"
→ Pre-filled email en contacto form
→ Submit
```
**Expected**: Cálculos correctos, pre-fill funciona, conversión smooth

### Journey 3: "About Page Exploration"
```
Homepage
→ Click "Sobre nosotros"
→ Read valores + equipo
→ Watch video (si hay)
→ Scroll timeline
→ Click CTA o link a `/apartamentos`
```
**Expected**: Compelling narrative, smooth scrolling, CTAs clear

---

## 🐛 BUG SEVERITY LEVELS

### CRÍTICO (Blocking Launch)
- [ ] Page no carga
- [ ] Calculadora cálculos incorrectos
- [ ] Forms no submitten
- [ ] 404 errors
- [ ] Security issues

### ALTO
- [ ] Mobile layout roto
- [ ] Accessibility bloqueantes (no keyboard nav)
- [ ] Performance < 2.5s load
- [ ] Images not showing

### MEDIO
- [ ] Typos
- [ ] Minor styling inconsistencies
- [ ] Non-critical form validation issues
- [ ] Hover states missing

### BAJO
- [ ] Nice-to-have animations missing
- [ ] Minor spacing issues
- [ ] Unused CSS warnings

---

## 📊 TESTING MATRIX

| Test | Desktop | Tablet | Mobile | Notes |
|------|---------|--------|--------|-------|
| /apartamentos loads | ✓ | ✓ | ✓ | < 2.5s |
| Filters work | ✓ | ✓ | ✓ | Combos OK |
| /calculadora loads | ✓ | ✓ | ✓ | < 2.5s |
| Form validates | ✓ | ✓ | ✓ | No vacio |
| Cálculos correctos | 5 casos ✓ | 5 casos ✓ | 5 casos ✓ | Audit |
| /sobre-nosotros loads | ✓ | ✓ | ✓ | < 2.5s |
| Video embeds | ✓ | ✓ | ✓ | Responsive |
| CTAs links OK | ✓ | ✓ | ✓ | No 404s |
| SEO meta | ✓ | - | ✓ | All pages |
| Accessibility | ✓ | ✓ | ✓ | WCAG AA |

---

## 📦 DELIVERABLES

**QA Report** incluye:
1. **Summary**
   - Total tests: X
   - Passed: X
   - Failed: X
   - Blocked: X/0

2. **Bug List** (por página)
   ```
   [CRÍTICO] /calculadora: Cálculos 15% bajo en 2-hab
   [ALTO] Mobile: Hero texto overlap
   [MEDIO] Typo: "servicIS" en footer
   ```

3. **Recommendations**
   - Performance improvements
   - UX tweaks
   - Post-launch monitoring

4. **Go/No-Go Decision**
   - ✅ GO (0 críticos, < 2 altos)
   - ⚠️ GO WITH CAUTION (documentar issues)
   - ❌ NO GO (blockers)

---

## 🚀 LAUNCH CHECKLIST

Before deploying to production:
- [ ] All critical bugs fixed
- [ ] All high-severity bugs fixed
- [ ] Performance baseline captured (screenshot Lighthouse)
- [ ] Backups created
- [ ] Monitor alerts set
- [ ] Team notified
- [ ] Rollback plan confirmed

---

## ⏱️ TIMELINE

**Thu 10 Apr 18:00** - Start QA testing (pages must be dev-ready)  
**Fri 11 Apr 10:00** - Initial bugs reported, devs fix  
**Fri 11 Apr 14:00** - Final QA sign-off  
**Fri 11 Apr 16:00** - Deploy to production  
**Post-launch**: Monitor for 48h

---

## 📞 COMMUNICATION

**If blockers found**: Escalate to orchestrator immediately  
**Daily status**: Slack standup at 10:00 CET  
**Final report**: Delivered by Fri 11 Apr 16:00
