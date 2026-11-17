import os
import random
import math
from math import cos, isinf, pi, sin

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line, Rectangle, RoundedRectangle
from kivy.metrics import dp, sp
from kivy.properties import NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def asset(name):
    path = os.path.join(BASE_DIR, name)
    return path if os.path.exists(path) else None


def asset_path(filename):
    return os.path.join(BASE_DIR, filename)


TXT = {
    "es": {
        "play": "Jugar",
        "story": "Modo historia",
        "quiz": "Quiz de electrónica",
        "info": "Info",
        "credits": "Creditos",
        "language": "Idioma",
        "back": "Volver",
        "simulate": "Simular",
        "reset": "Reiniciar",
        "next": "Siguiente",
        "menu": "Menu",
        "diagnostic": "Vista diagnostico",
        "normal": "Vista normal",
        "mode_series": "Cambiar a Serie",
        "mode_parallel": "Cambiar a Paralelo",
        "title": "Circuitos: Caos Controlado",
        "subtitle": "Arma circuitos, mide corriente y evita que el laboratorio se derrita.",
        "voltage": "Voltaje de bateria",
        "mission": "Mision",
        "target": "Meta",
        "limits": "Limites",
        "physics": "Modelo fisico",
        "readings": "Lecturas",
        "diagnosis": "Diagnostico",
        "performance": "Rendimiento",
        "build_first": "Construye el circuito y presiona Simular.",
        "story_text": (
            "La ciudad educativa perdio energia. Tu trabajo es reparar modulos electricos "
            "sin quemar resistencias, usando la Ley de Ohm como herramienta principal."
        ),
        "info_text": (
            "[b]¿Qué es este proyecto?[/b]\n"
            "Circuitos: Caos Controlado es un juego educativo sobre electricidad básica. El jugador arma "
            "circuitos, cambia el voltaje, alterna entre serie y paralelo, observa la corriente y aprende a "
            "evitar sobrecalentamientos.\n\n"
            "[b]Conceptos que enseña[/b]\n"
            "- Voltaje: la energía que empuja las cargas eléctricas.\n"
            "- Corriente: el flujo de carga que pasa por el circuito.\n"
            "- Resistencia: oposición al paso de corriente.\n"
            "- Potencia: energía consumida por segundo; si sube demasiado, aparece calor.\n\n"
            "[b]Ley de Ohm[/b]\n"
            "La relación principal es I = V / R. Si sube el voltaje, suele subir la corriente. Si sube la "
            "resistencia, la corriente baja.\n\n"
            "[b]Circuito en serie[/b]\n"
            "Las resistencias se suman: Rtotal = R1 + R2 + R3. La corriente es la misma en todos los componentes, "
            "pero el voltaje se reparte.\n\n"
            "[b]Circuito en paralelo[/b]\n"
            "Cada rama recibe el mismo voltaje. La resistencia total baja y la corriente puede aumentar mucho, "
            "por eso hay que vigilar el calor.\n\n"
            "[b]Objetivo educativo[/b]\n"
            "El juego no solo pide ganar niveles: obliga a medir, diagnosticar fallas y tomar decisiones seguras. "
            "Eso lo vuelve más parecido a un laboratorio que a un cuestionario normal.\n\n"
            "[b]Cómo jugar[/b]\n"
            "Arrastra la batería y las resistencias al tablero, ajusta el voltaje, elige serie o paralelo y presiona "
            "Simular. Si la corriente queda cerca de la meta sin superar los límites, el circuito es estable."
        ),
        "credits_text": (
            "Proyecto educativo hecho para feria de ciencias.\n"
            "Assets usados si existen en la carpeta: logo, fondos, bateria, iconos de correcto/incorrecto, "
            "y musica por pantalla."
        ),
    },
    "en": {
        "play": "Play",
        "story": "Story mode",
        "quiz": "Electronics Quiz",
        "info": "Info",
        "credits": "Credits",
        "language": "Language",
        "back": "Back",
        "simulate": "Simulate",
        "reset": "Reset",
        "next": "Next",
        "menu": "Menu",
        "diagnostic": "Diagnostic view",
        "normal": "Normal view",
        "mode_series": "Switch to Series",
        "mode_parallel": "Switch to Parallel",
        "title": "Circuits: Controlled Chaos",
        "subtitle": "Build circuits, measure current, and keep the lab from overheating.",
        "voltage": "Battery voltage",
        "mission": "Mission",
        "target": "Target",
        "limits": "Limits",
        "physics": "Physics model",
        "readings": "Readings",
        "diagnosis": "Diagnosis",
        "performance": "Performance",
        "build_first": "Build the circuit and press Simulate.",
        "story_text": (
            "The learning city lost power. Your job is to repair electric modules without burning "
            "resistors, using Ohm's Law as your main tool."
        ),
        "info_text": (
            "This educational game teaches voltage, current, resistance, power, series circuits, parallel circuits, "
            "diagnosis, and overheating risk. The main equation is Ohm's Law: I = V / R. Players build circuits, "
            "simulate them, compare readings, and learn why safe design matters."
        ),
        "credits_text": (
            "Educational science fair project.\n"
            "Assets are used when present: logo, backgrounds, battery, correct/incorrect icons, and music."
        ),
    },
    "pt": {
        "play": "Jogar",
        "story": "Modo historia",
        "quiz": "Quiz de eletrônica",
        "info": "Info",
        "credits": "Creditos",
        "language": "Idioma",
        "back": "Voltar",
        "simulate": "Simular",
        "reset": "Reiniciar",
        "next": "Proximo",
        "menu": "Menu",
        "diagnostic": "Vista diagnostico",
        "normal": "Vista normal",
        "mode_series": "Mudar para Serie",
        "mode_parallel": "Mudar para Paralelo",
        "title": "Circuitos: Caos Controlado",
        "subtitle": "Monte circuitos, meça corrente e evite superaquecimento.",
        "voltage": "Tensao da bateria",
        "mission": "Missao",
        "target": "Meta",
        "limits": "Limites",
        "physics": "Modelo fisico",
        "readings": "Leituras",
        "diagnosis": "Diagnostico",
        "performance": "Desempenho",
        "build_first": "Monte o circuito e pressione Simular.",
        "story_text": (
            "A cidade educativa ficou sem energia. Seu trabalho e reparar modulos eletricos "
            "sem queimar resistores, usando a Lei de Ohm."
        ),
        "info_text": (
            "O jogo ensina tensao, corrente, resistencia, potencia, circuitos em serie e paralelo, diagnostico "
            "e risco de superaquecimento. A formula principal e I = V / R. O jogador monta, simula e analisa."
        ),
        "credits_text": (
            "Projeto educativo para feira de ciencias.\n"
            "Assets usados se existirem: logo, fundos, bateria, correto/incorreto e musicas."
        ),
    },
    "gn": {
        "play": "Ñembosarai",
        "story": "Tembiasakue",
        "quiz": "Quiz de electrónica",
        "info": "Marandu",
        "credits": "Aguyje",
        "language": "Ñe'ẽ",
        "back": "Jevy",
        "simulate": "Ha'anga",
        "reset": "Ñepyrũ jey",
        "next": "Upeigua",
        "menu": "Menu",
        "diagnostic": "Jehecha porã",
        "normal": "Jehecha biasa",
        "mode_series": "Serie-pe",
        "mode_parallel": "Paralelo-pe",
        "title": "Circuitos: Caos Controlado",
        "subtitle": "Emopu'a circuito, ehecha corriente ha ani haku eterei.",
        "voltage": "Bateria voltaje",
        "mission": "Tembiapo",
        "target": "Meta",
        "limits": "Limite",
        "physics": "Fisika",
        "readings": "Medicion",
        "diagnosis": "Diagnostico",
        "performance": "Rendimiento",
        "build_first": "Emopu'a circuito ha eity Simular.",
        "story_text": (
            "Táva mbo'epy opyta energia'ỹre. Nde remyatyrõta modulo electrico Ley de Ohm reheve."
        ),
        "info_text": (
            "Ko juego ohechauka voltaje, corriente, resistencia, potencia, circuito serie ha paralelo. "
            "Formula iñimportanteve: I = V / R. Pe jugador omopu'a circuito ha ohecha mba'eichapa omba'apo."
        ),
        "credits_text": (
            "Proyecto feria de ciencias-pe guarã.\n"
            "Ojepuru assets oĩramo: logo, fondo, bateria, correcto/incorrecto ha musica."
        ),
    },
}


QUIZ_TEXT = {
    "es": {
        "title": "Quiz de electrónica",
        "menu_label": "Quiz de electrónica",
        "intro_title": "Antes de empezar: Ley de Ohm",
        "intro": "La Ley de Ohm relaciona voltaje (V), corriente (I) y resistencia (R):\n\n[b]V = I × R[/b]\n\nDespeja la incógnita: R = V / I, I = V / R o V = I × R. Sustituye los datos, calcula y escribe la unidad correcta.\n\nEjemplo: con 12 V y 3 Ω, I = 12 / 3 = 4 A.",
        "start": "Empezar quiz",
        "next": "Siguiente",
        "menu": "Volver al menú",
        "restart": "Intentar otra vez",
        "question": "Pregunta {current} de {total}",
        "correct": "¡Correcto!",
        "incorrect": "No exactamente.",
        "score": "Resultado: {score} de {total}",
        "done": "Quiz terminado",
        "pick": "Elige una respuesta:",
        "items": [
            {"q":"Un circuito tiene 120 V y circulan 2.4 A. ¿Cuál es su resistencia?", "o":["50 Ω", "288 Ω", "0.02 Ω", "122.4 Ω"], "a":0, "e":"R = V / I. Sustituye: R = 120 / 2.4 = 50 Ω."},
            {"q":"Por un conductor de 27 Ω circulan 6.5 A. ¿Qué voltaje hay?", "o":["4.15 V", "33.5 V", "175.5 V", "702 V"], "a":2, "e":"V = I × R. Sustituye: V = 6.5 × 27 = 175.5 V."},
            {"q":"Se aplican 120 V a una resistencia de 50 Ω. ¿Qué corriente circula?", "o":["0.42 A", "2.4 A", "70 A", "6000 A"], "a":1, "e":"I = V / R. Sustituye: I = 120 / 50 = 2.4 A."},
            {"q":"¿En qué unidad se mide la corriente eléctrica?", "o":["Voltios (V)", "Ohmios (Ω)", "Amperios (A)", "Vatios (W)"], "a":2, "e":"La corriente se mide en amperios (A). El voltio mide voltaje y el ohmio mide resistencia."},
            {"q":"Si el voltaje se mantiene y aumenta la resistencia, ¿qué pasa con la corriente?", "o":["Aumenta", "Disminuye", "No cambia nunca", "Se convierte en voltaje"], "a":1, "e":"Por I = V / R, al aumentar R con V constante, la corriente disminuye."},
            {"q":"¿Qué instrumento se conecta en paralelo para medir voltaje?", "o":["Amperímetro", "Voltímetro", "Ohmímetro en serie", "Interruptor"], "a":1, "e":"El voltímetro mide la diferencia de potencial y se conecta en paralelo con el componente."},
        ],
    },
    "en": {
        "title": "Electronics Quiz", "menu_label": "Electronics Quiz", "intro_title": "First: Ohm's Law",
        "intro": "Ohm's Law relates voltage (V), current (I), and resistance (R):\n\n[b]V = I × R[/b]\n\nRearrange for the unknown: R = V / I, I = V / R, or V = I × R. Substitute the values, calculate, and use the correct unit.\n\nExample: with 12 V and 3 Ω, I = 12 / 3 = 4 A.",
        "start": "Start quiz", "next": "Next", "menu": "Back to menu", "restart": "Try again",
        "question": "Question {current} of {total}", "correct": "Correct!", "incorrect": "Not quite.",
        "score": "Score: {score} out of {total}", "done": "Quiz complete", "pick": "Choose an answer:",
        "items": [
            {"q":"A circuit has 120 V and carries 2.4 A. What is its resistance?", "o":["50 Ω", "288 Ω", "0.02 Ω", "122.4 Ω"], "a":0, "e":"R = V / I. Substitute: R = 120 / 2.4 = 50 Ω."},
            {"q":"A current of 6.5 A flows through a 27 Ω conductor. What is the voltage?", "o":["4.15 V", "33.5 V", "175.5 V", "702 V"], "a":2, "e":"V = I × R. Substitute: V = 6.5 × 27 = 175.5 V."},
            {"q":"A 50 Ω resistor has 120 V across it. What current flows?", "o":["0.42 A", "2.4 A", "70 A", "6000 A"], "a":1, "e":"I = V / R. Substitute: I = 120 / 50 = 2.4 A."},
            {"q":"What is the unit of electric current?", "o":["Volts (V)", "Ohms (Ω)", "Amperes (A)", "Watts (W)"], "a":2, "e":"Current is measured in amperes (A). Volts measure voltage and ohms measure resistance."},
            {"q":"If voltage stays constant and resistance increases, what happens to current?", "o":["It increases", "It decreases", "It never changes", "It turns into voltage"], "a":1, "e":"From I = V / R, increasing R while V stays constant makes current decrease."},
            {"q":"Which instrument is connected in parallel to measure voltage?", "o":["Ammeter", "Voltmeter", "Ohmmeter in series", "Switch"], "a":1, "e":"A voltmeter measures potential difference and is connected in parallel with the component."},
        ],
    },
    "pt": {
        "title": "Quiz de eletrônica", "menu_label": "Quiz de eletrônica", "intro_title": "Antes: Lei de Ohm",
        "intro": "A Lei de Ohm relaciona tensão (V), corrente (I) e resistência (R):\n\n[b]V = I × R[/b]\n\nIsole a incógnita: R = V / I, I = V / R ou V = I × R. Substitua os valores, calcule e use a unidade correta.\n\nExemplo: com 12 V e 3 Ω, I = 12 / 3 = 4 A.",
        "start": "Começar quiz", "next": "Próxima", "menu": "Voltar ao menu", "restart": "Tentar novamente",
        "question": "Pergunta {current} de {total}", "correct": "Correto!", "incorrect": "Não exatamente.",
        "score": "Resultado: {score} de {total}", "done": "Quiz concluído", "pick": "Escolha uma resposta:",
        "items": [
            {"q":"Um circuito tem 120 V e corrente de 2,4 A. Qual é sua resistência?", "o":["50 Ω", "288 Ω", "0,02 Ω", "122,4 Ω"], "a":0, "e":"R = V / I. Substituindo: R = 120 / 2,4 = 50 Ω."},
            {"q":"Uma corrente de 6,5 A passa por um condutor de 27 Ω. Qual é a tensão?", "o":["4,15 V", "33,5 V", "175,5 V", "702 V"], "a":2, "e":"V = I × R. Substituindo: V = 6,5 × 27 = 175,5 V."},
            {"q":"Uma resistência de 50 Ω recebe 120 V. Qual corrente circula?", "o":["0,42 A", "2,4 A", "70 A", "6000 A"], "a":1, "e":"I = V / R. Substituindo: I = 120 / 50 = 2,4 A."},
            {"q":"Qual é a unidade da corrente elétrica?", "o":["Volts (V)", "Ohms (Ω)", "Ampères (A)", "Watts (W)"], "a":2, "e":"A corrente é medida em ampères (A). Volts medem tensão e ohms medem resistência."},
            {"q":"Se a tensão permanece constante e a resistência aumenta, o que acontece com a corrente?", "o":["Aumenta", "Diminui", "Nunca muda", "Vira tensão"], "a":1, "e":"Pela fórmula I = V / R, aumentando R com V constante, a corrente diminui."},
            {"q":"Qual instrumento é ligado em paralelo para medir tensão?", "o":["Amperímetro", "Voltímetro", "Ohmímetro em série", "Interruptor"], "a":1, "e":"O voltímetro mede a diferença de potencial e é ligado em paralelo ao componente."},
        ],
    },
    "gn": {
        "title": "Electrónica quiz", "menu_label": "Electrónica quiz", "intro_title": "Ñepyrũ mboyve: Ohm Léi",
        "intro": "Ohm Léi ombojoaju voltaje (V), corriente (I) ha resistencia (R):\n\n[b]V = I × R[/b]\n\nEheka mba'e reikuaase: R = V / I, I = V / R, térã V = I × R. Emoĩ papapy, ekalkula ha eipuru unidad hekopete.\n\nTechapyrã: 12 V ha 3 Ω reheve, I = 12 / 3 = 4 A.",
        "start": "Eñepyrũ quiz", "next": "Upeigua", "menu": "Ejevy menú-pe", "restart": "Eha'ã jey",
        "question": "Porandu {current} / {total}", "correct": "¡Hekopete!", "incorrect": "Ndaipóriete.",
        "score": "Resultado: {score} / {total}", "done": "Quiz oñemohu'ã", "pick": "Eiporavo peteĩ mbohovái:",
        "items": [
            {"q":"Peteĩ circuito oguereko 120 V ha 2,4 A. Mboypa resistencia?", "o":["50 Ω", "288 Ω", "0,02 Ω", "122,4 Ω"], "a":0, "e":"R = V / I. Emoĩ papapy: R = 120 / 2,4 = 50 Ω."},
            {"q":"6,5 A ohasa peteĩ conductor 27 Ω rehe. Mboypa voltaje?", "o":["4,15 V", "33,5 V", "175,5 V", "702 V"], "a":2, "e":"V = I × R. Emoĩ papapy: V = 6,5 × 27 = 175,5 V."},
            {"q":"50 Ω resistencia-pe oñemoĩ 120 V. Mboypa corriente ohasa?", "o":["0,42 A", "2,4 A", "70 A", "6000 A"], "a":1, "e":"I = V / R. Emoĩ papapy: I = 120 / 50 = 2,4 A."},
            {"q":"Mba'épe oñemedi corriente eléctrica?", "o":["Voltios (V)", "Ohmios (Ω)", "Amperios (A)", "Vatios (W)"], "a":2, "e":"Corriente oñemedi amperios (A)-pe. Voltios omedi voltaje ha ohmios omedi resistencia."},
            {"q":"Voltaje opyta peteĩchante ha resistencia ojupi ramo, mba'épa oiko corriente rehe?", "o":["Ojupi", "Oguejy", "Nomoambuéiva araka'eve", "Oiko voltaje-gui"], "a":1, "e":"I = V / R rupive, R ojupívo ha V opytávo peteĩchante, corriente oguejy."},
            {"q":"Mba'e instrumento oñembojoaju paralelo-pe omedi hag̃ua voltaje?", "o":["Amperímetro", "Voltímetro", "Ohmímetro serie-pe", "Interruptor"], "a":1, "e":"Voltímetro omedi diferencia de potencial ha oñembojoaju paralelo-pe componente ndive."},
        ],
    },
}


