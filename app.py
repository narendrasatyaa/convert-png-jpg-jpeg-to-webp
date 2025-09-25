import streamlit as st
from PIL import Image, ImageOps
import io

st.set_page_config(page_title="Image to WebP Converter", page_icon="🖼️")

st.title("Convert JPG/PNG ke WebP (Multiple Files)")

uploaded_files = st.file_uploader(
    "Upload gambar (bisa lebih dari 1)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        filename = uploaded_file.name
        st.write(f"📂 File: **{filename}**")

        try:
            # buka gambar
            img = Image.open(uploaded_file)
            img = ImageOps.exif_transpose(img).convert("RGB")

            # simpan ke buffer dalam format webp
            buf = io.BytesIO()
            img.save(buf, "WEBP", quality=80)
            byte_im = buf.getvalue()

            # preview + tombol download
            st.image(img, caption="Preview", use_column_width=True)
            st.download_button(
                "⬇️ Download WebP",
                data=byte_im,
                file_name=filename.rsplit(".", 1)[0] + ".webp",
                mime="image/webp"
            )
        except Exception as e:
            st.error(f"Gagal memproses {filename}: {e}")
