
#-------------------- LIBRERÍAS NECESARIAS-------------------------#

#Librerías fundamentales

import streamlit as st
import numpy as np
import pandas as pd

#Librerías de visualización
import matplotlib.pyplot as plt
import plotly_express as px
import plotly.graph_objects as go
import seaborn as sns
from matplotlib.image import imread
import matplotlib.image as mpimg

#Librerías de mapas
import folium 

#Librerías técnicas
import base64
from streamlit_option_menu import option_menu
from PIL import Image
import os
from folium.plugins import MarkerCluster
from IPython.display import IFrame

from pydantic import class_validators

from scipy.stats import chi2_contingency



#---------------------------- COSAS QUE PODEMOS USAR EN TODA NUESTRA APP ----------------------------

# Importamos los 3 datasets del proyecto
df_meteorites = pd.read_csv("datasets proyecto final/meteorite-landings.csv")
df_exo = pd.read_csv("datasets proyecto final/all_exoplanets_2021.csv")

#------------------ CONFIGURACIÓN DE PÁGINA ----------------

st.set_page_config(page_title="COSMIC EXPLORATION",
        layout="centered",
        page_icon="🏠",
        )



# Creo una hoja de estilo para toda la página
st.markdown(
    f"""
    <style>
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    [data-testid="stSidebar"]{{                 
    background-color: rgba(0, 0, 0, 0);
    border: 0.5px solid #ff4b4b;
        }}
    [data-testid="stMarkdownContainer"]{{                 
    color: #d9ad26;
    text-align: center;
    font-size: 35px;
        }}

    [data-testid="stMarkdownContainer"] {{
    background-color: rgba(0, 0, 0, 0);
    }}

    .stMetric {{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    }}

    .menu .nav-item .nav-link.active[data-v-4323f8ce] {{
    background-color: #dddad;
    }}


    table {{
        border-collapse: collapse;
        width: 60%;
    }}

    th {{
    background-color: #d9ad26;
    color: black;
    text-align: left;
    padding: 8px;
    }}

    td {{
    background-color: white;
    color: black;
    text-align: left;
    padding: 8px;
    border-bottom: 1px solid #ddd;
    }}


    </style>
    """
 , unsafe_allow_html=True)



#Establecemos la imagen de fondo de la app
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
     <style>
        .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local(r"imagenes/background5.png")

# Esto sirve para quitar la advertencia de algunos gráficos
st.set_option('deprecation.showPyplotGlobalUse', False)




#### MENÚ ####
menu = option_menu(None, ["Introduction", "Meteorites",  "Exoplanets", 'Space Missions'], 
    #icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important", 
            "background-image": "url('https://graficareal.pe/wp-content/uploads/2019/03/8.CMYKDORADO-1024x724.jpg')",
            "background-size": "cover",
            "border-radius": "0px"
        },

        #"container": {"padding": "0!important", "background-color": "#a87b05", "border-radius": "0px"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "18px", "text-align": "center", "margin":"3px", "--hover-color": "#333", "transition": "background-color 0.2s ease","color": "black", "font-weight": "bold"},
        "nav-link-selected": {"background-color": "#333", "color": "white"},
    }
)


# _______________________________________________________________________________


