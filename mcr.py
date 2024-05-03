import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def create_heart_shape():
    # Coordenadas de la forma del corazón
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

def plot_heart():
    x, y = create_heart_shape()
    # Configuración de la línea en zigzag
    step_size = 1.0  # Aumentado para reducir la cantidad de zigzags
    zigzag_x = []
    zigzag_y = []
    direction = 1

    # Rellenar la forma del corazón
    for xi in np.arange(np.min(x), np.max(x), step_size):
        y_vals = y[(x >= xi) & (x < xi + step_size)]
        if len(y_vals) > 0:
            min_y, max_y = np.min(y_vals), np.max(y_vals)
            yy = np.arange(min_y, max_y, step_size * direction)
            zigzag_x.extend([xi] * len(yy))
            zigzag_y.extend(yy)
            direction *= -1  # Cambiar dirección

    fig, ax = plt.subplots(figsize=(4, 4))  # Configura el tamaño aquí para la figura
    ax.plot(zigzag_x, zigzag_y, color='red', linewidth=1)
    ax.set_title("Mueve la línea de arriba")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)

    # Ajustes de los límites para el "zoom"
    zoom_level = st.slider("Zoom level", 0.5, 1.5, 0.5)  # Inicio en mínimo
    ax.set_xlim(-18 * zoom_level, 18 * zoom_level)
    ax.set_ylim(-18 * zoom_level, 18 * zoom_level)

    return fig

st.title("Te Amo Mariana ❤️ Te Amo mi Niña Bonita")
col1, col2 = st.columns([1,1])  # Dividir la pantalla en tres columnas
with col1:  # Colocar el gráfico en la columna central
    fig = plot_heart()
    st.pyplot(fig, use_container_width=True)  # Usa el ancho del contenedor

with col2:
    texto_markdown = """
    
    
    Hola mi niña bonita "solo mía" ,'ultimamente he sentido que estás diferente  y quería pedirte disculpas ‍♂️ porque entiendo que puedes sentir que a veces no te doy el tiempo suficiente ⏳.

    Te hago esto para decirte que no es porque no te quiera ❤️, al contrario, te amo muchísimo . Solo que uno a veces no actúa bien  y no sé qué pase por tu cabecita , pero me gustaría que expreses conmigo todo lo que sientes ️ y no te cierres , ya que yo soy tu novio  y para eso estamos los dos para darnos apoyo .

    Yo sé que tú a veces piensas que no te doy la misma cantidad de detalles que antes , pero no es que no quiera ‍♂️, si no que siempre pienso cómo darte algo mejor que la última vez . Tampoco quiero que por los problemas que hayas tenido te cierres en cosas conmigo ‍♀️ porque creeme que yo a ti te amo demasiado mi niña linda .

    Si tú supieras todo lo que me encanta pasar tiempo contigo  y disfrutar cada momento a tu lado , y no es que a veces no te de interés , solo que me ocupo un poquito , pero siempre pienso en ti antes de dormirme  y al levantarme , pienso en lo grandiosa y la gran mujer que eres .

    A veces pienso que por bobadas pueda perderte , pero no quiero eso porque no me considero un mal hombre . Tal vez como humano cometa errores  y no te haga sentir bien todo el tiempo ☹️, pero creeme que nunca hago nada de aposta para hacerte daño  y siempre intento darte lo mejor de mí para ti , y ser un mejor hombre para ti me motiva más cada día .

    Entiendo nuestra forma de pensar  y me dirás que uno se vuelve mejor para uno mismo, y tienes razón , pero también para la persona que uno eligió ❤️ ya que quiero que esta tenga una buena persona a su lado  para que construyamos un hogar bonito .

    Te amo mucho mi niña bonita .
    """

    # Se muestra el texto en Markdown usando st.markdown
    st.markdown(texto_markdown)

