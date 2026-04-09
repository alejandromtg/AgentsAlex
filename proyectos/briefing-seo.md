# 🔍 BRIEFING: SEO Agent
## Proyecto Stayva - 3 Nuevas Páginas

### CONTEXTO
- **Dominio**: stayvagroup.com (DA assumed ~30-40, nuevo pero con buena estructura)
- **Objetivo SEO**: +200/mes visitors orgánicos desde nuevas 3 páginas
- **Target Keywords**: Long-tail "gestión apartamentos madrid +ingresos", "calculadora rentabilidad airbnb", etc.
- **Mercados**: Madrid (primary), Medellín, Cancún, Costa Rica

---

## TAREA 1: SEO `/apartamentos`

### Keyword Research
**Primary keyword**: "apartamentos turísticos gestión madrid"  
**Primary intent**: Informational + Commercial (usuarios que buscan inspiración + opciones)

**Secondary keywords**:
- "apartamentos madrid airbnb manejados"
- "nuestros apartamentos stayva"
- "propiedades turísticas madrid lista"
- "apartamentos madrid alquiler corta duración"

### On-Page Optimization
1. **Title Tag** (55-60 caracteres)
   ```
   Nuestros Apartamentos en Madrid | 40+ Propiedades | Stayva
   ```

2. **Meta Description** (155-160 caracteres)
   ```
   Descubre 40+ apartamentos premium en Madrid gestionados por Stayva. 
   Ocupación 85%+, ingresos 1.200-2.500€/mes. Casos reales.
   ```

3. **H1**
   ```
   Nuestros Apartamentos Turísticos en Madrid
   ```

4. **H2s** (3-4)
   ```
   H2: Apartamentos en Malasaña, Salamanca y Chamberí
   H2: Social Proof: +50 inmuebles gestionados
   H2: ¿Tu piso podría ser el próximo?
   ```

5. **Schema Markup** (JSON-LD)
   ```json
   {
     "@context": "schema.org",
     "@type": "ItemList",
     "itemListElement": [
       {
         "@type": "RealEstateProperty",
         "name": "Estudio Malasaña",
         "address": {...},
         "priceRange": "900-1200 EUR/mes",
         "aggregateRating": { "ratingValue": 4.9, "bestRating": 5 }
       }
     ]
   }
   ```

6. **Internal Linking** (2-3 links)
   - Link a `/sobre-nosotros` ("Conoce nuestro equipo")
   - Link a `/calculadora` ("¿Cuánto ganaría tu apartamento?")
   - Link a contact form

---

## TAREA 2: SEO `/calculadora`

### Keyword Research
**Primary**: "calculadora rentabilidad apartamentos madrid"  
**Intent**: Transactional (usuarios que quieren resultado rápido)

**Secondaries**:
- "cuánto gano en airbnb madrid calculadora"
- "estimador ingresos alquiler turístico"
- "herramienta cálculo rentabilidad airbnb"

### On-Page Optimization
1. **Title** (55-60 chars)
   ```
   Calculadora de Rentabilidad de Apartamentos | Stayva
   ```

2. **Meta Description**
   ```
   Calcula cuánto podría ganar tu apartamento en Madrid en segundos. 
   Estimador basado en datos reales de mercado. 
   Resultado en 24h.
   ```

3. **H1**
   ```
   Calcula la Rentabilidad de Tu Apartamento en Madrid
   ```

4. **H2s**
   ```
   H2: ¿Cuánto ganaría tu apartamento?
   H2: Cálculo basado en datos de mercado real
   H2: Obtén tu valoración personalizada
   ```

5. **FAQ Schema** (si hay sección de preguntas)
   ```json
   {
     "@context": "schema.org",
     "@type": "FAQPage",
     "mainEntity": [
       {
         "@type": "Question",
         "name": "¿Cómo se calcula la rentabilidad?",
         "acceptedAnswer": { "text": "Multiplicamos la tarifa × ocupación % × 365 días..." }
       }
     ]
   }
   ```

6. **Internal Linking**
   - `/sobre-nosotros` ("Conoce nuestro método")
   - `/apartamentos` ("Ver ejemplos reales")
   - Main homepage

---

## TAREA 3: SEO `/sobre-nosotros`

### Keyword Target
**Primary**: "sobre stayva gestión apartamentos"  
**Secondary**:
- "quién es stayva madrid"
- "equipo gestoras apartamentos madrid"
- "sobre nosotros alquiler turístico"

