# Skill: Fiscalidad Inmobiliaria en España

## Propósito

Calcular y analizar los impuestos aplicables a operaciones inmobiliarias en España, con especial atención a Galicia (tipos autonómicos propios).

## Impuestos en la compraventa

### ITP (Impuesto sobre Transmisiones Patrimoniales) — vivienda usada

Aplica cuando el vendedor es **particular** (no empresa/promotor).

| Tipo en Galicia | Supuesto |
|-----------------|---------|
| **10%** | Tipo general |
| **8%** | Precio ≤ 150.000€ vivienda habitual |
| **6%** | Precio ≤ 150.000€ + comprador ≤ 36 años o familia numerosa |
| **3%** | Vivienda en núcleo rural ≤ 150.000€ compradores ≤ 36 años o VH + ciertas condiciones |

Base imponible: el **valor de referencia catastral** (desde 2022, Ley 11/2021) o el precio escriturado si es superior.

### IVA + AJD — vivienda nueva

Aplica cuando el vendedor es **promotor/empresa** en primera transmisión.

| Impuesto | Tipo | Observación |
|----------|------|-------------|
| IVA | 10% | Vivienda (4% VPO régimen especial) |
| IVA | 21% | Local comercial, garaje independiente (+2 plazas) |
| AJD Galicia | 1,5% | Tipo general |
| AJD Galicia | 1% | Vivienda habitual jóvenes ≤ 36 años |
| AJD Galicia | 0,5% | VPO régimen especial |

### Costes totales estimados de compra

```
Precio de compra:                    P
+ ITP (usada) o IVA+AJD (nueva):    8-10% de P
+ Gastos de notaría:                 0,1-0,5% (escala)
+ Gastos de registro:                0,05-0,3%
+ Honorarios gestoría:               300-600€
+ Tasación (si hay hipoteca):        250-600€
─────────────────────────────────────────────
Coste total estimado:                P + 10-12%
```

## IBI (Impuesto sobre Bienes Inmuebles)

- Municipal. Devengado el 1 de enero. Pagador: propietario a 1/1.
- Base imponible: **valor catastral**
- Tipo en Ribadeo: consultar ordenanza fiscal municipal (aprox. 0,5-0,7% urbano)
- Posibles bonificaciones: VPO, familias numerosas, domicilio domótico, energía renovable
- **Impugnación**: posible si valor catastral supera valor de mercado → recurso al Catastro o reclamación ante TEAR

## Plusvalía municipal (IIVTNU)

Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana.

Desde **STC 182/2021** (TC): solo se devenga si hay incremento real de valor del suelo.

Dos métodos de cálculo (contribuyente elige el más favorable):

**Método objetivo:**
```
Base = Valor catastral del suelo × Coeficiente (según años de tenencia)
Cuota = Base × Tipo municipal (máx. 30%)
```

**Método real (plusvalía real):**
```
Base = (Precio venta − Precio compra) × (Valor catastral suelo / Valor catastral total)
Cuota = Base × Tipo municipal
```

Coeficientes 2024 (RDL 26/2021, actualizados anualmente):
| Período (años) | Coeficiente máximo |
|----------------|--------------------|
| Hasta 1 año    | 0,14               |
| 1-2 años       | 0,13               |
| 2-3 años       | 0,15               |
| 3-4 años       | 0,16               |
| 5-10 años      | 0,17               |
| 10-20 años     | 0,12               |
| Más de 20      | 0,10               |

## IRPF — Fiscalidad del arrendador persona física

| Concepto | Deducible |
|----------|-----------|
| IBI | Sí (proporcional si arrendamiento parcial) |
| Comunidad de propietarios | Sí |
| Intereses hipoteca | Sí |
| Amortización (3% sobre valor construcción) | Sí |
| Seguros del inmueble | Sí |
| Gastos de conservación y reparación | Sí |
| Honorarios gestor/administrador | Sí |
| Gastos de publicidad (para arrendar) | Sí |

**Reducción por arrendamiento de vivienda habitual:**
- 60% sobre rendimiento neto (contratos nuevos post Ley 12/2023 en zonas no tensionadas)
- 90% en zonas de mercado tensionado con rebaja ≥ 5% sobre contrato anterior
- 70% en zona tensionada con arrendatario joven (≤ 35 años)
- 50% resto de casos post Ley 12/2023

**Tipo marginal**: rendimientos de capital inmobiliario tributan a tarifa general IRPF (19-47% según base).

## Fiscalidad del vendedor (IRPF — ganancia patrimonial)

```
Ganancia = Precio venta − (Precio compra + Gastos compra + mejoras + Gastos venta)
```

Tipos de gravamen 2024 (base del ahorro):
| Tramo | Tipo |
|-------|------|
| 0 – 6.000 € | 19% |
| 6.001 – 50.000 € | 21% |
| 50.001 – 200.000 € | 23% |
| 200.001 – 300.000 € | 27% |
| > 300.000 € | 28% |

**Exenciones relevantes:**
- Reinversión en vivienda habitual (art. 38 LIRPF): exención si se reinvierte el total en nueva VH en 2 años
- Mayores de 65 años: exención total en transmisión de vivienda habitual
- Dación en pago (RDL 6/2012): exención si se cumplen requisitos de vulnerabilidad

## Retención no residentes (IRNR)

Si el vendedor es no residente: el comprador retiene **3%** del precio de venta e ingresa en Hacienda (modelo 211).
