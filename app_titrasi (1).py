import streamlit as st

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Sistem Rekomendasi Titrasi",
    page_icon="🧪",
    layout="centered",
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown(
    """
    <style>
        /* ── global ── */
        body { font-family: 'Segoe UI', sans-serif; }

        /* ── header banner ── */
        .banner {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            border-radius: 14px;
            padding: 28px 20px;
            text-align: center;
            margin-bottom: 28px;
        }
        .banner h1 { color: #e0e0e0; font-size: 2em; margin: 0 0 6px 0; }
        .banner p  { color: #a0c4ff; font-size: 1em; margin: 0; }

        /* ── cards ── */
        .card {
            background: #ffffff;
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

        .card h4 { margin: 0 0 6px 0; font-size: 1.05em; }
        .card p  { margin: 2px 0; font-size: .93em; color: #444; }
        .badge {
            display: inline-block;
            background: #fff8e1;
            color: #f57f17;
            border: 1px solid #ffe082;
            border-radius: 20px;
            padding: 2px 10px;
            font-size: .8em;
            margin-top: 6px;
        }

        /* ── warning box ── */
        .warn {
            background: #fff3e0;
            border-left: 5px solid #FF9800;
            border-radius: 8px;
            padding: 14px 16px;
            margin: 10px 0;
            font-size: .92em;
            color: #5d4037;
        }
        .warn b { color: #e65100; }

        /* ── step badge ── */
        .step-badge {
            display: inline-block;
            background: #e8eaf6;
            color: #3949ab;
            border-radius: 20px;
            padding: 3px 14px;
            font-size: .82em;
            font-weight: 600;
            margin-bottom: 12px;
        }

        /* ── done banner ── */
        .done {
            background: linear-gradient(90deg,#e8f5e9,#f1f8e9);
            border: 1.5px solid #a5d6a7;
            border-radius: 10px;
            padding: 14px 18px;
            color: #2e7d32;
            font-weight: 600;
            margin-top: 14px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# BANNER
# ─────────────────────────────────────────────
st.markdown(
    """
    <div class="banner">
        <h1>🧪 Sistem Rekomendasi Titrasi</h1>
        <p>Pilih jenis titrasi → ikuti langkah → dapatkan rekomendasi indikator</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def card(title, rows: list, color="", starred=False):
    """Render a styled indicator card."""
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

# ─────────────────────────────────────────────
# STEP 1 – PILIH JENIS TITRASI
# ─────────────────────────────────────────────
step(1, "Pilih Jenis Titrasi")

JENIS = [
    "── Pilih ──",
    "🔴 Titrasi Asam-Basa",
    "⚡ Titrasi Redoks",
    "🔗 Titrasi Kompleksometri",
    "🌧️ Titrasi Pengendapan",
]
pilih_jenis = st.selectbox("Jenis Titrasi", JENIS, label_visibility="collapsed")

st.divider()

# ═══════════════════════════════════════════
# BRANCH 1 — TITRASI ASAM-BASA
# ═══════════════════════════════════════════
if pilih_jenis == "🔴 Titrasi Asam-Basa":
    st.subheader("🔴 Titrasi Asam-Basa")
    col1, col2 = st.columns(2)

    with col1:
        step(2, "Jenis Titran Asam-Basa")
        titran = st.radio(
            "Titran",
            [
                "Asam Kuat – Basa Kuat",
                "Asam Kuat – Basa Lemah",
                "Asam Lemah – Basa Kuat",
                "Asam Lemah – Basa Lemah",
            ],
            label_visibility="collapsed",
        )

    with col2:
        step(3, "Perkiraan pH Titik Ekuivalen")
        ph = st.radio(
            "pH",
            ["< 7  (Asam)", "= 7  (Netral)", "> 7  (Basa)"],
            label_visibility="collapsed",
        )

    st.divider()
    st.subheader("💡 Rekomendasi Indikator")

    if titran == "Asam Kuat – Basa Kuat":
        # pH ≈ 7, kurva curam → banyak pilihan
        card("Bromtimol Biru", ["Rentang pH: 6.0 – 7.6",
             "Perubahan: Kuning → Biru", "Cocok untuk titik ekuivalen netral"], "teal", True)
        card("Fenolftalein", ["Rentang pH: 8.2 – 10.0",
             "Perubahan: Tidak berwarna → Pink"], "red")
        card("Metil Oranye", ["Rentang pH: 3.1 – 4.4",
             "Perubahan: Merah → Oranye-Kuning"], "orange")

    elif titran == "Asam Kuat – Basa Lemah":
        card("Metil Oranye", ["Rentang pH: 3.1 – 4.4",
             "Perubahan: Merah → Oranye-Kuning",
             "pH ekuivalen < 7 → ideal"], "orange", True)
        card("Metil Merah", ["Rentang pH: 4.4 – 6.2",
             "Perubahan: Merah → Kuning"], "red")
        warn("Jangan gunakan fenolftalein — titik ekuivalen bersifat asam.")

    elif titran == "Asam Lemah – Basa Kuat":
        card("Fenolftalein", ["Rentang pH: 8.2 – 10.0",
             "Perubahan: Tidak berwarna → Pink",
             "pH ekuivalen > 7 → ideal"], "red", True)
        card("Timolftalein", ["Rentang pH: 9.3 – 10.5",
             "Perubahan: Tidak berwarna → Biru"], "purple")
        warn("Jangan gunakan metil oranye — perubahan warna terjadi jauh sebelum titik ekuivalen.")

    else:  # Asam Lemah – Basa Lemah
        warn(
            "Titrasi asam lemah – basa lemah <b>tidak direkomendasikan</b> secara analitik "
            "karena tidak memiliki titik ekuivalen yang tajam. Jika terpaksa, gunakan "
            "indikator universal dan berhati-hati dalam membaca perubahan warna."
        )

    done()

# ═══════════════════════════════════════════
# BRANCH 2 — TITRASI REDOKS
# ═══════════════════════════════════════════
elif pilih_jenis == "⚡ Titrasi Redoks":
    st.subheader("⚡ Titrasi Redoks")
    step(2, "Pilih Metode Titrasi Redoks")
    metode = st.radio(
        "Metode",
        ["Permanganometri", "Iodometri / Iodimetri"],
        horizontal=True,
        label_visibility="collapsed",
    )
    st.divider()
    st.subheader("💡 Rekomendasi Indikator")

    if metode == "Permanganometri":
        card(
            "KMnO₄ — Self-Indicator",
            [
                "KMnO₄ sendiri bertindak sebagai indikator",
                "Titik akhir: larutan berubah <b>merah muda / ungu permanen</b> (≥ 30 detik)",
                "Titrasi dalam suasana asam (H₂SO₄ encer)",
            ],
            "purple",
            True,
        )
        card(
            "Ferroin (kompleks Fe-fenantrolin)",
            [
                "Digunakan untuk titrasi balik",
                "Perubahan: Merah → Biru-hijau",
                "Konsentrasi: 0.025 M",
            ],
            "red",
        )
        warn(
            "Jangan gunakan HCl sebagai pengasam karena Cl⁻ dapat teroksidasi oleh KMnO₄ "
            "(reaksi sampingan). Gunakan H₂SO₄ encer."
        )

    else:
        card(
            "Larutan Kanji (Amilum)",
            [
                "Indikator spesifik untuk I₂",
                "Perubahan: Biru tua → Tidak berwarna (saat I₂ habis)",
                "Konsentrasi: 0.5% – 1% w/v",
            ],
            "teal",
            True,
        )
        warn(
            "Tambahkan larutan kanji <b>menjelang titik akhir titrasi</b> (saat warna sudah pucat kuning), "
            "bukan di awal — amilum yang berikatan terlalu lama dengan I₂ sulit terurai sehingga "
            "titik akhir menjadi tidak tajam."
        )

    done()

# ═══════════════════════════════════════════
# BRANCH 3 — TITRASI KOMPLEKSOMETRI
# ═══════════════════════════════════════════
elif pilih_jenis == "🔗 Titrasi Kompleksometri":
    st.subheader("🔗 Titrasi Kompleksometri (EDTA)")
    step(2, "Pilih Ion Logam yang Dititrasi")

    ION_DATA = {
        "Ca²⁺ / Mg²⁺": [
            ("EBT (Eriochrome Black T)", ["pH 10 — buffer amonia/amonium klorida",
             "Perubahan: Merah anggur → Biru"], "teal", True),
            ("Murexide", ["pH 12 — untuk Ca²⁺ saja (Mg²⁺ mengendap)",
             "Perubahan: Merah → Ungu"], "purple", False),
        ],
        "Zn²⁺": [
            ("EBT (Eriochrome Black T)", ["pH 10 — buffer amonia",
             "Perubahan: Merah anggur → Biru"], "teal", True),
            ("Xylenol Orange", ["pH 5–6 — buffer heksamin/asetat",
             "Perubahan: Merah-ungu → Kuning"], "orange", False),
        ],
        "Cu²⁺": [
            ("PAN (1-(2-Pyridylazo)-2-naphthol)", ["pH 4–5",
             "Perubahan: Violet → Kuning", "Pemanasan sedikit mempercepat reaksi"], "purple", True),
            ("Murexide", ["pH 8–9", "Perubahan: Kuning → Ungu"], "purple", False),
        ],
        "Fe²⁺ / Fe³⁺": [
            ("Asam Sulfosalisilat", ["pH 1–2 (untuk Fe³⁺ — suasana sangat asam)",
             "Perubahan: Merah → Tidak berwarna"], "red", True),
            ("Tiron", ["pH 4–10", "Perubahan: Biru → Tidak berwarna"], "teal", False),
        ],
        "Pb²⁺": [
            ("Xylenol Orange", ["pH 5–6 — buffer heksamin",
             "Perubahan: Merah-ungu → Kuning"], "orange", True),
            ("EBT", ["pH 10", "Perubahan: Merah anggur → Biru"], "teal", False),
        ],
        "Hg²⁺": [
            ("Xylenol Orange", ["pH 2–3 (asam nitrat encer)",
             "Perubahan: Merah → Kuning"], "orange", True),
            ("PAN", ["pH 3–4", "Perubahan: Violet → Kuning"], "purple", False),
        ],
        "Al³⁺": [
            ("PAN + titrasi balik ZnSO₄", ["pH 5–6 — buffer heksamin",
             "Perubahan (balik): Kuning → Merah", "Al³⁺ bereaksi lambat → titrasi balik"], "purple", True),
            ("Xylenol Orange + titrasi balik", ["pH 5",
             "Perubahan: Kuning → Merah-ungu"], "orange", False),
        ],
        "Ni²⁺": [
            ("Murexide", ["pH 8–9 — buffer amonia",
             "Perubahan: Kuning → Ungu"], "purple", True),
            ("PAN", ["pH 4–5", "Perubahan: Violet → Kuning"], "purple", False),
        ],
        "Co²⁺": [
            ("Murexide", ["pH 8–9 — buffer amonia",
             "Perubahan: Kuning → Ungu"], "purple", True),
            ("PAN", ["pH 4–5", "Perubahan: Violet → Kuning"], "purple", False),
        ],
    }

    ion = st.selectbox(
        "Ion Logam",
        ["── Pilih Ion Logam ──"] + list(ION_DATA.keys()),
        label_visibility="collapsed",
    )

    if ion != "── Pilih Ion Logam ──":
        st.divider()
        st.subheader(f"💡 Rekomendasi Indikator untuk **{ion}**")
        for name, rows, color, starred in ION_DATA[ion]:
            card(name, rows, color, starred)
        warn(
            "Titrasi kompleksometri umumnya menggunakan <b>EDTA (Na₂H₂Y)</b> sebagai titran. "
            "Pastikan pH larutan sesuai agar kompleks logam-indikator terbentuk dan terlepas dengan baik "
            "di titik akhir."
        )
        done()

# ═══════════════════════════════════════════
# BRANCH 4 — TITRASI PENGENDAPAN
# ═══════════════════════════════════════════
elif pilih_jenis == "🌧️ Titrasi Pengendapan":
    st.subheader("🌧️ Titrasi Pengendapan (Argentometri)")
    step(2, "Pilih Metode Argentometri")
    metode = st.radio(
        "Metode",
        ["Argentometri (Mohr)", "Argentometri (Volhard)", "Argentometri (Fajans)"],
        horizontal=True,
        label_visibility="collapsed",
    )
    st.divider()
    st.subheader("💡 Rekomendasi Indikator")

    if metode == "Argentometri (Mohr)":
        card(
            "Kalium Kromat — K₂CrO₄",
            [
                "Konsentrasi: 0.5% – 5% w/v",
                "Kondisi: pH 6.5 – 10.5 (netral – sedikit basa)",
                "Titik akhir: endapan <b>merah bata (Ag₂CrO₄)</b> permanen",
                "Analit: Cl⁻, Br⁻",
            ],
            "yellow",
            True,
        )
        warn(
            "Tidak dapat digunakan dalam suasana asam (pH < 6.5) — CrO₄²⁻ berubah menjadi Cr₂O₇²⁻. "
            "Juga tidak cocok untuk I⁻ dan SCN⁻ karena Ksp AgI dan AgSCN lebih kecil dari Ag₂CrO₄."
        )

    elif metode == "Argentometri (Volhard)":
        card(
            "Besi(III) Amonium Sulfat — NH₄Fe(SO₄)₂",
            [
                "Kondisi: suasana asam (HNO₃ encer, pH < 3)",
                "Titran: KSCN atau NH₄SCN (bukan AgNO₃ langsung untuk analit halida)",
                "Titik akhir: larutan berwarna <b>merah darah (FeSCN²⁺)</b> permanen",
                "Analit: Ag⁺, Cl⁻, Br⁻, I⁻, SCN⁻ (titrasi balik)",
            ],
            "red",
            True,
        )
        warn(
            "Untuk penetapan Cl⁻ secara tidak langsung, endapan AgCl harus disaring atau ditambahkan "
            "nitrobenzena agar SCN⁻ tidak bereaksi dengan AgCl. Jangan lakukan dalam suasana basa."
        )

    else:  # Fajans
        card(
            "Diklorofluoresein",
            [
                "Kondisi: pH 4 – 10 (rentang lebar)",
                "Titik akhir: endapan berubah dari putih → <b>merah muda</b>",
                "Analit: Cl⁻, Br⁻, I⁻",
                "Lebih sensitif dari fluoresein",
            ],
            "green",
            True,
        )
        card(
            "Fluoresein",
            [
                "Kondisi: pH 7 – 10 (netral – sedikit basa)",
                "Titik akhir: endapan berubah → <b>merah muda/kehijauan</b>",
                "Analit: Cl⁻ (paling umum)",
            ],
            "green",
        )
        warn(
            "Indikator adsorpsi (fluoresein/diklorofluoresein) bekerja dengan cara teradsorpsi pada "
            "permukaan endapan AgX. Hindari paparan cahaya matahari langsung yang intens selama titrasi "
            "karena dapat memfotodekomposisi indikator."
        )

    done()

# ─────────────────────────────────────────────
# PLACEHOLDER — belum pilih jenis
# ─────────────────────────────────────────────
else:
    st.info("👆 Pilih jenis titrasi di atas untuk memulai.", icon="ℹ️")
    st.markdown(
        """
        **Panduan singkat:**
        | Jenis | Titran | Contoh Analit |
        |---|---|---|
        | Asam-Basa | NaOH / HCl | Asam asetat, Na₂CO₃ |
        | Redoks | KMnO₄ / Na₂S₂O₃ | Fe²⁺, H₂O₂, I₂ |
        | Kompleksometri | EDTA | Ca²⁺, Mg²⁺, Zn²⁺ |
        | Pengendapan | AgNO₃ | Cl⁻, Br⁻, I⁻ |
        """
    )

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.divider()
st.markdown(
    """
    <div style='text-align:center; color:#999; font-size:.8em; margin-top:4px'>
        🧪 Sistem Rekomendasi Indikator Titrasi &nbsp;|&nbsp; Kimia Analitik &nbsp;|&nbsp; Kelompok 8
    </div>
    """,
    unsafe_allow_html=True,
)
