import sqlite3
import os

ruta_db = os.path.join(os.path.dirname(__file__), "usuarios.db")
conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    username TEXT,
    password TEXT
)
""")

cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", ("admin", "1234"))

conexion.commit()
conexion.close()
print("Base de datos creada con usuario admin/1234.")
