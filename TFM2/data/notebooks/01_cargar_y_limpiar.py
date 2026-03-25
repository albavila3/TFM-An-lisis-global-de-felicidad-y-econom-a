import pandas as pd
import os

os.chdir('c:/Users/Alba/Desktop/ThePower/TFM2')

print("=" * 50)
print("PASO 1: CARGAR DATOS")
print("=" * 50)

# Cargo datasets
df_felicidad = pd.read_csv('data/raw/World_Happiness_2005_2022.csv', encoding='latin1')
df_economia = pd.read_csv('data/raw/economia.csv')

print(f"✅ Felicidad: {len(df_felicidad)} filas, {len(df_felicidad.columns)} columnas")
print(f"✅ Economía: {len(df_economia)} filas, {len(df_economia.columns)} columnas")

print("\n" + "=" * 50)
print("PASO 2: LIMPIAR NOMBRES DE COLUMNAS")
print("=" * 50)

df_felicidad.columns = df_felicidad.columns.str.replace('ï»¿', '')

# Renombro columnas para que coincidan
df_felicidad = df_felicidad.rename(columns={'Country': 'pais', 'Year': 'año'})
df_economia = df_economia.rename(columns={'Country Name': 'pais', 'Year': 'año', 'Value': 'pib'})

print("✅ Columnas limpias y renombradas")

print("\n" + "=" * 50)
print("PASO 3: UNIR DATASETS")
print("=" * 50)

# Unir por país y año
df_final = pd.merge(df_felicidad, df_economia, on=['pais', 'año'], how='inner')

print(f"✅ Dataset final: {len(df_final)} filas, {len(df_final.columns)} columnas")

print("\n" + "=" * 50)
print("PASO 4: ELIMINAR COLUMNA SIN NOMBRE")
print("=" * 50)

if '' in df_final.columns:
    df_final = df_final.drop(columns=[''])
    print("✅ Columna vacía eliminada")
else:
    print("✅ No había columna vacía")

print(f"Columnas finales: {len(df_final.columns)}")

print("\n" + "=" * 50)
print("PASO 5: GUARDAR DATASET FINAL")
print("=" * 50)

os.makedirs('data/processed', exist_ok=True)

# Guardar
df_final.to_csv('data/processed/dataset_final.csv', index=False)
print("✅ Guardado en: data/processed/dataset_final.csv")