def qtr(key):
    app = App.get_running_app()
    lang = getattr(app, "lang", "es") if app else "es"
    return QUIZ_TEXT.get(lang, QUIZ_TEXT["es"])[key]


TXT["es"].update({
    "level1_name": "Nivel 1",
    "level1_mission": "Activa una luz de emergencia con 2 resistencias en serie.",
    "level1_tip": "En serie sube la resistencia total y baja la corriente.",
    "level2_name": "Nivel 2",
    "level2_mission": "Alimenta dos ramas usando paralelo sin sobrecalentar.",
    "level2_tip": "En paralelo cada rama recibe el mismo voltaje.",
    "level3_name": "Nivel 3",
    "level3_mission": "Protege un sensor delicado usando 3 resistencias en serie.",
    "level3_tip": "Mas resistencia protege el sensor.",
    "level4_name": "Nivel 4",
    "level4_mission": "Reto final: usa las 3 resistencias y encuentra una solucion eficiente.",
    "level4_tip": "Solucion pista: paralelo con 3.0 V queda cerca de 1.83 A.",
    "comp_battery": "Bateria",
    "comp_battery_piece": "Bateria\nV variable",
    "missing_battery": "Falta colocar la bateria.",
    "missing_resistors": "Faltan {count} resistencia(s).",
    "required_mode": "Este nivel exige modo {mode}.",
    "overcurrent": "Corriente excesiva: riesgo de corto.",
    "overheat": "Sobrecalentamiento: baja voltaje o cambia resistencia.",
    "win_msg": "Circuito estable. Objetivo alcanzado.",
    "not_target": "La lectura aun no coincide con la meta.",
    "piece_placed": "Componente colocado. Ahora puedes simular.",
    "drop_zone": "Suelta la pieza dentro de una zona del tablero.",
    "score_msg": "{message} Puntuacion: {score}/100 ({stars} estrellas).",
    "voltage_reading": "Voltaje",
    "total_current": "Corriente",
    "temps": "Temperaturas",
    "branches": "Ramas",
    "power": "Potencia",
    "best_score": "Mejor puntuacion",
    "no_score": "--",
    "low_current": "La corriente esta baja. Sube voltaje o baja resistencia total.",
    "high_current": "La corriente esta alta. Baja voltaje o sube resistencia total.",
    "hot_but_works": "Funciona, pero esta caliente. Explica P = I²R.",
    "lab_ready": "Laboratorio listo. Arma un circuito y presiona Analizar.",
    "analyze": "Analizar",
    "clear": "Limpiar",
    "instruments": "Instrumentos",
    "source_voltage": "Voltaje de fuente",
    "lab_title": "Laboratorio Sandbox",
    "lab_mission": "Sandbox libre: arma, cambia voltaje, alterna serie/paralelo y compara mediciones.",
    "lab_tip": "Usa este modo para explicar que un circuito no solo debe encender: debe ser medible y seguro.",
    "lab_no_battery": "Coloca la bateria para activar las lecturas.",
    "lab_no_resistor": "Agrega al menos una resistencia para cerrar el circuito.",
    "lab_danger_current": "Riesgo alto: corriente excesiva. Baja voltaje o sube resistencia.",
    "lab_danger_temp": "Riesgo alto: temperatura critica. El circuito no es seguro.",
    "lab_warn": "Riesgo medio: funciona, pero conviene reducir potencia.",
    "lab_stable": "Sistema estable: buen punto para explicar mediciones.",
    "risk_waiting": "Sin lectura",
    "risk_stable": "Bajo",
    "risk_warn": "Medio",
    "risk_danger": "Alto",
    "lab_intro": "[b]Modo Laboratorio[/b]\nExperimenta sin niveles. Cambia conexiones y observa como se comportan corriente, resistencia, temperatura y potencia.\n\n[b]Pruebas sugeridas[/b]\n- Compara serie vs paralelo.\n- Sube voltaje poco a poco.\n- Busca un circuito estable.\n- Explica por que aparece calor.",
    "lab_instruments": "[b]Instrumentos[/b]\nVoltimetro: mide V\nAmperimetro: mide I\nOhmetro virtual: calcula Rtotal\nTermometro: estima calentamiento",
    "lab_live": "Lecturas en vivo",
    "mode_label": "Modo",
    "branch_currents": "Corriente por ramas",
    "total_power": "Potencia total",
    "risk": "Riesgo",
    "lab_interpretation": "[b]Interpretacion[/b]\nMas voltaje aumenta corriente.\nMas resistencia reduce corriente.\nMas potencia suele significar mas calor.",
    "lab_series_tip": "En serie, sumar resistencias ayuda a controlar la corriente.",
    "lab_parallel_tip": "En paralelo, baja Rtotal y sube la corriente total: ideal para comparar ramas.",
    "credits_boot": "Cargando creditos...",
    "credits_error": "ERROR: exceso de talento detectado",
    "credits_log": "diagnostico: 12 cables, 1 cerebro, 0 presupuesto\nresultado: sorprendentemente presentable",
    "credits_warning_title": "Este juego puede contener:",
    "credits_warning_body": "logica dudosa\nmatematicas sospechosas\ndecisiones cuestionables\n\nSi funciona, no preguntar por que\n(el programador tampoco sabe)\n\nTiempo trabajando:\nmas del necesario\n\nTiempo perdiendo el tiempo:\ntambien mucho\n\nequilibrio perfecto XD",
    "credits_tina_name": "autora principal: Tina",
    "credits_tina_stats": "Programacion: 100%\nInvestigacion: 100%\nDiseño: 100%\nSueño: 0%\nPaciencia: variable\n\nNivel de 'yo si puedo': peligroso\nCantidad de canvas usado: si",
    "credits_people_title": "CREDITOS OFICIALMENTE SERIOS",
    "credits_design_title": "DISEÑO",
    "credits_design_body": "diseño: tambien Tina XD\n\nfue mucho ezzzfuerzo ya que la mayoria de cosas fueron hechas en canvas\n(y hasta para hacer un simple circulo tambien se tiene que programar)\n\nCreatividad: 80%\nInspiracion: 9999999999999%\nImprovisacion: 100%",
    "credits_measure_title": "MEDICIONES 100% CIENTIFICAS",
    "credits_measure_body": "Voltaje de creatividad: inestable pero poderoso\nResistencia al sueño: casi cero\nCorriente de ideas: peligrosa\nAmperaje de improvisacion: no medible\n\nDiagnostico final:\nsi prende, se presenta.",
    "credits_thanks_title": "GRACIAS",
    "credits_thanks_body": "este fue un juego hecho con poco presupuesto\npero con dedicacion\n\ngracias por no dormirse\n\nsi se rieron, era parte del plan\nsi aprendieron circuitos, tambien era parte del plan\nsi exploto algo... eso ya no estaba en el plan XD",
    "credits_patch_title": "PATCH NOTES DEL PROYECTO",
    "credits_patch_body": "v1.0 - edicion feria de ciencias\n\n- Se agrego electricidad para que parezca serio\n- Se redujo el panico en un 3%\n- Bug conocido: si algo funciona, no tocar\n- Balanceo: Tina hizo demasiado y el cafe hizo el resto\n- Modo profe: activar sonrisa y asentir con sabiduria",
    "credits_solo_title": "MODO UNA PERSONA",
    "credits_solo_body": "una mente\nmuchos cables\ndemasiados botones\n\nequipo detectado:\nTina\n\nestado del proyecto:\ncontra todo pronostico, sigue vivo",
    "credits_report_title": "INFORME TECNICO",
    "credits_report_body": "Hipotesis:\npodemos terminar el juego antes de que termine nuestra paciencia\n\nResultado:\nsi, pero a que costo XD\n\nConclusion:\nOhm estaria orgulloso... probablemente",
    "credits_teacher_title": "MODO PROFE",
        "credits_teacher_body": "Si el profe dice: 'muy creativo'\ntraduccion: no entendio todo, pero le cayo bien\n\nSi el profe pregunta por el codigo:\nrespuesta oficial: fue una experiencia de aprendizaje\n\nSi el circuito falla:\neso se llama demostracion de riesgos electricos",
    "missing_asset_msg": "Falta {filename}\npero el show sigue porque hay fe",
})