if menu == "Introduction":



    st.title("Meteoritos, misiones espaciales y exoplanetas: un viaje basado en datos")

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)


    st.image("imagenes/periodico.png")
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style='font-size: 20px; color: #d9ad26; font-family: Cabin, sans-serif; font-weight: bold; text-align: center;'>
        "¿Y si este titular es más real de lo que pensamos? ¿Se puede salvar a la humanidad con datos?"
        """, unsafe_allow_html=True)

    
    # Separación
    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea
    

    st.markdown(
        """
        <div style='font-size: 18px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: normal; text-align: left;'>
        En este proyecto...
        """, unsafe_allow_html=True)
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='font-size: 14px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: bold; text-align: center;'>
        Analizaremos un conjunto de datos sobre meteoritos, donde resolveremos cuestiones como:
        """, unsafe_allow_html=True)

    st.caption("""
        - ¿Qué masa media tienen los meteoritos que hemos registrado?
        - ¿En qué años se registraron más meteoritos?
        - ¿Dónde han caído los meteoritos? ¿En qué hemisferio se han registrado más? 
        """)

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style='font-size: 14px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: bold; text-align: center;'>
        Analizaremos un conjunto de datos sobre exoplanetas, donde resolveremos cuestiones como:
        """, unsafe_allow_html=True)

    st.caption("""
        - ¿En qué años se descubrieron más exoplanetas? ¿Cuándo fue el primero?
        - ¿Cuál es el método más efectivo para encontrarlos?
        - ¿Cuál es el centro de descubrimiento más importante?
        """)
    
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style='font-size: 14px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: bold; text-align: center;'>
        Analizaremos un conjunto de datos sobre todas las misiones espaciales, donde resolveremos cuestiones como:
        """, unsafe_allow_html=True)

    st.caption("""
        - ¿Qué porcentaje de misiones espaciales ha sido un éxito y cuál es la tasa de fracaso?
        - ¿Qué países han mandado más misiones espaciales?
        - ¿Cuál es la compañía con mejor porcentaje de éxito?
        """)
    
    # Separación
    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea
    

    st.markdown(
        """
        <div style='font-size: 18px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: normal; text-align: left;'>
        El objetivo de este proyecto será analizar estos tres conjuntos de datos para estudiar el peligro de impacto por parte de los
        meteoritos y encontrar patrones de comportamiento. Por otro lado, se analizarán los exoplanetas que nos puedan alojar en un futuro.
        Y terminaremos analizando las misiones espaciales para encontrar los parámetros que han cosechado mejor éxito en las misiones.
        """, unsafe_allow_html=True)
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)


