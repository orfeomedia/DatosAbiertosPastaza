import streamlit as st
import pandas as pd

# Soporte completo PWA
st.markdown("""
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="/icon-192.png">
<meta name="theme-color" content="#1E6B3A">
""", unsafe_allow_html=True)

st.set_page_config(page_title="Datos Abiertos Pastaza", layout="wide", initial_sidebar_state="expanded")

st.title("🌿 Pastaza Transparente")

st.markdown("""
Esta app facilita la navegación y visualización del Portal de Gobierno Abierto del Gobierno Provincial de Pastaza.  
Selecciona una sección en el menú lateral para verla en pantalla completa.  
Este portal es parte de la política pública de transparencia y gobierno abierto implementada por el Prefecto André Granda.
""")

st.sidebar.header("Navegación Rápida")

seccion = st.sidebar.selectbox(
    "Elige una sección",
    [
        "Inicio - Gobierno Abierto",
        "Una Obra X Semana",
        "Pastaza Conectada",
        "Obras Públicas",
        "Gestión Ambiental",
        "Desarrollo Sustentable",
        "Transparencia Patrimonial",
        "Sistema de Información Local (SIL)",
        "Descargas - Plan de Acción"
    ]
)

# URLs para iframes
urls = {
    "Inicio - Gobierno Abierto": "https://datos.pastaza.gob.ec/",
    "Una Obra X Semana": "https://gadppz.maps.arcgis.com/apps/dashboards/0409dbbb16764ec4a9a2b332fbed0e83",
    "Pastaza Conectada": "https://gadppz.maps.arcgis.com/apps/dashboards/52a632fef2c949038504c9c68b0edd3d",
    "Obras Públicas": "https://datos.pastaza.gob.ec/obras-publicas",
    "Gestión Ambiental": "https://datos.pastaza.gob.ec/gestion-ambiental",
    "Desarrollo Sustentable": "https://datos.pastaza.gob.ec/desarrollo-sustentable",
    "Sistema de Información Local (SIL)": "https://sil.pastaza.gob.ec/",
}

