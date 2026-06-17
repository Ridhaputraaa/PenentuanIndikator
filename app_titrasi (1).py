import streamlit as st
import base64
from pathlib import Path

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Sistem Rekomendasi Indikator Titrasi yang Dilengkapi dengan Perhitungan Standardisasi Larutan",
    page_icon="⚛️",
    layout="centered",
)

# ─────────────────────────────────────────────
# FOTO LATAR BELAKANG (LABORATORIUM)
# Letakkan file foto di: assets/lab_background.jpg
# (satu folder dengan file app_titrasi.py ini)
# ─────────────────────────────────────────────
ASSET_DIR = Path(__file__).parent / "assets"
BG_IMAGE_PATH = ASSET_DIR / "lab_background.jpg"

@st.cache_data
def _muat_base64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

_BG_B64 = _muat_base64(BG_IMAGE_PATH) if BG_IMAGE_PATH.exists() else ""

# Palet warna "tema" untuk tiap aktivitas/menu (disamakan dengan warna kartu
# rekomendasi yang sudah ada di aplikasi) supaya latar belakang foto lab ini
# ikut "hidup" / menyesuaikan suasana sesuai apa yang sedang dikerjakan user.
TEMA_WARNA = {
    "default":        "50,140,193",
    "standarisasi":   "0,137,123",
    "asam_basa":      "229,57,53",
    "redoks_kmno4":   "142,36,170",
    "redoks_iodo":    "0,137,123",
    "kompleksometri": "142,36,170",
    "argentometri_mohr":    "249,168,37",
    "argentometri_volhard": "229,57,53",
    "argentometri_fajans":  "67,160,71",
}