if menu == "Meteorites":    


    ##PREPROCESAMIENTO DENTRO DE METEORITES
    #Creo dos variables para filtrar el dataset y poder representar mejor las masas de los meteoritos
    meteoritos_pequeños = df_meteorites[df_meteorites['mass'] < 100]
    meteoritos_gigantes = df_meteorites[df_meteorites['mass'] > 2000000]

    #Filtrado para el dataframe del top 5 de meteoritos
    top_5_mass = df_meteorites.nlargest(5, "mass")
    top_5_mass = top_5_mass.dropna()
    top_5_mass = top_5_mass[~top_5_mass.isin([np.inf, -np.inf]).any(1)]
    top_5_mass["mass"] = top_5_mass["mass"].astype(int)
    top_5_mass["year"] = top_5_mass["year"].astype(int)

    #Filtrado para el histograma del tiempo
    data_1500_2020 = df_meteorites[(df_meteorites["year"] >= 1930) & (df_meteorites["year"] <= 2012)]




    #Ponemos dos columnas para datos generales
    col1, col2= st.columns(2)
    with col1:
        st.subheader("Meteoritos registrados hasta ahora:")
        metric_value = "45.716"
        st.markdown(f"""
            <div class="stMetric">
                {metric_value}
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.subheader("Toneladas de materia extraterrestre:")
        metric_value = "605.2"
        st.markdown(f"""
            <div class="stMetric">
                {metric_value}
            </div>
        """, unsafe_allow_html=True)
    

    # Separación
    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    #Ponemos el dataframe para poder investigarlo
    st.subheader("Dataframe Meteoritos")
    st.dataframe(df_meteorites)

    # Separación
    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea


    # st.markdown(
    #     """
    #     <div style='font-size: 22px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: bold; text-align: center;'>
    #     Correlación de variables
    #     """, unsafe_allow_html=True)
    st.subheader("Correlación de variables")

    # Gráfica correlación
    # Spearman sirve para comprobar la relación lineal entre dos variables.
    corr = df_meteorites.corr(method = 'spearman').sort_values(by = 'id', axis = 0, ascending = False).sort_values(by = 'id', axis = 1, ascending = False).round(1)
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(10,7))
    f.set_facecolor((0, 0, 0, 0))  # color transparente
    cmap = "coolwarm"
    img = imread(r"imagenes/pexels-pixabay-220201.jpg")
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr.iloc[0:5,0:5], mask=mask[0:5,0:5], cmap=cmap, vmax=1, center=0,
        square=True ,linewidths=.1, linecolor="black", cbar_kws={"shrink": 0.9},annot = True, annot_kws={"size": 10})
    cbar = ax.collections[0].colorbar
    cbar.set_ticks([-1,0,1])
    cbar.set_ticklabels(["-1","0","1"])
    for t in cbar.ax.get_yticklabels():
        t.set_color("white")
    ax.tick_params(axis='x', labelcolor='white')
    ax.set_xticklabels(ax.get_xticklabels(),fontsize=10 , color='white', rotation= 0)  # Variables blancas
    ax.set_yticklabels(ax.get_yticklabels(),fontsize=10 , color='white')  # Variables blancas
    plt.imshow(img, zorder=0, extent=[0, 6, 0, 5], origin="lower")

    st.pyplot(f)

    # Comentario matriz de correlación
    st.caption("""
    Se ha usado la matriz de correlación de tipo Spearman para analizar la correlación de las variables del dataset. Sin embargo,
    después de analizarlo no encontré ninguna relación apreciable en los datos.
    """)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) #Línea


    st.subheader("¿Qué masa tienen los meteoritos que caen en nuestro planeta?")

    fig = px.histogram(meteoritos_pequeños, x='mass', nbins=50, height=400)
    fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode="overlay",
    bargap=0.1,
    bargroupgap=0.2,
    )
    fig.update_xaxes(
    tickvals = list(range(0, 100, 10)),
    ticktext = list(range(0, 100, 10))
    )

    # Cambiamos el color de las barras
    for i in range(len(fig.data)):
        fig.data[i].marker.color = "#d9ad26"
        fig.data[i].marker.line.width = 1
        fig.data[i].marker.line.color = "#d9ad26"
    
    
    st.plotly_chart(fig)
    # Comentario masa meteoritos
    st.caption("""
    Se puede observar en este histograma la distribución de la masa de los meteoritos. Según los datos, la gran mayoría
    de los meteoritos son polvo estelar al atravesar la atmosfera, contando con unas pocas decenas de gramos. Esta representación
    está filtrada de 0 a 100 gr.
    """)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) #Línea


    #Imagen de violín para la distribución de la masa
    st.markdown("""
    <style>
    img {display: block; margin-left: 10px; margin-right:auto; width: 900px;}
    </style> """, unsafe_allow_html=True)
    st.image("imagenes/newplot.png")
    st.caption("""
    Con este gráfico de violín podemos observar la verdadera relación de todo el espectro de la distribución de los meteoritos según su masa.
    Aunque se pueden observar algunos meteoritos con toneladas, podemos observar que son casos aislados. La gran mayoría de ellos
    no supera el kilogramo de masa.
    """)


    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) #Línea

    
    #Top 5 meteoritos
    st.subheader("¿Cuáles son los 5 meteoritos más grandes que hay registrados?")
    st.dataframe(top_5_mass)
    st.caption("""
    Podemos obsevar a raíz de este dataframe el top 5 de los meteoritos más grandes que tenemos registrados.
    Hoba, el meteorito más extraordinario del mundo fue descubierto al norte de Namibia, en África. 
    """)


    st.markdown("""
    <style>
    img {display: block; margin-left: 10px; margin-right:auto; width: 680px;}
    </style> """, unsafe_allow_html=True)
    st.image("imagenes/hoba.PNG")
    

    if st.button("Píldoras de información"): 
        st.caption("""
        - Un asteroide y un meteorito no son lo mismo. Un asteroide es un objeto rocoso o metálico que se
            encuentra en el espacio y gira alrededor del sol. Mientras que el meteorito es un asteroide que ha entrado
            en la atmósfera de la Tierra y ha alcanzado la superficie.
        - El meteorito que se cree que provocó la extinción de los dinosaurios tuvo unas dimensiones estimadas
            de 10 a 15km. Su masa podría haber sido de miles de millones de toneladas.
        - El meteorito más grande que ha caído en españa tiene 162kg de masa, lo que equivaldría a 30 cm de diámetro.
        """)




    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) #Línea


    st.subheader("¿En qué años se han descubiertos más meteoritos?")
    #Histograma de descubrimientos
    fig3 = px.histogram(data_1500_2020, x='year', nbins=100, height=400)
    fig3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    barmode="overlay",
    bargap=0.1,
    bargroupgap=0.2,
    )
    fig3.update_xaxes(
    tickvals = list(range(1930, 2012, 5)),
    ticktext = list(range(1930, 2012, 5))
    )
    # Cambiamos el color de las barras
    for i in range(len(fig.data)):
        fig3.data[i].marker.color = "#d9ad26"
        fig3.data[i].marker.line.width = 1
        fig3.data[i].marker.line.color = "#d9ad26"
    st.plotly_chart(fig3)

    st.caption("""
    En este histograma podemos obsevar la relación de descubrimientos de estos cuerpos celestes a lo largo del tiempo.
    está filtrado desde el año 1930 por no haber nada relevante los años anteriores. Es el año 2003 el año de mayor número
    de descubrimientos, con 3323 meteoritos.
    """)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) #Línea

    st.subheader("¿Dónde han caído todos los meteoritos registrados?")
    # Leemos el mapa de
    path_to_html = "./mapa_espana.html"
    # Read file and keep in variable
    with open(path_to_html,'r') as f: 
        html_data = f.read()

    # Mostramos mapa
    st.components.v1.html(html_data,height=400)    

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) #Línea

    #Filtrado y gráfica de tarta de la distribución por hemisferios de la caída de los meteoritos
    st.subheader("¿En qué hemisferio hay más tendencia de caída de meteoritos?")

    df_meteorites['hemisferio'] = np.where((df_meteorites['reclat'] >= 0) & (df_meteorites['reclong'] >= 0), 'Norte-Este',
                            np.where((df_meteorites['reclat'] >= 0) & (df_meteorites['reclong'] < 0), 'Norte-Oeste',
                            np.where((df_meteorites['reclat'] < 0) & (df_meteorites['reclong'] >= 0), 'Sur-Este',
                                     'Sur-Oeste')))

    grouped3 = df_meteorites.groupby('hemisferio').count()['name']
    # Crea una tarta con los datos
    fig4 = px.pie(grouped3, values='name', names=grouped3.index)
    fig4.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", # fondo transparente
    )
    st.plotly_chart(fig4)

    st.caption("""
    Gracias a las coordenadas se ha podido extraer esta clasificación por hemisferios para obtener
    un patrón de dónde han sido registrados más meteoritos. Podemos encontrar con diferencia, un mayor volumen en el hemisferio 
    sur, más concretamente en el sureste.
    He de destacar que estos datos no son fieles si lo que queremos es saber dónde han caído más meteoritos, ya que estas caídas
    coinciden con haber sido encontrados por el ser humano. Es por ello que en zonas poco exploradas apenas hay registros.
    """)





