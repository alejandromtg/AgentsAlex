# 🛠️ BRIEFING: Web-App-DB Agent
## Proyecto Stayva - 3 Nuevas Páginas en Webflow

### CONTEXTO
- **Platform**: Webflow (no code-low code)
- **Domain**: stayvagroup.com
- **3 URLs a crear**: `/apartamentos`, `/calculadora`, `/sobre-nosotros`
- **Design System**: Verificar con componentes Webflow existentes (colores, fonts, spacings)

---

## TAREA 1: Build `/apartamentos` Page

### Requerimientos Técnicos
1. **Hero Section**
   - Background: Imagen professional de apartamento o gradient navy
   - Headline + Subheader (inputs de content-marketing)
   - CTA button "Descubre nuestros apartamentos"

2. **Filter Bar**
   - 3 dropdowns: Zona, Tamaño, Ordenar por
   - API/Dataset: Usar Collection List de Webflow si hay CMS, o hardcode 8-10 apartamentos simulados
   - Behavior: Mostrar resultados dinámicos al cambiar filters

3. **Apartment Grid**
   - Layout: 3 columns desktop, 2 tablet, 1 mobile
   - Card de apartamento:
     - Galería: 3-4 fotos, thumbnail scroll
     - Titulo: "Estudio | Malasaña"
     - Stats: Ocupación 85%, 1.650€/mes, ★4.9
     - Amenities: 5-7 tags (Wifi, AC, Cocina equipada, etc.)
     - CTA: "Ver detalles" (link a detail page o modal)

4. **Social Proof Section**
   - "Después de gestionar estos apartamentos..."
   - Stats block: Occupancy %, Revenue avg, Ratings

5. **Final CTA**
   - "¿Tu piso aquí?" → Link a /contacto form

### Performance Goals
- Load time: <2.5s
- LCP: <2s
- Mobile responsive

### Deliverables
- [ ] Página live en Webflow
- [ ] 8-10 apartamentos demo (puede ser dummy data)
- [ ] Filters funcionando
- [ ] Tested en mobile/tablet/desktop

---

## TAREA 2: Build `/calculadora` Page

### Requerimientos Técnicos
1. **Hero**
   - Headline + description (de content-marketing)
   - Trust signal: "Basado en datos reales del mercado"

2. **Calculator Form** (Lo más importante)
   - Input 1: Dropdown "Zona" (Madrid, Medellín, etc.)
   - Input 2: Radio buttons "Tamaño" (Estudio, 1 hab, 2hab, 3hab+)
   - Input 3: Radio buttons "Tipo" (Piso, Estudio, etc.)
   - Submit button: "Calcular"

3. **Logic/Computation** (POST-SUBMIT OUTPUT)
   - Backend: Usar Webflow Logic o Zapier/Make integration para guardar datos
   - Cálculos a mostrar:
     ```
     Base tarifas por zona:
     - Madrid: Estudio 80€/noche, 1hab 120€, 2hab 180€, 3hab 250€
     - Medellín: 40€/noche promedio
     - Etc.
     
     Ocupación promedio: 75% anual
     
     Fórmula: (Tarifa × 75% ocupación × 365 días) = Estimación anual
             ÷ 12 = Estimación mensual
     ```

4. **Output Section** (Dynamic)
   - Gran número destacado: "Tu apartamento podría generar ~1.850€/mes"
   - Breakdown cards:
     - Card 1: Estimación mensual
     - Card 2: Estimación anual
     - Card 3: Comparativa "vs. media actual"
   - CTA: "Quiero valoración personalizada" → Pre-rellena email + zona en form contacto

5. **Disclaimer**
   - "Estimación orientativa, no garantizada"

### Technical Approaches (Choose 1)
- **Option A**: Webflow Logic (nativo, fácil)
- **Option B**: Zapier/Make webhook → backend simple → resultado
- **Option C**: Embed Google Sheet with Form + Script

### Deliverables
- [ ] Formulario funcional
- [ ] Cálculos correctos (validar con 5 casos)
- [ ] Output dinámico mostrando resultado
- [ ] Mobile responsive
- [ ] Integration con CRM (Slack alert o email)

---

## TAREA 3: Build `/sobre-nosotros` (MEJORADA)

### Requerimientos Técnicos
1. **Hero Mejorado**
   - Background: Video loop (60s) "Día en Stayva" o imagen poderosa
   - Headline + Subheader (content-marketing)