TXT["en"].update({
    "level1_name": "Level 1",
    "level1_mission": "Turn on an emergency light with 2 resistors in series.",
    "level1_tip": "In series, total resistance rises and current drops.",
    "level2_name": "Level 2",
    "level2_mission": "Power two branches in parallel without overheating.",
    "level2_tip": "In parallel, each branch receives the same voltage.",
    "level3_name": "Level 3",
    "level3_mission": "Protect a delicate sensor using 3 resistors in series.",
    "level3_tip": "More resistance protects the sensor.",
    "level4_name": "Level 4",
    "level4_mission": "Final challenge: use all 3 resistors and find an efficient solution.",
    "level4_tip": "Hint: parallel at 3.0 V lands near 1.83 A.",
    "comp_battery": "Battery",
    "comp_battery_piece": "Battery\nVariable V",
    "missing_battery": "Place the battery first.",
    "missing_resistors": "{count} resistor(s) missing.",
    "required_mode": "This level requires {mode} mode.",
    "overcurrent": "Excess current: short-circuit risk.",
    "overheat": "Overheating: lower voltage or change resistance.",
    "win_msg": "Stable circuit. Target reached.",
    "not_target": "The reading does not match the target yet.",
    "piece_placed": "Component placed. Now you can simulate.",
    "drop_zone": "Drop the part inside a board slot.",
    "score_msg": "{message} Score: {score}/100 ({stars} stars).",
    "voltage_reading": "Voltage",
    "total_current": "Current",
    "temps": "Temperatures",
    "branches": "Branches",
    "power": "Power",
    "best_score": "Best score",
    "no_score": "--",
    "low_current": "Current is low. Raise voltage or lower total resistance.",
    "high_current": "Current is high. Lower voltage or raise total resistance.",
    "hot_but_works": "It works, but it is hot. Explain P = I²R.",
    "lab_ready": "Lab ready. Build a circuit and press Analyze.",
    "analyze": "Analyze",
    "clear": "Clear",
    "instruments": "Instruments",
    "source_voltage": "Source voltage",
    "lab_title": "Sandbox Laboratory",
    "lab_mission": "Free sandbox: build, change voltage, switch series/parallel, and compare readings.",
    "lab_tip": "Use this mode to explain that a circuit must be measurable and safe, not just turn on.",
    "lab_no_battery": "Place the battery to activate readings.",
    "lab_no_resistor": "Add at least one resistor to close the circuit.",
    "lab_danger_current": "High risk: excessive current. Lower voltage or raise resistance.",
    "lab_danger_temp": "High risk: critical temperature. The circuit is not safe.",
    "lab_warn": "Medium risk: it works, but reducing power is better.",
    "lab_stable": "Stable system: a good point for explaining measurements.",
    "risk_waiting": "No reading",
    "risk_stable": "Low",
    "risk_warn": "Medium",
    "risk_danger": "High",
    "lab_intro": "[b]Lab Mode[/b]\nExperiment without levels. Change connections and observe current, resistance, temperature, and power.\n\n[b]Suggested tests[/b]\n- Compare series vs parallel.\n- Raise voltage slowly.\n- Find a stable circuit.\n- Explain why heat appears.",
    "lab_instruments": "[b]Instruments[/b]\nVoltmeter: measures V\nAmmeter: measures I\nVirtual ohmmeter: calculates Rtotal\nThermometer: estimates heating",
    "lab_live": "Live readings",
    "mode_label": "Mode",
    "branch_currents": "Branch currents",
    "total_power": "Total power",
    "risk": "Risk",
    "lab_interpretation": "[b]Interpretation[/b]\nMore voltage increases current.\nMore resistance reduces current.\nMore power usually means more heat.",
    "lab_series_tip": "In series, adding resistance helps control current.",
    "lab_parallel_tip": "In parallel, Rtotal drops and total current rises: perfect for comparing branches.",
    "credits_boot": "Loading credits...",
    "credits_error": "ERROR: excessive talent detected",
    "credits_log": "diagnosis: 12 wires, 1 brain, 0 budget\nresult: surprisingly presentable",
    "credits_warning_title": "This game may contain:",
    "credits_warning_body": "questionable logic\nsuspicious math\nquestionable decisions\n\nIf it works, do not ask why\n(the programmer does not know either)\n\nTime working:\nmore than necessary\n\nTime procrastinating:\nalso a lot\n\nperfect balance XD",
    "credits_tina_name": "lead author: Tina",
    "credits_tina_stats": "Programming: 100%\nResearch: 100%\nDesign: 100%\nSleep: 0%\nPatience: variable\n\n'I can do this' level: dangerous\nAmount of canvas used: yes",
    "credits_people_title": "OFFICIALLY SERIOUS CREDITS",
    "credits_design_title": "DESIGN",
    "credits_design_body": "design: also Tina XD\n\nit took a lot of effffort because most things were made in canvas\n(even a simple circle has to be programmed)\n\nCreativity: 80%\nInspiration: 9999999999999%\nImprovisation: 100%",
    "credits_measure_title": "100% SCIENTIFIC MEASUREMENTS",
    "credits_measure_body": "Creativity voltage: unstable but powerful\nSleep resistance: almost zero\nIdea current: dangerous\nImprovisation amperage: not measurable\n\nFinal diagnosis:\nif it turns on, present it.",
    "credits_thanks_title": "THANK YOU",
    "credits_thanks_body": "this was a game made with little budget\nbut with dedication\n\nthanks for not falling asleep\n\nif you laughed, that was part of the plan\nif you learned circuits, that was also part of the plan\nif something exploded... that was not in the plan XD",
    "credits_patch_title": "PROJECT PATCH NOTES",
    "credits_patch_body": "v1.0 - science fair edition\n\n- Added electricity so it looks serious\n- Reduced panic by 3%\n- Known bug: if it works, do not touch it\n- Balance: Tina did too much and coffee did the rest\n- Teacher mode: smile and nod wisely",
    "credits_solo_title": "ONE PERSON MODE",
    "credits_solo_body": "one mind\nmany wires\ntoo many buttons\n\nteam detected:\nTina\n\nproject status:\nagainst all odds, still alive",
    "credits_report_title": "TECHNICAL REPORT",
    "credits_report_body": "Hypothesis:\nwe can finish the game before our patience runs out\n\nResult:\nyes, but at what cost XD\n\nConclusion:\nOhm would be proud... probably",
    "credits_teacher_title": "TEACHER MODE",
    "credits_teacher_body": "If the teacher says: 'very creative'\ntranslation: did not understand everything, but liked it\n\nIf the teacher asks about the code:\nofficial answer: it was a learning experience\n\nIf the circuit fails:\nthat is called an electrical risk demonstration",
    "missing_asset_msg": "Missing {filename}\nbut the show goes on because hope exists",
})

TXT["pt"].update({
    "level1_name": "Nivel 1",
    "level1_mission": "Acenda uma luz de emergencia com 2 resistores em serie.",
    "level1_tip": "Em serie, a resistencia total aumenta e a corrente diminui.",
    "level2_name": "Nivel 2",
    "level2_mission": "Alimente dois ramos em paralelo sem superaquecer.",
    "level2_tip": "Em paralelo, cada ramo recebe a mesma tensao.",
    "level3_name": "Nivel 3",
    "level3_mission": "Proteja um sensor delicado usando 3 resistores em serie.",
    "level3_tip": "Mais resistencia protege o sensor.",
    "level4_name": "Nivel 4",
    "level4_mission": "Desafio final: use os 3 resistores e encontre uma solucao eficiente.",
    "level4_tip": "Dica: paralelo com 3.0 V fica perto de 1.83 A.",
    "comp_battery": "Bateria",
    "comp_battery_piece": "Bateria\nV variavel",
    "missing_battery": "Falta colocar a bateria.",
    "missing_resistors": "Faltam {count} resistor(es).",
    "required_mode": "Este nivel exige modo {mode}.",
    "overcurrent": "Corrente excessiva: risco de curto.",
    "overheat": "Superaquecimento: baixe a tensao ou mude a resistencia.",
    "win_msg": "Circuito estavel. Objetivo alcancado.",
    "not_target": "A leitura ainda nao coincide com a meta.",
    "piece_placed": "Componente colocado. Agora voce pode simular.",
    "drop_zone": "Solte a peca dentro de uma zona do tabuleiro.",
    "score_msg": "{message} Pontuacao: {score}/100 ({stars} estrelas).",
    "voltage_reading": "Tensao",
    "total_current": "Corrente",
    "temps": "Temperaturas",
    "branches": "Ramos",
    "power": "Potencia",
    "best_score": "Melhor pontuacao",
    "no_score": "--",
    "low_current": "A corrente esta baixa. Aumente a tensao ou reduza a resistencia total.",
    "high_current": "A corrente esta alta. Baixe a tensao ou aumente a resistencia total.",
    "hot_but_works": "Funciona, mas esta quente. Explique P = I²R.",
    "lab_ready": "Laboratorio pronto. Monte um circuito e pressione Analisar.",
    "analyze": "Analisar",
    "clear": "Limpar",
    "instruments": "Instrumentos",
    "source_voltage": "Tensao da fonte",
    "lab_title": "Laboratorio Sandbox",
    "lab_mission": "Sandbox livre: monte, mude tensao, alterne serie/paralelo e compare leituras.",
    "lab_tip": "Use este modo para explicar que um circuito precisa ser medivel e seguro, nao so ligar.",
    "lab_no_battery": "Coloque a bateria para ativar as leituras.",
    "lab_no_resistor": "Adicione pelo menos um resistor para fechar o circuito.",
    "lab_danger_current": "Risco alto: corrente excessiva. Baixe a tensao ou aumente a resistencia.",
    "lab_danger_temp": "Risco alto: temperatura critica. O circuito nao e seguro.",
    "lab_warn": "Risco medio: funciona, mas e melhor reduzir a potencia.",
    "lab_stable": "Sistema estavel: bom ponto para explicar medicoes.",
    "risk_waiting": "Sem leitura",
    "risk_stable": "Baixo",
    "risk_warn": "Medio",
    "risk_danger": "Alto",
    "lab_intro": "[b]Modo Laboratorio[/b]\nExperimente sem niveis. Mude conexoes e observe corrente, resistencia, temperatura e potencia.\n\n[b]Testes sugeridos[/b]\n- Compare serie vs paralelo.\n- Aumente a tensao aos poucos.\n- Encontre um circuito estavel.\n- Explique por que aparece calor.",
    "lab_instruments": "[b]Instrumentos[/b]\nVoltimetro: mede V\nAmperimetro: mede I\nOhmetro virtual: calcula Rtotal\nTermometro: estima aquecimento",
    "lab_live": "Leituras ao vivo",
    "mode_label": "Modo",
    "branch_currents": "Corrente por ramos",
    "total_power": "Potencia total",
    "risk": "Risco",
    "lab_interpretation": "[b]Interpretacao[/b]\nMais tensao aumenta a corrente.\nMais resistencia reduz a corrente.\nMais potencia geralmente significa mais calor.",
    "lab_series_tip": "Em serie, adicionar resistencia ajuda a controlar a corrente.",
    "lab_parallel_tip": "Em paralelo, Rtotal diminui e a corrente total aumenta: ideal para comparar ramos.",
    "credits_boot": "Carregando creditos...",
    "credits_error": "ERROR: excesso de talento detectado",
    "credits_log": "diagnostico: 12 cabos, 1 cerebro, 0 orcamento\nresultado: surpreendentemente apresentavel",
    "credits_warning_title": "Este jogo pode conter:",
    "credits_warning_body": "logica duvidosa\nmatematica suspeita\ndecisoes questionaveis\n\nSe funciona, nao pergunte por que\n(a programadora tambem nao sabe)\n\nTempo trabalhando:\nmais que o necessario\n\nTempo enrolando:\ntambem muito\n\nequilibrio perfeito XD",
    "credits_tina_name": "autora principal: Tina",
    "credits_tina_stats": "Programacao: 100%\nPesquisa: 100%\nDesign: 100%\nSono: 0%\nPaciencia: variavel\n\nNivel de 'eu consigo': perigoso\nQuantidade de canvas usado: sim",
    "credits_people_title": "CREDITOS OFICIALMENTE SERIOS",
    "credits_design_title": "DESIGN",
    "credits_design_body": "design: tambem Tina XD\n\nfoi muito ezzzfuerzo porque a maioria das coisas foi feita em canvas\n(e ate um simples circulo precisa ser programado)\n\nCriatividade: 80%\nInspiracao: 9999999999999%\nImprovisacao: 100%",
    "credits_measure_title": "MEDICOES 100% CIENTIFICAS",
    "credits_measure_body": "Tensao de criatividade: instavel mas poderosa\nResistencia ao sono: quase zero\nCorrente de ideias: perigosa\nAmperagem de improviso: nao medivel\n\nDiagnostico final:\nse liga, apresenta.",
    "credits_thanks_title": "OBRIGADA",
    "credits_thanks_body": "este foi um jogo feito com pouco orcamento\nmas com dedicacao\n\nobrigada por nao dormir\n\nse riram, fazia parte do plano\nse aprenderam circuitos, tambem fazia parte\nse explodiu algo... isso nao estava no plano XD",
    "credits_patch_title": "PATCH NOTES DO PROJETO",
    "credits_patch_body": "v1.0 - edicao feira de ciencias\n\n- Foi adicionada eletricidade para parecer serio\n- O panico foi reduzido em 3%\n- Bug conhecido: se funciona, nao toque\n- Balanceamento: Tina fez demais e o cafe fez o resto\n- Modo professor: sorrir e concordar com sabedoria",
    "credits_solo_title": "MODO UMA PESSOA",
    "credits_solo_body": "uma mente\nmuitos cabos\nbotoes demais\n\nequipe detectada:\nTina\n\nestado do projeto:\ncontra todas as probabilidades, segue vivo",
    "credits_report_title": "RELATORIO TECNICO",
    "credits_report_body": "Hipotese:\npodemos terminar o jogo antes que acabe nossa paciencia\n\nResultado:\nsim, mas a que custo XD\n\nConclusao:\nOhm ficaria orgulhoso... provavelmente",
    "credits_teacher_title": "MODO PROFESSOR",
    "credits_teacher_body": "Se o professor disser: 'muito criativo'\ntraducao: nao entendeu tudo, mas gostou\n\nSe perguntar sobre o codigo:\nresposta oficial: foi uma experiencia de aprendizagem\n\nSe o circuito falhar:\nisso se chama demonstracao de riscos eletricos",
    "missing_asset_msg": "Falta {filename}\nmas o show continua porque existe fe",
})