def set_background(tema: str = "default", opacity: float = 0.42):
    if not _BG_B64:
        return
    accent = TEMA_WARNA.get(tema, TEMA_WARNA["default"])
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image:
                linear-gradient(135deg, rgba(7,18,32,0.66) 0%, rgba({accent},{opacity}) 100%),
                url("data:image/jpeg;base64,{_BG_B64}");
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            transition: background 0.7s ease-in-out;
        }}
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0) !important;
        }}
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, rgba(11,60,93,0.92), rgba(50,140,193,0.92));
        }}
        [data-testid="stSidebar"] * {{
            color: #ffffff !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Pasang latar belakang versi default sejak awal
set_background("default")

page_bg_img = """
<style>
h1, h2, h3, h4, h5, h6,
p, label, .stMarkdown, .stText, .stRadio label, .stSelectbox label {
    color: black !important;
    font-weight: bold !important;
}
div[data-baseweb="select"] > div {
    background: linear-gradient(135deg, #0b3c5d 0%, #328cc1 100%) !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[data-baseweb="select"] span, 
div[data-baseweb="select"] div {
    color: white !important;
    font-weight: bold !important;
}
div[data-baseweb="popover"] ul,
div[role="listbox"],
[data-baseweb="menu"],
[data-baseweb="menu"] ul {
    background: linear-gradient(135deg, #0b3c5d 0%, #1d5f8a 100%) !important;
    background-color: #0b3c5d !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[role="option"],
div[role="option"] span,
div[role="option"] div,
li[role="option"],
li[role="option"] span {
    color: white !important;
    background-color: transparent !important;
    font-weight: bold !important;
    font-size: 14px !important;
}
div[role="option"]:hover,
div[role="option"]:active,
li[role="option"]:hover,
li[role="option"]:focus,
div[data-baseweb="popover"] ul li:hover {
    background-color: #328cc1 !important;
    background: #328cc1 !important;
    color: white !important;
}
div[data-baseweb="input"] {
    background: linear-gradient(135deg, #0b3c5d 0%, #328cc1 100%) !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[data-baseweb="input"] input {
    background-color: transparent !important;
    color: black !important;
    font-weight: bold !important;
}
div[data-baseweb="input"] input:focus {
    color: black !important;
}
div[data-baseweb="input"] button {
    color: black !important;
    background-color: transparent !important;
}
.main .block-container {
    background: rgba(255,255,255,0.80);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    padding: 2rem;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.18);
}
table, th, td {
    color: black !important;
    font-weight: bold !important;
}
.stInfo {
    color: black !important;
    font-weight: bold !important;
}
.custom-white-box {
    background-color: rgba(255, 255, 255, 0.9) !important;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CUSTOM CSS UNTUK BANNER DAN CARD
# ─────────────────────────────────────────────
st.markdown(
    """
    <style>
        body { font-family: 'Segoe UI', sans-serif; }
        .banner h1 {
            color: #0b3c5d !important; 
            font-weight: bold !important;
            font-size: 2em;
        }
        .banner p {
            color: #328cc1 !important; 
            font-weight: bold !important;
        }
        .banner {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 50%, #80deea 100%);
            border-radius: 14px;
            padding: 28px 20px;
            text-align: center;
            margin-bottom: 28px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }
        /* Kartu Rekomendasi Indikator */
        .card {
            background: #ffffff !important;
            border-radius: 12px;
            padding: 18px 20px;
            margin: 10px 0;
            border-left: 6px solid #2196F3;
            box-shadow: 0 2px 8px rgba(0,0,0,.08);
        }
        .card.red    { border-color: #e53935; }
        .card.green  { border-color: #43a047; }
        .card.orange { border-color: #fb8c00; }
        .card.purple { border-color: #8e24aa; }
        .card.yellow { border-color: #f9a825; }
        .card.teal   { border-color: #00897b; }
        /* Tulisan di dalam kartu selalu hitam */
        .card, .card h4, .card p, .card span, .card li {
            color: #000000 !important;
            font-weight: bold !important;
        }
        .card h4 { margin: 0 0 6px 0; font-size: 1.05em; }
        .card p { margin: 2px 0; font-size: .93em; }
        .badge {
            display: inline-block;
            background: #fff8e1;
            color: #000000 !important;
            border: 1px solid #ffe082;
            border-radius: 20px;
            padding: 2px 10px;
            font-size: .8em;
            margin-top: 6px;
        }
        .warn {
            background: #fff3e0;
            border-left: 5px solid #FF9800;
            border-radius: 8px;
            padding: 14px 16px;
            margin: 10px 0;
            font-size: .92em;
            color: #5d4037 !important;
        }
        .warn b { color: #e65100 !important; }
        .warn * { color: #5d4037 !important; }
        .step-badge {
            display: inline-block;
            background: #e8eaf6;
            color: #3949ab !important;
            border-radius: 20px;
            padding: 3px 14px;
            font-size: .82em;
            font-weight: 600;
            margin-bottom: 12px;
        }
        .done {
            background: linear-gradient(90deg,#e8f5e9,#f1f8e9);
            border: 1.5px solid #a5d6a7;
            border-radius: 10px;
            padding: 14px 18px;
            color: #2e7d32 !important;
            font-weight: 600;
            margin-top: 14px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# BANNER ATAS
# ─────────────────────────────────────────────
st.markdown(
    """
    <div class="banner">
        <h1>👩🏻‍🔬 Sistem Perhitungan Standarisasi Larutan dan Rekomendasi Indikator Titrasi</h1>
        <p>Pilih jenis titrasi → Ikuti langkah → Dapatkan rekomendasi indikator</p>
        <p>Pilih jenis metode standarisasi → Masukkan nilainya → Dapatkan hasil perhitungannya</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# TENTANG APLIKASI
# ─────────────────────────────────────────────
st.markdown(
    """
    <div class="custom-white-box" style="text-align:justify;">
        <p style="margin:0; color:black !important; font-weight:bold !important; font-size:1em; line-height:1.6;">
            ℹ️ Aplikasi ini dirancang khusus untuk membantu mahasiswa
            <span style="color:#0b3c5d;">Politeknik AKA Bogor</span> dalam menentukan indikator
            titrasi yang tepat berdasarkan <span style="color:#0b3c5d;">jenis titrasi, pH titik
            ekuivalen, serta karakteristik asam–basa larutan</span>. Selain memberikan
            rekomendasi indikator secara otomatis, aplikasi ini juga dilengkapi fitur
            <span style="color:#0b3c5d;">perhitungan standardisasi larutan</span> untuk membantu
            memperoleh konsentrasi larutan standar.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# IDENTITAS PEMBUAT APLIKASI (TIM PENGEMBANG)
# ─────────────────────────────────────────────
st.markdown(
    """
    <div class="custom-white-box" style="border-left:6px solid #0b3c5d;">
        <p style="margin:0 0 10px 0; color:#0b3c5d !important; font-weight:900 !important; font-size:1.05em;">
            👥 Tim Pengembang — Kelompok 5
        </p>
        <p style="margin:2px 0; color:black !important; font-weight:bold !important;">1. Diaz Aqilia Ghyfary</p>
        <p style="margin:2px 0; color:black !important; font-weight:bold !important;">2. Izamary Layla Muzdalifah</p>
        <p style="margin:2px 0; color:black !important; font-weight:bold !important;">3. Nicholas Kusuma Irwana P.</p>
        <p style="margin:2px 0; color:black !important; font-weight:bold !important;">4. Nida Nafisah Herlistyo</p>
        <p style="margin:2px 0; color:black !important; font-weight:bold !important;">5. Ridha Putra Pertama</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Identitas tim juga ditampilkan di sidebar agar selalu terlihat di setiap halaman
with st.sidebar:
    st.markdown("### ⚛️ Tentang Aplikasi")
    st.markdown(
        "Sistem rekomendasi indikator titrasi & perhitungan standardisasi larutan "
        "untuk mahasiswa **Politeknik AKA Bogor**."
    )
    st.markdown("---")
    st.markdown("### 👥 Tim Pengembang")
    st.markdown(
        "1. Diaz Aqilia Ghyfary\n"
        "2. Izamary Layla Muzdalifah\n"
        "3. Nicholas Kusuma Irwana P.\n"
        "4. Nida Nafisah Herlistyo\n"
        "5. Ridha Putra Pertama"
    )

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────
def card(title, rows: list, color="", starred=False):
    extra = f' <span class="badge">⭐ Direkomendasikan</span>' if starred else ""
    body = "".join(f"<p>• {r}</p>" for r in rows)
    st.markdown(
        f'<div class="card {color}"><h4>{title}{extra}</h4>{body}</div>',
        unsafe_allow_html=True,
    )

def warn(msg):
    st.markdown(f'<div class="warn">⚠️ <b>Catatan:</b> {msg}</div>', unsafe_allow_html=True)

def done():
    st.markdown('<div class="done">✅ Selesai — gunakan indikator di atas sesuai ketersediaan laboratorium.</div>', unsafe_allow_html=True)

def step(n, label):
    st.markdown(f'<div class="step-badge">Langkah {n}</div>', unsafe_allow_html=True)
    st.markdown(f"**{label}**")

# =============================================
# MENU UTAMA
# =============================================
st.markdown("### 🎯 Pilih Tujuan")

fitur = st.radio(
    "",
    [
        "MENENTUKAN INDIKATOR TITRASI",
        "MENGHITUNG STANDARISASI LARUTAN"
    ]
)

# Latar belakang menyesuaikan menu utama yang sedang dipilih
set_background("standarisasi" if fitur == "MENGHITUNG STANDARISASI LARUTAN" else "default")

st.divider()

# ─────────────────────────────────────────────
# FITUR 1 — STANDARISASI LARUTAN
# ─────────────────────────────────────────────
if fitur == "MENGHITUNG STANDARISASI LARUTAN":
    st.subheader("🧪 PERHITUNGAN STANDARISASI LARUTAN")
    metode = st.selectbox(
        "Pilih Metode Standarisasi",
        [
            "── PILIH ──",
            "Natrium Hidroksida (NaOH) dengan Asam Oksalat (H₂C₂O₄)",
            "Asam Klorida (HCl) dengan Boraks (Na₂B₄O₇.10H₂O)",
            "Kalium Permanganat (KMnO₄) dengan Asam Oksalat (H₂C₂O₄)",
            "Tiosulfat (Na₂S₂O₃) dengan Kalium Dikromat (K₂Cr₂O₇)",
            "EDTA (C₁₀H₁₆N₂O₈) dengan Kalium Karbonat (CaCO₃)",
        ]
    )

    if metode == "Natrium Hidroksida (NaOH) dengan Asam Oksalat (H₂C₂O₄)":
        massa = st.number_input("Massa Asam Oksalat (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume NaOH (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 63.0  
                N = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code("N = massa Asam Oksalat (mg) / ((100mL / 25mL) × volume NaOH (mL) × BE Asam Oksalat)")
                st.write("**Perhitungan:**")
                st.write(f"N = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE} mg/mgrek)")
                st.success(f"Normalitas NaOH = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "Asam Klorida (HCl) dengan Boraks (Na₂B₄O₇.10H₂O)":
        massa = st.number_input("Massa Boraks (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume HCl (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 190.7  
                N = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code("N = massa Boraks (mg) / ((100mL / 25mL) × volume HCl (mL) × BE Boraks)")
                st.write("**Perhitungan:**")
                st.write(f"N = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE} mg/mgrek)")
                st.success(f"Normalitas HCl = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "Kalium Permanganat (KMnO₄) dengan Asam Oksalat (H₂C₂O₄)":
        massa = st.number_input("Massa Asam Oksalat (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume KMnO₄ (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 63.0  
                N = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code("N = massa Asam Oksalat (mg) / ((100mL / 25mL) × volume KMnO₄ (mL) × BE Asam Oksalat)")
                st.write("**Perhitungan:**")
                st.write(f"N = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE} mg/mgrek)")
                st.success(f"Normalitas KMnO₄ = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "Tiosulfat (Na₂S₂O₃) dengan Kalium Dikromat (K₂Cr₂O₇)":
        massa = st.number_input("Massa K₂Cr₂O₇ (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume Na₂S₂O₃ (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 49.04  
                N = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code("N = massa K₂Cr₂O₇ (mg) / ((100mL / 25mL) × volume Tiosulfat (mL) × BE K₂Cr₂O₇)")
                st.write("**Perhitungan:**")
                st.write(f"N = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE} mg/mgrek)")
                st.success(f"Normalitas Na₂S₂O₃ = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "EDTA (C₁₀H₁₆N₂O₈) dengan Kalium Karbonat (CaCO₃)":
        massa = st.number_input("Massa CaCO₃ (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume EDTA (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BM = 100.09  
                M = massa / ((100 / 25) * volume * BM)
                st.write("**Rumus:**")
                st.code("M = massa CaCO₃ (mg) / ((100mL / 25mL) × volume EDTA (mL) × BM CaCO₃)") 
                st.write("**Perhitungan:**")
                st.write(f"M = {massa:.1f} mg / (4 × {volume:.2f} mL × {BM} mg/mmol)")
                st.success(f"Molaritas EDTA = {M:.4f} M")
            else:
                st.error("Volume tidak boleh 0.")

# ─────────────────────────────────────────────
# FITUR 2 — MENENTUKAN INDIKATOR
# ─────────────────────────────────────────────
elif fitur == "MENENTUKAN INDIKATOR TITRASI":
    st.subheader("🧪 PILIH JENIS TITRASI")
    JENIS = [
        "── PILIH ──",
        "🔴 JENIS TITRASI ASAM-BASA",
        "🟡 TITRASI REDOKS",
        "🟣 TITRASI KOMPLEKSOMETRI",
        "🟢 TITRASI ARGENTOMETRI",
    ]
    pilih_jenis = st.selectbox("Jenis Titrasi", JENIS, label_visibility="collapsed")
    st.divider()

    if pilih_jenis == "🔴 JENIS TITRASI ASAM-BASA":
        set_background("asam_basa")
        st.subheader("🔴 JENIS TITRASI ASAM-BASA")
        col1, col2 = st.columns(2)

        with col1:
            step(2, "JENIS TITRASI ASAM-BASA")
            titran = st.radio(
                "Titran",
                [
                    "Asam Kuat oleh Basa Kuat",
                    "Basa Lemah oleh Asam Kuat",
                    "Asam Lemah oleh Basa Kuat",
                    "Asam Lemah oleh Basa Lemah",
                ],
                label_visibility="collapsed",
            )

        with col2:
            st.divider()
            st.subheader("💡 Rekomendasi Indikator")
            if titran == "Asam Kuat oleh Basa Kuat":
                card("Bromtimol Biru", ["Rentang pH: 6.0 – 7.6",
                     "Perubahan: Kuning → Biru", "Warna hijau akan muncul sebagai warna antara"], "teal", True)
                card("Fenolftalein", ["Rentang pH: 8.2 – 10.0",
                     "Perubahan: Tidak berwarna → Pink"], "red")
            elif titran == "Basa Lemah oleh Asam Kuat":
                card("Metil Jingga", ["Rentang pH: 3.1 – 4.4",
                     "Perubahan: Kuning → Merah", "Sangat sesuai untuk titik ekuivalen yang bersifat asam"], "orange", True)
                card("Metil Merah", ["Rentang pH: 4.2 – 6.2",
                     "Perubahan: Kuning → Merah", "Warna jingga akan muncul sebagai warna antara"], "red")
                warn("Fenolftalein tidak direkomendasikan karena perubahan warnanya terjadi pada daerah basa.")
            elif titran == "Asam Lemah oleh Basa Kuat":
                card("Fenolftalein", ["Rentang pH: 8.2 – 10.0",
                     "Perubahan: Tidak berwarna → Pink",
                     "pH ekuivalen > 7 → ideal"], "red", True)
                warn("Jangan gunakan metil oranye, metil merah dan BTB — Pengamatan pada titik akhir akan kurang jelas karena trayek pH tidak sesuai dengan titik ekuivalen.")
            else:
                warn("Titrasi asam lemah – basa lemah <b>tidak direkomendasikan</b> secara analitik karena tidak memiliki titik ekuivalen yang tajam, sehingga titik akhir titrasi sangat sulit dideteksi menggunakan indikator warna standar.")
        done()

    elif pilih_jenis == "🟡 TITRASI REDOKS":
        st.subheader("🟡 TITRASI REDOKS")
        step(2, "PILIH METODE TITRASI REDOKS")
        metode = st.radio(
            "Metode",
            ["Permanganometri", "Iodometri / Iodimetri"],
            horizontal=True,
            label_visibility="collapsed",
        )
        set_background("redoks_kmno4" if metode == "Permanganometri" else "redoks_iodo")
        st.divider()
        st.subheader("💡 Rekomendasi Indikator")
        if metode == "Permanganometri":
            card("KMnO₄ — Autoindicator",
                ["KMnO₄ sendiri bertindak sebagai indikator", "Titik akhir: larutan berubah merah muda", "Titrasi dalam suasana asam (H₂SO₄ encer)"], "purple", True)
            warn("Penggunaan blanko sangat dianjurkan untuk mengoreksi hasil titrasi.")
            card("Ferroin (1,10-fenantrolin)", ["Dalam keadaan tereduksi, kompleks ini berwarna merah pekat.", "Ketika dioksidasi, kompleks ini berubah menjadi berwarna biru pucat (atau biru).", "Perubahan warna ini bersifat reversibel"], "red")
        else:
            card("Larutan Kanji (Amilum)", ["Digunakan pada titrasi redoks yang melibatkan iodin (I₂)", "Perubahan: Biru → Tidak berwarna (saat I₂ habis)"], "teal", True)
            warn("Tambahkan larutan kanji <b>menjelang titik akhir titrasi</b> (saat warna sudah pucat kuning), bukan di awal — amilum yang berikatan terlalu lama dengan I₂ sulit terurai sehingga titik akhir menjadi tidak tajam.")
        done()

    elif pilih_jenis == "🟣 TITRASI KOMPLEKSOMETRI":
        st.subheader("🟣 TITRASI KOMPLEKSOMETRI (EDTA)")
        step(2, "Pilih Ion Logam yang Dititrasi")
        ION_DATA = {
            "Ca²⁺ / Mg²⁺": [
                ("EBT (Eriochrome Black T)", ["pH 10 — buffer amonia/amonium klorida", "Perubahan: Merah anggur → Biru"], "teal", True),
            ],
            "Zn²⁺": [
                ("EBT (Eriochrome Black T)", ["pH 10 — buffer amonia", "Perubahan: Merah anggur → Biru"], "teal", True),
            ],
            "Cu²⁺": [
                ("Murexide", ["pH 8–9", "Perubahan: Kuning → Ungu"], "purple", True),
            ],
            "Fe²⁺ / Fe³⁺": [
                ("Asam salisilat", ["pH 1–2 (untuk Fe³⁺ — suasana sangat asam)", "Perubahan: Merah → Tidak berwarna"], "red", True),
                ("Tiron", ["pH 4–10", "Perubahan: Biru → Tidak berwarna"], "teal", False),
            ],
            "Pb²⁺": [
                ("Xylenol Orange", ["pH 5–6 — buffer heksamin", "Perubahan: Merah-ungu → Kuning"], "orange", True),
            ],
            "Hg²⁺": [
                ("Xylenol Orange", ["pH 2–3 (asam nitrat encer)", "Perubahan: Merah → Kuning"], "orange", True),
            ],
            "Al³⁺": [
                ("Xylenol Orange + titrasi balik", ["pH 5", "Perubahan: Kuning → Merah-ungu"], "orange", True),
            ],
            "Ni²⁺": [
                ("Murexide", ["pH 8–9 — buffer amonia", "Perubahan: Kuning → Ungu"], "purple", True),
            ],
            "Co²⁺": [
                ("Murexide", ["pH 8–9 — buffer amonia", "Perubahan: Kuning → Ungu"], "purple", True),
            ],
        }
        ion = st.selectbox("Ion Logam", ["── Pilih Ion Logam ──"] + list(ION_DATA.keys()), label_visibility="collapsed")
        if ion != "── Pilih Ion Logam ──":
            st.divider()
            st.subheader(f"💡 Rekomendasi Indikator untuk **{ion}**")
            for name, rows, color, starred in ION_DATA[ion]:
                card(name, rows, color, starred)
            warn("Titrasi kompleksometri umumnya menggunakan <b>EDTA (Na₂H₂Y)</b> sebagai titran. Pastikan pH larutan sesuai agar kompleks logam-indikator terbentuk dan terlepas dengan baik di titik akhir.")
            done()

    elif pilih_jenis == "🟢 TITRASI ARGENTOMETRI":
        st.subheader("🟢 TITRASI ARGENTOMETRI")
        step(2, "PILIH METODE ARGENTOMETRI")
        metode = st.radio(
            "Metode",
            ["Argentometri (Mohr)", "Argentometri (Volhard)", "Argentometri (Fajans)"],
            horizontal=True,
            label_visibility="collapsed",
        )
        st.divider()
        st.subheader("💡 Rekomendasi Indikator")
        if metode == "Argentometri (Mohr)":
            card("Kalium Kromat — K₂CrO₄", ["Kondisi: pH 6.5 – 10,0 (netral – sedikit basa)", "Titik akhir: endapan merah bata (Ag₂CrO₄) permanen", "Analit: halida, CN⁻, dan CNS"], "yellow", True)
            warn("Tidak dapat digunakan dalam suasana asam karena CrO₄²⁻ akan berubah menjadi Cr₂O₇²⁻. Tidak dapat digunakan dalam suasana basa karena akan terbentuk endapan AgOH.")
        elif metode == "Argentometri (Volhard)":
            card("Besi(III) Amonium Sulfat — NH₄Fe(SO₄)₂", ["Kondisi: suasana asam (HNO₃ 4N)", "Titik akhir: larutan berwarna merah (FeSCN²⁺) permanen", "Analit: Ag⁺, Cl⁻, Br⁻, I⁻"], "red", True)
            warn("Untuk penetapan Cl⁻ secara tidak langsung, endapan AgCl harus disaring atau ditambahkan pelarut organik agar SCN⁻ tidak bereaksi dengan AgCl.")
        else:
            card("Diklorofluoresein", ["Kondisi: pH 4 – 10", "Titik akhir: endapan putih → merah muda", "Analit: Cl⁻, Br⁻, I⁻"], "green", True)
            card("Fluoresein", ["Kondisi: pH 7 – 8,5 (netral – sedikit basa)", "Titik akhir: endapan putih → merah muda", "Analit: Cl⁻"], "green")
            warn("Indikator adsorpsi (fluoresein/diklorofluoresein) bekerja dengan cara teradsorpsi pada permukaan endapan AgX.")
        done()
    else:
        st.info("👆 Pilih jenis titrasi di atas untuk memulai.", icon="⚠️")
        # Kotak panduan singkat
        st.markdown(
            """
            <div class="custom-white-box">
                <p style="margin-bottom: 8px; color: black !important; font-weight: bold !important;">Panduan singkat:</p>
                <table style="width:100%; border-collapse: collapse;">
                    <thead>
                        <tr style="border-bottom: 2px solid black;">
                            <th style="text-align:left; padding: 8px; color: black !important; font-weight: bold !important;">Jenis</th>
                            <th style="text-align:left; padding: 8px; color: black !important; font-weight: bold !important;">Titran</th>
                            <th style="text-align:left; padding: 8px; color: black !important; font-weight: bold !important;">Contoh Analit</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #ddd;">
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">Asam-Basa</td>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">NaOH / HCl</td>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">CH₃COOH, Na₂CO₃</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #ddd;">
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">Redoks</td>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">KMnO₄ / Na₂S₂O₃</td>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">Fe²⁺, Cl⁻, I₂</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #ddd;">
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">Kompleksometri</td>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">EDTA</td>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">Ca²⁺, Mg²⁺, Zn²⁺</td>
                        </tr>
                        <tr>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">Pengendapan</td>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">AgNO₃</td>
                            <td style="padding: 8px; color: black !important; font-weight: bold !important;">Cl⁻, Br⁻, I⁻</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """,
            unsafe_allow_html=True
        )

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.divider()
st.markdown(
    """
    <div class="custom-white-box" style="text-align:center; max-width: 400px; margin: 0 auto;">
        <span style='color: #000000 !important; font-weight: 900 !important; font-size: .9em;'>
            ⚛️ Sistem Rekomendasi Titrasi &nbsp;|&nbsp; Kelompok 5
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
