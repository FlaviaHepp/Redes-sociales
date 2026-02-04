# Análisis de perfiles de redes sociales

Este proyecto realiza un **análisis exploratorio de datos (EDA)** sobre perfiles de redes sociales con el objetivo de **entender la relación entre publicaciones, seguidores e interacciones**, y detectar patrones de rendimiento entre distintos tipos de cuentas.

El análisis está orientado a **marketing digital y social media analytics**, aportando insights útiles para la gestión y optimización de perfiles.

---

## 📱 Contexto del análisis

En redes sociales, no siempre más publicaciones implican más seguidores o mayor engagement.  
Este proyecto busca responder preguntas clave como:

- ¿Existe relación entre cantidad de publicaciones y número de seguidores?
- ¿Qué perfiles generan más interacciones?
- ¿Qué cuentas están sobre-publicando sin crecer?
- ¿Qué perfiles muestran oportunidades de mejora?

---

## 🎯 Objetivos

- Analizar métricas clave de perfiles de redes sociales
- Calcular estadísticas descriptivas relevantes
- Explorar la relación entre publicaciones, seguidores e interacciones
- Identificar perfiles con alto y bajo rendimiento
- Visualizar patrones de engagement

---

## 📊 Dataset

El dataset contiene información básica de perfiles de redes sociales.

### Variables incluidas
- `Perfil`
- `Cantidad de Publicaciones`
- `Número de Seguidores`
- `Cantidad de Interacciones`

Los datos se cargan desde un archivo CSV (`redes_sociales.csv`).

---

## 🧪 Metodología

### 1. Análisis exploratorio de datos (EDA)
- Carga y visualización inicial del dataset
- Revisión de métricas generales
- Estadísticas descriptivas básicas

### 2. Análisis descriptivo
- Promedio de seguidores de los primeros 10 perfiles
- Ranking de perfiles por:
  - número de seguidores
  - cantidad de interacciones

### 3. Segmentación de perfiles
Se identifican perfiles con características específicas:
- Más de 100 publicaciones y menos de 3000 seguidores
- Más de 10 publicaciones y menos de 1000 seguidores

Estos casos permiten detectar **perfiles con bajo crecimiento relativo**.

---

## 📈 Visualizaciones

- **Gráfico de dispersión** entre:
  - cantidad de publicaciones
  - número de seguidores

El gráfico permite observar:
- posibles correlaciones
- perfiles outliers
- eficiencia relativa de crecimiento

---

## 📌 Principales insights

- Publicar más no garantiza mayor cantidad de seguidores
- Algunos perfiles presentan alto nivel de publicaciones con bajo crecimiento
- El engagement (interacciones) es un indicador clave complementario al número de seguidores
- Existen perfiles con potencial de optimización de contenido y estrategia

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **pandas**
- **NumPy**
- **matplotlib**

---

## 📂 Estructura del repositorio

├── redes_sociales.csv
├── Análisis de perfiles de redes sociales.py
├── README.md


---

## 🚀 Próximos pasos

- Calcular métricas de engagement (interacciones / seguidores)
- Incorporar análisis por tipo de contenido
- Comparar crecimiento relativo entre perfiles
- Construir un dashboard interactivo
- Automatizar reportes para social media managers

---

## 👤 Autor

**Flavia Hepp**  
Data Analyst / Marketing Analytics en formación  