TXT["gn"].update({
    "level1_name": "Nivel 1",
    "level1_mission": "Emyendy luz emergencia 2 resistencia serie-pe.",
    "level1_tip": "Serie-pe resistencia total ojupi ha corriente oguejy.",
    "level2_name": "Nivel 2",
    "level2_mission": "Emongaru mokoi rama paralelo-pe ani haku eterei.",
    "level2_tip": "Paralelo-pe cada rama oguereko voltaje peteĩcha.",
    "level3_name": "Nivel 3",
    "level3_mission": "Eprotege sensor delicado 3 resistencia serie-pe.",
    "level3_tip": "Resistencia hetave oprotege sensor.",
    "level4_name": "Nivel 4",
    "level4_mission": "Reto paha: eipuru 3 resistencia ha ejuhu solucion eficiente.",
    "level4_tip": "Pista: paralelo 3.0 V rehe og̃uahẽ 1.83 A rupi.",
    "comp_battery": "Bateria",
    "comp_battery_piece": "Bateria\nV variable",
    "missing_battery": "Falta bateria.",
    "missing_resistors": "Falta {count} resistencia.",
    "required_mode": "Ko nivel oikotevẽ modo {mode}.",
    "overcurrent": "Corriente hetaiterei: riesgo corto.",
    "overheat": "Haku eterei: emboguejy voltaje térã emoambue resistencia.",
    "win_msg": "Circuito estable. Meta ojehupyty.",
    "not_target": "Lectura ne'ĩra og̃uahẽ meta-pe.",
    "piece_placed": "Componente oñemoĩma. Ikatu resimula.",
    "drop_zone": "Epoi pieza tablero zona ryepýpe.",
    "score_msg": "{message} Puntaje: {score}/100 ({stars} estrella).",
    "voltage_reading": "Voltaje",
    "total_current": "Corriente",
    "temps": "Temperatura",
    "branches": "Rama",
    "power": "Potencia",
    "best_score": "Puntaje iporãvéva",
    "no_score": "--",
    "low_current": "Corriente oguejy. Embojupi voltaje térã emboguejy resistencia total.",
    "high_current": "Corriente ojupi. Emboguejy voltaje térã embojupi resistencia.",
    "hot_but_works": "Omba'apo, ha katu haku. Eexplica P = I²R.",
    "lab_ready": "Laboratorio listo. Emopu'a circuito ha eity Analizar.",
    "analyze": "Analizar",
    "clear": "Mopotĩ",
    "instruments": "Instrumento",
    "source_voltage": "Fuente voltaje",
    "lab_title": "Laboratorio Sandbox",
    "lab_mission": "Sandbox libre: emopu'a, emoambue voltaje, serie/paralelo ha embojoja medicion.",
    "lab_tip": "Eipuru ko modo rehechauka hag̃ua circuito oikotevẽha medicion ha seguridad.",
    "lab_no_battery": "Emoĩ bateria oñepyrũ hag̃ua lectura.",
    "lab_no_resistor": "Emoĩ por lo menos peteĩ resistencia emboty hag̃ua circuito.",
    "lab_danger_current": "Riesgo yvate: corriente hetaiterei. Emboguejy voltaje térã embojupi resistencia.",
    "lab_danger_temp": "Riesgo yvate: temperatura critica. Circuito ndaha'ei seguro.",
    "lab_warn": "Riesgo medio: omba'apo, pero iporãve emboguejy potencia.",
    "lab_stable": "Sistema estable: iporã explicación medicion-pe.",
    "risk_waiting": "Sin lectura",
    "risk_stable": "Bajo",
    "risk_warn": "Medio",
    "risk_danger": "Alto",
    "lab_intro": "[b]Modo Laboratorio[/b]\nEexperimenta sin niveles. Emoambue conexion ha ehecha corriente, resistencia, temperatura ha potencia.\n\n[b]Prueba sugerida[/b]\n- Embojoja serie vs paralelo.\n- Embojupi voltaje mbeguekatúpe.\n- Ejuhu circuito estable.\n- Eexplica mba'erepa haku.",
    "lab_instruments": "[b]Instrumento[/b]\nVoltimetro: omide V\nAmperimetro: omide I\nOhmetro virtual: okalkula Rtotal\nTermometro: oestima haku",
    "lab_live": "Lectura en vivo",
    "mode_label": "Modo",
    "branch_currents": "Corriente rama-pe",
    "total_power": "Potencia total",
    "risk": "Riesgo",
    "lab_interpretation": "[b]Interpretacion[/b]\nVoltaje hetave ombojupi corriente.\nResistencia hetave omboguejy corriente.\nPotencia hetave ojapo hakuve.",
    "lab_series_tip": "Serie-pe, resistencia hetave ocontrola corriente.",
    "lab_parallel_tip": "Paralelo-pe, Rtotal oguejy ha corriente total ojupi: iporã embojoja hag̃ua rama.",
    "credits_boot": "Ojekarga creditos...",
    "credits_error": "ERROR: talento hetaiterei detectado",
    "credits_log": "diagnostico: 12 cable, 1 cerebro, 0 presupuesto\nresultado: sorprendentemente presentable",
    "credits_warning_title": "Ko juego ikatu oreko:",
    "credits_warning_body": "logica dudosa\nmatematica sospechosa\ndecisiones raras\n\nOmba'aporamo, ani reporandu mba'erepa\n(programadora ndoikuaái avei)\n\nTiempo trabajando:\nhetave necesario-gui\n\nTiempo perdido:\navei heta\n\nequilibrio perfecto XD",
    "credits_tina_name": "autora principal: Tina",
    "credits_tina_stats": "Programacion: 100%\nInvestigacion: 100%\nDiseño: 100%\nSueño: 0%\nPaciencia: variable\n\nNivel 'yo si puedo': peligroso\nCanvas ojepuru: si",
    "credits_people_title": "CREDITOS SERIOSITE",
    "credits_design_title": "DISEÑO",
    "credits_design_body": "diseño: Tina avei XD\n\nheta ezzzfuerzo, la mayoria ojejapo canvas-pe\n(ha circulo simple jepe oñeprograma)\n\nCreatividad: 80%\nInspiracion: 9999999999999%\nImprovisacion: 100%",
    "credits_measure_title": "MEDICION 100% CIENTIFICA",
    "credits_measure_body": "Creatividad voltaje: inestable pero poderoso\nSueño resistencia: casi cero\nIdeas corriente: peligrosa\nImprovisacion amperaje: ndaikatui oñemide\n\nDiagnostico final:\nomyendy ramo, epresenta.",
    "credits_thanks_title": "AGUYJE",
    "credits_thanks_body": "ko juego ojejapo poco presupuesto reheve\npero dedicacion reheve\n\naguyje nderekei haguere\n\npeñepukáramo, upéva plan-pe oĩ\npeaprendéramo circuito, avei\nexplota ramo mba'e... upéva ndaha'ei plan XD",
    "credits_patch_title": "PROYECTO PATCH NOTES",
    "credits_patch_body": "v1.0 - feria de ciencias edition\n\n- Oñemoĩ electricidad ojehecha hag̃ua serio\n- Panico oguejy 3%\n- Bug conocido: omba'apo ramo, ani repoko\n- Balance: Tina ojapo hetaiterei ha cafe ojapo ambue\n- Modo profe: epuka ha emoneĩ sabiduria reheve",
    "credits_solo_title": "MODO PETEĨ PERSONA",
    "credits_solo_body": "peteĩ mente\nheta cable\nboton hetaiterei\n\nequipo detectado:\nTina\n\nestado proyecto:\ncontra todo pronostico, oikove gueteri",
    "credits_report_title": "INFORME TECNICO",
    "credits_report_body": "Hipotesis:\nikatu jajapo juego paciencia opa mboyve\n\nResultado:\nsi, pero mba'e costo XD\n\nConclusion:\nOhm ovy'ane... probablemente",
    "credits_teacher_title": "MODO PROFE",
    "credits_teacher_body": "Profe he'iramo: 'muy creativo'\ntraduccion: ndoentendepái, pero ogusta chupe\n\nOporeguntáramo codigo rehe:\nrespuesta oficial: fue experiencia aprendizaje\n\nCircuito ofalláramo:\nupéva demostracion riesgo electrico",
    "missing_asset_msg": "Falta {filename}\npero show osegi esperanza reheve",
})


def tr(key):
    app = App.get_running_app()
    lang = getattr(app, "lang", "es") if app else "es"
    return TXT.get(lang, TXT["es"]).get(key, TXT["es"].get(key, key))


def trf(key, **kwargs):
    return tr(key).format(**kwargs)


def fit_label(lbl):
    lbl.size_hint_y = None
    lbl.halign = "left"
    lbl.valign = "top"
    lbl.bind(width=lambda s, w: setattr(s, "text_size", (max(w - dp(16), dp(50)), None)))
    lbl.bind(texture_size=lambda s, t: setattr(s, "height", max(t[1] + dp(6), dp(26))))


def heat_color(temp_c):
    if temp_c < 40:
        return (0.18, 0.65, 1.00, 0.55)
    if temp_c < 65:
        return (0.22, 0.90, 0.45, 0.66)
    if temp_c < 85:
        return (1.00, 0.86, 0.22, 0.72)
    if temp_c < 100:
        return (1.00, 0.50, 0.14, 0.80)
    return (1.00, 0.12, 0.10, 0.90)


def current_color(current, target):
    if target <= 0:
        return (0.30, 0.90, 0.50, 0.95)
    diff = abs(current - target)
    if diff <= target * 0.10:
        return (0.26, 0.96, 0.40, 0.95)
    if diff <= target * 0.25:
        return (0.96, 0.82, 0.20, 0.95)
    return (1.00, 0.26, 0.20, 0.95)


def safe_ohms(value):
    return "∞" if isinf(value) else f"{value:.2f} Ω"


def panel(widget, rgba=(0.055, 0.070, 0.105, 0.84), radius=20):
    with widget.canvas.before:
        widget._panel_bg_color = Color(*rgba)
        widget._panel_bg = RoundedRectangle(pos=widget.pos, size=widget.size, radius=[radius])
        widget._panel_border_color = Color(1, 1, 1, 0.14)
        widget._panel_border = Line(rounded_rectangle=(widget.x, widget.y, widget.width, widget.height, radius), width=1.1)

    def redraw(*_):
        widget._panel_bg.pos = widget.pos
        widget._panel_bg.size = widget.size
        widget._panel_border.rounded_rectangle = (widget.x, widget.y, widget.width, widget.height, radius)

    widget.bind(pos=redraw, size=redraw)


class Music:
    def __init__(self):
        self.current = None
        self.current_name = None

    def play(self, filename, loop=True):
        path = asset(filename)
        if not path or self.current_name == filename:
            return
        self.stop()
        try:
            snd = SoundLoader.load(path)
            if snd:
                snd.loop = loop
                snd.volume = 0.55
                snd.play()
                self.current = snd
                self.current_name = filename
        except Exception:
            self.current = None
            self.current_name = None

    def stop(self):
        if self.current:
            try:
                self.current.stop()
            except Exception:
                pass
        self.current = None
        self.current_name = None


class AssetBackground(FloatLayout):
    def __init__(self, filename, **kwargs):
        super().__init__(**kwargs)
        path = asset(filename)
        if path:
            self.add_widget(Image(source=path, allow_stretch=True, keep_ratio=False))
        else:
            self.add_widget(Starfield())


class Starfield(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._redraw, size=self._redraw)

    def _redraw(self, *_):
        self.canvas.clear()
        with self.canvas:
            Color(0.018, 0.024, 0.040, 1)
            Rectangle(pos=self.pos, size=self.size)
            Color(0.06, 0.20, 0.29, 0.45)
            Line(points=[0, self.height * 0.22, self.width, self.height * 0.36], width=2)
            Color(0.16, 0.45, 0.90, 0.18)
            for i in range(34):
                x = (self.width * (i * 37 % 101)) / 101.0
                y = (self.height * (i * 59 % 97)) / 97.0
                s = dp(2 + i % 3)
                Ellipse(pos=(x, y), size=(s, s))


class GlassPanel(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        panel(self)

    def add_widget(self, widget, *args, **kwargs):
        super().add_widget(widget, *args, **kwargs)
        self._fit_child(widget)

    def _fit_child(self, widget):
        widget.pos = self.pos
        widget.size = self.size
        self.bind(pos=lambda *_: setattr(widget, "pos", self.pos))
        self.bind(size=lambda *_: setattr(widget, "size", self.size))


class MenuButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(260), dp(54))
        self.font_size = dp(18)
        self.bold = True
        self.background_color = (0.17, 0.46, 0.86, 1)


class TextScreen(Screen):
    music_file = "musica_menu.mp3"
    title_key = "info"
    body_key = "info_text"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = FloatLayout()
        self.add_widget(self.root)
        self.root.add_widget(AssetBackground("fondo_menu.png"))
        self.card = GlassPanel(size_hint=(None, None), size=(dp(720), dp(420)), pos_hint={"center_x": 0.5, "center_y": 0.52})
        self.root.add_widget(self.card)
        box = BoxLayout(orientation="vertical", spacing=dp(18), padding=dp(34))
        self.card.add_widget(box)
        self.title = Label(font_size=dp(30), bold=True, color=(1, 1, 1, 1), size_hint=(1, None), height=dp(54))
        body_scroll = ScrollView(size_hint=(1, 1), do_scroll_x=False, bar_width=dp(8))
        self.body = Label(font_size=dp(18), color=(0.90, 0.96, 1, 1), markup=True)
        fit_label(self.body)
        body_scroll.add_widget(self.body)
        self.back = MenuButton()
        self.back.bind(on_release=lambda *_: setattr(self.manager, "current", "menu"))
        box.add_widget(self.title)
        box.add_widget(body_scroll)
        box.add_widget(self.back)

    def on_pre_enter(self):
        App.get_running_app().music.play(self.music_file)
        self.update_texts()

    def update_texts(self):
        self.title.text = tr(self.title_key)
        self.body.text = tr(self.body_key)
        self.back.text = tr("back")


class InfoScreen(TextScreen):
    title_key = "info"
    body_key = "info_text"


class ElectricBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phase = 0.0
        self.nodes = []
        self.lines = []
        self.bind(size=self.rebuild, pos=self.rebuild)
        Clock.schedule_interval(self.animate, 1 / 24)

    def rebuild(self, *_):
        self.canvas.clear()
        width, height = self.size
        if width <= 10 or height <= 10:
            return
        rng = random.Random(42)
        self.nodes = [
            (rng.uniform(0.08, 0.92) * width, rng.uniform(0.08, 0.92) * height)
            for _ in range(28)
        ]
        self.lines = []
        for index, point in enumerate(self.nodes):
            for other in self.nodes[index + 1:]:
                distance = math.dist(point, other)
                if dp(70) < distance < dp(190) and rng.random() < 0.16:
                    self.lines.append((point, other))
        self.redraw()

    def animate(self, dt):
        self.phase += dt
        if self.width > 10:
            self.redraw()

    def redraw(self):
        self.canvas.clear()
        pulse = 0.55 + 0.35 * math.sin(self.phase * 2.4)
        with self.canvas:
            Color(0.015, 0.02, 0.025, 1)
            Rectangle(pos=self.pos, size=self.size)
            Color(0.0, 0.36 + pulse * 0.12, 0.2, 0.22)
            grid = dp(42)
            x = self.x
            while x < self.right:
                Line(points=[x, self.y, x, self.top], width=1)
                x += grid
            y = self.y
            while y < self.top:
                Line(points=[self.x, y, self.right, y], width=1)
                y += grid
            Color(0.0, 0.95, 0.45, 0.45 + pulse * 0.25)
            for start, end in self.lines:
                sx, sy = start
                ex, ey = end
                Line(points=[sx, sy, ex, sy, ex, ey], width=1.35)
            for number, (nx, ny) in enumerate(self.nodes):
                hot = 0.65 + 0.35 * math.sin(self.phase * 3.3 + number)
                Color(0.1, 1.0, 0.55, 0.45 + hot * 0.35)
                Ellipse(pos=(nx - dp(3), ny - dp(3)), size=(dp(6), dp(6)))


class SparkLayer(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sparks = []
        self._spawn_timer = 0
        Clock.schedule_interval(self.animate, 1 / 30)

    def spawn_burst(self, x=None, y=None, amount=18):
        if self.width <= 10 or self.height <= 10:
            return
        x = x if x is not None else random.uniform(self.x + dp(60), self.right - dp(60))
        y = y if y is not None else random.uniform(self.y + dp(60), self.top - dp(60))
        for _ in range(amount):
            angle = random.uniform(0, math.tau)
            speed = random.uniform(dp(35), dp(180))
            life = random.uniform(0.45, 0.9)
            self.sparks.append({
                "x": x,
                "y": y,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,
                "life": life,
                "max_life": life,
            })

    def animate(self, dt):
        self._spawn_timer += dt
        if self._spawn_timer > 1.15:
            self._spawn_timer = 0
            self.spawn_burst(amount=random.randint(5, 10))
        alive = []
        for spark in self.sparks:
            spark["life"] -= dt
            spark["x"] += spark["vx"] * dt
            spark["y"] += spark["vy"] * dt
            spark["vy"] -= dp(70) * dt
            if spark["life"] > 0:
                alive.append(spark)
        self.sparks = alive[-120:]
        self.redraw()

    def redraw(self):
        self.canvas.clear()
        with self.canvas:
            for spark in self.sparks:
                alpha = max(0, spark["life"] / spark["max_life"])
                Color(0.15, 1.0, 0.58, alpha)
                Line(
                    points=[
                        spark["x"],
                        spark["y"],
                        spark["x"] - spark["vx"] * 0.035,
                        spark["y"] - spark["vy"] * 0.035,
                    ],
                    width=dp(1.25),
                )


class ScanlineOverlay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phase = 0
        self.bind(size=self.redraw, pos=self.redraw)
        Clock.schedule_interval(self.animate, 1 / 12)

    def animate(self, dt):
        self.phase += dt
        self.redraw()

    def redraw(self, *_):
        self.canvas.clear()
        if self.width <= 10:
            return
        with self.canvas:
            step = dp(7)
            y = self.y + (self.phase * 24) % step
            while y < self.top:
                Color(0.0, 0.0, 0.0, 0.12)
                Line(points=[self.x, y, self.right, y], width=1)
                y += step


class CanvasProgressBar(Widget):
    progress = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.redraw, size=self.redraw, progress=self.redraw)

    def redraw(self, *_):
        self.canvas.clear()
        width, height = self.size
        fill_width = max(0, min(width, width * self.progress))
        with self.canvas:
            Color(0.02, 0.08, 0.04, 1)
            Rectangle(pos=self.pos, size=self.size)
            Color(0.0, 1.0, 0.42, 1)
            Rectangle(pos=self.pos, size=(fill_width, height))
            Color(0.65, 1.0, 0.78, 1)
            Line(rectangle=(self.x, self.y, width, height), width=dp(2))


