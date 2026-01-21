📊 Data Quality Framework – Validación de Calidad de Datos
📌 Descripción general

Este proyecto implementa un framework de validación de calidad de datos en Python, orientado a evaluar la integridad, consistencia y confiabilidad de un dataset de ventas (ventas.csv).

El framework permite:

Validar reglas de calidad de datos críticas

Automatizar pruebas mediante pytest

Generar un reporte estructurado en Excel

Facilitar la trazabilidad y el aseguramiento de la calidad de datos en pipelines analíticos



🎯 Objetivo del proyecto

Garantizar que los datos utilizados en procesos analíticos y de negocio cumplan con estándares mínimos de calidad antes de ser consumidos por reportes, modelos o sistemas downstream.


ID	        Caso de Prueba	                Descripción
-------------------------------------------------------------------------------------
CT00	    Columnas obligatorias	        Validar presencia de columnas requeridas                                                
CT01	    Valores nulos	                Validar ausencia de valores nulos                                            
CT02	    Tipos numéricos	                Validar campos numéricos                                         
CT03	    Consistencia matemática	        Precio x cantidad = total                               
CT04	    Fechas válidas	                Validar formato y validez de fechas                           
CT05	    Cantidad positiva	            Validar cantidad vendida>0                               
CT06	    Categorías permitidas   	    Validar categorías válidas                           



⚙️ Requisitos

Python 3.10+
Librerías:

pandas
numpy
openpyxl
pytest

Instalación de dependencias:
pip install -r requirements.txt


▶️ Ejecución del pipeline de calidad

Para ejecutar todas las validaciones sobre el dataset:
python run_quality_check.py


Resultado:

Se genera un archivo Excel con el reporte de calidad de datos

Cada validación indica:
    Resultado (Aprobado / Fallido)
    Número de incidencias
    Observaciones automáticas


👤 Autor
Pedro Javier Martínez Daza
Data & QA Automation Engineer
Proyecto desarrollado como parte de una prueba técnica de aseguramiento de calidad de datos.
