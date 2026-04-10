const tarifas = {
  "Madrid":     { "Estudio": 80, "1 hab": 120, "2 hab": 180, "3 hab+": 250 },
  "Medellin":   { "Estudio": 40, "1 hab": 60,  "2 hab": 90,  "3 hab+": 120 },
  "Cancun":     { "Estudio": 60, "1 hab": 90,  "2 hab": 130, "3 hab+": 180 },
  "Costa Rica": { "Estudio": 50, "1 hab": 75,  "2 hab": 110, "3 hab+": 150 }
};

function calcularIngreso(zona, habitaciones) {
  const tarifa = tarifas[zona][habitaciones];
  const anual = Math.round(tarifa * 0.75 * 365);
  const mensual = Math.round(anual / 12);
  const mejora = Math.round(((anual / (anual * 0.7)) - 1) * 100);

  return {
    mensual: `${mensual.toLocaleString("es-ES")} €/mes`,
    anual: `${anual.toLocaleString("es-ES")} €/año`,
    mejora: `+${mejora}% vs. gestión tradicional`,
    disclaimer: "Estimación orientativa. Resultados pueden variar según ubicación, estado y estrategia de precios."
  };
}

// Ejemplo de uso:
console.log(calcularIngreso("Madrid", "Estudio"));
// → { mensual: "1.825 €/mes", anual: "21.900 €/año", ... }
