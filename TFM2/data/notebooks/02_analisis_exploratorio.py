
import pandas as pd
import os
import matplotlib.pyplot as plt

# Cambiar a la carpeta del proyecto
os.chdir('c:/Users/Alba/Desktop/ThePower/TFM2')

print("=" * 60)
print("ANÁLISIS EXPLORATORIO: RELACIÓN ENTRE FELICIDAD Y ECONOMÍA")
print("=" * 60)

# Cargar el dataset final
df = pd.read_csv('data/processed/dataset_final.csv')
print(f"\n Dataset cargado: {len(df)} filas, {len(df.columns)} columnas")

print("\n" + "=" * 60)
print("1. ESTADÍSTICAS BÁSICAS")
print("=" * 60)

# Ver estadísticas de las columnas numéricas
print("\n Estadísticas de felicidad y PIB:")
print(df[['Happiness', 'pib']].describe())

print("\n" + "=" * 60)
print("2. CORRELACIÓN ENTRE FELICIDAD Y PIB")
print("=" * 60)

# Calcular correlación
correlacion = df['Happiness'].corr(df['pib'])
print(f"\n Correlación entre Happiness y PIB: {correlacion:.3f}")

if correlacion > 0.7:
    print("✅ ¡Correlación muy fuerte! Los países más ricos tienden a ser más felices.")
elif correlacion > 0.5:
    print("✅ Correlación moderada. El dinero influye, pero no lo es todo.")
else:
    print("⚠️ Correlación débil. La felicidad depende más de otros factores.")

print("\n" + "=" * 60)
print("3. TOP 10 PAÍSES MÁS FELICES (PROMEDIO)")
print("=" * 60)

# Top 10 países por felicidad promedio
top_felicidad = df.groupby('pais')['Happiness'].mean().sort_values(ascending=False).head(10)
print("\n Los 10 países más felices:")
for i, (pais, felicidad) in enumerate(top_felicidad.items(), 1):
    print(f"   {i}. {pais}: {felicidad:.2f}")

print("\n" + "=" * 60)
print("4. TOP 10 PAÍSES CON MAYOR PIB (PROMEDIO)")
print("=" * 60)

# Top 10 países por PIB promedio
top_pib = df.groupby('pais')['pib'].mean().sort_values(ascending=False).head(10)
print("\n Los 10 países más ricos:")
for i, (pais, pib) in enumerate(top_pib.items(), 1):
    print(f"   {i}. {pais}: {pib/1e12:.2f} billones USD")

print("\n" + "=" * 60)
print("5. ¿HA CAMBIADO LA FELICIDAD CON LOS AÑOS?")
print("=" * 60)

# Evolución de la felicidad por año
felicidad_por_año = df.groupby('año')['Happiness'].mean()
print("\n Felicidad promedio por año:")
for año, felicidad in felicidad_por_año.items():
    print(f"   {año}: {felicidad:.2f}")

# Gráfico simple 
plt.figure(figsize=(10, 6))
plt.plot(felicidad_por_año.index, felicidad_por_año.values, marker='o', color='green')
plt.title('Evolución de la Felicidad Mundial (2008-2022)')
plt.xlabel('Año')
plt.ylabel('Puntuación de Felicidad')
plt.grid(True, alpha=0.3)
plt.xticks(felicidad_por_año.index[::2], rotation=45)
plt.tight_layout()
plt.show()

print("\n ¡ANÁLISIS COMPLETADO!")