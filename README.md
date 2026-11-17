# Circuitos: Caos Controlado

**Circuitos: Caos Controlado** es un videojuego educativo e interactivo diseñado para transformar el aprendizaje de la física y la electricidad en una experiencia dinámica, visual y segura. Desarrollado como prototipo didáctico en **Secundaria M Montessori** (VII Zona Escolar), el proyecto busca cerrar la brecha entre los conceptos teóricos abstractos y la experimentación práctica sin el riesgo físico de "quemar" componentes reales. 
---

##   Propósito y Objetivos

El proyecto responde a la pregunta: *¿Puede un videojuego educativo interactivo facilitar la comprensión de los circuitos eléctricos en comparación con los métodos tradicionales de enseñanza?*

* **Simulación Visual e Interactiva:** Representación dinámica del flujo de corriente, voltaje y resistencia
* **Física Aplicada:** Mecánicas basadas en principios reales como la **Ley de Ohm** ($I = V/R$)[cite: 6, 10], potencia eléctrica ($P = V \cdot I$) y circuitos en serie y paralelo
* **Progresión y Retroalimentación:** Niveles con dificultad incremental y validación en tiempo real para aprender mediante el ensayo y error
* **Inclusión Multilingüe:** Soporte integrado en **Español, Inglés, Portugués y Guaraní** para ampliar el acceso al conocimiento
---

## Alineación con los ODS (ONU)

Este proyecto contribuye directamente a los Objetivos de Desarrollo Sostenible[cite: 5]:
* **ODS 4 (Educación de calidad):** Aprendizaje práctico e interactivo mediante gamificación (DGBL)
* **ODS 7 (Energía asequible y no contaminante):** Comprensión del consumo y uso responsable de la energía eléctrica
* **ODS 9 (Industria, innovación e infraestructura):** Uso de programación y desarrollo de software aplicado a la educación
* **ODS 10 (Reducción de las desigualdades):** Interfaz multilingüe (incluyendo lenguas originarias como el guaraní)

---

## Arquitectura y Stack Tecnológico

El software fue construido bajo una arquitectura modular inspirada en el patrón **Modelo-Vista-Controlador (MVC)**, separando la lógica de simulación de la interfaz gráfica:

* **Lenguaje:** Python 3
* **Framework GUI:** [Kivy](https://kivy.org/) & Kivy Language (`.kv`)
* **Entorno de Desarrollo:** Thonny IDE
* **Prototipado Físico Complementario:** Arduino, Protoboard, LEDs, resistencias y cables jumper
### Características Técnicas Destacadas
* **Modelado de Circuitos como Grafos/Redes:** Los componentes se representan mediante estructuras de datos (listas y diccionarios) como nodos con atributos (tipo, valor, estado) y enlaces para validar la continuidad eléctrica
* **Interfaz Reactiva:** Uso de `NumericProperty` y `StringProperty` de Kivy para actualizar los valores eléctricos y visuales en tiempo real
* **Gestión de Vistas:** Navegación estructurada mediante `ScreenManager` (menú principal, selector de niveles y tablero de simulación) y layouts adaptables (`BoxLayout`, `FloatLayout`)

---

##  Resultados de Validación

En pruebas comparativas realizadas con 20 participantes evaluando el método tradicional frente al videojuego[cite: 21]:
* **Retroalimentación inmediata:** 95% de aprobación
* **Interacción activa:** 95% de aprobación
* **Motivación intrínseca:** 90% de aprobación
* **Desarrollo de pensamiento lógico:** 90% de aprobación
* **Comprensión de conceptos:** 85% de aprobación (superando significativamente la retención del método tradicional)

---
escrito por: Tina (inzã)


##  Instalación y Ejecución

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/circuitos-caos-controlado.git](https://github.com/tu-usuario/circuitos-caos-controlado.git)
   cd circuitos-caos-controlado
