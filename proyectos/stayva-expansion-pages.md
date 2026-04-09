# 🏗️ PROYECTO: Stayva - Expansion de Páginas

**RequestID**: REQ-20260409-002  
**Fecha**: 2026-04-09  
**Deadline**: 2026-04-12  
**Estado**: 🔄 EN PROGRESO

---

## 📋 OBJETIVO GENERAL

Expandir stayvagroup.com con 3 nuevas páginas + calculadora activa para mejorar conversión, SEO y experiencia del usuario.

---

## 🎯 PÁGINAS A CREAR

### 1. `/apartamentos` - Nuestros Apartamentos
**Purpose**: Escaparate de propiedades gestionadas  
**Audiencia**: Usuarios que quieren ver casos reales, familias potenciales  
**Secciones**:
- Hero: "40+ apartamentos premium gestionados en Madrid"
- Galería filtrada: (Por zona, tipología, precio)
- Ficha de apartamento: Fotos, servicios, ubicación, reviews huéspedes
- CTA: "¿Tu piso aquí?"

**Benchmark**: Airbnb listings, Booking property pages

---

### 2. `/calculadora` - Calcula tu Rentabilidad
**Purpose**: Lead magnet interactivo  
**Audiencia**: Propietarios potenciales con dudas sobre ingresos  
**Funcionalidad**:
- Input: Zona (dropdown Madrid), Tamaño (1-4 hab), Tipo (piso/estudio)
- Cálculo: Ocupación media × tarifa media × 12 meses
- Output: Estimación mensual + anual, comparativa con rentabilidad actual
- CTA: "Ver mi oportunidad →" leads a contacto

**Tech**: Form interactivo Webflow + Airtable data (opcional)

---

### 3. `/sobre-nosotros` - Mejorado
**Current**: Existe pero genérico  
**Mejoras**:
- Equipo: Cards con photos, roles, backgrounds
- Timeline: De cero a +50 inmuebles
- Valores: Transparencia, velocidad, especialización
- Logos clientes mayores (si hay)
- Video: "¿Quiénes somos en 60 segundos?"

---

## 👥 ASIGNACIONES

| Tarea | Owner | Status |
|-------|-------|--------|
| **T1**: Copy + estructura `/apartamentos` | content-marketing | ⏳ PENDING |
| **T2**: Copy `/calculadora` + campos input | content-marketing | ⏳ PENDING |
| **T3**: Copy mejorado `/sobre-nosotros` | content-marketing | ⏳ PENDING |
| **T4**: Build Webflow `/apartamentos` | web-app-db | ⏳ PENDING |
| **T5**: Build Webflow `/calculadora` (calcs) | web-app-db | ⏳ PENDING |
| **T6**: Build Webflow `/sobre-nosotros` | web-app-db | ⏳ PENDING |
| **T7**: SEO metadata + internal links | seo | ⏳ PENDING |
| **T8**: QA completo 3 páginas | qa-process | ⏳ PENDING |

---

## 📊 Entregables Esperados

### Content-Marketing
```
- Copy documento (1 documento)
  - /apartamentos: Hero, galería, fichas
  - /calculadora: Labels, placeholders, CTA
  - /sobre-nosotros: Equipo, timeline, valores
- Variantes A/B si aplica
- Recomendaciones UX/copy
```

### Web-App-DB
```
- 3 páginas Webflow funcionales
- Calculadora con lógica (form + output dinámica)
- Responsive: Desktop + Tablet + Mobile
- Documentación de integración
- Performance baseline
```

### SEO
```
- Title/Meta description × 3 páginas
- Estructura H1-H3 × 3
- Keywords recomendadas
- Internal linking strategy
- Schema.org enhancements
```

### QA
```
- Reporte bugs × 3 páginas
- Checklist: Funcionalidad, UX, Performance
- Validación CTA funnel completo
- Recomendaciones post-launch
```

---

## 🚀 Timeline

**Wed 09 Apr - 14:00**: ✅ Análisis + delegación  
**Wed 09 Apr - 18:00**: 📝 Content-Marketing entrega copy  
**Thu 10 Apr - 10:00**: 🛠️ Web-App-DB comienza build  
**Thu 10 Apr - 14:00**: 🔍 SEO revisa y optimiza  
**Fri 11 Apr - 10:00**: ✔️ QA valida todo  
**Fri 11 Apr - 17:00**: 🚀 Deploy a Webflow + test final  

---

## 🎨 Constraints & Notas

- **Webflow only** - No cambiar hosting
- **Reutilizar** diseño system existente (colores, fonts, spacings)
- **Mobile first** - Prioridad mobile experience
- **Load time** - Target <2.5s
- **Datos apartamentos**: Simulados o de fixture (confirmar fuente)

---

## ✅ Criterios de Éxito Global

- [ ] 3 páginas live en stayvagroup.com
- [ ] Calculadora funcional + entrega estimación en 2 clicks
- [ ] 0 errores blocking en QA
- [ ] SEO score >90 Lighthouse cada página
- [ ] Conversión form +15% vs baseline (post-launch)
- [ ] Sitemap actualizado + indexación

---

## 📝 LOG

**09 Apr 14:15** - Plan creado, tareas delegadas a agentes  
