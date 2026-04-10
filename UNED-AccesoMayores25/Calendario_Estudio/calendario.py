from datetime import datetime, timedelta
import json
import csv

# CONFIGURACIÓN
HORAS_DIARIAS = 2
INICIO = datetime(2026, 1, 15)  # Jueves - AJUSTA TU FECHA REAL
DURACION_SEMANAS = 12

# Asignaturas y horas recomendadas
ASIGNATURAS = {
    "Lengua Castellana": 25,
    "Comentario Texto": 20,
    "Inglés": 28,
    "Matemáticas Aplicadas": 30,
    "Administración Empresas": 22
}

total_horas = sum(ASIGNATURAS.values())
horas_por_dia = {asig: round((horas/total_horas) * HORAS_DIARIAS, 1) 
                 for asig, horas in ASIGNATURAS.items()}

# Generar calendario
calendario = []
current_date = INICIO
asig_keys = list(horas_por_dia.keys())
asig_idx = 0

while (current_date - INICIO).days < (DURACION_SEMANAS * 7):
    if current_date.weekday() < 5:  # Lunes-Viernes
        asignatura = asig_keys[asig_idx % len(asig_keys)]
        horas = horas_por_dia[asignatura]
        
        calendario.append({
            "fecha": current_date.strftime("%Y-%m-%d"),
            "dia": current_date.strftime("%A"),
            "asignatura": asignatura,
            "horas": horas,
            "tipo": "teoría" if asig_idx % 2 == 0 else "ejercicios"
        })
        
        asig_idx += 1
    
    current_date += timedelta(days=1)

# Guardar JSON
with open("calendario.json", "w", encoding="utf-8") as f:
    json.dump(calendario, f, indent=2, ensure_ascii=False)

# Guardar CSV
with open("calendario.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["fecha", "dia", "asignatura", "horas", "tipo"])
    writer.writeheader()
    writer.writerows(calendario)

print(f"✅ Calendario generado ({len(calendario)} días)")
print(f"📊 Total: {total_horas}h en {DURACION_SEMANAS} semanas")
print("\n📅 Distribución diaria (~2h):")
for asig, h in horas_por_dia.items():
    print(f"  • {asig}: {h}h/día")