2. **Valores** (4 cards)
   - Cada uno: Icono + Título + Descripción 3-4 líneas
   - Grid: 2x2 desktop, 1 mobile
   - Hover effect: Subtle shadow/scale

3. **Equipo** (Team Section)
   - 4-5 personas
   - Card per person: Photo (headshot), Nombre, Rol, Bio 2 líneas
   - Grid: 3 desktop, 2 tablet, 1 mobile
   - Hover: Slight zoom o overlay con Bio completa

4. **Timeline**
   - Vertical timeline (responsive)
   - 2024: Primer apartamento
   - 2025: 25 inmuebles
   - 2026: 50+ inmuebles
   - Each point: Año + descripción + icon

5. **Stats Block**
   - 4 big numbers: 50+, 4.85★, 3, 100%
   - Labels bajo cada numero
   - Animated counters (si performance permite)

6. **Video Section** (Optional)
   - Embed YouTube: "¿Quiénes somos en 60 segundos?"
   - Poster image + play button

7. **Final CTA**
   - "Tu apartamento podría ser el próximo"
   - Button: "Habla con nosotros"

### Design Consistency
- Use existing color palette (Navy, Teal, Cream)
- Fonts: Playfair Display (headlines), DM Sans (body)
- Spacing: Consistent con rest of site

### Deliverables
- [ ] Página live
- [ ] Team section con fotos (placeholder o real)
- [ ] Timeline responsive
- [ ] Video embeds working
- [ ] CTAs linking correctly

---

## 🔧 GENERAL TECHNICAL SPECS

### URLs & Meta
```
/apartamentos
  - Title: "Nuestros Apartamentos Turísticos en Madrid | Stayva"
  - Meta: "40+ apartamentos gestionados..."
  - Canonical: https://stayvagroup.com/apartamentos

/calculadora
  - Title: "Calculadora de Rentabilidad - Stayva"
  - Meta: "Calcula cuánto podría ganar tu apartamento..."
  - Canonical: https://stayvagroup.com/calculadora

/sobre-nosotros
  - Title: "Su Nosotros - Especialistas en Gestión de Apartamentos"
  - Meta: "Conoce el equipo Stayva..."
  - Canonical: https://stayvagroup.com/sobre-nosotros
```

### Webflow Best Practices
- [ ] Usar Components para reutilizar (Cards, CTA buttons, etc.)
- [ ] Responsive design first (Mobile, Tablet, Desktop)
- [ ] Accessibility: Alt text en iamgenes, ARIA labels
- [ ] Performance: Optimize images (WebP), lazy load videos
- [ ] Cross-linking: Internal links a otras páginas
- [ ] Form handling: Conectar con CMS o Zapier

### Integration Points
- Contact form: Pre-llenar zona desde /calculadora si viene de ese funnel
- Apartment detail page: Modal o página nueva (TBD)
- Navigation: Agregar links en nav principal a nuevas páginas

---

## ✅ TESTING CHECKLIST

- [ ] Desktop (1920x1080): All sections visible, no layout breaks
- [ ] Tablet (768x1024): Properly stacked, readable
- [ ] Mobile (375x812): Optimized, CTA above fold
- [ ] Forms: Validation working, submissions captured
- [ ] Links: All internal links working
- [ ] Load time: <2.5s
- [ ] Lighthouse score: >85 (performance)

---

## 📦 DELIVERABLES

1. 3 páginas live en Webflow
2. Funcionalidad 100% (calculadora operativa, filtros working)
3. Responsive en todos los breakpoints
4. Documentation: "Cómo editar [página]" si tiene CMS
5. Performance baseline screenshot

---

## ⏱️ TIMELINE

**Thu 10 Apr 10:00** - START build  
**Thu 10 Apr 18:00** - `/apartamentos` + `/sobre-nosotros` beta  
**Fri 11 Apr 10:00** - `/calculadora` funcionando  
**Fri 11 Apr 16:00** - QA testing phase

---

## 🚨 BLOCKERS & QUESTIONS

- [ ] ¿Dataset de apartamentos viene de CMS Webflow o hardcoded?
- [ ] ¿Team photos (real or placeholder)?
- [ ] ¿Video para la sección "Sobre nosotros"?
- [ ] ¿Integración con CRM para leads de calculadora?
