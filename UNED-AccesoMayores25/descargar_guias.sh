#!/bin/bash

ASIGNATURAS=(
  "00001011:Lengua_Castellana"
  "00001012:Comentario_Texto"
  "00001013:Ingles"
  "00001014:Matematicas_Aplicadas"
  "00001015:Administracion_Empresas"
)

for asig in "${ASIGNATURAS[@]}"; do
  codigo=$(echo $asig | cut -d: -f1)
  carpeta=$(echo $asig | cut -d: -f2)
  
  url="https://www.uned.es/universidad/pdf/GuiasAsignaturasAcceso/PDFGuiaAcceso?codigoAsignatura=${codigo}&curso=2026&codigoPrograma=-1&language=es"
  
  echo "📥 Descargando: $carpeta..."
  curl -L "$url" -o "$carpeta/Guia_Oficial_2026.pdf" 2>/dev/null
done

echo "✅ Guías descargadas"
