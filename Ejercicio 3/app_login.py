import tkinter as tk
from tkinter import messagebox
import sqlite3
import urllib.request
import json
import os


def validar_usuario(username, password): # Verificar usuario y contraseña en la BD
    ruta_db = os.path.join(os.path.dirname(__file__), "usuarios.db")
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None

def obtener_personajes(): # Obtener datos de API
    url = "https://rickandmortyapi.com/api/character"
    try:
        respuesta = urllib.request.urlopen(url)
        datos = json.loads(respuesta.read())
        personajes = datos["results"]
        return [p["name"] for p in personajes[:5]]
    except Exception as e:
        return ["Error al obtener personajes"]

def login():
    user = entrada_usuario.get()
    pwd = entrada_contraseña.get()

    if validar_usuario(user, pwd):
        personajes = obtener_personajes()
        mensaje = "Login exitoso. Personajes:\n" + "\n".join(personajes)
        messagebox.showinfo("Bienvenido", mensaje)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana = tk.Tk()
ventana.title("Login con API")

tk.Label(ventana, text="Usuario:").grid(row=0, column=0)
entrada_usuario = tk.Entry(ventana)
entrada_usuario.grid(row=0, column=1)

tk.Label(ventana, text="Contraseña:").grid(row=1, column=0)
entrada_contraseña = tk.Entry(ventana, show="*")
entrada_contraseña.grid(row=1, column=1)

tk.Button(ventana, text="Login", command=login).grid(row=2, column=0, columnspan=2)

ventana.mainloop()
