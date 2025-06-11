# Informe de Resultados de Práctica 3: Simulación y Evaluación de Filtros de Kalman

## 1. Introducción

El presente trabajo se enfoca en la implementación y análisis comparativo de tres variantes del filtro de Kalman, cada una con una dimensionalidad distinta del vector de estado (3D, 7D y 8D). Se evaluó su desempeño mediante simulaciones en escenarios con diferentes niveles de ruido, analizando su precisión y estabilidad mediante visualizaciones y métricas relevantes.

## 2. Filtros de Kalman Evaluados

Se aplicaron tres versiones del filtro de Kalman, diferenciadas por la cantidad de variables incluidas en su estado:

- **Filtro Kalman con estado 3D**
- **Filtro Kalman con estado 7D**
- **Filtro Kalman con estado 8D**

## 3. Enfoque Metodológico

1. **Estimación**: Cada filtro fue aplicado sobre datos provenientes de un rosbag.
2. **Visualización**: Las trayectorias estimadas fueron comparadas visualmente con la trayectoria real.
3. **Evaluación por escenarios**: Se analizaron tres contextos distintos con niveles variables de ruido:

   - **Configuración base**: sin modificaciones.
   - **Ruido elevado en las mediciones**: aumento en la covarianza de los sensores.
   - **Ruido elevado en el modelo dinámico**: incremento en la incertidumbre del proceso.

## 4. Resultados

### 4.1 Configuración Base

- El modelo 3D destacó por su rapidez, aunque presentó menor precisión.
- El modelo 7D logró un buen compromiso entre exactitud y costo computacional.
- El modelo 8D fue más preciso en trayectorias complejas, aunque con ligeras señales de sobreajuste.

### 4.2 Alta Incertidumbre en las Mediciones

- El modelo 3D fue el más afectado por el ruido en las observaciones, mostrando desviaciones notables.
- El modelo 8D mantuvo estabilidad gracias a su estructura más rica en estados.

### 4.3 Alta Incertidumbre en el Modelo de Movimiento

- El filtro 3D se mostró más robusto en este escenario debido a su simplicidad.
- El filtro 7D tuvo un desempeño razonable frente al aumento del ruido del proceso.
- El filtro 8D evidenció inestabilidad en variables derivadas como la aceleración, debido a la mayor complejidad del modelo dinámico.

## 5. Conclusiones

- **Filtro 3D**: adecuado para sistemas con recursos limitados o aplicaciones en tiempo real, pero con limitaciones en contextos complejos o ruidosos.
- **Filtro 7D**: se posiciona como una opción equilibrada entre eficiencia y exactitud.
- **Filtro 8D**: ofrece buen rendimiento en entornos exigentes, aunque requiere un diseño más cuidadoso y puede ser más vulnerable a errores de modelado.

El análisis visual de las trayectorias permitió detectar patrones de error y confirmó el comportamiento esperado para cada filtro según su complejidad.
