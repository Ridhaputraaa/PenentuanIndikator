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
# CONFIGURASI BACKGROUND (MENGGUNAKAN GAMBAR GITHUB ANDA)
# ─────────────────────────────────────────────
ASSET_DIR = Path(__file__).parent / "assets"
BG_IMAGE_PATH = ASSET_DIR / "lab_background.jpg"

@st.cache_data
def _muat_base64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

#Latar Belakang utama
if BG_IMAGE_PATH.exists():
    _BG_B64 = _muat_base64(BG_IMAGE_PATH)
    bg_src = f'url("data:image/jpeg;base64,{_BG_B64}")'
else:
    # memunculkan gambar utama
    bg_src = 'url("https://raw.githubusercontent.com/Ridhaputraaa/PenentuanIndikator/blob/174a223ba46498957ef8294ead24a9ce15982bb2/Gambar%20titrasi%20LPK.jpeg")'

# Palet warna tema dinamis untuk pencampuran gradasi latar belakang
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

def set_background(tema: str = "default", opacity: float = 0.50):
    accent = TEMA_WARNA.get(tema, TEMA_WARNA["default"])
    st.markdown(
        f"""
        <style>
        .stApp, [data-testid="stAppViewContainer"] {{
            background-image:
                linear-gradient(135deg, rgba(7,18,32,0.72) 0%, rgba({accent},{opacity}) 100%),
                {bg_src} !important;
            background-size: cover !important;
            background-position: center center !important;
            background-attachment: fixed !important;
            background-repeat: no-repeat !important;
            transition: background 0.8s ease-in-out;
        }}
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0) !important;
        }}
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, rgba(11,60,93,0.95), rgba(50,140,193,0.95)) !important;
        }}
        [data-testid="stSidebar"] * {{
            color: #ffffff !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# CUSTOM STYLING INTERFACES (KETERBACAAN TEKS)
# ─────────────────────────────────────────────
page_styles = """
<style>
h1, h2, h3, h4, h5, h6,
p, label, .stMarkdown, .stText, .stRadio label, .stSelectbox label {
    color: #111111 !important;
    font-weight: bold !important;
}

/* Modifikasi kotak input agar teks yang diketik berwarna PUTIH (kontras dengan warna biru tua) */
div[data-baseweb="select"] > div, div[data-baseweb="input"] {
    background: linear-gradient(135deg, #0b3c5d 0%, #1d5f8a 100%) !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
div[data-baseweb="select"] span, 
div[data-baseweb="select"] div,
div[data-baseweb="input"] input {
    color: #ffffff !important; 
    font-weight: bold !important;
    background-color: transparent !important;
}
div[data-baseweb="popover"] ul,
div[role="listbox"],
[data-baseweb="menu"],
[data-baseweb="menu"] ul {
    background-color: #0b3c5d !important;
    border: 2px solid #328cc1 !important;
    border-radius: 8px !important;
}
li[role="option"], li[role="option"] span {
    color: #ffffff !important;
    font-weight: bold !important;
}
li[role="option"]:hover {
    background-color: #328cc1 !important;
}

/* Container Transparan Utama */
.main .block-container {
    background: rgba(255,255,255,0.88);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    padding: 2.5rem;
    border-radius: 18px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
}
.custom-white-box {
    background-color: rgba(255, 255, 255, 0.95) !important;
    padding: 18px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    margin: 12px 0;
}

/* Desain Komponen Banner & Card */
.banner {
    background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 50%, #80deea 100%);
    border-radius: 14px;
    padding: 24px 20px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}
.banner h1 { color: #0b3c5d !important; font-size: 1.75em; }
.banner p { color: #1d5f8a !important; margin: 4px 0; }

.card {
    background: #ffffff !important;
    border-radius: 12px;
    padding: 16px 18px;
    margin: 12px 0;
    border-left: 6px solid #2196F3;
    box-shadow: 0 3px 10px rgba(0,0,0,.08);
}
.card.red    { border-color: #e53935; }
.card.green  { border-color: #43a047; }
.card.orange { border-color: #fb8c00; }
.card.purple { border-color: #8e24aa; }
.card.teal   { border-color: #00897b; }
.card.yellow { border-color: #f9a825; }

.card, .card h4, .card p, .card span, .card li {
    color: #111111 !important;
    font-weight: bold !important;
}
.badge {
    display: inline-block;
    background: #fff8e1;
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
    margin: 12px 0;
}
.warn * { color: #5d4037 !important; }
.step-badge {
    display: inline-block;
    background: #e8eaf6;
    color: #3949ab !important;
    border-radius: 20px;
    padding: 3px 14px;
    font-size: .82em;
    margin-bottom: 8px;
}
.done {
    background: linear-gradient(90deg,#e8f5e9,#f1f8e9);
    border: 1.5px solid #a5d6a7;
    border-radius: 10px;
    padding: 14px 18px;
    color: #2e7d32 !important;
    text-align: center;
    margin-top: 15px;
}
</style>
"""
st.markdown(page_styles, unsafe_allow_html=True)

# Pasang background awal (default)
set_background("default")

# ─────────────────────────────────────────────
# BANNER ATAS & DEFINISI TIM SIDEBAR
# ─────────────────────────────────────────────
st.markdown(
    """
    <div class="banner">
        <h1>👩🏻‍🔬 Sistem Perhitungan Standarisasi Larutan dan Rekomendasi Indikator Titrasi</h1>
        <p>Pilih jenis titrasi → Ikuti langkah → Dapatkan rekomendasi indikator</p>
        <p>Pilih jenis metode standarisasi → Masukkan nilainya → Dapatkan hasil perhitungannya</p>
    </div>
    <div class="custom-white-box" style="text-align:justify;">
        <p style="margin:0; line-height:1.6;">
            ℹ️ Aplikasi ini dirancang khusus untuk membantu mahasiswa
            <span style="color:#0b3c5d;">Politeknik AKA Bogor</span> dalam menentukan indikator
            titrasi yang tepat berdasarkan jenis titrasi, pH titik ekuivalen, serta karakteristik asam–basa larutan. 
            Selain memberikan rekomendasi indikator secara otomatis, aplikasi ini juga dilengkapi fitur 
            <span style="color:#0b3c5d;">perhitungan standardisasi larutan</span> untuk membantu memperoleh konsentrasi larutan standar.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### ⚛️ Tentang Aplikasi")
    st.markdown("Sistem rekomendasi indikator titrasi & perhitungan standardisasi larutan untuk mahasiswa **Politeknik AKA Bogor**.")
    st.markdown("---")
    st.markdown("### 👥 Tim Pengembang")
    st.markdown("1. Diaz Aqilia Ghyfary\n2. Izamary Layla Muzdalifah\n3. Nicholas Kusuma Irwana P.\n4. Nida Nafisah Herlistyo\n5. Ridha Putra Pertama")

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────
def card(title, rows: list, color="", starred=False):
    extra = f' <span class="badge">⭐ Direkomendasikan</span>' if starred else ""
    body = "".join(f"<p style='margin:4px 0;'>• {r}</p>" for r in rows)
    st.markdown(f'<div class="card {color}"><h4>{title}{extra}</h4>{body}</div>', unsafe_allow_html=True)

def warn(msg):
    st.markdown(f'<div class="warn">⚠️ <b>Catatan:</b> {msg}</div>', unsafe_allow_html=True)

def done():
    st.markdown('<div class="done">✅ Selesai — gunakan indikator di atas sesuai ketersediaan laboratorium.</div>', unsafe_allow_html=True)

def step(n, label):
    st.markdown(f'<div class="step-badge">Langkah {n}</div>', unsafe_allow_html=True)
    st.markdown(f"**{label}**")

# ─────────────────────────────────────────────
# TENTUKAN MENU AKTIVITAS
# ─────────────────────────────────────────────
st.markdown("### 🎯 Pilih Tujuan")
fitur = st.radio("", ["MENENTUKAN INDIKATOR TITRASI", "MENGHITUNG STANDARISASI LARUTAN"], label_visibility="collapsed")
st.divider()

# ─────────────────────────────────────────────
# FITUR 1 — STANDARISASI LARUTAN
# ─────────────────────────────────────────────
if fitur == "MENGHITUNG STANDARISASI LARUTAN":
    set_background("standarisasi")
    st.subheader("🧪 PERHITUNGAN STANDARISASI LARUTAN")
    metode = st.selectbox(
        "Pilih Metode Standarisasi",
        [
            "── PILIH ──",
            "Natrium Hidroksida (NaOH) dengan Asam Oksalat (H₂C₂O₄)",
            "Asam Klorida (HCl) dengan Boraks (Na₂B₄O₇.10H₂O)",
            "Kalium Permanganat (KMnO₄) dengan Asam Oksalat (H₂C₂O₄)",
            "Tiosulfat (Na₂S₂O₃) dengan Kalium Dikromat (K₂Cr₂O₇)",
            "EDTA (C₁₀H₁₆N₂O₈) dengan Kalsium Karbonat (CaCO₃)",
        ]
    )

    if metode != "── PILIH ──":
        massa = st.number_input("Massa Zat Primer (mg)", min_value=0.0, format="%.1f")
        volume = st.number_input("Volume Titran / Larutan Standar Sekunder (mL)", min_value=0.0, format="%.2f")
        
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                if "NaOH" in metode or "KMnO₄" in metode:
                    BE, unit, label = 63.0, "N", "Normalitas"
                    formula = "N = mg / ((100mL / 25mL) × mL Titran × BE)"
                elif "HCl" in metode:
                    BE, unit, label = 190.7, "N", "Normalitas"
                    formula = "N = mg / ((100mL / 25mL) × mL Titran × BE)"
                elif "Tiosulfat" in metode:
                    BE, unit, label = 49.04, "N", "Normalitas"
                    formula = "N = mg / ((100mL / 25mL) × mL Titran × BE)"
                elif "EDTA" in metode:
                    BE, unit, label = 100.09, "M", "Molaritas"
                    formula = "M = mg / ((100mL / 25mL) × mL Titran × BM)"

                hasil = massa / ((100 / 25) * volume * BE)
                st.write("**Rumus:**")
                st.code(formula)
                st.write("**Perhitungan:**")
                st.write(f"Hasil = {massa:.1f} mg / (4 × {volume:.2f} mL × {BE})")
                st.success(f"{label} Larutan = {hasil:.4f} {unit}")
            else:
                st.error("Volume tidak boleh 0.")

# ─────────────────────────────────────────────
# FITUR 2 — MENENTUKAN INDIKATOR TITRASI
# ─────────────────────────────────────────────
elif fitur == "MENENTUKAN INDIKATOR TITRASI":
    st.subheader("🧪 PILIH JENIS TITRASI")
    pilih_jenis = st.selectbox(
        "Jenis Titrasi", 
        ["── PILIH ──", "🔴 JENIS TITRASI ASAM-BASA", "🟡 TITRASI REDOKS", "🟣 TITRASI KOMPLEKSOMETRI", "🟢 TITRASI ARGENTOMETRI"],
        label_visibility="collapsed"
    )
    st.divider()

    if pilih_jenis == "🔴 JENIS TITRASI ASAM-BASA":
        set_background("asam_basa")
        st.subheader("🔴 JENIS TITRASI ASAM-BASA")
        col1, col2 = st.columns(2)
        with col1:
            step(2, "Pilih Karakteristik Reaktan")
            titran = st.radio(
                "Titran",
                ["Asam Kuat oleh Basa Kuat", "Basa Lemah oleh Asam Kuat", "Asam Lemah oleh Basa Kuat", "Asam Lemah oleh Basa Lemah"],
                label_visibility="collapsed",
            )
        with col2:
            st.subheader("💡 Rekomendasi Indikator")
            if titran == "Asam Kuat oleh Basa Kuat":
                card("Bromtimol Biru", ["Rentang pH: 6.0 – 7.6", "Perubahan: Kuning → Biru", "Warna hijau muncul sebagai warna antara"], "teal", True)
                card("Fenolftalein", ["Rentang pH: 8.2 – 10.0", "Perubahan: Tidak berwarna → Pink"], "red")
            elif titran == "Basa Lemah oleh Asam Kuat":
                card("Metil Jingga", ["Rentang pH: 3.1 – 4.4", "Perubahan: Kuning → Merah", "Sangat sesuai untuk titik ekuivalen asam"], "orange", True)
                card("Metil Merah", ["Rentang pH: 4.2 – 6.2", "Perubahan: Kuning → Merah"], "red")
                warn("Fenolftalein tidak direkomendasikan karena trayek warnanya berada di area basa.")
            elif titran == "Asam Lemah oleh Basa Kuat":
                card("Fenolftalein", ["Rentang pH: 8.2 – 10.0", "Perubahan: Tidak berwarna → Pink", "Sangat ideal karena pH ekuivalen > 7"], "red", True)
                warn("Jangan menggunakan Metil Jingga atau Metil Merah karena titik akhir akan kabur sebelum ekuivalen tercapai.")
            else:
                warn("Titrasi Asam Lemah - Basa Lemah <b>tidak direkomendasikan</b> karena tidak memiliki lonjakan pH yang tajam.")
        done()

    elif pilih_jenis == "🟡 TITRASI REDOKS":
        st.subheader("🟡 TITRASI REDOKS")
        step(2, "PILIH METODE TITRASI REDOKS")
        metode = st.radio("Metode", ["Permanganometri", "Iodometri / Iodimetri"], horizontal=True, label_visibility="collapsed")
        set_background("redoks_kmno4" if metode == "Permanganometri" else "redoks_iodo")
        st.divider()
        st.subheader("💡 Rekomendasi Indikator")
        if metode == "Permanganometri":
            card("KMnO₄ — Autoindicator", ["Zat peniter bertindak langsung sebagai indikator", "Titik akhir: Merah muda seulas bertahan 30 detik", "Kondisi: Suasana asam encer (H₂SO₄)"], "purple", True)
            card("Ferroin", ["Menggunakan kompleks 1,10-fenantrolin", "Perubahan warna: Merah (tereduksi) → Biru Pucat (teroksidasi)"], "red")
        else:
            card("Larutan Kanji (Amilum)", ["Membentuk kompleks amilum-iodin", "Perubahan: Biru Tua → Tidak Berwarna (pada Iodometri)"], "teal", True)
            warn("Tambahkan larutan kanji **menjelang titik akhir** (saat larutan berwarna kuning jerami pucat) agar kompleks tidak merusak ketajaman TA.")
        done()

    elif pilih_jenis == "🟣 TITRASI KOMPLEKSOMETRI":
        set_background("kompleksometri")
        st.subheader("🟣 TITRASI KOMPLEKSOMETRI (EDTA)")
        step(2, "Pilih Ion Logam yang Dititrasi")
        ION_DATA = {
            "Ca²⁺ / Mg²⁺": [("EBT (Eriochrome Black T)", ["Kondisi: pH 10 (Buffer Amonia)", "Perubahan: Merah Anggur → Biru murni"], "teal", True)],
            "Zn²⁺": [("EBT (Eriochrome Black T)", ["Kondisi: pH 10 (Buffer)", "Perubahan: Merah Anggur → Biru"], "teal", True)],
            "Cu²⁺": [("Murexide", ["Kondisi: pH 8–9", "Perubahan: Kuning → Ungu"], "purple", True)],
            "Fe²⁺ / Fe³⁺": [
                ("Asam Salisilat", ["Kondisi: pH 1–2 (Suasana sangat asam)", "Perubahan: Merah/Ungu gelap → Tidak Berwarna"], "red", True),
                ("Tiron", ["Kondisi: pH 4–10", "Perubahan: Biru → Tidak Berwarna"], "teal", False)
            ],
            "Pb²⁺": [("Xylenol Orange", ["Kondisi: pH 5–6 (Buffer Heksamin)", "Perubahan: Merah-Ungu → Kuning"], "orange", True)],
        }
        ion = st.selectbox("Ion Logam", ["── Pilih Ion Logam ──"] + list(ION_DATA.keys()), label_visibility="collapsed")
        if ion != "── Pilih Ion Logam ──":
            st.divider()
            st.subheader(f"💡 Rekomendasi Indikator untuk {ion}")
            for name, rows, color, starred in ION_DATA[ion]:
                card(name, rows, color, starred)
            done()

    elif pilih_jenis == "🟢 TITRASI ARGENTOMETRI":
        st.subheader("🟢 TITRASI ARGENTOMETRI")
        step(2, "PILIH METODE ARGENTOMETRI")
        metode = st.radio("Metode", ["Argentometri (Mohr)", "Argentometri (Volhard)", "Argentometri (Fajans)"], horizontal=True, label_visibility="collapsed")
        st.divider()
        st.subheader("💡 Rekomendasi Indikator")
        if metode == "Argentometri (Mohr)":
            set_background("argentometri_mohr")
            card("Kalium Kromat (K₂CrO₄)", ["Kondisi: pH netral hingga sedikit basa (6.5 - 10.0)", "Titik akhir: Terbentuk endapan Merah Bata (Ag₂CrO₄)"], "yellow", True)
            warn("Hindari suasana asam (kromat berubah jadi dikromat) maupun basa kuat (terbentuk endapan cokelat AgOH).")
        elif metode == "Argentometri (Volhard)":
            set_background("argentometri_volhard")
            card("Besi(III) Amonium Sulfat", ["Kondisi: Suasana asam kuat (HNO₃)", "Titik akhir: Terbentuk kompleks larutan Merah (FeSCN²⁺)"], "red", True)
        else:
            set_background("argentometri_fajans")
            card("Diklorofluoresein", ["Kondisi: pH 4.0 – 10.0", "Mekanisme: Indikator Adsorpsi pada permukaan endapan", "Titik akhir: Endapan berubah warna menjadi Merah Muda"], "green", True)
        done()
        
    else:
        set_background("default")
        st.info("👆 Pilih jenis titrasi di atas untuk memulai.", icon="⚠️")
        st.markdown(
            """
            <div class="custom-white-box">
                <p style="margin-bottom: 8px;"><b>Panduan Singkat Lapangan:</b></p>
                <table style="width:100%; border-collapse: collapse; color: black;">
                    <thead>
                        <tr style="border-bottom: 2px solid #0b3c5d;">
                            <th style="text-align:left; padding: 8px;">Jenis</th>
                            <th style="text-align:left; padding: 8px;">Titran Umum</th>
                            <th style="text-align:left; padding: 8px;">Aplikasi Analit</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #ddd;"><td style="padding: 8px;">Asam-Basa</td><td style="padding: 8px;">NaOH / HCl</td><td style="padding: 8px;">Asam Cuka, Soda Abu</td></tr>
                        <tr style="border-bottom: 1px solid #ddd;"><td style="padding: 8px;">Redoks</td><td style="padding: 8px;">KMnO₄ / Na₂S₂O₃</td><td style="padding: 8px;">Besi(II), Vitamin C, Iod</td></tr>
                        <tr style="border-bottom: 1px solid #ddd;"><td style="padding: 8px;">Kompleksometri</td><td style="padding: 8px;">EDTA</td><td style="padding: 8px;">Kesadahan Air (Ca²⁺, Mg²⁺)</td></tr>
                        <tr><td style="padding: 8px;">Argentometri</td><td style="padding: 8px;">AgNO₃</td><td style="padding: 8px;">Kadar Garam Cl⁻</td></tr>
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
        <span style='color: #0b3c5d !important; font-weight: 900 !important; font-size: .9em;'>
            ⚛️ Sistem Rekomendasi Titrasi &nbsp;|&nbsp; Kelompok 5 Politeknik AKA
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
