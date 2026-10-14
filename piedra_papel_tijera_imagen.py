import tkinter as tk
import random
import os

# Música (opcional): si pygame no está instalado, el juego funciona sin música
try:
    import pygame
    PYGAME_OK = True
except ImportError:
    PYGAME_OK = False

OPCIONES = ["Piedra", "Papel", "Tijera"]
EMOJIS = {"Piedra": "✊", "Papel": "✋", "Tijera": "✌️"}
GANA_A = {"Piedra": "Tijera", "Papel": "Piedra", "Tijera": "Papel"}

# Los archivos tienen que estar en la misma carpeta que este programa
ARCHIVO_MUSICA = "Renai_Circulation_saturado.mp3"
ARCHIVO_FONDO = "fondo.png"   # imagen de fondo (no necesita librerías extra)
VOLUMEN = 0.4                 # de 0.0 a 1.0

ANCHO, ALTO = 420, 480
COLOR_FONDO = "#1e1e2e"       # fondo liso si no se encuentra la imagen


class Juego:
    def __init__(self, root):
        self.root = root
        root.title("Piedra, Papel o Tijera")
        root.geometry(f"{ANCHO}x{ALTO}")
        root.resizable(False, False)

        self.rondas = 0
        self.puntos_jugador = 0
        self.puntos_compu = 0
        self.empates = 0

        self.canvas = tk.Canvas(root, width=ANCHO, height=ALTO,
                                bg=COLOR_FONDO, highlightthickness=0)
        self.canvas.pack()

        self.iniciar_musica()
        self.poner_fondo()   # se crea primero para quedar detrás de todo
        root.protocol("WM_DELETE_WINDOW", self.cerrar)

        # ---------- Textos (con sombra para que se lean sobre el fondo) ----------
        self.t_titulo = self.crear_texto(210, 35, "Piedra, Papel o Tijera", 18, "bold")
        self.t_ronda = self.crear_texto(210, 85, "Ronda: 0", 14)
        self.t_puntos = self.crear_texto(
            210, 120, "Vos: 0  |  Compu: 0  |  Empates: 0", 13)
        self.t_lider = self.crear_texto(
            210, 150, "Todavía nadie tiene puntos", 12, "italic", "#dddddd")
        self.crear_texto(210, 195, "Elegí tu jugada:", 12)
        self.t_jugadas = self.crear_texto(210, 340, "", 13)
        self.t_resultado = self.crear_texto(210, 385, "", 16, "bold")

        # ---------- Botones ----------
        for opcion, x in zip(OPCIONES, (80, 210, 340)):
            b = tk.Button(self.canvas, text=f"{EMOJIS[opcion]}\n{opcion}",
                          font=("Arial", 12), width=8, height=3,
                          command=lambda o=opcion: self.jugar(o))
            self.canvas.create_window(x, 265, window=b)

        b_reiniciar = tk.Button(self.canvas, text="Reiniciar juego",
                                font=("Arial", 11), command=self.reiniciar)
        self.canvas.create_window(210, 440, window=b_reiniciar)

    # ---------- Fondo ----------
    def poner_fondo(self):
        carpeta = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(carpeta, ARCHIVO_FONDO)
        try:
            self.imagen_fondo = tk.PhotoImage(file=ruta)  # hay que guardarla en self
            self.canvas.create_image(0, 0, anchor="nw", image=self.imagen_fondo)
        except tk.TclError as e:
            print(f"No se pudo cargar la imagen '{ARCHIVO_FONDO}': {e}")

    # ---------- Ayudas para dibujar texto ----------
    def crear_texto(self, x, y, texto, tam, estilo="normal", color="white"):
        fuente = ("Arial", tam, estilo)
        sombra = self.canvas.create_text(x + 2, y + 2, text=texto,
                                         font=fuente, fill="black")
        principal = self.canvas.create_text(x, y, text=texto,
                                            font=fuente, fill=color)
        return (sombra, principal)

    def cambiar_texto(self, par, texto, color=None):
        self.canvas.itemconfig(par[0], text=texto)
        self.canvas.itemconfig(par[1], text=texto)
        if color:
            self.canvas.itemconfig(par[1], fill=color)

    # ---------- Música ----------
    def iniciar_musica(self):
        if not PYGAME_OK:
            print("pygame no está instalado: el juego funciona sin música.")
            return
        try:
            pygame.mixer.init()
            carpeta = os.path.dirname(os.path.abspath(__file__))
            ruta = os.path.join(carpeta, ARCHIVO_MUSICA)
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(VOLUMEN)
            pygame.mixer.music.play(-1)  # en bucle hasta cerrar el programa
        except Exception as e:
            print(f"No se pudo reproducir la música: {e}")

    def cerrar(self):
        if PYGAME_OK:
            try:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            except Exception:
                pass
        self.root.destroy()

    # ---------- Juego ----------
    def jugar(self, eleccion):
        compu = random.choice(OPCIONES)
        self.rondas += 1

        if eleccion == compu:
            resultado, color = "¡Empate!", "#dddddd"
            self.empates += 1
        elif GANA_A[eleccion] == compu:
            resultado, color = "¡Ganaste esta ronda!", "#66ff66"
            self.puntos_jugador += 1
        else:
            resultado, color = "Perdiste esta ronda", "#ff6666"
            self.puntos_compu += 1

        self.cambiar_texto(
            self.t_jugadas,
            f"Vos: {EMOJIS[eleccion]} {eleccion}    "
            f"Compu: {EMOJIS[compu]} {compu}")
        self.cambiar_texto(self.t_resultado, resultado, color)
        self.actualizar()

    def actualizar(self):
        self.cambiar_texto(self.t_ronda, f"Ronda: {self.rondas}")
        self.cambiar_texto(
            self.t_puntos,
            f"Vos: {self.puntos_jugador}  |  "
            f"Compu: {self.puntos_compu}  |  Empates: {self.empates}")

        if self.puntos_jugador > self.puntos_compu:
            diff = self.puntos_jugador - self.puntos_compu
            texto = f"Vas ganando por {diff} punto(s)"
        elif self.puntos_compu > self.puntos_jugador:
            diff = self.puntos_compu - self.puntos_jugador
            texto = f"La compu va ganando por {diff} punto(s)"
        else:
            texto = "Van empatados"
        self.cambiar_texto(self.t_lider, texto, "white")

    def reiniciar(self):
        self.rondas = 0
        self.puntos_jugador = 0
        self.puntos_compu = 0
        self.empates = 0
        self.cambiar_texto(self.t_jugadas, "")
        self.cambiar_texto(self.t_resultado, "")
        self.actualizar()
        self.cambiar_texto(self.t_lider, "Todavía nadie tiene puntos", "#dddddd")


if __name__ == "__main__":
    root = tk.Tk()
    Juego(root)
    root.mainloop()
