# 🎕️ Saria's River – Glamping de Lujo en Costa Rica

**Saria's River** es una aplicación web que simula el sitio de un hotel de glamping exclusivo para parejas, ubicado en Buenos Aires, Puntarenas, Costa Rica. Fue desarrollada como proyecto educativo integrando HTML, CSS, JavaScript, FastAPI y una base de datos MySQL.

---

## 📁 Estructura del Proyecto

```bash
hotel_sarias_river/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   ├── reseñas.json
│   └── images/
│       ├── sarias_river.png
│       ├── suit_monteverde.png
│       ├── suit_yiguirro.png
│       └── master_suit_jaguar.png
│
└── sql/
    └── create_tables.sql
```

---

## 🚀 Tecnologías Utilizadas

### Frontend

* HTML5
* CSS3
* JavaScript (Vanilla)

### Backend

* Python 3.11+
* FastAPI
* SQLAlchemy
* MySQL Connector

### Base de Datos

* MySQL 8.x

### API Externa

* **Mockaroo** (para simular reseñas de visitantes en español)

---

## ⚙️ Configuración y Ejecución

### 1. Clonar el Repositorio

```bash
git clone https://github.com/sklinderton/sarias-river.git
cd hotel_sarias_river
```

### 2. Configurar el Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # En Windows
# source venv/bin/activate   # En Linux/Mac

pip install -r requirements.txt
```

### 3. Configurar credenciales de MySQL

Abre el archivo `backend/database.py` y modifica las siguientes líneas con tu propia contraseña de MySQL:

```python
def init_db():
    try:
        # Conexión temporal sin especificar base de datos
        temp_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="TU_CONTRASENA"
        )
```

Y también modifica esta otra línea:

```python
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:TU_CONTRASENA@localhost/sarias_river"
```

Reemplaza `TU_CONTRASENA` por la contraseña correspondiente a tu usuario de MySQL.

### 5. Ejecutar el Backend

```bash
uvicorn main:app --reload
```

Disponible en:

* API: `http://localhost:8000`
* Documentación Swagger: `http://localhost:8000/docs`

### 6. Abrir el Frontend

Abre el archivo:

```
frontend/index.html
```

con doble clic o arrástralo al navegador.

---

## ✅ Características

* Fondo con imagen de la selva tropical costarricense.
* 3 suites exclusivas:

  * **Monteverde** (\$450 por noche, 3 comidas incluidas)
  * **Yigüirro** (\$450 por noche, 3 comidas incluidas)
  * **Master Jaguar** (\$900 por noche, incluye spa)
* Formulario de reservación para parejas.
* Visualización de reservas desde la base de datos.
* Reseñas simuladas en español consumidas desde archivo JSON generado con Mockaroo.

---

## 📢 Requisitos Mínimos

* Python 3.11+
* MySQL 8.x
* Navegador moderno (Chrome, Firefox, Edge)

---

## 💬 Autores

Proyecto desarrollado por **Jason Barrantes, Melany Ramírez, Junior Ramírez y Jasser Palacios**

Lead University — Proyecto Web Personalizado con HTML, CSS, JS y FastAPI

---

## 📃 Licencia

Este proyecto es de uso académico. No está autorizado para fines comerciales sin permiso del equipo desarrollador.

