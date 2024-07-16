<div align="center">
   <img src="../../0-Assets/logo.png" alt="Descripción de la imagen" width="200px" height="200px">
   <h1>FECHAS Y HORAS EN PYTHON</h1>
</div>


# Importar el modulo `datetime`

# Obtener la fecha y hora actuales

```python
now = datetime.now()
```

# Crear Objeto de fecha y hora

```python
fecha = datetime.date(2024, 6, 18)
hora = datetime.time(14, 30, 45)
fecha_hora = datetime.datetime(2024, 6, 18, 14, 30, 45)
```

# Formatear fechas y horas

```python
formato = now.strftime("%Y-%m-%d %H:%M:%S")
```

# Operaciones con fechas y horas
futuro = now + datetime.timedelta(days=10)
pasado = now - datetime.timedelta(hours=2)

# Convertir cadenas en fechas

```python
fecha_str = "2024-06-18 14:30:45"
fecha_obj = datetime.datetime.strptime(fecha_str,"%Y-%m-%d %H:%M:%S")
```