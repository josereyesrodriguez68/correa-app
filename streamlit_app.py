
import streamlit as st
import math

st.set_page_config(page_title="Cálculo de Correa", page_icon="🔧", layout="centered")
st.title("🔧 Cálculo de Longitud de Correa y Deflexión")

D = st.number_input("Diámetro polea mayor (D) [mm]", min_value=0.0, step=0.1)
d = st.number_input("Diámetro polea menor (d) [mm]", min_value=0.0, step=0.1)
C = st.number_input("Distancia entre centros (C) [mm]", min_value=0.0, step=0.1)

if st.button("Calcular TL y Deflexión"):
    diferencia = (D - d) / 2
    if C <= diferencia:
        st.error("Error: La distancia entre centros debe ser mayor que (D - d)/2.")
    else:
        TL = math.sqrt(C**2 - diferencia**2) / 1000
        deflexion_corregida = TL * 16
        st.success("✅ Resultados:")
        st.write(f"📏 Longitud TL = **{TL:.3f} m**")
        st.write(f"📐 Deflexión corregida = **{deflexion_corregida:.1f} mm**")
