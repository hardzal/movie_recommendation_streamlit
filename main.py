import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


option = st.sidebar.selectbox(
    'Menu:',
    ('Home','Explore Data',  'Recommendation', 'About')
)

@st.cache_data
def load_data():
    url = "http://data.insideairbnb.com/japan/kant%C5%8D/tokyo/2022-12-29/visualisations/listings.csv"
    return pd.read_csv(url)

@st.cache_data
def load_movie():
    return pd.read_csv('./movies.csv')

@st.cache_data
def load_rating():
    return pd.read_csv('./ratings.csv')

if option == 'Home' or option == '':
    st.write("""# Homepage """)
    
    st.title("Streamlit Tutorial")
    st.markdown("Ini contoh penerapan markdown pada streamlit")
    st.markdown("Contoh penulisan warna teks :red[merah], dan ini penerapan warna **:blue[biru]** and bold")
    st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pytagorean theorem. :pencil2:")
    
    
    st.header("Header text")
    st.subheader("Ini subheader")
    st.subheader("Subheader dengan _italics_ :blue[colors] and emojis :sunglasses:")
    st.caption("Ini contoh tulisan caption")
    code_example = '''def hello_world():
    print("Hello World")'''
    st.text("Ini teks")
  
    st.code(code_example, language='python')
    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
    
    st.subheader("Daftaframe load")
    df = load_data()
    st.write(df.head())

    st.subheader("Contoh penampilan data map, \"Lokasi property yang mahal di Tokyo\"")
    st.map(df.query("price>=50000")[["latitude","longitude"]].dropna(how="any"))

    st.subheader("Penerapan Multiselect")
    st.write("Dari kolom sebanyak {df.shape[1]} kolom, pilihakan kolom yang ingin ditampilkan")
    defaultcols = ["name", "host_name", "neighbourhood", "room_type", "price"]
    cols = st.multiselect("Columsn", df.columns.tolist(), default=defaultcols)
    st.dataframe(df[cols].head(10))

    # pada table data yang ada bersifat static
    st.subheader("Penerapan Table (static)")
    st.table(df.groupby("room_type").price.mean().reset_index()\
        .round(2).sort_values("price", ascending=False)\
        .assign(avg_price=lambda x: x.pop("price").apply(lambda y: f"${y}")))
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    st.subheader("Penerapan JSON")
   
    data_movie = load_movie()
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")
    st.json({
      "movie1": {
        "movieId": data_movie.iloc[0]['movieId'],
        "title": data_movie.iloc[0]['title'],
        "genres": data_movie.iloc[0]['genres'],
       }
    })

    values = st.sidebar.slider("Price range", float(df.price.min()), 100000., (5000., 30000.))
    f = px.histogram(df.query(f"price.between{values}"), x="price", nbins=15, title="Price distribution")
    f.update_xaxes(title="Price")
    f.update_yaxes(title="No. of listings")
    st.plotly_chart(f, use_container_width=True)

    x = st.slider('x')
    st.write("""## Perhitungan Slider """)
    st.write(x, """x squared is""", x*x)

    pics = {
        "Cat": "https://www.dcnewsnow.com/wp-content/uploads/sites/14/2022/07/Cat.jpg",
        "Dog": "https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg",
        "Guine Pig": "https://www.catexpert.co.uk/wp-content/themes/shopperpress/thumbs/portrait.jpg"
    }

    pic_select = st.selectbox("Picture choices", list(pics.keys()), 0)
    st.image(pics[pic_select], use_column_width=True, caption=pics[pic_select])

    st.write("finally!")
    btn = st.button("Celebrate!")
    if btn:
        st.balloons()
elif option == 'Explore Data':
    st.write(""" # Explore Data """)

    st.subheader("Data Movie")
    st.dataframe(load_movie())

    st.subheader("Data Rating")
    st.dataframe(load_rating())
elif option == 'Recommendation':
    st.header("Recommendation")
    
elif option == 'About':
    st.write(""" # About """)




    