class TypewriterLabel(Label):
    def __init__(self, speed=0.018, **kwargs):
        super().__init__(**kwargs)
        self.full_text = ""
        self.speed = speed
        self._index = 0
        self._event = None
        self._on_done = None

    def start(self, text, on_done=None):
        self.stop()
        self.text = ""
        self.full_text = text
        self._index = 0
        self._on_done = on_done
        self._event = Clock.schedule_interval(self._tick, self.speed)

    def stop(self):
        if self._event is not None:
            self._event.cancel()
            self._event = None

    def finish_now(self):
        self.stop()
        self.text = self.full_text
        if self._on_done is not None:
            callback = self._on_done
            self._on_done = None
            callback()

    def _tick(self, _dt):
        if self._index >= len(self.full_text):
            self.finish_now()
            return False
        jump = 2 if self.full_text[self._index] not in "\n " else 1
        self._index = min(len(self.full_text), self._index + jump)
        self.text = self.full_text[: self._index]
        return True


class MissingAsset(AnchorLayout):
    def __init__(self, filename, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.08, 0.13, 0.09, 0.92)
            self.bg = Rectangle(pos=self.pos, size=self.size)
            Color(0.0, 1.0, 0.42, 0.8)
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=dp(2))
        self.bind(pos=self._sync, size=self._sync)
        label = Label(
            text=trf("missing_asset_msg", filename=filename),
            color=(0.75, 1.0, 0.82, 1),
            halign="center",
            valign="middle",
            font_size=sp(18),
        )
        label.bind(size=lambda s, _: setattr(s, "text_size", s.size))
        self.add_widget(label)

    def _sync(self, *_):
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.border.rectangle = (self.x, self.y, self.width, self.height)


def credit_image(filename, **kwargs):
    path = asset_path(filename)
    if os.path.exists(path):
        return Image(source=path, allow_stretch=True, keep_ratio=True, **kwargs)
    return MissingAsset(filename, **kwargs)


