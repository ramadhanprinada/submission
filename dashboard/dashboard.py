# Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style untuk seaborn
sns.set(style='dark')

# Load dataset 
all_df = pd.read_csv('main_data.csv')  

# Title
st.title("Proyek Akhir Belajar Analisis Data dengan Python")
st.text("By: Muhammad Ramadhan Prinada")

# 1. Bar Chart: Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (weathersit_y)

st.subheader('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')

# Membuat bar chart
plt.figure(figsize=(8, 5))
sns.barplot(data=all_df, x='weathersit_y', y='cnt_y', estimator=sum)
plt.title('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
plt.xlabel('Kondisi Cuaca (1=Clear, 2=Mist, 3=Light Snow/Rain, 4=Heavy Rain)')
plt.ylabel('Total Penyewaan Sepeda')

st.pyplot(plt)
st.write("""
Gambar ini menunjukkan bagaimana kondisi cuaca memengaruhi total penyewaan sepeda. 
Cuaca yang lebih baik (Clear) cenderung mendorong lebih banyak penyewaan sepeda dibandingkan cuaca yang lebih buruk (Heavy Rain).
""")

# 2. Box Plot: Distribusi Penyewaan Sepeda Berdasarkan Kondisi Cuaca

st.subheader('Distribusi Penyewaan Sepeda Berdasarkan Kondisi Cuaca')

# box plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=all_df, x='weathersit_y', y='cnt_y')
plt.title('Distribusi Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca (1=Clear, 2=Mist, 3=Light Snow/Rain, 4=Heavy Rain)')
plt.ylabel('Jumlah Penyewaan Sepeda')

st.pyplot(plt)
st.write("""
Box plot ini menunjukkan distribusi jumlah penyewaan sepeda untuk setiap kategori kondisi cuaca. 
Cuaca yang buruk biasanya menyebabkan lebih sedikit penyewaan sepeda, dengan rentang yang lebih rendah.
""")

# 3. Bar Chart: Penyewaan Sepeda Berdasarkan Kategori Hari Kerja

st.subheader('Pengaruh Hari Kerja terhadap Jumlah Penyewaan Sepeda')

# bar chart untuk hari kerja
plt.figure(figsize=(8, 5))
sns.barplot(data=all_df, x='workingday_y', y='cnt_y', estimator=sum)
plt.title('Pengaruh Hari Kerja terhadap Jumlah Penyewaan Sepeda')
plt.xlabel('Kategori Hari (0=Non-Workingday, 1=Workingday)')
plt.ylabel('Total Penyewaan Sepeda')

st.pyplot(plt)
st.write("""
Grafik ini menunjukkan perbedaan total penyewaan sepeda pada hari kerja dan hari libur. 
Biasanya, penyewaan sepeda lebih tinggi pada hari kerja dibandingkan hari libur.
""")

# 4. Pie Chart: Pengguna Kasual dan Terdaftar pada Hari Kerja vs Hari Libur

st.subheader('Perbandingan Pengguna Kasual vs Terdaftar pada Hari Kerja dan Hari Libur')

# filter data untuk hari kerja dan hari libur
workingday_data = all_df[all_df['workingday_y'] == 1]
non_workingday_data = all_df[all_df['workingday_y'] == 0]

# hitung jumlah pengguna kasual dan terdaftar
casual_workingday = workingday_data['casual_y'].sum()
registered_workingday = workingday_data['registered_y'].sum()
casual_non_workingday = non_workingday_data['casual_y'].sum()
registered_non_workingday = non_workingday_data['registered_y'].sum()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# pie chart untuk hari kerja
ax1.pie([casual_workingday, registered_workingday], labels=['Casual Users', 'Registered Users'], autopct='%1.1f%%', startangle=90)
ax1.set_title('Hari Kerja')
ax1.axis('equal')

# pie chart untuk hari libur
ax2.pie([casual_non_workingday, registered_non_workingday], labels=['Casual Users', 'Registered Users'], autopct='%1.1f%%', startangle=90)
ax2.set_title('Hari Libur')
ax2.axis('equal')

# menampilkan kedua pie chart
st.pyplot(fig)
st.write("""
Pie chart ini menunjukkan proporsi pengguna kasual dan terdaftar pada hari kerja dan hari libur. 
Pada hari kerja, sebagian besar pengguna adalah pengguna terdaftar, sedangkan pada hari libur, proporsi pengguna kasual meningkat.
""")

# Footer
st.caption('Copyright (c) Muhammad Ramadhan Prinada 2024')
