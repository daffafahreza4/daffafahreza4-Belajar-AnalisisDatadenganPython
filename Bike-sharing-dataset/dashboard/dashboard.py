import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
hour_df = pd.read_csv("hour.csv")
day_df = pd.read_csv("day.csv")

# Calculate monthly rentals
monthly_rentals = day_df.groupby('mnth')['cnt'].sum()
bulan_puncak = monthly_rentals.idxmax()

# Set page layout
st.set_page_config(layout="wide")

# Add Title and Tabs
st.title("Proyek Analisis Data: Bike Sharing Dataset")
tab1, tab2, tab3 = st.columns(3)

# Page 1
if tab1.button("Halaman 1"):
    st.title('Pengaruh Suhu Udara terhadap Peminjaman Sepeda')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(hour_df['temp'], hour_df['cnt'], alpha=0.5)
    ax.set_xlabel('Suhu Udara (Celsius)')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.grid(True)

    # Show plot in Streamlit
    st.pyplot(fig)
    st.write("Scatter plot yang kita lihat menunjukkan adanya korelasi positif antara suhu udara dan jumlah peminjaman sepeda. Artinya, ketika suhu udara meningkat, jumlah peminjaman sepeda juga cenderung meningkat.")

# Page 2
if tab2.button("Halaman 2"):
    st.title('Rata-rata Peminjaman Sepeda per Bulan')

    # Calculate average rentals per month
    monthly_rentals = day_df.groupby('mnth')['cnt'].sum()
    days_in_month = day_df.groupby('mnth')['dteday'].nunique()
    average_rentals_per_month = monthly_rentals / days_in_month

    # Convert to DataFrame
    average_rentals_df = pd.DataFrame({'Bulan': average_rentals_per_month.index, 'Rata-rata Peminjaman Sepeda': average_rentals_per_month.values})

    # Display table
    st.write(average_rentals_df)

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 6))
    average_rentals_per_month.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Rata-rata Peminjaman Sepeda per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rata-rata Peminjaman Sepeda')
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    ax.grid(axis='y')
    plt.tight_layout()

    # Show plot in Streamlit
    st.pyplot(fig)
    st.write("Bar plot ini memberikan gambaran tentang rata-rata jumlah peminjaman sepeda setiap bulan, menunjukkan fluktuasi dalam penggunaan sepeda selama periode yang diteliti. Plot ini, yang diwarnai dengan biru, dengan jelas menunjukkan bulan-bulan dengan rata-rata peminjaman sepeda paling tinggi dan paling rendah. Dengan menganalisis visual ini, kita mendapatkan pemahaman yang berharga tentang pola musiman dalam penggunaan sepeda. Informasi ini bisa digunakan untuk merencanakan strategi manajemen dan pemasaran yang lebih efektif, serta menyesuaikan layanan dengan permintaan yang berubah-ubah sepanjang tahun.")

# Page 3
if tab3.button("Halaman 3"):
    st.title('Total Peminjaman Sepeda tiap Bulan')

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 6))
    monthly_rentals.plot(color='skyblue', marker='o', linestyle='-')
    ax.set_title('Total Peminjaman Sepeda tiap Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Total Peminjaman Sepeda')
    ax.set_xticks(monthly_rentals.index)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    ax.axvline(x=bulan_puncak, color='red', linestyle='--', linewidth=2, label='Bulan Puncak')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()

    # Show plot in Streamlit
    st.pyplot(fig)
    st.write("Grafik ini menggambarkan pola bulanan total peminjaman sepeda, di mana setiap titik menunjukkan jumlah peminjaman pada bulan tertentu. Bulan dengan peminjaman sepeda terbanyak ditandai dengan garis merah vertikal. Melalui analisis grafik ini, kita dapat memahami pola umum penggunaan layanan peminjaman sepeda sepanjang tahun, mengidentifikasi bulan-bulan penting di mana permintaan mencapai titik tertinggi, dan mengamati pola musiman dalam penggunaan sepeda.")
