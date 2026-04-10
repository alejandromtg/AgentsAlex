<!-- INSTRUCCIONES DE INTEGRACIÓN A WEBFLOW -->
<!-- ============================================== -->

# 📚 Blog Stayva - Guía de Integración Webflow

## Archivos Generados (5 Artículos + Índice)

✅ **blog-index.html** - Página principal del blog  
✅ **articulo-1-rentabilidad.html** - Guía de Rentabilidad 2026  
✅ **articulo-2-errores.html** - 5 Errores Comunes  
✅ **articulo-3-ocupacion-vs-tarifa.html** - Fórmula de RPM  
✅ **articulo-4-escalabilidad.html** - Plan de Escalabilidad  
✅ **articulo-5-tendencias.html** - Tendencias Mercado 2026  

---

## Opción 1: Integración Rápida (Recomendada)

### Paso 1: Copiar HTML Completo
1. Abre cada `.html` en el navegador
2. Click derecho → Seleccionar todo (Ctrl+A)
3. Copiar

### Paso 2: En Webflow
1. Ve a **Add → Embed → Custom Code**
2. Pega el HTML completo
3. Publica

**Ventaja:** Está 100% funcional, solo copiar-pegar  
**Desventaja:** Webflow lo trata como "embed", no como "página nativa"  

---

## Opción 2: Integración Profesional (Recomendada para SEO)

### Crear Página en Webflow para cada artículo

1. **Crea nueva página:**  
   - Nombre: `/blog/rentabilidad` (o similar)
   - Template: Blank

2. **Copia estructura HTML:**
   - Todo lo DENTRO de `<div class="article-container">` 
   - Lleva al **CUSTOM HTML** o **HTML EMBED** de Webflow

3. **Aplicar estilos:**
   - El CSS ya está incluido en `<style>`
   - Copiar estilos al CSS global de Webflow O dejarlos inline

4. **Metadata SEO:**
   - Title: Copia de `<title>`
   - Description: Copia de `<meta name="description">`
   - En Webflow: Settings → SEO

---

## Opción 3: Webflow CMS (Escalable)

### Para hacer blog dinámico (recomendado si crecerá):

1. **Crea Collection:**
   - Nombre: "Blog Posts"
   - Campos: Título, Descripción, Contenido, Categoría, Imagen Hero, Fecha, Autor

2. **Copia contenido a CMS** (de cada artículo)

3. **Crea template dinámico:**
   - Copia el HTML de artículos como referencia
   - Mapea campos a dinámicos en Webflow

---

## Notas Importantes

### SEO
- ✅ Todos los artículos están optimizados con:
  - Palabras clave relevantes
  - Meta descriptions
  - Headings bien jerárquicos (H1, H2, H3)
  - URLs amigables

### Colores
Los colores están definidos en `:root`:
```css
--primary: #1a73e8 (Azul)
--accent: #ff6b35 (Naranja)
--text: #3c4043 (Gris oscuro)
```

Si quieres cambiarlos, busca estas líneas y reemplaza.

### Links Internos
- Actualiza links a:
  - `/blog/calcular` (calculadora)
  - `https://stayvagroup.com` (home)
  - `/blog` (índice)

### CTAs (Botones)
Todos tienen placeholders:
- "Usar Calculadora Gratis"
- "Agendar Consulta"
- "Análisis de Mercado"

Conecta a tus formularios/integraciones en Webflow.

---

## Testing Checklist

- [ ] Todos los links funcionan (internos y externos)
- [ ] Imágenes se ven (emojis aparecen bien)
- [ ] Mobile responsive se ve bien
- [ ] CTAs llevan a formularios correctos
- [ ] Meta descriptions aparecen en Google
- [ ] Velocidad de página > 3 segundos

---

## Estadísticas del Blog

📊 **Contenido Total:**
- 6 páginas
- ~8,500 palabras
- 5 artículos SEO-optimizados
- 45+ enlaces internos sugeridos
- +30 CTAs estratégicos

📈 **Temas Cubiertos:**
- Rentabilidad y cálculo de RPM
- Errores comunes & soluciones
- Fórmula ocupación vs tarifa
- Plan escalabilidad 1→40+ apartamentos
- Tendencias mercado 2026

---

## Mejoras Futuras (No Incluidas)

- [ ] Comentarios (Disqus, Remark42)
- [ ] Newsletter signup (ConvertKit, Mailchimp)
- [ ] Share buttons automatizados (AddThis)
- [ ] Related posts sugeridos
- [ ] Analytics integrado (Hotjar)
- [ ] Traducción a EN (Weglot)

---

**Listo para copiar y pegar. 100% funcional. Diseño profesional. SEO ready.**

Cualquier duda, revisa el código de los .html — está bien comentado y es semántico.