# ==================== TRANSPARENCIA PATRIMONIAL ====================
if seccion == "Transparencia Patrimonial":
    st.markdown("**Transparencia Patrimonial**")
    st.markdown("**Compromiso absoluto con cero corrupción**")
    st.info("""
    Declaraciones juramentadas de patrimonio del Prefecto André Granda y de su equipo directivo.  
    **Fecha de publicación oficial:** 15 de junio de 2023
    """)

    # Datos actualizados (versión más reciente y limpia)
    data = {
        "Nombre": [
            "André Mauricio Granda Garrido", "Lineth Rosenda Calapucha Cerda",
            "Marcelo Sebastián Jácome Pérez", "Angel Eduardo Escobar Villamil",
            "Dario Javier Recalde Freire", "Josselyne Dayanara Quiróz Pazmiño",
            "Willam Gabriel Villarroel Paredes", "Luis Salvador Lascano Andrade",
            "Boris Napoleón Noboa Araujo", "Cristian Fabricio Quintanilla Diaz",
            "Livia Marilú Ordoñez Paredes", "Diego Wladimir Garcés Mayorga",
            "Anthony Javier Maldonado Tamayo", "Hector Vinicio Alarcón Yépez",
            "Andrés Eduardo Coloma Herrera", "Edwing Patricio García Manzano",
            "Jair Fernando Ledesma Bastidas", "Valeria Pozo Guerrero",
            "Cristian Daniel Dagua Cadena", "Gabriel Alejandro Sosa Espinel",
            "Lenín Santiago Racines Silva", "Diego Xavier Escobar Duche",
            "Alexis Faustyno Fernández Solis", "César Augusto Andino Cajas",
            "Yessenia Lizbeth Tello Solano", "María Augusta Cajas Orellana",
            "Mariela Alexandra Herrera Tapia", "Jaime Eduardo Rivadeneira Jaramillo",
            "Grace Estefanía Valdiviezo Quispe", "Daniel Alejandro Maldonado Ortíz",
            "Héctor Marcelo Quishpi Lliquin", "Gabriela Tatiana Luzuriaga Rosado",
            "Jorge Marcelo Cueva Romero", "Jorge Washington Castillo Mejía",
            "Jairo Alberto Narváez Guevara", "Jesús Emanuel Romero Rosero",
            "Stalin Xavier Cáceres Valverde", "María Emilia Torres Caicedo",
            "Diego Alexander Vasco Realpe", "Israel Eduardo Guevara Basantes",
            "Henrry Paúl León Loza", "Jorge Jairo Yaguar Mariño",
            "Karina Sthefanny Altarmirano Caiza", "Jessie Verónica Rivadeneira Salas",
            "Galo René Bravo Chango", "Eryka Mireya Silva Manzano"
        ],
        "Cargo": [
            "Prefecto de la Provincia de Pastaza", "Vice-prefecta de la Provincia de Pastaza",
            "Asesor 1", "Asesor 2", "Asesor 3", "Secretaria de Prefectura",
            "Director de Administración de Talento Humano", "Director Administrativo",
            "Director de Comunicación Social", "Procurador Síndico",
            "Director Financiero (E)", "Secretario General",
            "Director de Planificación", "Director de Obras Públicas (E)",
            "Director de Gestión Ambiental", "Director de Desarrollo Sustentable",
            "Director de Fiscalización", "Director de Turismo, Cultura y Deporte",
            "Director de Pueblos, Nacionalidades y Cooperación Internacional",
            "Tesorero", "Subdirector Administrativo", "Subdirector de Comunicación Social (E)",
            "Subdirector de Desarrollo Sustentable", "Subdirector de Gestión Ambiental",
            "Subdirector de Obras Públicas", "Subdirectora de Planificación",
            "Subdirectora de Administración de Talento Humano", "Subdirector Financiero",
            "Subdirector de Fiscalización", "Subprocurador Síndico",
            "Jefe de Bodega", "Jefe de Compras Públicas (E)", "Jefe de Presupuestos (E)",
            "Jefe de Desarrollo Productivo", "Jefe de Estudios y Proyectos",
            "Jefe de Mecánica y Mantenimiento", "Jefe de Gestión Ambiental (E)",
            "Jefe de Minería y Riesgos", "Jefe de Seguridad y Salud Ocupacional",
            "Jefe de Servicios Generales", "Jefe de Talento Humano (E)",
            "Jefe de TIC's", "Jefe de Cooperación Internacional",
            "Jefe de Contabilidad (S)", "Jefe de Documentación y Archivo (E)",
            "Jefe de Unidad Vial (E)"
        ],
        "Declaración Juramentada": [
            "https://pastaza.gob.ec/download/prefecto-provincial/",
            "https://pastaza.gob.ec/download/viceprefecta-provincial/",
            "https://pastaza.gob.ec/download/asesor-de-prefectura-1/",
            "https://pastaza.gob.ec/download/asesor-de-prefectura-2/",
            "https://pastaza.gob.ec/download/asesor-de-prefectura-3/",
            "https://pastaza.gob.ec/download/secretaria-de-prefectura/",
            "https://pastaza.gob.ec/download/director-talento-humano/",
            "https://pastaza.gob.ec/download/director-administrativo/",
            "https://pastaza.gob.ec/download/director-de-comunicacion/",
            "https://pastaza.gob.ec/download/procurador-sindico/",
            "https://pastaza.gob.ec/download/director-financiero/",
            "https://pastaza.gob.ec/download/secretario-general/",
            "https://pastaza.gob.ec/download/director-de-planificacion/",
            "https://pastaza.gob.ec/download/director-de-obras-publicas/",
            "https://pastaza.gob.ec/download/director-de-gestion-ambiental/",
            "https://pastaza.gob.ec/download/director-de-desarrollo-sustentable/",
            "https://pastaza.gob.ec/download/director-de-fiscalizacion/",
            "https://pastaza.gob.ec/download/director-de-turismo-cultura-y-deporte/",
            "https://pastaza.gob.ec/download/director-de-cooperacion-internacional-pueblos-y-nacionalidades/",
            "https://pastaza.gob.ec/download/tesorero/",
            "https://pastaza.gob.ec/download/subdirector-administrativo/",
            "https://pastaza.gob.ec/download/subdirector-de-comunicacion/",
            "https://pastaza.gob.ec/download/subdirector-de-desarrollo-sustentable/",
            "https://pastaza.gob.ec/download/subdirector-de-gestion-ambiental/",
            "https://pastaza.gob.ec/download/subdirector-de-obras-publicas/",
            "https://pastaza.gob.ec/download/subdirector-de-planificacion/",
            "https://pastaza.gob.ec/download/subdirector-de-talento-humano/",
            "https://pastaza.gob.ec/download/subdirector-financiero/",
            "https://pastaza.gob.ec/download/subdirector-de-fiscalizacion/",
            "https://pastaza.gob.ec/download/subprocurador-sindico/",
            "https://pastaza.gob.ec/download/jefe-de-bodega/",
            "https://pastaza.gob.ec/download/jefe-de-compras-publicas/",
            "https://pastaza.gob.ec/download/jefe-de-presupuesto/",
            "https://pastaza.gob.ec/download/jefe-de-desarrollo-productivo/",
            "https://pastaza.gob.ec/download/jefe-de-estudios-y-proyectos/",
            "https://pastaza.gob.ec/download/jefe-de-mecanica-y-mantenimiento/",
            "https://pastaza.gob.ec/download/jefe-de-gestion-ambiental/",
            "https://pastaza.gob.ec/download/jefe-de-mineria-y-riesgos/",
            "https://pastaza.gob.ec/download/jefe-de-seguridad-y-salud-ocupacional/",
            "https://pastaza.gob.ec/download/jefe-de-servicios-generales/",
            "https://pastaza.gob.ec/download/jefe-de-talento-humano/",
            "https://pastaza.gob.ec/download/jefe-de-tics/",
            "https://pastaza.gob.ec/download/jefe-de-cooperacion-internacional/",
            "https://pastaza.gob.ec/download/contador-general/",
            "https://pastaza.gob.ec/download/jefe-de-documentacion-y-archivo/",
            "https://pastaza.gob.ec/download/jefe-de-unidad-vial/"
        ]
    }

    df = pd.DataFrame(data)

    # Buscador
    search = st.text_input("🔎 Busca por nombre o cargo:")

    if search:
        df_filtered = df[
            df.apply(lambda row: search.lower() in row["Nombre"].lower() or 
                               search.lower() in row["Cargo"].lower(), axis=1)
        ]
    else:
        df_filtered = df

    # Mostrar tabla con enlaces clicables
    st.dataframe(
        df_filtered,
        column_config={
            "Declaración Juramentada": st.column_config.LinkColumn(
                "Declaración Juramentada",
                help="Haz clic para descargar el PDF",
                display_text="📄 Descargar PDF"
            )
        },
        use_container_width=True,
        hide_index=True
    )

    st.caption("Fuente: https://pastaza.gob.ec/institucion/equipo-de-trabajo/ • Actualizado según publicación oficial del 15 de junio de 2023")

# ==================== OTRAS SECCIONES ====================
elif seccion == "Descargas - Plan de Acción":
    st.markdown("### Descargas directas del Plan de Acción de Gobierno Abierto")
    st.markdown("- [Plan.pdf](https://datos.pastaza.gob.ec/descargas/Plan.pdf)")
    st.markdown("- [Matriz.pdf](https://datos.pastaza.gob.ec/descargas/Matriz.pdf)")
    st.markdown("- [Imagen.pdf](https://datos.pastaza.gob.ec/descargas/Imagen.pdf)")
    st.markdown("Más recursos en el portal principal.")

else:
    # Mostrar iframe para las demás secciones
    st.components.v1.iframe(urls[seccion], height=1000, scrolling=True)

# Footer sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("App oficial del Gobierno Provincial de Pastaza 👏")
st.sidebar.markdown("Desarrollada con ❤️ por Grok - Marzo 2026")
st.sidebar.markdown("André Granda - Prefecto de Pastaza 2023 - 2027")
