import pandas as pd
from functions import check_allowed_categories, check_numeric_fields, check_price_quantity_total, check_positive_quantity, check_required_columns, check_valid_dates, check_nulls
import pytest
from config import REQUIRED_COLUMNS

#---------------------------------------------------------------------------------------------------------------
# Pruebas para la validación de presencia de columnas obligatorias
@pytest.mark.parametrize(
    "df_columns, expected_passed",
    [
        (REQUIRED_COLUMNS, True),
        (["fecha_venta", "id_producto", "nombre_producto"], False),
        (REQUIRED_COLUMNS + ["extra_column"], True),
        (["id_producto", "nombre_producto", "categoria"], False)
    ]    
)
def test_required_columns(df_columns, expected_passed):
    df = pd.DataFrame(columns=df_columns)
    result = check_required_columns(df, REQUIRED_COLUMNS)
    assert result["passed"] == expected_passed


#---------------------------------------------------------------------------------------------------------------
# Pruebas para la validación de ausencia de valores nulos en todo el dataset
@pytest.mark.parametrize("column", REQUIRED_COLUMNS)
def test_no_nulls_in_column(column):
    df = pd.DataFrame({
        column : [1, 2, 3, None, 5]
    })
    result = check_nulls(df)
    assert not result["passed"]


#---------------------------------------------------------------------------------------------------------------
# Pruebas para la validación de que el total de venta es igual a precio por cantidad vendida
@pytest.mark.parametrize(
        "precio, cantidad_vendida, total_venta, expected_passed",
        [
            ([10], [2], [20], True),
            ([10], [2], [25], False),
            ([5, 3], [2, 4], [10, 12], True),
            ([5, 3], [2, 4], [10, 11], False)
        ]
)
def test_price_quantity_total(precio, cantidad_vendida, total_venta, expected_passed):
    df = pd.DataFrame({
        "precio": precio,
        "cantidad_vendida": cantidad_vendida,
        "total_venta": total_venta
    })
    result = check_price_quantity_total(df)
    assert result["passed"] == expected_passed


#---------------------------------------------------------------------------------------------------------------
# Pruebas para la validación de que la cantidad vendida es siempre positiva
@pytest.mark.parametrize(
    "cantidad_vendida, expected_passed",
    [
        ([1, 2, 3], True),
        ([1, 0, 2], False),
        ([0, -1, 3], False),
        ([-5, -2], False)
    ]
)
def test_check_positive_quantity(cantidad_vendida, expected_passed):
    df = pd.DataFrame({
        "cantidad_vendida": cantidad_vendida
    })
    result = check_positive_quantity(df)
    assert result["passed"] == expected_passed


#---------------------------------------------------------------------------------------------------------------
# Pruebas para la validación de que las fechas de venta son válidas
@pytest.mark.parametrize(
    "fecha_venta, expected_passed",
    [
        (["2024-01-01", "2024-12-31"], True),
        (["2024-01-01", "31-05-2024"], False),
        (["2024/02/15", "2024-03-20"], False),
        (["2024-04-10", "2024-13-01"], False)
    ]
)
def test_check_valid_dates(fecha_venta, expected_passed):
    df = pd.DataFrame({
        "fecha_venta": fecha_venta
    })
    result = check_valid_dates(df)
    assert result["passed"] == expected_passed


#---------------------------------------------------------------------------------------------------------------
# Pruebas para la validación de que las categorías son permitidas
@pytest.mark.parametrize(
    "categoria, expected_passed",
    [
        (["Electrónica", "Oficina"], True),
        (["Electrónica", "Juguetes"], False),
        (["Ropa", "Accesorios"], False),
        (["Fotografía", "Computación", "Audio"], True)
    ])

def test_check_allowed_categories(categoria, expected_passed):
    df = pd.DataFrame({
        "categoria": categoria
    })
    result = check_allowed_categories(df)
    assert result["passed"] == expected_passed




#---------------------------------------------------------------------------------------------------------------
# Pruebas para la validación de que los campos numéricos contienen solo valores numéricos
@pytest.mark.parametrize(
    "precio, total_venta, cantidad_vendida, expected_passed",
    [
        (["10.5", "20.0"], ["21", "40"], ["2", "2"], True),
        (["10.5", "veinte"], ["21", "40"], ["2", "2"], False),
        (["diez", "20.0"], ["21", "cuarenta"], ["2", "2"], False),
        (["10.5", "20.0"], ["veintiuno", "40"], ["dos", "2"], False)
    ]
)
def test_numeric_fields(precio, total_venta, cantidad_vendida, expected_passed):
    df = pd.DataFrame({
        "precio": precio,
        "total_venta": total_venta,
        "cantidad_vendida": cantidad_vendida
    })
    result = check_numeric_fields(df)
    assert result["passed"] == expected_passed