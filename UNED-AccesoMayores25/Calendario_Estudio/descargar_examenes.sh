#!/bin/bash

echo "📥 Descargando exámenes desde educalive.com..."

# Crear subcarpetas para exámenes
mkdir -p {Lengua_Castellana,Comentario_Texto,Ingles,Matematicas_Aplicadas,Administracion_Empresas}/Examenes_Anteriores

# Descargar página principal
curl -s "https://www.educalive.com/examenes-prueba-acceso-mayores-25-uned" -o examenes_page.html

echo "✅ Página descargada. Buscando enlaces a PDFs..."

# Extraer todos los enlaces de descarga
grep -o 'href="[^"]*\.pdf"' examenes_page.html | cut -d'"' -f2 | sort -u > enlaces_pdf.txt

echo "📋 Enlaces encontrados:"
cat enlaces_pdf.txt

# Descargar cada PDF
while IFS= read -r enlace; do
  filename=$(basename "$enlace")
  echo "⬇️  Descargando: $filename"
  curl -L "$enlace" -o "downloads/$filename" 2>/dev/null
done < enlaces_pdf.txt

echo "✅ Descargas completadas en /downloads"
ls -lh downloads/ 2>/dev/null || echo "⚠️  No se descargó nada. Quizás requiere JavaScript."