### On-Page Optimization
1. **Title** (55-60)
   ```
   Sobre Stayva | Especialistas en Gestión de Apartamentos Madrid
   ```

2. **Meta Description**
   ```
   Conoce el equipo Stayva. +50 inmuebles gestionados, 
   especialización en Madrid, gestión 100% integral. 
   Valores de transparencia y excelencia.
   ```

3. **H1**
   ```
   Sobre Stayva: Especialistas en Gestión de Apartamentos
   ```

4. **H2s**
   ```
   H2: Nuestra Historia
   H2: Nuestros Valores
   H2: El Equipo Stayva
   H2: Nuestro Impacto
   ```

5. **Organization Schema** (Priority)
   ```json
   {
     "@context": "schema.org",
     "@type": "Organization",
     "name": "Stayva",
     "logo": "https://stayvagroup.com/logo.png",
     "sameAs": ["https://www.linkedin.com/company/stayva"],
     "aggregateRating": { "ratingValue": 4.85, "bestRating": 5 }
   }
   ```

6. **Internal Linking**
   - `/apartamentos` ("Nuestra cartera")
   - `/calculadora` ("Valora tu apartamento")
   - `/servicios` (si existe en homepage)

---

## 🔗 INTER-PAGE LINKING STRATEGY

```
Homepage
├── /apartamentos ("Nuestros apartamentos" en nav)
├── /calculadora ("Calcula tu rentabilidad")
└── /sobre-nosotros ("Quiénes somos")

/apartamentos
├── CTA → /calculadora
├── Link → /sobre-nosotros
└── Link → contact form

/calculadora
├── Link → /apartamentos (casos reales)
├── Link → /sobre-nosotros (método)
└── CTA → contact form

/sobre-nosotros
├── Link → /apartamentos (cartera)
├── Link → /calculadora (valoración)
└── CTA → contact form
```

---

## 📊 TECHNICAL SEO

### For all 3 pages:
- [ ] Canonical URLs set
- [ ] Mobile-friendly verified
- [ ] Structured data markup (JSON-LD)
- [ ] Meta robots: index, follow
- [ ] Sitemap.xml updated
- [ ] robots.txt allows indexing
- [ ] Open Graph tags (og:title, og:description, og:image, og:url)
- [ ] Hreflang tags if multilingual (es-ES, es-CO, etc.)

### Performance (also affects SEO)
- [ ] LCP < 2.5s
- [ ] CLS < 0.1
- [ ] FID < 100ms

---

## 🔍 CONTENT RECOMMENDATIONS

### `/apartamentos`
- Agregar 1-2 comparativas "Apartamento X: antes vs después Stayva"
- Rich snippets con ratings del apartamento
- Alt text detallado en imágenes

### `/calculadora`
- Crear sección "FAQs sobre cálculos"
- Agregar disclaimers pero en subtle
- FAQ Schema para aparecer en search features

### `/sobre-nosotros`
- Mencionar certificaciones/awards si hay (Airbnb Superhost, etc.)
- Incluir cuota de mercado o stat único ("Gestionamos 1 de cada 10 apartamentos en Malasaña")
- Agregar CTA secundario "Únete al equipo" si hiring

---

## 📈 POST-LAUNCH MONITORING

### Métricas a trackear (primera semana)
- Impressiones + CTR en Search Console
- Keyword rankings (top 50 keywords)
- Organic traffic
- Bounce rate por página
- Time on page
- Conversion rate (form submissions)

### Tools
- Google Search Console
- Google Analytics 4
- SEMrush/Ahrefs (si tienen acceso)
- Lighthouse (PageSpeed Insights)

---

## ✅ DELIVERABLES

- [ ] Title tags + Meta descriptions × 3
- [ ] H1-H3 structure × 3 pages
- [ ] JSON-LD schema por página
- [ ] Internal linking map
- [ ] Sitemap update
- [ ] Open Graph tags
- [ ] Checklist: "Before going live"

---

## ⏱️ DEADLINE

**Thu 10 Apr 14:00** - SEO metadata + schema ready  
**Fri 11 Apr 09:00** - Final review before launch

---

## 🚨 QUESTIONS FOR CLARIFICATION

- ¿Blog en el sitio? (si hay, hay oportunidad de linkear a las nuevas páginas)
- ¿Geo-targeting configurado en GSC para múltiples países?
- ¿Analytics implementada? (GA4 o Universal?)