if menu == "Exoplanets":



    ####  Preprocesamiento de exoplanets ----------------------------------------------------------------------------------------------

    # Elijo las variables que me interesan para mi objetivo
    df_exo = df_exo[['Planet Name', 'Discovery Method','Discovery Year', 'Discovery Facility', 'Orbital Period Days',
    'Orbit Semi-Major Axis' , 'Mass', 'Eccentricity', 'Equilibrium Temperature', 'Distance', 'Gaia Magnitude']]


    


    ####  Contenido de exoplanets -----------------------------------------------------------
    
    col1, col2, col3= st.columns(3)
    with col1:
        st.subheader("Exoplanetas descubiertos hasta el 2012:")
        metric_value = "4.575"
        st.markdown(f"""
            <div class="stMetric">
                {metric_value}
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.subheader("Años luz del exoplaneta más cercano:")
        metric_value = "1.30119"
        st.markdown(f"""
            <div class="stMetric">
                {metric_value}
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.subheader("Temperatura del exoplaneta más caluroso")
        metric_value = "4050 K-3776 °C"

        st.markdown(f"""
            <div class="stMetric">
                {metric_value}
            </div>
        """, unsafe_allow_html=True)

    # Separación
    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    #Ponemos el dataframe para poder investigarlo
    st.subheader("Dataframe Exoplanetas")
    st.dataframe(df_exo)



    # Separación
    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    
    st.subheader("Correlación de variables")
    corr = df_exo.corr(method = 'spearman').sort_values(by = 'Discovery Year', axis = 0, ascending = False).sort_values(by = 'Discovery Year', axis = 1, ascending = False).round(1)
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(10,7))
    f.set_facecolor((0, 0, 0, 0))  # color transparente
    cmap = "coolwarm"
    img = imread(r"imagenes/exoplaneta.jpg")
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr.iloc[0:5,0:5], mask=mask[0:5,0:5], cmap=cmap, vmax=1, center=0,
        square=True ,linewidths=.1, linecolor="black", cbar_kws={"shrink": 0.9},annot = True, annot_kws={"size": 10})
    cbar = ax.collections[0].colorbar
    cbar.set_ticks([-1,0,1])
    cbar.set_ticklabels(["-1","0","1"])
    for t in cbar.ax.get_yticklabels():
        t.set_color("white")
    ax.tick_params(axis='x', labelcolor='white')
    ax.set_xticklabels(ax.get_xticklabels(),fontsize=9 , color='white', rotation= 20)  # Variables blancas
    ax.set_yticklabels(ax.get_yticklabels(),fontsize=9 , color='white', rotation= 70)  # Variables blancas
    plt.imshow(img, zorder=0, extent=[0, 6, 0, 5], origin="lower")
    st.pyplot(f)    

    #Explicación Matriz de correlación
    st.caption("""
    Se ha usado la matriz de correlación de tipo Spearman para analizar la correlación de las variables del dataset. 
    Únicamente, las variables "Distancia" y "Magnitud Gaia" tienen una correlación significativa. Lo cuál, tiene sentido, ya que
    la Magnitud Gaia es un indicador de luminosidad de la estrella anfitriona del exoplaneta. Por ello, cuánto más lejos esté el exoplaneta, 
    más magnitud gaia tendrá, que significa que la luminosidad será más débil. 
    """)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    st.subheader("¿En qué años se han descubierto más exoplanetas?")
    exoplanetas_por_ano = df_exo.groupby("Discovery Year").count().reset_index() 

    fig5 = go.Figure()
    fig5.add_trace(go.Bar(
    x=exoplanetas_por_ano["Discovery Year"],
    y=exoplanetas_por_ano["Planet Name"],
    # name='Exoplanetas por año',
    text=exoplanetas_por_ano["Planet Name"],
    texttemplate="%{y}",
    textposition="outside",
    marker_color="#d9ad26"
    ))
    fig5.update_traces(textfont_color='white')
    fig5.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig5)
    st.caption("""
        - Aunque el satélite Kepler fue lanzado en marzo de 2009 y ya comenzó a registrar algunos planetas, fue en 2014 cuando se anunció un gran número de descubrimientos de exoplanetas gracias a los datos recopilados por el satélite Kepler en los años anteriores. Este satélite utilizaba el método de tránsito para detectar planetas fuera de nuestro sistema solar. 
        - En 2016, se anunció el descubrimiento del exoplaneta más cercano a la Tierra hasta la fecha, llamado Proxima Centauri b, utilizando la técnica de velocidad radial. Este descubrimiento generó un gran interés en la búsqueda de exoplanetas cercanos y habitables. Es por ello que durante este año se invirtió más en este tipo de investigación.
    """)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    st.subheader("¿Existe algún patrón entre el descubrimiento de exoplanetas con su Centro o Instalación de descubrimiento?")
    df_exo_grouped = df_exo.groupby(["Discovery Year", "Discovery Facility"]).size().reset_index(name="count")
    df_exo_grouped = df_exo_grouped.sort_values(by="count", ascending=False)
    fig8 = px.bar(df_exo_grouped, x="Discovery Year", y="count", color="Discovery Facility", barmode="stack")
    fig8.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig8)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    st.subheader("¿Cuál es el Centro de Descubrimiento que más exoplanetas ha descubierto?")
    fig7 = px.pie(df_exo["Discovery Facility"].value_counts().head(5), values=df_exo["Discovery Facility"].value_counts().head(5).values,
    names=df_exo["Discovery Facility"].value_counts().head(5).index)
    fig7.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig7)   
    st.caption("""
        El satélite Kepler es la plataforma de descubrimientos más importante. Operó 9 años, desde 2009 hasta 2018 y durante
        su misión detectó más de 2600 exoplanetas confirmados, además de varios miles de candidatos a
        exoplanetas que aún están en proceso de validación.
    """)




    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    st.subheader("¿Cuál fue el primer exoplaneta descubierto?")
    st.dataframe(df_exo[df_exo["Discovery Year"]==1995])

    st.image("imagenes/51pegasib.PNG")

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea



    st.subheader("¿Cuál es el método de descubrimiento más efectivo?")
    # Contar las ocurrencias de cada método de descubrimiento
    metodos = df_exo["Discovery Method"].value_counts().reset_index()
    metodos.columns = ["Discovery Method", "Count"]
    # Crear el gráfico de embudo
    fig6 = px.funnel(metodos, x="Discovery Method", y="Count", 
    color_discrete_sequence=['#d9ad26'],
    opacity=1,
    template='none')
    fig6.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
    font_color='white', xaxis_title="", xaxis_title_standoff=10, xaxis_tickangle=20)
    st.plotly_chart(fig6)

    #Explicación gráfico funnel del método de descrubrimiento más efectivo.
    st.caption("""
        Se puede observar que los dos métodos más efectivos son el tránsito (Transit) y la velocidad radial (Radial Velocity),
        con un gran número de exoplanetas descubiertos utilizando cada uno de ellos.
        - El método de tránsito se basa en la observación de la disminución del brillo de una estrella cuando un planeta pasa frente a ella (transita).
        - El método de velocidad radial se basa en la detección de pequeñas fluctuaciones en la velocidad de una estrella causadas por la presencia de un planeta en órbita alrededor de ella.
    """)
    





