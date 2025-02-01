import streamlit as st
from streamlit_option_menu import option_menu

# Konfigurasi Halaman
st.set_page_config(page_title="Portofolio Data Science", layout="wide")

# CSS untuk mengganti background utama dan sidebar
st.markdown(
    """
    <style>
        /* Background utama */
        .stApp {
            background: url("https://wc.wallpaperuse.com/wallp/78-787047_s.jpg");
            background-size: cover;
        }

        /* Sidebar dengan gambar */
        section[data-testid="stSidebar"] {
            background: url("https://cdn.prod.website-files.com/5fda9e054c8f10649883f27d/64f78ee1d49618f094e64111_vationventures_datascience.jpeg");
            background-size: cover;
            background-position: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Inisialisasi session_state untuk bahasa
if "language" not in st.session_state:
    st.session_state.language = "ID"  # Default: Bahasa Indonesia

# Pilihan bahasa dengan selectbox
with st.sidebar:
    lang = st.selectbox(
        "🌐 Pilih Bahasa | Choose Language",
        ["ID", "EN"],
        index=0 if st.session_state.language == "ID" else 1,
    )
    st.session_state.language = lang  # Simpan pilihan bahasa

# ---------------- TEKS MULTI-BAHASA ----------------
# Tambahkan Sertifikasi ke dictionary text untuk ID dan EN
text = {
    "ID": {
        "nav": [
            "Home",
            "Layanan",
            "Tentang Saya",
            "Portofolio",
            "Sertifikasi",
            "Kontak",
        ],
        "welcome": "Selamat datang di Portofolio Saya",
        "desc": "Di sini Anda dapat melihat proyek yang telah saya kerjakan serta layanan yang saya tawarkan.",
        "skills": "🛠️ Keterampilan & Alat",
        "services": "Layanan Saya",
        "about": "Tentang Saya",
        "portfolio": "Portofolio Saya",
        "contact": "Hubungi Saya",
        "certifications": "Sertifikasi Saya",
    },
    "EN": {
        "nav": [
            "Home",
            "Services",
            "About Me",
            "Portfolio",
            "Certifications",
            "Contact",
        ],
        "welcome": "Welcome to My Portfolio",
        "desc": "Here you can see the projects I have worked on and the services I offer.",
        "skills": "🛠️ Skills & Tools",
        "services": "My Services",
        "about": "About Me",
        "portfolio": "My Portfolio",
        "contact": "Contact Me",
        "certifications": "My Certifications",
    },
}


# Sidebar Navigasi dengan Sertifikasi
with st.sidebar:
    menu = option_menu(
        "Navigasi" if st.session_state.language == "ID" else "Navigation",
        text[st.session_state.language]["nav"],
        icons=[
            "house",
            "gear",
            "person",
            "briefcase",
            "file-earmark",
            "envelope",
        ],
        menu_icon="cast",
        default_index=0,
    )


# ---------------- Home ----------------
if menu == text[lang]["nav"][0]:  # Beranda / Home
    st.markdown(
        f"<h1 style='text-align: center;'>{text[lang]['welcome']}</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align: center;'>{text[lang]['desc']}</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<h3 style='text-align: center;'>{text[lang]['skills']}</h3>",
        unsafe_allow_html=True,
    )

    skills = [
        (
            "Python",
            "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
        ),
        ("R", "https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg"),
        (
            "SQL",
            "https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png",
        ),
        (
            "Pandas",
            "https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg",
        ),
        (
            "Matplotlib",
            "https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg",
        ),
        ("Seaborn", "https://seaborn.pydata.org/_images/logo-mark-lightbg.svg"),
        (
            "Tableau",
            "https://upload.wikimedia.org/wikipedia/commons/4/4b/Tableau_Logo.png",
        ),
        (
            "Excel",
            "https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg",
        ),
        (
            "Streamlit",
            "https://images.seeklogo.com/logo-png/44/2/streamlit-logo-png_seeklogo-441815.png",
        ),
        (
            "TensorFlow",
            "https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg",
        ),
        (
            "Jupyter Notebook",
            "https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg",
        ),
    ]

    cols = st.columns(5)
    for i, (name, logo) in enumerate(skills):
        with cols[i % 5]:
            st.markdown(
                f"<div style='text-align: center;'><img src='{logo}' width='50'><p>{name}</p></div>",
                unsafe_allow_html=True,
            )

# ---------------- TEKS MULTI-BAHASA UNTUK SERVICES ----------------
text_services = {
    "ID": {
        "title": "Layanan Saya",
        "services": [
            (
                "📊 Analisis Data",
                "Analisis data dengan Python dan SQL untuk menemukan pola dan tren tersembunyi.",
            ),
            (
                "🤖 Machine Learning",
                "Membangun model prediktif dengan regresi, klasifikasi, dan clustering.",
            ),
            (
                "📈 Visualisasi Data",
                "Membuat visualisasi interaktif dengan Matplotlib, Seaborn, dan Tableau.",
            ),
            (
                "📊 Data Science",
                "Mengolah, membersihkan, dan mengekstrak insight dari data bisnis dan akademik.",
            ),
            (
                "🧠 Kecerdasan Buatan (AI)",
                "Mengembangkan sistem AI seperti NLP dan Computer Vision.",
            ),
            (
                "🕸 Web Scraping",
                "Mengambil data dari website otomatis dengan BeautifulSoup dan Selenium.",
            ),
            (
                "💾 Data Warehouse",
                "Membangun sistem penyimpanan data dengan SQL, BigQuery, dan Snowflake.",
            ),
            (
                "⚡ Pemrosesan Big Data",
                "Mengelola dan menganalisis data besar dengan Hadoop dan Spark.",
            ),
            (
                "📂 Manajemen Basis Data",
                "Mengelola basis data dengan MySQL, PostgreSQL, dan MongoDB.",
            ),
            (
                "📜 Analisis Statistik",
                "Melakukan analisis statistik untuk eksperimen dan pengambilan keputusan.",
            ),
            (
                "📡 Peramalan Deret Waktu",
                "Menganalisis dan memprediksi data deret waktu dengan Python.",
            ),
            (
                "🌎 Analisis Data Geospasial",
                "Menganalisis data geografis dengan GeoPandas dan Folium.",
            ),
            ("🛠 Rekayasa Data", "Membangun pipeline data untuk pemrosesan otomatis."),
            (
                "🔍 Deteksi Kecurangan",
                "Menerapkan machine learning untuk mendeteksi anomali transaksi.",
            ),
            (
                "🎯 A/B Testing",
                "Menganalisis eksperimen bisnis untuk meningkatkan performa.",
            ),
            (
                "📌 Business Intelligence",
                "Menggunakan data untuk optimasi strategi bisnis dan operasional.",
            ),
        ],
    },
    "EN": {
        "title": "My Services",
        "services": [
            (
                "📊 Data Analysis",
                "Analyze data using Python and SQL to uncover hidden patterns and trends.",
            ),
            (
                "🤖 Machine Learning",
                "Build predictive models using regression, classification, and clustering.",
            ),
            (
                "📈 Data Visualization",
                "Create interactive visualizations using Matplotlib, Seaborn, and Tableau.",
            ),
            (
                "📊 Data Science",
                "Process, clean, and extract insights from business and academic data.",
            ),
            (
                "🧠 Artificial Intelligence (AI)",
                "Develop AI systems such as NLP and Computer Vision.",
            ),
            (
                "🕸 Web Scraping",
                "Automatically extract data from websites using BeautifulSoup and Selenium.",
            ),
            (
                "💾 Data Warehouse",
                "Build data storage systems using SQL, BigQuery, and Snowflake.",
            ),
            (
                "⚡ Big Data Processing",
                "Manage and analyze large datasets with Hadoop and Spark.",
            ),
            (
                "📂 Database Management",
                "Handle databases using MySQL, PostgreSQL, and MongoDB.",
            ),
            (
                "📜 Statistical Analysis",
                "Perform statistical analysis for experiments and decision-making.",
            ),
            (
                "📡 Time Series Forecasting",
                "Analyze and predict time-series data using Python.",
            ),
            (
                "🌎 Geographic Data Analysis",
                "Analyze geospatial data with GeoPandas and Folium.",
            ),
            ("🛠 Data Engineering", "Build data pipelines for automated processing."),
            (
                "🔍 Fraud Detection",
                "Apply machine learning to detect transaction anomalies.",
            ),
            ("🎯 A/B Testing", "Analyze business experiments to improve performance."),
            (
                "📌 Business Intelligence",
                "Use data to optimize business strategies and operations.",
            ),
        ],
    },
}

# ---------------- SERVICES PAGE ----------------
if menu == text[st.session_state.language]["nav"][1]:  # Layanan / Services
    st.markdown(
        f"<h1 style='text-align: center;'>{text_services[st.session_state.language]['title']}</h1>",
        unsafe_allow_html=True,
    )

    num_columns = 4  # Maksimal 4 kolom dalam satu baris
    services_list = text_services[st.session_state.language]["services"]
    rows = [
        services_list[i : i + num_columns]
        for i in range(0, len(services_list), num_columns)
    ]

    for row in rows:
        cols = st.columns(num_columns)
        for col, (title, desc) in zip(cols, row):
            with col:
                st.markdown(f"### {title}")
                st.write(desc)

# ---------------- TEKS MULTI-BAHASA UNTUK ABOUT ME ----------------
text_about_me = {
    "ID": {
        "title": "Tentang Saya",
        "intro": "### 👋 Hai, saya [Nama Anda]!",
        "desc": """
        Saya adalah mahasiswa yang tertarik pada **Data Science, Artificial Intelligence (AI), dan Machine Learning**.  
        Saya selalu berusaha meningkatkan keterampilan dengan terus belajar, mengikuti perkembangan teknologi,  
        dan mengerjakan proyek-proyek nyata.
        """,
        "why": "### 🔥 Mengapa Data Science?",
        "why_desc": """
        Ketertarikan saya dimulai ketika saya mengambil mata kuliah **Statistik & Pemrograman**.  
        Saya kagum bagaimana data dapat menghasilkan insight yang berharga untuk pengambilan keputusan.  
        Beberapa bidang yang saya minati:
        - 📊 **Analisis Data** → Mengungkap pola tersembunyi dalam data.
        - 🤖 **Machine Learning** → Membangun model prediktif yang cerdas.
        - 📈 **Visualisasi Data** → Menceritakan data dengan grafik interaktif.
        """,
        "goals": "### 🚀 Tujuan Saya",
        "goals_desc": """
        - Menjadi seorang **Data Scientist** atau **Machine Learning Engineer**.
        - Berkontribusi dalam proyek **AI yang berdampak positif**.
        - Terus belajar & membagikan ilmu seputar **Data Science**.
        """,
    },
    "EN": {
        "title": "About Me",
        "intro": "### 👋 Hi, I'm [Your Name]!",
        "desc": """
        I am a student passionate about **Data Science, Artificial Intelligence (AI), and Machine Learning**.  
        I always strive to improve my skills by continuously learning, keeping up with technological advancements,  
        and working on real-world projects.
        """,
        "why": "### 🔥 Why Data Science?",
        "why_desc": """
        My interest started when I took the course **Statistics & Programming**.  
        I was fascinated by how data can provide valuable insights for decision-making.  
        Some areas that interest me:
        - 📊 **Data Analysis** → Discovering hidden patterns in data.
        - 🤖 **Machine Learning** → Building smart predictive models.
        - 📈 **Data Visualization** → Telling data stories through interactive charts.
        """,
        "goals": "### 🚀 My Goals",
        "goals_desc": """
        - Become a **Data Scientist** or **Machine Learning Engineer**.
        - Contribute to **AI projects with a positive impact**.
        - Keep learning & sharing knowledge about **Data Science**.
        """,
    },
}

# ---------------- ABOUT ME PAGE ----------------
if menu == text[st.session_state.language]["nav"][2]:  # Tentang Saya / About Me
    st.markdown(
        f"<h1 style='text-align: center;'>{text_about_me[st.session_state.language]['title']}</h1>",
        unsafe_allow_html=True,
    )

    # Gunakan dua kolom: 1 untuk foto, 1 untuk deskripsi
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("profile.jpg", width=250)  # Ganti dengan foto profil Anda

    with col2:
        st.markdown(text_about_me[st.session_state.language]["intro"])
        st.write(text_about_me[st.session_state.language]["desc"])

        st.markdown(text_about_me[st.session_state.language]["why"])
        st.write(text_about_me[st.session_state.language]["why_desc"])

        st.markdown(text_about_me[st.session_state.language]["goals"])
        st.write(text_about_me[st.session_state.language]["goals_desc"])


# ---------------- Portfolio ----------------
elif menu == text[lang]["nav"][3]:  # Portofolio / Portfolio
    st.markdown(
        f"<h1 style='text-align: center;'>{text[lang]['portfolio']}</h1>",
        unsafe_allow_html=True,
    )

    projects = [
        {
            "title": "🚀 Prediksi Cuaca",
            "desc": (
                "Model prediksi cuaca menggunakan data BMKG."
                if lang == "ID"
                else "Weather prediction model using BMKG data."
            ),
        },
        {
            "title": "📊 Analisis Penjualan",
            "desc": (
                "Eksplorasi tren bisnis dengan data penjualan."
                if lang == "ID"
                else "Exploring business trends with sales data."
            ),
        },
    ]

    for project in projects:
        st.subheader(project["title"])
        st.write(project["desc"])

# ---------------- CERTIFICATIONS PAGE ----------------
if menu == text[st.session_state.language]["nav"][4]:  # Sertifikasi / Certifications
    st.markdown(
        f"<h1 style='text-align: center;'>{text[st.session_state.language]['certifications']}</h1>",
        unsafe_allow_html=True,
    )

    certifications = [
        {
            "title": "📜 Introduction to Data Science (CISCO)",
            "desc": (
                "Sertifikat yang diperoleh setelah menyelesaikan kursus Data Science di XYZ Academy."
                if st.session_state.language == "ID"
                else "Certificate obtained after completing the Data Science course at XYZ Academy."
            ),
            "date": (
                "Januari 2024" if st.session_state.language == "ID" else "January 2024"
            ),
            "link": "https://www.linkedin.com/in/andri-ihza-nasrulloh/details/certifications/1720576177582/single-media-viewer/?type=DOCUMENT&profileId=ACoAAD587H4BE7V-bOlxAqOdgo3aD8KOEnGVxxE",
            "pdf": "certificates/Introduction_to_Data_Science_Badge20231214-40-p37chz.pdf",
            "image": "certificates/Introduction_to_Data_Science.png",
        },
        {
            "title": "📜 Data Analytics Essentials (CISCO)",
            "desc": (
                "Sertifikat dari kursus Machine Learning yang diselenggarakan oleh ABC Institute."
                if st.session_state.language == "ID"
                else "Certificate from the Machine Learning course held by ABC Institute."
            ),
            "date": "Maret 2024" if st.session_state.language == "ID" else "March 2024",
            "link": "https://www.linkedin.com/in/andri-ihza-nasrulloh/details/certifications/1720576635219/single-media-viewer/?type=DOCUMENT&profileId=ACoAAD587H4BE7V-bOlxAqOdgo3aD8KOEnGVxxE",
            "pdf": "certificates/Data_Analytics_Essentials_Badge20231227-29-f8dbz1.pdf",
            "image": "certificates/Data_Analytics_Essentials.png",
        },
        # Tambahkan sertifikasi lainnya di sini jika ada...
    ]

    # Menyusun sertifikasi dalam format 3 kolom per baris
    for i in range(0, len(certifications), 3):
        cols = st.columns(3)  # Membuat 3 kolom

        for j in range(3):  # Mengisi setiap kolom
            if i + j < len(certifications):  # Cek apakah masih ada sertifikat
                cert = certifications[i + j]
                with cols[j]:  # Menempatkan dalam kolom ke-j
                    st.image(
                        cert["image"], caption=cert["title"], width=500
                    )  # Gambar lebih kecil
                    st.write(f"📅 {cert['date']}")
                    st.markdown(
                        f"[🔗 Lihat di LinkedIn]({cert['link']})",
                        unsafe_allow_html=True,
                    )

                    with open(cert["pdf"], "rb") as pdf_file:
                        pdf_data = pdf_file.read()
                        st.download_button(
                            label=(
                                "📄 Unduh Sertifikat"
                                if st.session_state.language == "ID"
                                else "📄 Download Certificate"
                            ),
                            data=pdf_data,
                            file_name=cert["pdf"].split("/")[-1],
                            mime="application/pdf",
                        )


# ---------------- Contact ----------------
elif menu == text[lang]["nav"][5]:  # Kontak / Contact
    st.markdown(
        f"<h1 style='text-align: center;'>{text[lang]['contact']}</h1>",
        unsafe_allow_html=True,
    )

    # Deskripsi dalam dua bahasa
    contact_desc = {
        "ID": """
        Jika Anda tertarik untuk berdiskusi lebih lanjut mengenai proyek data science, kolaborasi, atau ingin mengetahui lebih lanjut tentang saya, 
        silakan hubungi saya melalui salah satu platform berikut. Saya akan dengan senang hati merespons pesan Anda secepat mungkin.
        """,
        "EN": """
        If you are interested in discussing data science projects, collaborations, or learning more about me, 
        feel free to reach out through one of the following platforms. I will be happy to respond to your message as soon as possible.
        """,
    }

    st.write(contact_desc[lang])

    contact_info = [
        (
            "📧 Email",
            "ianandri007@gmail.com",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/2560px-Gmail_icon_%282020%29.svg.png",
        ),
        (
            "🔗 LinkedIn",
            "www.linkedin.com/in/andri-ihza-nasrulloh",
            "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
        ),
        (
            "🐱 GitHub",
            "https://github.com/andriihzan",
            "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg",
        ),
        (
            "📊 Kaggle",
            "https://www.kaggle.com/ianandri",
            "https://upload.wikimedia.org/wikipedia/commons/7/7c/Kaggle_logo.png",
        ),
        (
            "🐦 Twitter/X",
            "https://x.com/andriihzan34",
            "https://static.vecteezy.com/system/resources/thumbnails/042/148/611/small_2x/new-twitter-x-logo-twitter-icon-x-social-media-icon-free-png.png",
        ),
        (
            "✍ Medium",
            "https://medium.com/@ianandri007",
            "https://upload.wikimedia.org/wikipedia/commons/0/0d/Medium_%28website%29_logo.svg",
        ),
    ]

    # Menampilkan logo secara terpusat dalam grid
    cols = st.columns(len(contact_info))

    for col, (platform, link, logo) in zip(cols, contact_info):
        with col:
            st.markdown(
                f"<div style='text-align: center;'><a href='{link}' target='_blank'>"
                f"<img src='{logo}' width='50'></a><br><a href='{link}' target='_blank'>{platform}</a></div>",
                unsafe_allow_html=True,
            )
