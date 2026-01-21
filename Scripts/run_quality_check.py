from functions import load_csv, check_required_columns, check_nulls, check_numeric_fields, check_price_quantity_total, check_valid_dates, check_positive_quantity, check_allowed_categories, run_validations, results_to_dataframe, export_results_to_excel
from config import REQUIRED_COLUMNS

df = load_csv(r"C:\Users\PEDRO\OneDrive\Documentos\DataKnow\data_quality_framework\Data\ventas.csv")

 #Validar esquema de columnas obligatorias
schema_result = check_required_columns(df, REQUIRED_COLUMNS)
# Si falla la validación de esquema, generar reporte e interrumpir pipeline
if not schema_result["passed"]:
    report = results_to_dataframe([{
        "ID caso de prueba": schema_result["test_id"],
        "Descripción del Caso": schema_result["description"],
        "Resultado": "Fallido",
        "Descripción del Resultado": schema_result["details"],
        "Número de Incidencias Detectadas": schema_result["issues_count"],
        "Observaciones": "Pipeline detenido por error de esquema"
    }])

else:
    validations = [
        lambda df: check_required_columns(df, REQUIRED_COLUMNS),
        check_nulls,
        check_numeric_fields,
        check_price_quantity_total,
        check_valid_dates,
        check_positive_quantity,
        check_allowed_categories
    ]

    results = run_validations(df, validations)
    report = results_to_dataframe(results)
    export_results_to_excel(report, r"C:\Users\PEDRO\OneDrive\Documentos\DataKnow\data_quality_framework\Data\data_quality_report.xlsx")

    print(report)