import pandas as pd
import streamlit as st

st.set_page_config(page_title="My First App", page_icon="🚀", layout="wide")


# ---------------------------------------------------------- fake data
@st.cache_data
def load_data():
    """Simple fake sales data (easy to read every value)."""
    df = pd.DataFrame({
        "region":  ["Cairo", "Alex", "Giza", "Cairo", "Alex", "Giza"],
        "product": ["Food", "Drinks", "Snacks", "Drinks", "Food", "Snacks"],
        "units":   [10, 20, 15, 30, 25, 5],
        "price":   [5.0, 3.5, 2.0, 3.5, 5.0, 2.0],
    })
    df["revenue"] = df["units"] * df["price"]
    return df


# ---------------------------------------------------------- pages
def home():
    st.title("🚀 My First Streamlit App")
    st.write("Welcome! This app is made with **Python only**.")

    st.subheader("How Streamlit works")
    st.markdown("""
    1. Write a normal Python script.
    2. Streamlit turns it into a web page.
    3. Every time the user changes a widget, the script runs again.
    """)

    st.subheader("Try it")
    name = st.text_input("What is your name?", "Student")
    st.write(f"Hello, **{name}**! 👋")


def widgets():
    st.header("1. Widgets (inputs)")

    name  = st.text_input("Name", "Ali")
    age   = st.slider("Age", 0, 100, 20)
    color = st.selectbox("Favourite color", ["Red", "Green", "Blue"])
    likes = st.checkbox("I like Python")
    skills = st.multiselect("Skills", ["Pandas", "NumPy", "SQL"], ["Pandas"])

    st.divider()
    st.subheader("You entered:")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Color:", color)
    st.write("Likes Python:", likes)
    st.write("Skills:", skills)


def data_page():
    st.header("2. Data & Charts")

    df = load_data()
    st.subheader("The data")
    st.dataframe(df)

    st.subheader("Total revenue")
    st.metric("Revenue", f"${df['revenue'].sum():,.0f}")

    st.subheader("Revenue by region")
    st.bar_chart(df.groupby("region")["revenue"].sum())

    st.subheader("Filter")
    region = st.selectbox("Choose a region", df["region"].unique())
    st.dataframe(df[df["region"] == region])


def chat_page():
    st.header("3. Chat")
    st.write("A simple chat that repeats what you say. Later you can connect a real AI model.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    if prompt := st.chat_input("Type a message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": f"You said: {prompt}"})
        st.rerun()


# ---------------------------------------------------------- navigation
PAGES = {
    "🏠 Home": home,
    "1 · Widgets": widgets,
    "2 · Data & Charts": data_page,
    "3 · Chat": chat_page,
}

page = st.sidebar.radio("Go to", list(PAGES))
PAGES[page]()