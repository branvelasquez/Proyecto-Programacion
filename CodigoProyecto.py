import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

# Clase Usuario
class Usuario:
    def __init__(self, nombre, saldo, contraseña, id_usuario):
        self.nombre = nombre
        self.saldo = saldo
        self.contraseña = contraseña
        self.id_usuario = id_usuario

    def verificar_saldo(self, monto):
        return self.saldo >= monto

    def actualizar_saldo(self, monto):
        self.saldo -= monto

    def agregar_fondos(self, monto):
        self.saldo += monto


# Clase Gasto
class Gasto:
    def __init__(self, descripcion, monto, categoria):
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria