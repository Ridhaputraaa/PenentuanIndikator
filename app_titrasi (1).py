import streamlit as st

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Sistem Rekomendasi Indikator Titrasi",
    page_icon="🥉",
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
            color: #000000 !important;
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

        .card,
        .card *,
        .card h4,
        .card p,
        .card div,
        .card span {
            color: #000000 !important;
        }

        .card h4 {
            margin: 0 0 6px 0;
            font-size: 1.05em;
        }

        .card p {
            margin: 2px 0;
            font-size: .93em;
        }

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
        <h1>👩🏻‍🔬 Sistem Rekomendasi Indikator Titrasi</h1>
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


# =========================
# MENU UTAMA
# =========================
st.markdown("### 🎯 Pilih Tujuan")

fitur = st.radio(
    "",
    [
        "Menentukan Indikator Titrasi",
        "Menghitung Standarisasi Larutan"
    ]
)

st.divider()

# ─────────────────────────────────────────────
# FITUR 1 — STANDARISASI LARUTAN
# ─────────────────────────────────────────────
if fitur == "Menghitung Standarisasi Larutan":

    st.subheader("🧪 Perhitungan Standarisasi Larutan")

    # FIX: gunakan selectbox dengan pilihan string biasa, bukan st.button()
    metode = st.selectbox(
        "Pilih Metode Standarisasi",
        [
            "── Pilih ──",
            "NaOH dengan Asam Oksalat",
            "HCl dengan Boraks",
            "KMnO4 dengan Asam Oksalat",
            "Na2S2O3 dengan Kalium Dikromat",
            "EDTA dengan CaCO3",
        ]
    )

    if metode == "NaOH dengan Asam Oksalat":
        massa = st.number_input("Massa Asam Oksalat (mg)", min_value=0.0, format="%.4f")
        volume = st.number_input("Volume NaOH (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 0.063  # mg/mgrek (BM=126, valensi=2 → BE=63 g/ek = 0.063 mg/mgrek)
                N = massa / ((100 / 25) * volume * BE)
                st.success(f"Normalitas NaOH = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "HCl dengan Boraks":
        massa = st.number_input("Massa Boraks (mg)", min_value=0.0, format="%.4f")
        volume = st.number_input("Volume HCl (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 0.1907  # mg/mgrek (BM=381.4, valensi=2 → BE=190.7 g/ek = 0.1907 mg/mgrek)
                N = massa / ((100 / 25) * volume * BE)
                st.success(f"Normalitas HCl = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "KMnO4 dengan Asam Oksalat":
        massa = st.number_input("Massa Asam Oksalat (mg)", min_value=0.0, format="%.4f")
        volume = st.number_input("Volume KMnO4 (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 0.063  # mg/mgrek (BM=126, valensi=2 → BE=63 g/ek = 0.063 mg/mgrek)
                N = massa / ((100 / 25) * volume * BE)
                st.success(f"Normalitas KMnO₄ = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "Na2S2O3 dengan Kalium Dikromat":
        massa = st.number_input("Massa K2Cr2O7 (mg)", min_value=0.0, format="%.4f")
        volume = st.number_input("Volume Na2S2O3 (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 0.04904  # mg/mgrek (BM=294.2, valensi=6 → BE=49.04 g/ek = 0.04904 mg/mgrek)
                N = massa / ((100 / 25) * volume * BE)
                st.success(f"Normalitas Na₂S₂O₃ = {N:.4f} N")
            else:
                st.error("Volume tidak boleh 0.")

    elif metode == "EDTA dengan CaCO3":
        massa = st.number_input("Massa CaCO3 (mg)", min_value=0.0, format="%.4f")
        volume = st.number_input("Volume EDTA (mL)", min_value=0.0, format="%.2f")
        if st.button("Hitung Konsentrasi"):
            if volume > 0:
                BE = 0.05005  # mg/mgrek (BM=100.09, valensi=2 → BE=50.05 g/ek = 0.05005 mg/mgrek)
                M = massa / ((100 / 25) * volume * BE)
                st.success(f"Molaritas EDTA = {M:.4f} M")
            else:
                st.error("Volume tidak boleh 0.")

# ─────────────────────────────────────────────
# FITUR 2 — MENENTUKAN INDIKATOR
# ─────────────────────────────────────────────
elif fitur == "Menentukan Indikator Titrasi":

    step(1, "Pilih Jenis Titrasi")

    JENIS = [
        "── Pilih ──",
        "🔴 Titrasi Asam-Basa",
        "🟡 Titrasi Redoks",
        "🟣 Titrasi Kompleksometri",
        "🟢 Titrasi Argentometri",
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

            else:  # Asam Lemah oleh Basa Lemah
                warn(
                    "Titrasi asam lemah – basa lemah <b>tidak direkomendasikan</b> secara analitik "
                    "karena tidak memiliki titik ekuivalen yang tajam, sehingga titik akhir titrasi sangat sulit dideteksi menggunakan indikator warna standar.")

        done()

    # ═══════════════════════════════════════════
    # BRANCH 2 — TITRASI REDOKS
    # ═══════════════════════════════════════════
    elif pilih_jenis == "🟡 Titrasi Redoks":
        st.subheader("🟡 Titrasi Redoks")
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
            card("KMnO₄ — Autoindicator",
                [
                    "KMnO₄ sendiri bertindak sebagai indikator",
                    "Titik akhir: larutan berubah merah muda",
                    "Titrasi dalam suasana asam (H₂SO₄ encer)",
                ], "purple", True)
            warn("Penggunaan blanko sangat dianjurkan untuk mengoreksi hasil titrasi.")
            card(
                "Ferroin (1,10-fenantrolin)",
                [
                    "Dalam keadaan tereduksi, kompleks ini berwarna merah pekat.",
                    "Ketika dioksidasi, kompleks ini berubah menjadi berwarna biru pucat (atau biru).",
                    "Perubahan warna ini bersifat reversibel",
                ],
                "red",
            )

        else:  # Iodometri / Iodimetri
            card(
                "Larutan Kanji (Amilum)",
                [
                    "Digunakan pada titrasi redoks yang melibatkan iodin (I₂)",
                    "Perubahan: Biru → Tidak berwarna (saat I₂ habis)",
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
    elif pilih_jenis == "🟣 Titrasi Kompleksometri":
        st.subheader("🟣 Titrasi Kompleksometri (EDTA)")
        step(2, "Pilih Ion Logam yang Dititrasi")

        ION_DATA = {
            "Ca²⁺ / Mg²⁺": [
                ("EBT (Eriochrome Black T)", ["pH 10 — buffer amonia/amonium klorida",
                 "Perubahan: Merah anggur → Biru"], "teal", True),
            ],
            "Zn²⁺": [
                ("EBT (Eriochrome Black T)", ["pH 10 — buffer amonia",
                 "Perubahan: Merah anggur → Biru"], "teal", True),
            ],
            "Cu²⁺": [
                ("Murexide", ["pH 8–9", "Perubahan: Kuning → Ungu"], "purple", True),
            ],
            "Fe²⁺ / Fe³⁺": [
                ("Asam salisilat", ["pH 1–2 (untuk Fe³⁺ — suasana sangat asam)",
                 "Perubahan: Merah → Tidak berwarna"], "red", True),
                ("Tiron", ["pH 4–10", "Perubahan: Biru → Tidak berwarna"], "teal", False),
            ],
            "Pb²⁺": [
                ("Xylenol Orange", ["pH 5–6 — buffer heksamin",
                 "Perubahan: Merah-ungu → Kuning"], "orange", True),
            ],
            "Hg²⁺": [
                ("Xylenol Orange", ["pH 2–3 (asam nitrat encer)",
                 "Perubahan: Merah → Kuning"], "orange", True),
            ],
            "Al³⁺": [
                ("Xylenol Orange + titrasi balik", ["pH 5",
                 "Perubahan: Kuning → Merah-ungu"], "orange", True),
            ],
            "Ni²⁺": [
                ("Murexide", ["pH 8–9 — buffer amonia",
                 "Perubahan: Kuning → Ungu"], "purple", True),
            ],
            "Co²⁺": [
                ("Murexide", ["pH 8–9 — buffer amonia",
                 "Perubahan: Kuning → Ungu"], "purple", True),
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
    # BRANCH 4 — TITRASI ARGENTOMETRI
    # ═══════════════════════════════════════════
    elif pilih_jenis == "🟢 Titrasi Argentometri":
        st.subheader("🟢 Titrasi Argentometri")
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
                    "Kondisi: pH 6.5 – 10,0 (netral – sedikit basa)",
                    "Titik akhir: endapan merah bata (Ag₂CrO₄) permanen",
                    "Analit: halida, CN⁻, dan CNS",
                ], "yellow", True)
            warn(
                "Tidak dapat digunakan dalam suasana asam karena CrO₄²⁻ akan berubah menjadi Cr₂O₇²⁻. "
                "Tidak dapat digunakan dalam suasana basa karena akan terbentuk endapan AgOH.")

        elif metode == "Argentometri (Volhard)":
            card(
                "Besi(III) Amonium Sulfat — NH₄Fe(SO₄)₂",
                [
                    "Kondisi: suasana asam (HNO₃ 4N)",
                    "Titik akhir: larutan berwarna merah (FeSCN²⁺) permanen",
                    "Analit: Ag⁺, Cl⁻, Br⁻, I⁻",
                ],
                "red",
                True,
            )
            warn(
                "Untuk penetapan Cl⁻ secara tidak langsung, endapan AgCl harus disaring atau ditambahkan "
                "pelarut organik agar SCN⁻ tidak bereaksi dengan AgCl."
            )

        else:  # Fajans
            card(
                "Diklorofluoresein",
                [
                    "Kondisi: pH 4 – 10",
                    "Titik akhir: endapan putih → merah muda",
                    "Analit: Cl⁻, Br⁻, I⁻",
                ],
                "green",
                True,
            )
            card(
                "Fluoresein",
                [
                    "Kondisi: pH 7 – 8,5 (netral – sedikit basa)",
                    "Titik akhir: endapan putih → merah muda",
                    "Analit: Cl⁻",
                ],
                "green",
            )
            warn(
                "Indikator adsorpsi (fluoresein/diklorofluoresein) bekerja dengan cara teradsorpsi pada "
                "permukaan endapan AgX."
            )

        done()

    # ─────────────────────────────────────────────
    # PLACEHOLDER — belum pilih jenis
    # ─────────────────────────────────────────────
    else:
        st.info("👆 Pilih jenis titrasi di atas untuk memulai.", icon="⚠️")
        st.markdown(
            """
            **Panduan singkat:**
            | Jenis | Titran | Contoh Analit |
            |---|---|---|
            | Asam-Basa | NaOH / HCl | CH₃COOH, Na₂CO₃ |
            | Redoks | KMnO₄ / Na₂S₂O₃ | Fe²⁺, Cl⁻, I₂ |
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
        🥉 Sistem Rekomendasi Indikator Titrasi &nbsp;|&nbsp; Kelompok 8
    </div>
    """,
    unsafe_allow_html=True,
)
