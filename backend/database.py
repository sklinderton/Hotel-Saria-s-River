from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path
import mysql.connector
import os

def init_db():
    try:
        # Conexión temporal sin especificar base de datos
        temp_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="J7102006"
        )
        cursor = temp_conn.cursor()
        
        # Ruta relativa al archivo SQL (sube un nivel y entra a la carpeta sql)
        base_dir = Path(__file__).parent.parent  # Sube a Hotel-Saria-s-River
        sql_path = base_dir / "sql" / "create_tables.sql"
        
        # Verifica si el archivo existe
        if not sql_path.exists():
            raise FileNotFoundError(f"No se encontró el archivo SQL en {sql_path}")
        
        # Leer y ejecutar el archivo SQL
        with open(sql_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
        
        # Ejecutar cada sentencia del script
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        temp_conn.commit()
        print("✅ Base de datos y tablas creadas exitosamente")
    except Exception as e:
        print(f"❌ Error al inicializar la base de datos: {str(e)}")
    finally:
        if 'temp_conn' in locals() and temp_conn.is_connected():
            temp_conn.close()

# Llamar a la función de inicialización primero
init_db()

# Configuración normal de SQLAlchemy
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:J7102006@localhost/sarias_river"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()