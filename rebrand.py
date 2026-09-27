# Script untuk rebranding index.html
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Melakukan penggantian teks secara presisi
html_content = html_content.replace('TLIBRARY ID', 'TLIBRARY ID')
html_content = html_content.replace('TLIBRARY ID.org', 'tlibrary.id')

# Menyimpan hasil ke file baru agar file lama tetap aman
with open('index_tlibrary.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Rebranding selesai! File HTML yang utuh telah disimpan sebagai index_tlibrary.html")