class CircuitMeter(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phase = 0
        self.bind(size=self.redraw, pos=self.redraw)
        Clock.schedule_interval(self.animate, 1 / 24)

    def animate(self, dt):
        self.phase += dt
        self.redraw()

    def redraw(self, *_):
        self.canvas.clear()
        if self.width <= 10 or self.height <= 10:
            return
        left = self.x + dp(22)
        bottom = self.y + dp(22)
        width = self.width - dp(44)
        height = self.height - dp(44)
        wave_y = bottom + height * 0.62
        wave_h = height * 0.18
        with self.canvas:
            Color(0.015, 0.045, 0.028, 0.94)
            Rectangle(pos=self.pos, size=self.size)
            Color(0.0, 1.0, 0.42, 0.85)
            Line(rectangle=(self.x, self.y, self.width, self.height), width=dp(2))
            Color(0.0, 0.45, 0.22, 0.55)
            for i in range(7):
                x = left + width * i / 6
                Line(points=[x, bottom, x, bottom + height], width=1)
            for i in range(5):
                y = bottom + height * i / 4
                Line(points=[left, y, left + width, y], width=1)
            points = []
            for i in range(90):
                ratio = i / 89
                x = left + width * ratio
                y = wave_y + math.sin(ratio * math.tau * 3.0 + self.phase * 3.2) * wave_h
                y += math.sin(ratio * math.tau * 8.0 + self.phase * 1.8) * dp(6)
                points.extend([x, y])
            Color(0.2, 1.0, 0.55, 1)
            Line(points=points, width=dp(2))
            bars = [0.92, 0.08 + 0.04 * math.sin(self.phase * 2), 0.48 + 0.24 * math.sin(self.phase * 1.4), 0.98]
            bar_top = bottom + height * 0.38
            for index, value in enumerate(bars):
                y = bar_top - index * dp(32)
                Color(0.03, 0.13, 0.07, 1)
                Rectangle(pos=(left, y), size=(width * 0.72, dp(16)))
                Color(0.0, 1.0, 0.42, 0.95)
                Rectangle(pos=(left, y), size=(width * 0.72 * value, dp(16)))
                Color(0.68, 1.0, 0.78, 0.9)
                Line(rectangle=(left, y, width * 0.72, dp(16)), width=1)
            center = (left + width * 0.86, bottom + height * 0.22)
            radius = min(width, height) * 0.12
            Color(0.03, 0.13, 0.07, 1)
            Ellipse(pos=(center[0] - radius, center[1] - radius), size=(radius * 2, radius * 2))
            Color(0.0, 1.0, 0.42, 0.9)
            Line(circle=(center[0], center[1], radius), width=dp(2))
            angle = -140 + (100 + 35 * math.sin(self.phase * 2.8))
            tip_x = center[0] + math.cos(math.radians(angle)) * radius * 0.82
            tip_y = center[1] + math.sin(math.radians(angle)) * radius * 0.82
            Line(points=[center[0], center[1], tip_x, tip_y], width=dp(2))


class SlidingAsset(FloatLayout):
    x_ratio = NumericProperty(0)

    def __init__(self, filename, width_ratio=0.38, height_ratio=0.62, center_y=0.46, **kwargs):
        super().__init__(size_hint=(None, None), **kwargs)
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio
        self.center_y_ratio = center_y
        self.add_widget(credit_image(filename, size_hint=(1, 1), pos_hint={"x": 0, "y": 0}))
        self.bind(x_ratio=self._sync_to_parent)

    def on_parent(self, _widget, parent):
        if parent is not None:
            parent.bind(size=self._sync_to_parent, pos=self._sync_to_parent)
        self._sync_to_parent()

    def _sync_to_parent(self, *_):
        if not self.parent:
            return
        parent = self.parent
        self.size = (parent.width * self.width_ratio, parent.height * self.height_ratio)
        self.pos = (
            parent.x + parent.width * self.x_ratio,
            parent.y + parent.height * self.center_y_ratio - self.height / 2,
        )


class CreditSceneBase(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = FloatLayout()
        self.background = ElectricBackground(size_hint=(1, 1))
        self.sparks = SparkLayer(size_hint=(1, 1))
        self.scanlines = ScanlineOverlay(size_hint=(1, 1))
        self.root.add_widget(self.background)
        self.root.add_widget(self.sparks)
        self.root.add_widget(self.scanlines)
        self.add_widget(self.root)

    def on_enter(self, *_):
        self._bring_effects_to_front()
        self.sparks.spawn_burst(amount=24)

    def _bring_effects_to_front(self):
        if self.scanlines.parent is self.root:
            self.root.remove_widget(self.scanlines)
            self.root.add_widget(self.scanlines)


class BootCreditScene(CreditSceneBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = Label(text="", color=(0.1, 1.0, 0.45, 1), font_size=sp(42), bold=True, size_hint=(0.92, None), height=dp(70), pos_hint={"center_x": 0.5, "center_y": 0.66})
        self.bar = CanvasProgressBar(size_hint=(0.76, None), height=dp(34), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.percent = Label(text="0%", color=(0.75, 1.0, 0.82, 1), font_size=sp(24), size_hint=(0.8, None), height=dp(40), pos_hint={"center_x": 0.5, "center_y": 0.43})
        self.error = Label(text="", color=(1.0, 0.23, 0.18, 1), font_size=sp(30), bold=True, size_hint=(0.9, None), height=dp(80), pos_hint={"center_x": 0.5, "center_y": 0.31})
        self.log = TypewriterLabel(speed=0.018, text="", color=(0.75, 1.0, 0.82, 1), font_size=sp(18), halign="center", valign="middle", size_hint=(0.88, None), height=dp(80), pos_hint={"center_x": 0.5, "center_y": 0.19})
        self.log.bind(size=lambda label, value: setattr(label, "text_size", value))
        for widget in (self.title, self.bar, self.percent, self.error, self.log):
            self.root.add_widget(widget)
        self._percent_event = None
        self._error_event = None
        self._log_event = None

    def on_enter(self, *_):
        super().on_enter()
        self.title.text = tr("credits_boot")
        self.bar.progress = 0
        self.percent.text = "0%"
        self.error.text = ""
        self.log.text = ""
        Animation(progress=1, duration=5.5, t="out_quad").start(self.bar)
        self._percent_event = Clock.schedule_interval(self.update_percent, 0.05)
        self._error_event = Clock.schedule_once(self.show_error, 6.0)
        self._log_event = Clock.schedule_once(self.show_log, 7.2)

    def on_leave(self, *_):
        self.log.stop()
        for event in (self._percent_event, self._error_event, self._log_event):
            if event is not None:
                event.cancel()
        self._percent_event = None
        self._error_event = None
        self._log_event = None

    def update_percent(self, _dt):
        percent = int(self.bar.progress * 100)
        blocks = "#" * max(1, int(percent / 9.1))
        self.percent.text = f"{blocks} {percent}%"
        return percent < 100

    def show_error(self, _dt):
        self.error.text = tr("credits_error")
        boom = Animation(font_size=sp(36), duration=0.18) + Animation(font_size=sp(30), duration=0.18)
        boom.start(self.error)
        self.sparks.spawn_burst(self.center_x, self.center_y, amount=42)

    def show_log(self, _dt):
        self.log.start(tr("credits_log"))


class TextCreditScene(CreditSceneBase):
    title_text = ""
    body_text = ""
    title_key = ""
    body_key = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = Label(text="", color=(0.08, 1.0, 0.43, 1), font_size=sp(36), bold=True, halign="center", valign="middle", size_hint=(0.92, None), height=dp(80), pos_hint={"center_x": 0.5, "top": 0.91})
        self.body = TypewriterLabel(speed=0.015, text="", color=(0.9, 1.0, 0.9, 1), font_size=sp(26), halign="center", valign="top", size_hint=(0.86, 0.68), pos_hint={"center_x": 0.5, "top": 0.76})
        self.body.bind(size=lambda label, value: setattr(label, "text_size", value))
        self.root.add_widget(self.title)
        self.root.add_widget(self.body)

    def on_enter(self, *_):
        super().on_enter()
        self.title.text = tr(self.title_key) if self.title_key else self.title_text
        body_text = tr(self.body_key) if self.body_key else self.body_text
        self.body.start(body_text)

    def on_leave(self, *_):
        self.body.stop()


class WarningScene(TextCreditScene):
    title_key = "credits_warning_title"
    body_key = "credits_warning_body"


class PersonScene(CreditSceneBase):
    def __init__(self, name_text="", stats_text="", image_file="", name_key="", stats_key="", **kwargs):
        super().__init__(**kwargs)
        self.name_text = name_text
        self.stats_text = stats_text
        self.name_key = name_key
        self.stats_key = stats_key
        self.image_file = image_file
        self.title = Label(text="", color=(0.08, 1.0, 0.43, 1), font_size=sp(32), bold=True, size_hint=(0.94, None), height=dp(70), pos_hint={"center_x": 0.5, "top": 0.94})
        self.portrait = credit_image(image_file, size_hint=(0.34, 0.58), pos_hint={"x": 0.08, "center_y": 0.48})
        self.body = TypewriterLabel(speed=0.014, text="", color=(0.92, 1.0, 0.92, 1), font_size=sp(28), halign="left", valign="middle", size_hint=(0.48, 0.58), pos_hint={"x": 0.48, "center_y": 0.48})
        self.body.bind(size=lambda label, value: setattr(label, "text_size", value))
        self.root.add_widget(self.title)
        self.root.add_widget(self.portrait)
        self.root.add_widget(self.body)

    def on_enter(self, *_):
        super().on_enter()
        self.title.text = tr("credits_people_title")
        self.portrait.opacity = 0
        Animation(opacity=1, duration=0.7, t="out_quad").start(self.portrait)
        name_text = tr(self.name_key) if self.name_key else self.name_text
        stats_text = tr(self.stats_key) if self.stats_key else self.stats_text
        self.body.start(f"{name_text}\n\n{stats_text}")

    def on_leave(self, *_):
        self.body.stop()


class DesignScene(CreditSceneBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = Label(text="", color=(0.08, 1.0, 0.43, 1), font_size=sp(42), bold=True, size_hint=(0.9, None), height=dp(80), pos_hint={"center_x": 0.5, "top": 0.94})
        self.design = SlidingAsset("diseno.png", width_ratio=0.38, height_ratio=0.62, center_y=0.46)
        self.body = TypewriterLabel(speed=0.013, color=(0.92, 1.0, 0.92, 1), font_size=sp(24), halign="left", valign="middle", size_hint=(0.47, 0.65), pos_hint={"x": 0.49, "center_y": 0.46})
        self.body.bind(size=lambda label, value: setattr(label, "text_size", value))
        self.root.add_widget(self.title)
        self.root.add_widget(self.design)
        self.root.add_widget(self.body)

    def on_enter(self, *_):
        super().on_enter()
        self.title.text = tr("credits_design_title")
        self.design.x_ratio = -0.45
        Animation(x_ratio=0.07, duration=1.15, t="out_back").start(self.design)
        self.body.start(tr("credits_design_body"))

    def on_leave(self, *_):
        self.body.stop()


class MeasurementScene(CreditSceneBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = Label(text="", color=(0.08, 1.0, 0.43, 1), font_size=sp(34), bold=True, size_hint=(0.94, None), height=dp(70), pos_hint={"center_x": 0.5, "top": 0.94})
        self.meter = CircuitMeter(size_hint=(0.46, 0.56), pos_hint={"x": 0.07, "center_y": 0.46})
        self.body = TypewriterLabel(speed=0.013, color=(0.92, 1.0, 0.92, 1), font_size=sp(24), halign="left", valign="middle", size_hint=(0.38, 0.58), pos_hint={"x": 0.58, "center_y": 0.46})
        self.body.bind(size=lambda label, value: setattr(label, "text_size", value))
        self.root.add_widget(self.title)
        self.root.add_widget(self.meter)
        self.root.add_widget(self.body)

    def on_enter(self, *_):
        super().on_enter()
        self.title.text = tr("credits_measure_title")
        self.meter.opacity = 0
        Animation(opacity=1, duration=0.8, t="out_quad").start(self.meter)
        self.body.start(tr("credits_measure_body"))

    def on_leave(self, *_):
        self.body.stop()


class ThanksScene(TextCreditScene):
    title_key = "credits_thanks_title"
    body_key = "credits_thanks_body"


class PatchNotesScene(TextCreditScene):
    title_key = "credits_patch_title"
    body_key = "credits_patch_body"


class SoloBuildScene(TextCreditScene):
    title_key = "credits_solo_title"
    body_key = "credits_solo_body"


class LabReportScene(TextCreditScene):
    title_key = "credits_report_title"
    body_key = "credits_report_body"


class TeacherModeScene(TextCreditScene):
    title_key = "credits_teacher_title"
    body_key = "credits_teacher_body"


class CreditsDeckManager(ScreenManager):
    def __init__(self, owner, **kwargs):
        super().__init__(**kwargs)
        self.owner = owner

    def on_touch_down(self, touch):
        self.owner.next_credit_screen()
        return True


class CreditsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deck = CreditsDeckManager(self, transition=FadeTransition(duration=0.65))
        self.add_widget(self.deck)
        self.deck.add_widget(BootCreditScene(name="boot"))
        self.deck.add_widget(WarningScene(name="warning"))
        self.deck.add_widget(PersonScene(name="tina", image_file="tina.png", name_key="credits_tina_name", stats_key="credits_tina_stats"))
        self.deck.add_widget(DesignScene(name="design"))
        self.deck.add_widget(MeasurementScene(name="measurements"))
        self.deck.add_widget(PatchNotesScene(name="patch_notes"))
        self.deck.add_widget(SoloBuildScene(name="solo_build"))
        self.deck.add_widget(LabReportScene(name="lab_report"))
        self.deck.add_widget(TeacherModeScene(name="teacher_mode"))
        self.deck.add_widget(ThanksScene(name="thanks"))

    def on_pre_enter(self):
        App.get_running_app().music.play("musica_creditos.mp3", loop=False)
        self.deck.current = "boot"
        Window.bind(on_key_down=self._advance_from_key)

    def on_leave(self):
        Window.unbind(on_key_down=self._advance_from_key)

    def _advance_from_key(self, *_):
        self.next_credit_screen()
        return True

    def next_credit_screen(self):
        names = self.deck.screen_names
        current_index = names.index(self.deck.current)
        current = self.deck.get_screen(self.deck.current)
        if isinstance(current, TextCreditScene):
            current.body.finish_now()
        if current_index >= len(names) - 1:
            self.manager.current = "menu"
            return
        self.deck.current = names[current_index + 1]


class LanguageScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = FloatLayout()
        self.add_widget(root)
        root.add_widget(AssetBackground("fondo_menu.png"))
        self.title = Label(font_size=dp(30), bold=True, color=(1, 1, 1, 1), pos_hint={"center_x": 0.5, "top": 0.88}, size_hint=(1, None), height=dp(60))
        root.add_widget(self.title)
        box = BoxLayout(orientation="vertical", spacing=dp(14), size_hint=(None, None), size=(dp(280), dp(330)), pos_hint={"center_x": 0.5, "center_y": 0.50})
        root.add_widget(box)
        for code, label in [("es", "Español"), ("en", "English"), ("pt", "Português"), ("gn", "Guarani")]:
            btn = MenuButton(text=label)
            btn.bind(on_release=lambda _, c=code: self.set_language(c))
            box.add_widget(btn)
        self.back = MenuButton()
        self.back.bind(on_release=lambda *_: setattr(self.manager, "current", "menu"))
        box.add_widget(self.back)

    def on_pre_enter(self):
        App.get_running_app().music.play("musica_menu.mp3")
        self.update_texts()

    def update_texts(self):
        self.title.text = tr("language")
        self.back.text = tr("back")

    def set_language(self, code):
        App.get_running_app().lang = code
        for screen in self.manager.screens:
            if hasattr(screen, "update_texts"):
                screen.update_texts()
        self.manager.current = "menu"


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = FloatLayout()
        self.add_widget(root)
        root.add_widget(AssetBackground("fondo_menu.png"))

        logo_path = asset("logo.png")
        if logo_path:
            logo = Image(source=logo_path, allow_stretch=True, keep_ratio=True, size_hint=(None, None), size=(dp(330), dp(170)), pos_hint={"center_x": 0.5, "top": 0.96})
            root.add_widget(logo)

        self.title = Label(markup=True, font_size=dp(34), color=(1, 1, 1, 1), pos_hint={"center_x": 0.5, "center_y": 0.70})
        self.subtitle = Label(font_size=dp(17), color=(0.86, 0.93, 1.0, 1), pos_hint={"center_x": 0.5, "center_y": 0.61}, halign="center")
        self.subtitle.bind(size=lambda s, _: setattr(s, "text_size", (min(Window.width * 0.84, dp(780)), None)))
        root.add_widget(self.title)
        root.add_widget(self.subtitle)

        self.buttons = {}
        btn_box = BoxLayout(orientation="vertical", spacing=dp(12), size_hint=(None, None), size=(dp(280), dp(330)), pos_hint={"center_x": 0.5, "center_y": 0.36})
        root.add_widget(btn_box)
        for key, screen_name in [
            ("play", "juego"),
            ("quiz", "quiz"),
            ("info", "info"),
            ("credits", "creditos"),
            ("language", "idioma"),
        ]:
            btn = MenuButton()
            btn.bind(on_release=lambda _, s=screen_name: self.go(s))
            self.buttons[key] = btn
            btn_box.add_widget(btn)

    def on_pre_enter(self):
        App.get_running_app().music.play("musica_menu.mp3")
        self.update_texts()

    def go(self, screen_name):
        if screen_name == "juego":
            game = self.manager.get_screen("juego")
            game.story_mode = False
            game.start_level(0)
        self.manager.current = screen_name

    def update_texts(self):
        self.title.text = f"[b]{tr('title')}[/b]"
        self.subtitle.text = tr("subtitle")
        for key, btn in self.buttons.items():
            btn.text = tr(key)


class ComponentIcon(Widget):
    def __init__(self, kind, **kwargs):
        super().__init__(**kwargs)
        self.kind = kind
        self.bind(pos=self._redraw, size=self._redraw)

    def _redraw(self, *_):
        self.canvas.clear()
        x, y = self.pos
        w, h = self.size
        cx, cy = self.center
        with self.canvas:
            if self.kind == "battery":
                Color(0.12, 0.20, 0.28, 1)
                RoundedRectangle(pos=(x + w * 0.25, y + h * 0.10), size=(w * 0.50, h * 0.78), radius=[10])
                Color(0.25, 0.75, 1.0, 1)
                Rectangle(pos=(x + w * 0.36, y + h * 0.88), size=(w * 0.28, h * 0.08))
                Color(1, 1, 1, 0.95)
                Line(points=[cx - w * 0.12, cy, cx + w * 0.12, cy], width=2.0)
                Line(points=[cx, cy - h * 0.10, cx, cy + h * 0.10], width=2.0)
            else:
                Color(0.95, 0.76, 0.28, 1)
                RoundedRectangle(pos=(x + w * 0.22, y + h * 0.34), size=(w * 0.56, h * 0.28), radius=[12])
                Color(0.10, 0.12, 0.16, 1)
                for offset in (0.33, 0.47, 0.61):
                    Line(points=[x + w * offset, y + h * 0.35, x + w * (offset + 0.05), y + h * 0.61], width=2)
                Color(0.85, 0.95, 1.00, 0.95)
                Line(points=[x + w * 0.06, cy, x + w * 0.22, cy], width=2.0)
                Line(points=[x + w * 0.78, cy, x + w * 0.94, cy], width=2.0)


class DragPiece(Scatter):
    def __init__(self, game, kind, label_text, value=None, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.kind = kind
        self.value = value
        self.do_rotation = False
        self.do_scale = False
        self.auto_bring_to_front = True
        self.size_hint = (None, None)
        self.size = (dp(92), dp(112))
        self.home_pos = (0, 0)
        self.current_slot = None
        self._dragging = False

        self.card = BoxLayout(orientation="vertical", spacing=dp(2), padding=dp(5))
        panel(self.card, rgba=(0.10, 0.13, 0.20, 0.92), radius=16)
        battery_path = asset("battery.png")
        if kind == "battery" and battery_path:
            icon = Image(source=battery_path, allow_stretch=True, keep_ratio=True, size_hint=(1, 0.70))
        else:
            icon = ComponentIcon(kind, size_hint=(1, 0.70))
        self.lbl = Label(text=label_text, font_size=dp(13), bold=True, color=(1, 1, 1, 1), size_hint=(1, 0.30), halign="center", valign="middle")
        self.lbl.bind(size=lambda s, _: setattr(s, "text_size", (s.width, None)))
        self.card.add_widget(icon)
        self.card.add_widget(self.lbl)
        self.add_widget(self.card)

    def return_home(self):
        Animation.cancel_all(self)
        self.pos = self.home_pos

    def pulse(self, color=(0.25, 0.90, 1.0, 1)):
        self.card._panel_border_color.rgba = color
        Animation(rgba=(1, 1, 1, 0.14), duration=0.35).start(self.card._panel_border_color)

    def on_touch_down(self, touch):
        if self.game.locked:
            return False
        if self.collide_point(*touch.pos):
            self._dragging = True
            self.opacity = 0.92
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.game.locked:
            return False
        result = super().on_touch_up(touch)
        if self._dragging:
            self._dragging = False
            self.opacity = 1.0
            self.game.handle_piece_drop(self)
            return True
        return result


class CircuitSlot(FloatLayout):
    def __init__(self, kind, title, **kwargs):
        super().__init__(**kwargs)
        self.kind = kind
        self.title = title
        self.occupant = None
        self.size_hint = (None, None)
        self.slot_lbl = Label(text=title, font_size=dp(14), bold=True, color=(1, 1, 1, 0.90), halign="center", valign="middle")
        self.slot_lbl.bind(size=lambda s, _: setattr(s, "text_size", (s.width, None)))
        self.add_widget(self.slot_lbl)
        with self.canvas.before:
            self._bg_color = Color(0.12, 0.16, 0.24, 0.36)
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[18])
            self._border_color = Color(1, 1, 1, 0.34)
            self.border = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 18), width=1.4)
        self.bind(pos=self._redraw, size=self._redraw)

    def _redraw(self, *_):
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.border.rounded_rectangle = (self.x, self.y, self.width, self.height, 18)
        self.slot_lbl.pos = self.pos
        self.slot_lbl.size = self.size
        self._bg_color.rgba = (0.13, 0.22, 0.30, 0.66) if self.occupant else (0.12, 0.16, 0.24, 0.36)

    def accepts(self, piece):
        return piece.kind == self.kind


class Confetti(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.particles = []
        self.event = None

    def burst(self, count=360):
        self.particles = []
        colors = [
            (1, 0.18, 0.16, 1),
            (0.22, 0.96, 0.40, 1),
            (0.20, 0.70, 1, 1),
            (1, 0.88, 0.12, 1),
            (0.95, 0.30, 1, 1),
            (1, 0.55, 0.12, 1),
        ]
        for _ in range(count):
            from_bottom = random.random() < 0.38
            if from_bottom:
                x = random.uniform(self.width * 0.15, self.width * 0.85)
                y = random.uniform(-dp(20), self.height * 0.15)
                vx = random.uniform(-260, 260)
                vy = random.uniform(360, 720)
            else:
                x = random.uniform(-self.width * 0.10, self.width * 1.10)
                y = random.uniform(self.height * 0.72, self.height * 1.16)
                vx = random.uniform(-210, 210)
                vy = random.uniform(-360, -80)
            self.particles.append({
                "x": x,
                "y": y,
                "vx": vx,
                "vy": vy,
                "s": random.uniform(dp(5), dp(16)),
                "rot": random.random() * 6.28,
                "color": random.choice(colors),
                "life": random.uniform(2.4, 4.5),
                "shape": random.choice(("rect", "rect", "circle")),
            })
        if self.event:
            self.event.cancel()
        self.event = Clock.schedule_interval(self._update, 1 / 30.0)

    def _update(self, dt):
        alive = []
        for p in self.particles:
            p["life"] -= dt
            p["vy"] -= 520 * dt
            p["vx"] *= 0.992
            p["x"] += p["vx"] * dt
            p["y"] += p["vy"] * dt
            p["rot"] += dt * 10
            if p["life"] > 0 and p["y"] > -80:
                alive.append(p)
        self.particles = alive
        self._draw()
        if not self.particles:
            self.canvas.clear()
            self.event.cancel()
            self.event = None
            return False
        return True

    def _draw(self):
        self.canvas.clear()
        with self.canvas:
            for p in self.particles:
                Color(*p["color"])
                if p["shape"] == "circle":
                    Ellipse(pos=(p["x"], p["y"]), size=(p["s"] * 0.75, p["s"] * 0.75))
                else:
                    Rectangle(pos=(p["x"], p["y"]), size=(p["s"], p["s"] * 0.50))


class BoardPainter(Widget):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.phase = 0.0
        self.warning_flash = 0.0

    def flash_warning(self):
        self.warning_flash = 1.0

    def refresh(self, state):
        game = self.game
        self.canvas.clear()
        if not game.board_rect:
            return
        bx, by, bw, bh = game.board_rect
        with self.canvas:
            Color(0.025, 0.035, 0.055, 0.94)
            RoundedRectangle(pos=(bx, by), size=(bw, bh), radius=[26])
            Color(0.18, 0.55, 0.85, 0.07)
            for i in range(16):
                x = bx + bw * i / 15.0
                Line(points=[x, by, x, by + bh], width=1)
            for i in range(10):
                y = by + bh * i / 9.0
                Line(points=[bx, y, bx + bw, y], width=1)

            for idx, slot in enumerate(game.resistor_slots):
                Color(*heat_color(state["temps_by_slot"][idx]) if slot.occupant else (0.40, 0.42, 0.48, 0.14))
                RoundedRectangle(pos=(slot.x - dp(12), slot.y - dp(12)), size=(slot.width + dp(24), slot.height + dp(24)), radius=[22])

            if state["battery_present"]:
                self._draw_wires(state)
                self._draw_particles(state)
            self._draw_meter(state)
            if game.diagnostic_mode:
                self._draw_diagnostic(state)
            if self.warning_flash > 0:
                Color(1.0, 0.18, 0.12, 0.22 * self.warning_flash)
                RoundedRectangle(pos=(bx, by), size=(bw, bh), radius=[26])

    def _draw_wires(self, state):
        bx, by, bw, bh = self.game.board_rect
        wire = current_color(state["current"], state["target_current"])
        bcx, bcy = self.game.battery_slot.center
        with self.canvas:
            Color(*wire)
            if self.game.mode == "serie":
                centers = [slot.center for slot in self.game.resistor_slots if slot.occupant]
                if centers:
                    points = [bcx, bcy]
                    for cx, cy in centers:
                        points += [cx, cy]
                    points += [bx + bw * 0.88, by + bh * 0.50, bcx, bcy]
                    Line(points=points, width=3.1, joint="round")
            else:
                junction_x = bx + bw * 0.38
                junction_y = by + bh * 0.52
                out_x = bx + bw * 0.84
                Line(points=[bcx, bcy, junction_x, junction_y], width=3.0)
                Line(points=[junction_x, junction_y, out_x, junction_y], width=3.0)
                for slot in self.game.resistor_slots:
                    if slot.occupant:
                        cx, cy = slot.center
                        Line(points=[junction_x, junction_y, cx, cy, out_x, junction_y], width=2.4)

    def _draw_particles(self, state):
        if state["current"] <= 0.01:
            return
        pts = self._particle_path()
        if len(pts) < 2:
            return
        intensity = min(1.0, state["current"] / max(state["target_current"], 0.1))
        radius = dp(3.0 + 2.0 * intensity)
        with self.canvas:
            Color(0.50, 0.95, 1.00, 0.55 + 0.35 * intensity)
            for i in range(10):
                x, y = self._point_on_path(pts, (self.phase + i / 10.0) % 1.0)
                Ellipse(pos=(x - radius, y - radius), size=(radius * 2, radius * 2))

    def _particle_path(self):
        bx, by, bw, bh = self.game.board_rect
        if self.game.mode == "serie":
            pts = [self.game.battery_slot.center]
            pts += [slot.center for slot in self.game.resistor_slots if slot.occupant]
            pts += [(bx + bw * 0.88, by + bh * 0.50), self.game.battery_slot.center]
            return pts
        junction = (bx + bw * 0.38, by + bh * 0.52)
        out = (bx + bw * 0.84, by + bh * 0.52)
        active = [slot.center for slot in self.game.resistor_slots if slot.occupant]
        branch = active[int(self.phase * len(active)) % len(active)] if active else out
        return [self.game.battery_slot.center, junction, branch, out]

    def _point_on_path(self, pts, t):
        lengths, total = [], 0.0
        for a, b in zip(pts, pts[1:]):
            seg = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
            lengths.append(seg)
            total += seg
        target, walked = t * total, 0.0
        for idx, seg in enumerate(lengths):
            if walked + seg >= target:
                local = (target - walked) / max(seg, 0.001)
                a, b = pts[idx], pts[idx + 1]
                return (a[0] + (b[0] - a[0]) * local, a[1] + (b[1] - a[1]) * local)
            walked += seg
        return pts[-1]

    def _draw_meter(self, state):
        bx, by, bw, bh = self.game.board_rect
        x, y = bx + bw * 0.86, by + bh * 0.80
        r = min(bw, bh) * 0.062
        angle = -140 + min(1.0, state["current"] / max(state["max_current"], 0.01)) * 280
        needle = (x + cos(angle * pi / 180.0) * r * 0.75, y + sin(angle * pi / 180.0) * r * 0.75)
        with self.canvas:
            Color(0.02, 0.03, 0.05, 0.92)
            Ellipse(pos=(x - r, y - r), size=(r * 2, r * 2))
            Color(*current_color(state["current"], state["target_current"]))
            Line(circle=(x, y, r), width=2.0)
            Color(1, 1, 1, 0.90)
            Line(points=[x, y, needle[0], needle[1]], width=2.1)
            Ellipse(pos=(x - dp(3), y - dp(3)), size=(dp(6), dp(6)))

    def _draw_diagnostic(self, state):
        bx, by, bw, bh = self.game.board_rect
        with self.canvas:
            Color(0.35, 0.95, 1.00, 0.24)
            Line(rectangle=(bx + dp(20), by + dp(20), bw - dp(40), bh - dp(40)), width=1.5)
            for slot, amps in zip(self.game.resistor_slots, state["branch_currents"]):
                if slot.occupant:
                    Color(0.35, 0.95, 1.00, 0.75)
                    Line(circle=(slot.center_x, slot.center_y, min(slot.width, slot.height) * 0.54), width=1.1)
                    bar_h = min(slot.height * 0.82, dp(8) + amps * dp(18))
                    Color(0.25, 0.95, 0.55, 0.70)
                    RoundedRectangle(pos=(slot.right + dp(8), slot.y), size=(dp(8), bar_h), radius=[4])


class Level:
    def __init__(self, name, mission, objective_current, tolerance, required_mode, required_resistors, max_temp, max_current, start_voltage, tip):
        self.name = name
        self.mission = mission
        self.objective_current = objective_current
        self.tolerance = tolerance
        self.required_mode = required_mode
        self.required_resistors = required_resistors
        self.max_temp = max_temp
        self.max_current = max_current
        self.start_voltage = start_voltage
        self.tip = tip


class GameScreen(Screen):
    background_asset = "fondo_juego.png"
    music_asset = "musica_juego.mp3"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.locked = False
        self.mode = "serie"
        self.level_index = 0
        self.board_rect = None
        self.diagnostic_mode = False
        self.story_mode = False
        self.last_result = tr("build_first")
        self.best_scores = {}
        self.levels = [
            Level("Nivel 1", "Activa una luz de emergencia con 2 resistencias en serie.", 1.00, 0.12, "serie", 2, 85, 2.20, 9.0, "En serie sube la resistencia total y baja la corriente."),
            Level("Nivel 2", "Alimenta dos ramas usando paralelo sin sobrecalentar.", 2.00, 0.18, "paralelo", 2, 90, 3.10, 9.0, "En paralelo cada rama recibe el mismo voltaje."),
            Level("Nivel 3", "Protege un sensor delicado usando 3 resistencias en serie.", 0.75, 0.08, "serie", 3, 80, 1.40, 12.0, "Mas resistencia protege el sensor."),
            Level("Nivel 4", "Reto final: usa las 3 resistencias y encuentra una solucion eficiente.", 1.83, 0.10, "libre", 3, 95, 2.60, 3.0, "Solucion pista: paralelo con 3.0 V queda cerca de 1.83 A."),
        ]

        self.root = FloatLayout()
        self.add_widget(self.root)
        self.root.add_widget(AssetBackground(self.background_asset))
        self.info_left_panel = GlassPanel(size_hint=(None, None))
        self.board_center_panel = GlassPanel(size_hint=(None, None))
        self.controls_right_panel = GlassPanel(size_hint=(None, None))
        self.root.add_widget(self.info_left_panel)
        self.root.add_widget(self.board_center_panel)
        self.root.add_widget(self.controls_right_panel)
        self.board_painter = BoardPainter(self)
        self.root.add_widget(self.board_painter)

        self.level_label = Label(font_size=dp(24), bold=True, color=(1, 1, 1, 1), size_hint=(1, None), height=dp(54), pos_hint={"center_x": 0.5, "top": 0.99})
        self.root.add_widget(self.level_label)
        self.battery_slot = CircuitSlot("battery", "Bateria")
        self.resistor_slots = [CircuitSlot("resistor", f"R{i + 1}") for i in range(3)]
        self.root.add_widget(self.battery_slot)
        for slot in self.resistor_slots:
            self.root.add_widget(slot)
        self.battery_piece = DragPiece(self, "battery", "Bateria\nV variable", value=0.0)
        self.resistor_pieces = [
            DragPiece(self, "resistor", "R1\n3 Ω", value=3.0),
            DragPiece(self, "resistor", "R2\n6 Ω", value=6.0),
            DragPiece(self, "resistor", "R3\n9 Ω", value=9.0),
        ]
        self.root.add_widget(self.battery_piece)
        for piece in self.resistor_pieces:
            self.root.add_widget(piece)

        self._build_left_panel()
        self._build_right_panel()
        self.feedback = Image(allow_stretch=True, keep_ratio=True, opacity=0, size_hint=(None, None), size=(dp(140), dp(140)), pos_hint={"right": 0.98, "top": 0.98})
        self.root.add_widget(self.feedback)
        self.confetti = Confetti()
        self.root.add_widget(self.confetti)
        self.bind(size=lambda *_: self.layout_scene())
        Clock.schedule_once(lambda *_: self.start_level(0), 0)
        Clock.schedule_interval(self.live_update, 1 / 30.0)

    def _build_left_panel(self):
        scroll = ScrollView(size_hint=(1, 1), do_scroll_x=False, bar_width=dp(8))
        self.info_left_panel.add_widget(scroll)
        box = BoxLayout(orientation="vertical", padding=(dp(28), dp(18), dp(12), dp(18)), spacing=dp(15), size_hint_y=None)
        box.bind(minimum_height=box.setter("height"))
        scroll.add_widget(box)
        self.goal_label = Label(font_size=dp(14), color=(0.95, 0.95, 0.95, 1), markup=True)
        self.formula_label = Label(font_size=dp(14), bold=True, color=(0.92, 0.92, 0.92, 1), markup=True)
        self.state_label = Label(font_size=dp(14), color=(0.96, 0.96, 0.96, 1), markup=True)
        self.diagnostic_label = Label(font_size=dp(14), color=(0.70, 0.92, 1.0, 1), markup=True)
        self.score_label = Label(font_size=dp(14), color=(0.96, 0.86, 0.35, 1), markup=True)
        self.hint_label = Label(font_size=dp(14), color=(0.78, 0.90, 1.0, 1), italic=True)
        for lbl in (self.goal_label, self.formula_label, self.state_label, self.diagnostic_label, self.score_label, self.hint_label):
            fit_label(lbl)
            box.add_widget(lbl)

    def _build_right_panel(self):
        right = BoxLayout(orientation="vertical", padding=(dp(26), dp(16), dp(14), dp(14)), spacing=dp(10))
        self.controls_right_panel.add_widget(right)
        right.add_widget(FloatLayout(size_hint=(1, 1)))
        controls = BoxLayout(orientation="vertical", size_hint=(1, None), height=dp(282), spacing=dp(8), padding=(dp(10), 0, dp(6), 0))
        self.voltage_title = Label(font_size=dp(14), bold=True, size_hint=(1, None), height=dp(22), halign="left", valign="middle")
        self.voltage_title.bind(size=lambda s, _: setattr(s, "text_size", (s.width, None)))
        self.voltage_value = Label(text="9.0 V", font_size=dp(19), bold=True, color=(0.82, 0.94, 1, 1), size_hint=(1, None), height=dp(28), halign="left", valign="middle")
        self.voltage_value.bind(size=lambda s, _: setattr(s, "text_size", (s.width, None)))
        self.voltage_slider = Slider(min=3.0, max=15.0, value=9.0, step=0.1, size_hint=(1, None), height=dp(40))
        self.mode_button = Button(size_hint=(1, None), height=dp(46), background_color=(0.18, 0.62, 0.34, 1), font_size=dp(14))
        self.diagnostic_button = Button(size_hint=(1, None), height=dp(46), background_color=(0.20, 0.52, 0.74, 1), font_size=dp(14))
        self.sim_button = Button(size_hint=(1, None), height=dp(50), background_color=(0.20, 0.45, 0.95, 1), font_size=dp(17), bold=True)
        for w in (self.voltage_title, self.voltage_value, self.voltage_slider, self.mode_button, self.diagnostic_button, self.sim_button):
            controls.add_widget(w)
        right.add_widget(controls)
        row = BoxLayout(orientation="horizontal", size_hint=(1, None), height=dp(52), spacing=dp(10), padding=(dp(10), 0, dp(6), 0))
        self.reset_button = Button(background_color=(0.78, 0.32, 0.18, 1))
        self.next_button = Button(background_color=(0.18, 0.45, 0.90, 1), disabled=True)
        row.add_widget(self.reset_button)
        row.add_widget(self.next_button)
        right.add_widget(row)
        self.voltage_slider.bind(value=self.on_voltage_change)
        self.mode_button.bind(on_release=self.toggle_mode)
        self.diagnostic_button.bind(on_release=self.toggle_diagnostic)
        self.sim_button.bind(on_release=lambda *_: self.evaluate_circuit())
        self.reset_button.bind(on_release=lambda *_: self.reset_level())
        self.next_button.bind(on_release=lambda *_: self.on_next_pressed())

    def on_pre_enter(self):
        App.get_running_app().music.play(self.music_asset)
        self.update_texts()

    def update_texts(self):
        self.voltage_title.text = tr("voltage")
        self.sim_button.text = tr("simulate")
        self.reset_button.text = tr("reset")
        self.next_button.text = tr("next")
        self.diagnostic_button.text = tr("normal") if self.diagnostic_mode else tr("diagnostic")
        self.mode_button.text = tr("mode_series") if self.mode == "paralelo" else tr("mode_parallel")
        self.battery_slot.slot_lbl.text = tr("comp_battery")
        self.battery_piece.lbl.text = tr("comp_battery_piece")
        self.refresh_ui()

    def layout_scene(self):
        W, H = self.width, self.height
        if W <= 0 or H <= 0:
            return
        left_w, center_w, right_w = W * 0.24, W * 0.48, W * 0.24
        panel_h, y_pos = H * 0.84, H * 0.055
        left_x, center_x, right_x = W * 0.018, W * 0.26, W * 0.742
        self.info_left_panel.pos, self.info_left_panel.size = (left_x, y_pos), (left_w, panel_h)
        self.board_center_panel.pos, self.board_center_panel.size = (center_x, y_pos), (center_w, panel_h)
        self.controls_right_panel.pos, self.controls_right_panel.size = (right_x, y_pos), (right_w, panel_h)
        self.board_rect = (center_x + dp(12), y_pos + dp(12), center_w - dp(24), panel_h - dp(24))
        self.board_painter.pos, self.board_painter.size = (0, 0), (W, H)
        self.confetti.pos, self.confetti.size = (0, 0), (W, H)
        self._layout_piece_homes(right_x, y_pos, right_w, panel_h)
        self.place_slots()
        self.sync_occupied_pieces()
        self.refresh_ui()

    def _layout_piece_homes(self, right_x, y_pos, right_w, panel_h):
        piece_w = self.battery_piece.width
        piece_h = self.battery_piece.height
        available_w = max(piece_w * 2 + dp(16), right_w - dp(58))
        panel_top = y_pos + panel_h - dp(66)
        col_gap = max(dp(16), available_w - piece_w * 2)
        row_gap = dp(22)
        grid_w = piece_w * 2 + col_gap
        col1 = right_x + max(dp(18), (right_w - grid_w) / 2)
        col2 = col1 + piece_w + col_gap
        row1 = panel_top - piece_h
        row2 = row1 - piece_h - row_gap
        homes = [
            (self.battery_piece, (col1, row1)),
            (self.resistor_pieces[0], (col2, row1)),
            (self.resistor_pieces[1], (col1, row2)),
            (self.resistor_pieces[2], (col2, row2)),
        ]
        for piece, pos in homes:
            piece.home_pos = pos
            if not piece.current_slot and not piece._dragging:
                piece.return_home()

    def place_slots(self):
        if not self.board_rect:
            return
        bx, by, bw, bh = self.board_rect
        self.battery_slot.size = (dp(112), dp(130))
        self.battery_slot.pos = (bx + bw * 0.07, by + bh * 0.40)
        if self.mode == "serie":
            positions = [(bx + bw * 0.32, by + bh * 0.42), (bx + bw * 0.53, by + bh * 0.42), (bx + bw * 0.74, by + bh * 0.42)]
        else:
            positions = [(bx + bw * 0.56, by + bh * 0.63), (bx + bw * 0.56, by + bh * 0.43), (bx + bw * 0.56, by + bh * 0.23)]
        for idx, slot in enumerate(self.resistor_slots):
            slot.size = (dp(102), dp(112))
            slot.pos = positions[idx]

    def sync_occupied_pieces(self):
        for slot in [self.battery_slot] + self.resistor_slots:
            if slot.occupant:
                slot.occupant.center = slot.center

    def start_level(self, index):
        App.get_running_app().music.play(self.music_asset)
        self.level_index = index
        self.locked = False
        self.last_result = tr("build_first")
        level = self.levels[self.level_index]
        self.mode = level.required_mode if level.required_mode in ("serie", "paralelo") else "serie"
        for slot in [self.battery_slot] + self.resistor_slots:
            slot.occupant = None
        for piece in [self.battery_piece] + self.resistor_pieces:
            piece.current_slot = None
            piece.return_home()
        self.feedback.opacity = 0
        self.voltage_slider.value = level.start_voltage
        self.next_button.disabled = True
        self.place_slots()
        self.refresh_ui()

    def reset_level(self):
        self.start_level(self.level_index)

    def handle_piece_drop(self, piece):
        if self.locked:
            piece.return_home()
            return
        if piece.current_slot:
            piece.current_slot.occupant = None
            piece.current_slot = None
        target = None
        for slot in [self.battery_slot] + self.resistor_slots:
            if slot.accepts(piece) and slot.collide_point(*piece.center):
                target = slot
                break
        if target:
            if target.occupant and target.occupant is not piece:
                target.occupant.current_slot = None
                target.occupant.return_home()
            target.occupant = piece
            piece.current_slot = target
            piece.center = target.center
            piece.pulse()
            self.last_result = tr("piece_placed")
        else:
            piece.return_home()
            self.last_result = tr("drop_zone")
        self.refresh_ui()

    def toggle_mode(self, *_):
        if self.locked:
            return
        self.mode = "paralelo" if self.mode == "serie" else "serie"
        self.place_slots()
        self.sync_occupied_pieces()
        self.update_texts()

    def toggle_diagnostic(self, *_):
        self.diagnostic_mode = not self.diagnostic_mode
        self.update_texts()

    def on_voltage_change(self, *_):
        self.voltage_value.text = f"{self.voltage_slider.value:.1f} V"
        self.refresh_ui()

    def compute_state(self):
        level = self.levels[self.level_index]
        battery_present = self.battery_slot.occupant is not None
        values_by_slot = [slot.occupant.value if slot.occupant else None for slot in self.resistor_slots]
        placed = [v for v in values_by_slot if v is not None]
        V = float(self.voltage_slider.value) if battery_present else 0.0
        if not placed:
            R_total = float("inf")
        elif self.mode == "serie":
            R_total = sum(placed)
        else:
            inv = sum(1.0 / r for r in placed if r > 0)
            R_total = 1.0 / inv if inv > 0 else float("inf")
        current = V / R_total if battery_present and not isinf(R_total) and R_total > 0 else 0.0
        temps, branch_currents, powers = [], [], []
        for r in values_by_slot:
            if r is None or not battery_present:
                temps.append(25.0)
                branch_currents.append(0.0)
                powers.append(0.0)
                continue
            if self.mode == "serie":
                branch_i = current
                power = current ** 2 * r
            else:
                branch_i = V / r if r > 0 else 0.0
                power = V ** 2 / r if r > 0 else 0.0
            branch_currents.append(branch_i)
            powers.append(power)
            temps.append(25.0 + power * 9.0)
        return {
            "level": level,
            "battery_present": battery_present,
            "resistor_count": len(placed),
            "R_total": R_total,
            "current": current,
            "voltage": V,
            "branch_currents": branch_currents,
            "temps_by_slot": temps,
            "max_temp": max(temps) if temps else 25.0,
            "target_current": level.objective_current,
            "max_current": level.max_current,
            "total_power": V * current,
        }

    def check_circuit(self, state):
        level = state["level"]
        if not state["battery_present"]:
            return "waiting", tr("missing_battery")
        if state["resistor_count"] < level.required_resistors:
            return "waiting", trf("missing_resistors", count=level.required_resistors - state["resistor_count"])
        if level.required_mode != "libre" and self.mode != level.required_mode:
            return "waiting", trf("required_mode", mode=level.required_mode)
        if state["current"] > level.max_current:
            return "lose", tr("overcurrent")
        if state["max_temp"] > level.max_temp:
            return "lose", tr("overheat")
        if abs(state["current"] - level.objective_current) <= level.tolerance:
            return "win", tr("win_msg")
        return "waiting", tr("not_target")

    def score_state(self, state):
        level = state["level"]
        error = abs(state["current"] - level.objective_current)
        accuracy = max(0.0, 1.0 - error / max(level.objective_current, 0.01))
        heat_penalty = max(0.0, (state["max_temp"] - 45.0) / 70.0)
        power_penalty = min(0.30, state["total_power"] / 80.0)
        score = int(max(0, min(100, 55 + accuracy * 50 - heat_penalty * 18 - power_penalty * 20)))
        stars = 3 if score >= 90 else 2 if score >= 74 else 1
        return score, stars

    def evaluate_circuit(self):
        state = self.compute_state()
        result, message = self.check_circuit(state)
        self.last_result = message
        if result == "win":
            score, stars = self.score_state(state)
            self.best_scores[self.level_index] = max(score, self.best_scores.get(self.level_index, 0))
            self.locked = True
            self.next_button.disabled = False
            self.next_button.text = tr("menu") if self.level_index + 1 >= len(self.levels) else tr("next")
            self.last_result = trf("score_msg", message=message, score=score, stars=stars)
            self.show_feedback(True)
            App.get_running_app().music.play("musica_win.mp3", loop=False)
            self.confetti.burst()
        elif result == "lose":
            self.board_painter.flash_warning()
            self.show_feedback(False)
            self._shake_board()
        self.refresh_ui()

    def show_feedback(self, ok):
        path = asset("correcto.png" if ok else "incorrecto.png")
        if path:
            self.feedback.source = path
            self.feedback.reload()
            self.feedback.opacity = 1
            Animation(opacity=0, duration=1.2).start(self.feedback)

    def _shake_board(self):
        x = self.board_center_panel.x
        anim = Animation(x=x + dp(7), duration=0.04) + Animation(x=x - dp(7), duration=0.04) + Animation(x=x, duration=0.04)
        anim.start(self.board_center_panel)

    def refresh_ui(self):
        if not hasattr(self, "goal_label"):
            return
        state = self.compute_state()
        level = state["level"]
        result, hint = self.check_circuit(state)
        level_key = f"level{self.level_index + 1}"
        self.level_label.text = tr(f"{level_key}_name")
        self.goal_label.text = f"[b]{tr('mission')}[/b]\n{tr(f'{level_key}_mission')}\n\n[b]{tr('target')}[/b]\n{level.objective_current:.2f} A +/- {level.tolerance:.2f} A\n{tr('limits')}: {level.max_current:.2f} A, {level.max_temp:.0f} C"
        self.formula_label.text = f"[b]{tr('physics')}[/b]\nSerie: Rtotal = R1 + R2 + R3\nParalelo: 1/Rtotal = 1/R1 + 1/R2 + 1/R3\nI = V / R"
        temps = ", ".join([f"{int(t)} C" for t in state["temps_by_slot"]])
        branches = ", ".join([f"{i:.2f} A" for i in state["branch_currents"]])
        self.state_label.text = f"[b]{tr('readings')}[/b]\n{tr('voltage_reading')}: {state['voltage']:.1f} V\nR total: {safe_ohms(state['R_total'])}\n{tr('total_current')}: {state['current']:.2f} A\n{tr('temps')}: {temps}"
        self.diagnostic_label.text = f"[b]{tr('diagnosis')}[/b]\n{self.build_diagnostic_text(state, result, hint)}\n{tr('branches')}: {branches}"
        best = self.best_scores.get(self.level_index)
        best_line = f"{tr('best_score')}: {best}/100" if best is not None else f"{tr('best_score')}: {tr('no_score')}"
        self.score_label.text = f"[b]{tr('performance')}[/b]\n{tr('power')}: {state['total_power']:.2f} W\n{best_line}"
        self.hint_label.text = self.last_result
        self.board_painter.refresh(state)

    def build_diagnostic_text(self, state, result, hint):
        if result in ("lose", "waiting"):
            return hint
        if state["current"] < state["target_current"] * 0.75:
            return tr("low_current")
        if state["current"] > state["target_current"] * 1.25:
            return tr("high_current")
        if state["max_temp"] > state["level"].max_temp * 0.85:
            return tr("hot_but_works")
        return tr(f"level{self.level_index + 1}_tip")

    def live_update(self, dt):
        self.board_painter.phase = (self.board_painter.phase + dt * 0.32) % 1.0
        self.board_painter.warning_flash = max(0.0, self.board_painter.warning_flash - dt * 1.8)
        self.refresh_ui()

    def on_next_pressed(self, *_):
        App.get_running_app().music.play(self.music_asset)
        if self.level_index + 1 >= len(self.levels):
            self.manager.current = "menu"
        else:
            self.start_level(self.level_index + 1)


class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = -1
        self.score = 0
        self.answered = False
        self.root = FloatLayout()
        self.add_widget(self.root)
        self.root.add_widget(AssetBackground("fondo_quiz.png"))
        self.panel = GlassPanel(size_hint=(0.88, 0.86), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.root.add_widget(self.panel)
        content = BoxLayout(orientation="vertical", padding=(dp(24), dp(18)), spacing=dp(12))
        self.panel.add_widget(content)

        self.title = Label(font_size=sp(30), bold=True, color=(0.75, 1, 0.84, 1), size_hint=(1, None), height=dp(46))
        self.progress = Label(font_size=sp(16), color=(0.75, 0.9, 1, 1), size_hint=(1, None), height=dp(28))
        self.prompt = Label(font_size=sp(22), color=(1, 1, 1, 1), halign="center", valign="middle", markup=True)
        self.prompt.bind(size=lambda s, _: setattr(s, "text_size", (s.width - dp(20), s.height)))
        self.options_box = BoxLayout(orientation="vertical", spacing=dp(9), size_hint=(1, 0.48))
        self.option_buttons = []
        for _ in range(4):
            button = Button(font_size=sp(17), background_normal="", background_color=(0.08, 0.30, 0.23, 0.96), color=(1, 1, 1, 1))
            button.bind(on_release=self.answer)
            self.option_buttons.append(button)
            self.options_box.add_widget(button)
        self.feedback = Label(font_size=sp(16), color=(0.9, 1, 0.92, 1), halign="left", valign="middle", markup=True)
        self.feedback.bind(size=lambda s, _: setattr(s, "text_size", (s.width - dp(12), s.height)))
        actions = BoxLayout(orientation="horizontal", size_hint=(1, None), height=dp(54), spacing=dp(12))
        self.primary = MenuButton()
        self.primary.bind(on_release=self.advance)
        self.back = MenuButton()
        self.back.bind(on_release=lambda *_: setattr(self.manager, "current", "menu"))
        actions.add_widget(self.primary)
        actions.add_widget(self.back)
        content.add_widget(self.title)
        content.add_widget(self.progress)
        content.add_widget(self.prompt)
        content.add_widget(self.options_box)
        content.add_widget(self.feedback)
        content.add_widget(actions)
        self.update_texts()

    def on_pre_enter(self):
        App.get_running_app().music.play("musica_quiz.mp3")
        self.begin()

    def update_texts(self):
        self.back.text = qtr("menu")
        if self.index < 0:
            self.title.text = qtr("intro_title")
            self.progress.text = ""
            self.prompt.text = qtr("intro")
            self.options_box.opacity = 0
            self.options_box.disabled = True
            self.feedback.text = ""
            self.primary.text = qtr("start")
            self.primary.disabled = False
        elif self.index >= len(qtr("items")):
            self.title.text = qtr("done")
            self.progress.text = ""
            self.prompt.text = qtr("score").format(score=self.score, total=len(qtr("items")))
            self.options_box.opacity = 0
            self.options_box.disabled = True
            self.feedback.text = ""
            self.primary.text = qtr("restart")
            self.primary.disabled = False
        else:
            self.options_box.opacity = 1
            self.options_box.disabled = False
            item = qtr("items")[self.index]
            self.title.text = qtr("title")
            self.progress.text = qtr("question").format(current=self.index + 1, total=len(qtr("items")))
            self.prompt.text = item["q"]
            self.feedback.text = "" if not self.answered else self.feedback.text
            for button, choice in zip(self.option_buttons, item["o"]):
                button.text = choice
                button.disabled = self.answered
                button.background_color = (0.08, 0.30, 0.23, 0.96)
            self.primary.text = qtr("next") if self.answered else qtr("pick")
            self.primary.disabled = not self.answered

    def begin(self):
        self.index = -1
        self.score = 0
        self.answered = False
        self.update_texts()

    def answer(self, button):
        if self.answered or self.index < 0:
            return
        item = qtr("items")[self.index]
        selected = self.option_buttons.index(button)
        correct = selected == item["a"]
        self.answered = True
        if correct:
            self.score += 1
        for index, option in enumerate(self.option_buttons):
            option.disabled = True
            option.background_color = (0.08, 0.55, 0.28, 1) if index == item["a"] else (0.35, 0.16, 0.18, 0.95) if index == selected else (0.08, 0.30, 0.23, 0.96)
        self.feedback.text = f"[b]{qtr('correct') if correct else qtr('incorrect')}[/b]\n{item['e']}"
        self.primary.text = qtr("next")
        self.primary.disabled = False

    def advance(self, *_):
        if self.index == -1 or self.index >= len(qtr("items")):
            self.index = 0
            self.score = 0
        elif self.answered:
            self.index += 1
        self.answered = False
        self.feedback.text = ""
        self.update_texts()


class CircuitosCaosControladoApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lang = "es"
        self.music = Music()

    def build(self):
        Window.clearcolor = (0.025, 0.030, 0.045, 1)
        Window.minimum_width = dp(980)
        Window.minimum_height = dp(620)
        sm = ScreenManager(transition=FadeTransition(duration=0.18))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(InfoScreen(name="info"))
        sm.add_widget(CreditsScreen(name="creditos"))
        sm.add_widget(LanguageScreen(name="idioma"))
        sm.add_widget(GameScreen(name="juego"))
        sm.add_widget(QuizScreen(name="quiz"))
        return sm


if __name__ == "__main__":
    CircuitosCaosControladoApp().run()

