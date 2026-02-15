import streamlit as st
import pandas as pd

st.set_page_config(page_title=" Datos Abiertos Pastaza", layout="wide", initial_sidebar_state="expanded")

st.title("🌿Pastaza Transparente")
st.markdown("""
Esta app facilita la navegación y visualización del Portal de Gobierno Abierto del Gobierno Provincial de Pastaza.
Selecciona una sección en el menú lateral para verla en pantalla completa. Este portal es parte de la política pública de transparencia y gobierno abierto implementada por el Prefecto André Granda.
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

# Contenido según selección
if seccion == "Transparencia Patrimonial":
    st.markdown("**Transparencia Patrimonial - Compromiso absoluto con cero corrupción**")
    st.markdown("Declaraciones juramentadas de patrimonio del Prefecto André Granda y de su equipo directivo. Haz click en el botón para ver/descargar el PDF.")

    # Datos completos (44 filas verificadas)
    data = {
        "Nombre": [
            "André Mauricio Granda Garrido",
            "Lineth Rosenda Calapucha Cerda", "Ana Elizabeth Villalba Noriega", "Rodman Fabricio Tamayo Aman",
            "Josselyne Dayanara Quiróz Pazmiño", "Willam Gabriel Villarroel Paredes", "Luis Salvador Lascano Andrade",
            "Boris Napoleón Noboa Araujo", "Gabriela Belén Rivera Arévalo", "Livia Marilú Ordoñez Paredes",
            "Diego Wladimir Garcés Mayorga", "Anthony Javier Maldonado Tamayo", "Jorge Luis Nuñez Meneses",
            "Andrés Eduardo Coloma Herrera", "Edwing Patricio García Manzano", "Jair Fernando Ledesma Bastidas",
            "Gabriel Alejandro Sosa Espinel", "Wendy Janeth Jaramillo Ponce", "Franzua Efraín Freire Prieto",
            "Alexis Faustyno Fernández Solis", "Luis Alberto Guamán Escobar", "Yessenia Lizbeth Tello Solano",
            "María Augusta Cajas Orellana", "Mariela Alexandra Herrera Tapia", "Jaime Eduardo Rivadeneira Jaramillo",
            "Eryka Mireya Silva Manzano", "Damaris Priscila Ortiz Pasuy", "Héctor Marcelo Quishpi Lliquin",
            "Lenín Santiago Racines Silva", "Jorge Marcelo Cueva Romero", "Jorge Washington Castillo Mejía",
            "Jairo Alberto Narváez Guevara", "Jesús Emanuel Romero Rosero", "Brian Steven Coronel García",
            "Johan Javier Hernández Ballesteros", "Diego Alexander Vasco Realpe", "Israel Eduardo Guevara Basantes",
            "Stalin Jouseph Barriga Chávez", "Jorge Jairo Yaguar Mariño", "Valeria Pozo Guerrero",
            "Jennifer Sharlyn Zuñiga Miranda", "Mónica Alexandra Pozo Rosero", "José Enrique Yanez Vargas",
            "Héctor Vinicio Alarcón Yépez"
        ],
        "Cargo": [
            "Prefecto Provincial de Pastaza",
            "Vice-prefecta de la Provincia de Pastaza", "Asesor 2", "Asesor 3",
            "Secretario de Prefectura", "Director de Administración de Talento Humano", "Director Administrativo",
            "Director de Comunicación Social", "Procurador Síndico", "Director Financiero",
            "Secretario General", "Director de Planificación", "Director de Obras Públicas",
            "Directora de Gestión Ambiental (E)", "Director de Desarrollo Sustentable", "Director de Fiscalización",
            "Tesorero", "Subdirector Administrativo", "Subdirector de Comunicación Social",
            "Subdirector de Desarrollo Sustentable", "Subdirector de Gestión Ambiental (E)", "Subdirector de Obras Públicas",
            "Subdirectora de Planificación", "Subdirectora de Administración de Talento Humano", "Subdirector Financiero",
            "Subdirector de Fiscalización (E)", "Subprocurador Síndico", "Jefe de Bodega",
            "Jefe de Compras Públicas", "Jefe de Presupuestos (E)", "Jefe de Desarrollo Productivo",
            "Jefe de Estudios y Proyectos", "Jefe de Mecánica y Mantenimiento", "Jefe de Gestión Ambiental (E)",
            "Jefe de Minería y Riesgos (E)", "Jefe de Seguridad y Salud Ocupacional", "Jefe de Servicios Generales",
            "Jefe de Talento Humano", "Jefe de TIC's", "Jefe de Turismo",
            "Jefe de Cooperación Nacional e Internacional", "Jefe de Contabilidad (E)", "Jefe de Archivo (E)",
            "Jefe de Unidad Vial"
        ],
        "Declaración Juramentada": [
            "https://pastaza.gob.ec/download/prefecto-provincial/?wpdmdl=22607&refresh=698fcf73956661771032435",
            "https://pastaza.gob.ec/download/viceprefecta-provincial/?wpdmdl=22676&refresh=698fcf73960421771032435",
            "https://pastaza.gob.ec/download/asesor-de-prefectura-2/?wpdmdl=22550&refresh=698fcf73966121771032435",
            "https://pastaza.gob.ec/download/asesor-de-prefectura-3/?wpdmdl=22552&refresh=698fcf7396be01771032435",
            "https://pastaza.gob.ec/download/secretaria-de-prefectura/?wpdmdl=22611&refresh=698fcf73971ba1771032435",
            "https://pastaza.gob.ec/download/director-talento-humano/?wpdmdl=22544&refresh=698fcf73977581771032435",
            "https://pastaza.gob.ec/download/director-administrativo/?wpdmdl=22554&refresh=698fcf7397d591771032435",
            "https://pastaza.gob.ec/download/director-de-comunicacion/?wpdmdl=22556&refresh=698fcf73983301771032435",
            "https://pastaza.gob.ec/download/procurador-sindico/?wpdmdl=22609&refresh=698fcf73989031771032435",
            "https://pastaza.gob.ec/download/director-financiero/?wpdmdl=22560&refresh=698fcf7398ed51771032435",
            "https://pastaza.gob.ec/download/secretario-general/?wpdmdl=22613&refresh=698fcf73994d21771032435",
            "No disponible",
            "https://pastaza.gob.ec/download/director-de-obras-publicas/?wpdmdl=22567&refresh=698fcf7399adc1771032435",
            "No disponible",
            "https://pastaza.gob.ec/download/director-de-desarrollo-sustentable/?wpdmdl=22558&refresh=698fcf739a0991771032435",
            "https://pastaza.gob.ec/download/director-de-fiscalizacion/?wpdmdl=22563&refresh=698fcf739a6611771032435",
            "https://pastaza.gob.ec/download/tesorero/?wpdmdl=22663&refresh=698fcf739ac2b1771032435",
            "https://pastaza.gob.ec/download/subdirector-administrativo/?wpdmdl=22615&refresh=698fcf739b1ea1771032435",
            "https://pastaza.gob.ec/download/subdirector-de-comunicacion/?wpdmdl=22617&refresh=698fcf739b8261771032435",
            "https://pastaza.gob.ec/download/subdirector-de-desarrollo-sustentable/?wpdmdl=22619&refresh=698fcf739bdd21771032435",
            "No disponible",
            "https://pastaza.gob.ec/download/subdirector-de-obras-publicas/?wpdmdl=22627&refresh=698fcf739c38f1771032435",
            "https://pastaza.gob.ec/download/subdirector-de-planificacion/?wpdmdl=22630&refresh=698fcf739c9561771032435",
            "https://pastaza.gob.ec/download/subdirector-de-talento-humano/?wpdmdl=22632&refresh=698fcf739cf0f1771032435",
            "https://pastaza.gob.ec/download/subdirector-financiero/?wpdmdl=22621&refresh=698fcf739d4c41771032435",
            "https://pastaza.gob.ec/download/subdirector-de-fiscalizacion/?wpdmdl=22623&refresh=698fcf739da6b1771032435",
            "https://pastaza.gob.ec/download/subprocurador-sindico/?wpdmdl=22661&refresh=698fcf739e0901771032435",
            "https://pastaza.gob.ec/download/jefe-de-bodega/?wpdmdl=22573&refresh=698fcf739e6921771032435",
            "https://pastaza.gob.ec/download/jefe-de-compras-publicas/?wpdmdl=22575&refresh=698fcf739ec3b1771032435",
            "https://pastaza.gob.ec/download/jefe-de-presupuesto/?wpdmdl=22591&refresh=698fcf739f1e01771032435",
            "https://pastaza.gob.ec/download/jefe-de-desarrollo-productivo/?wpdmdl=22581&refresh=698fcf739f7851771032435",
            "https://pastaza.gob.ec/download/jefe-de-estudios-y-proyectos/?wpdmdl=22583&refresh=698fcf739fdb21771032435",
            "https://pastaza.gob.ec/download/jefe-de-mecanica-y-mantenimiento/?wpdmdl=22587&refresh=698fcf73a039e1771032435",
            "No disponible",
            "No disponible",
            "https://pastaza.gob.ec/download/jefe-de-seguridad-y-salud-ocupacional/?wpdmdl=22593&refresh=698fcf73a097a1771032435",
            "https://pastaza.gob.ec/download/jefe-de-servicios-generales/?wpdmdl=22595&refresh=698fcf73a0f481771032435",
            "https://pastaza.gob.ec/download/jefe-de-talento-humano/?wpdmdl=22597&refresh=698fcf73a15591771032435",
            "https://pastaza.gob.ec/download/jefe-de-tics/?wpdmdl=22599&refresh=698fcf73a1b2f1771032435",
            "https://pastaza.gob.ec/download/jefe-de-turismo/?wpdmdl=22601&refresh=698fcf73a21081771032435",
            "https://pastaza.gob.ec/download/jefe-de-cooperacion-nacional-e-internacional/?wpdmdl=22579&refresh=698fcf73a26d41771032435",
            "https://pastaza.gob.ec/download/contador-general/?wpdmdl=22577&refresh=698fcf73a2c8a1771032435",
            "No disponible",
            "https://pastaza.gob.ec/download/jefe-de-unidad-vial/?wpdmdl=22604&refresh=698fcf73a32261771032435"
        ]
    }

    df = pd.DataFrame(data)

    # Función para botones estilizados
    def make_button(url):
        if url.startswith("http"):
            return f'<a href="{url}" target="_blank" class="btn-declaracion">📄 Ver / Descargar Declaración</a>'
        else:
            return '<span class="no-disponible">No disponible</span>'

    # Búsqueda
    search = st.text_input("Busca por nombre o cargo:")
    if search:
        df_filtered = df[df.apply(lambda row: search.lower() in row["Nombre"].lower() or search.lower() in row["Cargo"].lower(), axis=1)]
    else:
        df_filtered = df

    # Tabla con botones
    df_styled = df_filtered.style.format({"Declaración Juramentada": make_button})
    st.dataframe(df_styled, use_container_width=True, hide_index=True)

elif seccion == "Descargas - Plan de Acción":
    st.markdown("### Descargas directas del Plan de Acción de Gobierno Abierto")
    st.markdown("- [Plan.pdf](https://datos.pastaza.gob.ec/descargas/Plan.pdf)")
    st.markdown("- [Matriz.pdf](https://datos.pastaza.gob.ec/descargas/Matriz.pdf)")
    st.markdown("- [Imagen.pdf](https://datos.pastaza.gob.ec/descargas/Imagen.pdf)")
    st.markdown("Más recursos en el portal principal.")

else:
    st.components.v1.iframe(urls[seccion], height=1000, scrolling=True)

# Footer sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("App oficial del Gobierno Provincial de Pastaza 👏")
st.sidebar.markdown("Desarrollada con ❤️ por Grok - Feb 2026")
st.sidebar.markdown("André Granda - Prefecto de Pastaza 2023 - 2027")