if menu == "Space Missions":

    #PREPROCESAMIENTO DEL DATASET DE SPACE MISSIONS
    # Importamos Data de las misiones espaciales
    df_missions = pd.read_csv("datasets proyecto final/space_missions.csv",encoding = "ISO-8859-1", skipinitialspace = True)
    df_missions_dictionary = pd.read_csv("datasets proyecto final/space_missions_data_dictionary.csv")


    # Extraemos de Location el país y creamos una nueva columna con ello
    df_missions['Country'] = df_missions['Location'].str.extract(r',\s*([A-Za-z ]+)$')

    # Borramos la variable Time, ya que no me aporta demasiada información
    df_missions = df_missions.drop('Time', axis=1)

    # Cambiamos el tipo de columna de object a formato fecha para Date
    df_missions['Date'] = pd.to_datetime(df_missions['Date'], utc=True).dt.date
    df_missions['Date'] = pd.to_datetime(df_missions['Date'])


    # Creamos una copia del dataframe sin valores nulos, para analizar los precios aparte
    df_missions_price = df_missions.dropna()

    # Del nuevo df con el precio limpio, quitamos las "," y hacemos la variable numérica
    df_missions_price.Price = df_missions_price.Price.astype(str).str.replace(',', '')
    df_missions_price.Price = pd.to_numeric(df_missions_price.Price)






    # CONTENIDO SPACE MISSIONS -------------------------------------------------------


    col1, col2, col3= st.columns(3)
    with col1:
    
        st.markdown(
        """
        <div style='font-size: 16px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: bold; text-align: center;'>
        Total de misiones espaciales en el dataset:
        """, unsafe_allow_html=True)
        metric_value = "4.630"
        st.markdown(f"""
            <div class="stMetric">
                {metric_value}
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(
        """
        <div style='font-size: 16px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: bold; text-align: center;'>
        Tipos de cohetes usados en las misiones: 
        """, unsafe_allow_html=True)
        metric_value = "370"
        st.markdown(f"""
            <div class="stMetric">
                {metric_value}
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(
        """
        <div style='font-size: 16px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: bold; text-align: center;'>
        Millones invertidos en las misiones: 
        """, unsafe_allow_html=True)
        metric_value = "162.304"

        st.markdown(f"""
            <div class="stMetric">
                {metric_value}
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    st.subheader("Dataframe Misiones Espaciales")
    st.dataframe(df_missions)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    # Opciones del selectbox
    options = {
        'Tabla de contingencia cruzada con ["Country" , "MissionStatus"]': 'Seleccionaste la opción 1',
        'Tabla de contingencia cruzada con ["Rocket" , "MissionStatus"]': 'Seleccionaste la opción 2'
    }

    st.subheader("¿Existe relación entre el país o el tipo de cohete con el éxito de la misión?")

    # Mostrar el selectbox en Streamlit
    option_selected = st.selectbox('Selecciona una opción', list(options.keys()))


    # Mostrar contenido dependiendo de la opción seleccionada
    if option_selected == 'Tabla de contingencia cruzada con ["Country" , "MissionStatus"]':
        
        df_country_missionstatus = df_missions[['Country', 'MissionStatus']]
        ct = pd.crosstab(df_country_missionstatus['Country'], df_country_missionstatus['MissionStatus'])

        st.image('imagenes\contingencia1.png')
        st.code("chi2, pval, dof, expected = chi2_contingency(ct)")
           
        # muestra el resultado
        st.text("""
        Chi-cuadrado: 744.0847364407593
        p-valor: 4.972397480935078e-117
        """)

        st.caption("""
        El análisis de las variables Country y MissionStatus muestra un valor del chi-cuadrado de 744.08 y
        un p-valor muy pequeño de 4.97e-117, lo que indica una relación significativa entre ambas variables.
        Esto sugiere que la tasa de éxito de las misiones varía significativamente entre los países en los
        que se realizan las misiones espaciales, lo que puede estar relacionado con factores como la infraestructura,
        la tecnología, la inversión y la experiencia en misiones espaciales.
        """)

    elif option_selected == 'Tabla de contingencia cruzada con ["Rocket" , "MissionStatus"]':
        
        df_country_missionstatus = df_missions[['Rocket', 'MissionStatus']]
        ct = pd.crosstab(df_country_missionstatus['Rocket'], df_country_missionstatus['MissionStatus'])

        st.image('imagenes\contingencia2.png')
        st.code("chi2, pval, dof, expected = chi2_contingency(ct)")


        # muestra el resultado
        st.text("""
        Chi-cuadrado: 31.299732587761305
        p-valor: 0.02657119040683537
        """)

        st.caption("""
        El análisis de relación entre las variables Rocket y MissionStatus, muestran un valor del chi-cuadrado es de 31.3 con un p-valor
        de 0.027. Esto significa que existe una relación significativa entre la variable Rocket y MissionStatus.
        En otras palabras, el resultado del análisis indica que la proporción de misiones exitosas y fallidas difiere
        significativamente entre los cohetes utilizados en las misiones.
        """)
        


    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea


    st.subheader("¿Qué porcentaje de misiones espaciales ha sido un éxito y cuál es la tasa de fracaso?")


    fig8 = px.pie(df_missions["MissionStatus"].value_counts(), values=df_missions["MissionStatus"].value_counts().values,
    names=df_missions["MissionStatus"].value_counts().index)
    fig8.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig8)



    ### CREAMOS BOTÓN DE MÁS INFORMACIÓN
    # Inicializar el estado de alternancia como falso
    toggle_state = False

    # Crear un botón que se utiliza para alternar el estado
    if st.button('Ampliar información', key="boton1"):
        toggle_state = not toggle_state

    # Si el estado de alternancia es verdadero, mostrar el texto
    if toggle_state:

        st.markdown(
        """
        <div style='font-size: 14px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: normal; text-align: left;'>
        - Success: La misión se llevó a cabo según lo previsto y se considera un éxito. <br>
        - Failure: La misión no se llevó a cabo según lo previsto y se considera un fracaso completo.<br>
        - Partial Failure: La misión se llevó a cabo pero no se cumplieron todas las metas previstas, lo que se considera un fracaso parcial.<br>
        - Prelaunch Failure: El fracaso se produjo antes del lanzamiento, por ejemplo, durante el proceso de preparación en tierra, y la misión nunca se llevó a cabo.
        """, unsafe_allow_html=True)

        # Cambiar el estado de alternancia a falso al volver a hacer clic en el botón
        if st.button('Ocultar información'):
            toggle_state = False

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    st.subheader("¿Qué países ha mandado más misiones y qué porcentaje de éxito tienen?")

    # Creamos el histograma
    fig9= px.histogram(df_missions, x = "Country", color = "MissionStatus", text_auto=True, width=730, height=650)
    # Personalizar la apariencia del gráfico
    fig9.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig9.update_xaxes(tickangle=45)
    st.plotly_chart(fig9)

    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    st.subheader("¿Qué compañías aeroespaciales han mandado más misiones y qué porcentaje de éxito tienen?")
    # Filtrar el dataframe para incluir solo las 12 compañías principales
    top_companies = df_missions['Company'].value_counts().nlargest(12).index.tolist()
    #Creamos el histograma
    fig10 = px.histogram(df_missions[df_missions['Company'].isin(top_companies)], 
                        x='Company', 
                        color='MissionStatus', 
                        text_auto=True, 
                        category_orders={'Company': top_companies}, width=730, height=600)
    fig10.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')


    st.plotly_chart(fig10)



    ### CREAMOS BOTÓN DE MÁS INFORMACIÓN
    # Inicializar el estado de alternancia como falso
    toggle_state = False

    # Crear un botón que se utiliza para alternar el estado
    if st.button('Ampliar información', key="boton2"):
        toggle_state = not toggle_state

    # Si el estado de alternancia es verdadero, mostrar el texto
    if toggle_state:

        st.markdown(
        """
        <div style='font-size: 14px; color: #ffffff; font-family: Cabin, sans-serif; font-weight: normal; text-align: left;'>
        - RVSN USSR: Fuerza de Misiles Estratégicos de la antigua Unión Soviética. <br>
        - CASC: Corporación de Ciencia y Tecnología Aeroespacial de China. <br>
        - Arianespace: Compañía francesa que opera servicios de lanzamiento de satélites. <br>
        - General Dynamics: Compañía estadounidense que fabrica productos de defensa y tecnología. <br>
        - VKS RF: Fuerza Aeroespacial de Rusia. <br>
        - NASA: Agencia espacial estadounidense encargada de programas civiles de exploración y investigación en el espacio. <br>
        - SpaceX: Compañía estadounidense de transporte aeroespacial fundada por Elon Musk. <br>
        - US Air Force: Fuerza Aérea de los Estados Unidos. <br>
        - ULA: United Launch Alliance, una compañía conjunta entre Lockheed Martin y Boeing que proporciona servicios de lanzamiento de satélites. <br>
        - Boeing: Compañía estadounidense de aeronáutica y defensa. <br>
        - Martin Marietta: Compañía estadounidense de materiales de construcción y productos de defensa. <br>
        - Northrop: Northrop Corporation, una compañía estadounidense de productos aeroespaciales y de defensa. <br>
        """, unsafe_allow_html=True)

        # Cambiar el estado de alternancia a falso al volver a hacer clic en el botón
        if st.button('Ocultar información'):
            toggle_state = False


    st.markdown("<hr style='color:#d9ad26;background-color:#d9ad26;height:1px;'/>", unsafe_allow_html=True) # línea

    st.subheader("Rusia vs USA | La carrera espacial", )


    df_count = df_missions.groupby(['Country', pd.Grouper(key='Date', freq='Y')])['MissionStatus'].count().reset_index()
    df_count = df_count[df_count['Country'].isin(['USA', 'Russia'])]
    df_count.rename(columns={'MissionStatus': 'Count'}, inplace=True)


    fig11 = px.line(df_count, x='Date', y='Count', color='Country', markers= True, color_discrete_sequence= ["#59CCE6", "#d9ad26"])
    fig11.add_annotation(x='1991', y=30, text="Disolución de la URSS")
    fig11.add_annotation(x='1969', y=22, text="Llegada a la luna")

    fig11.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig11)











        # st.markdown(
        # """
        # <div style='font-size: 24px; color: #ff5a60; font-family: Helvetica, sans-serif; font-weight: bold;'>
        # En este proyecto nos enfocaremos en comprender mejor la presencia de Airbnb en Madrid.
        # </div>
        # <div style='font-size: 18px; color: #000000; font-family: Arial, sans-serif; font-weight: normal;'>
        # El objetivo será utilizar los datos de la plataforma para analizar tendencias en el número de viviendas disponibles, precios, ubicaciones,
        # y cómo estos factores están afectando al mercado del alojamiento en la ciudad.
        # </div>
        # <div style='font-size: 16px; color: #333333; font-family: Verdana, sans-serif; font-weight: normal;'>
        # Por último, se creará un modelo predictivo que puede ayudar a los propietarios a establecer precios realistas para sus propiedades.
        # </div>
        # """, unsafe_allow_html=True)
