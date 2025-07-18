# 🎕️ Saria's River – Glamping de Lujo en Costa Rica

**Saria's River** es una aplicación web que simula el sitio de un hotel de glamping exclusivo para parejas, ubicado en Buenos Aires, Puntarenas, Costa Rica.

---

## 📁 Estructura del Proyecto

```
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
│   └── images/
│       ├── sarias_river.png
│       ├── suit_monteverde.png
│       ├── suit_yiguirro.png
│       └── master_suit_jagar.png
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
* Rust (para compilar dependencias de Pydantic)
* Cargo (administrador de paquetes de Rust)

### Base de Datos

* MySQL 8.x

### API Externa

* JSONPlaceholder (para simular reseñas de visitantes)

---

## ⚙️ Configuración y Ejecución

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/sarias-river.git
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

### 3. Crear la Base de Datos

Ejecutar el script SQL:

```bash
mysql -u tu_usuario -p < ../sql/create_tables.sql
```

O ingresar manualmente a MySQL y copiar el contenido.

### 4. Ejecutar el Backend

```bash
uvicorn main:app --reload
```

Disponible en:

* API: `http://localhost:8000`
* Documentación Swagger: `http://localhost:8000/docs`

### 5. Abrir el Frontend

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
* Reseñas simuladas desde JSONPlaceholder.

---

## 📢 Requisitos Mínimos

* Python 3.11+
* MySQL 8.x
* Rust + Cargo (para compilar dependencias en Python 3.13)
* Navegador moderno (Chrome, Firefox, Edge)

---

## 💬 Autor

Proyecto desarrollado por \*\*Jason Barrantes, Melany Ramírez, Junior Ramírez, Jasser Palacios\*\*

Lead University — Proyecto Web Personalizado con HTML, CSS, JS y FastAPI

---

## 📃 Licencia

Este proyecto es de uso académico. No está autorizado para fines comerciales sin permiso.
