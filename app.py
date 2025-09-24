import streamlit as st
from PIL import Image, ImageOps
from pdf2image import convert_from_path
import io

st.set_page_config(page_title="Image/PDF to WebP Converter", page_icon="🖼️")

st.title("🖼️ Convert JPG/PNG/PDF ke WebP (Multiple Files)")

# Bisa upload banyak file sekaligus
uploaded_files = st.file_uploader(
    "Upload file (bisa lebih dari 1)",
    type=["jpg", "jpeg", "png", "pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        filename = uploaded_file.name
        st.write(f"📂 File: **{filename}**")

        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(uploaded_file)
            img = ImageOps.exif_transpose(img).convert("RGB")

            buf = io.BytesIO()
            img.save(buf, "WEBP", quality=80)
            byte_im = buf.getvalue()

            st.image(img, caption="Preview", use_column_width=True)
            st.download_button(
                "⬇️ Download WebP",
                data=byte_im,
                file_name=filename.rsplit(".", 1)[0] + ".webp",
                mime="image/webp"
            )

        elif filename.lower().endswith(".pdf"):
            try:
                images = convert_from_path(uploaded_file, dpi=200)
                for i, img in enumerate(images, start=1):
                    img = img.convert("RGB")
                    buf = io.BytesIO()
                    img.save(buf, "WEBP", quality=80)
                    byte_im = buf.getvalue()

                    st.image(img, caption=f"{filename} - Halaman {i}", use_column_width=True)
                    st.download_button(
                        f"⬇️ Download {filename}_page{i}.webp",
                        data=byte_im,
                        file_name=f"{filename.rsplit('.',1)[0]}_page{i}.webp",
                        mime="image/webp"
                    )
            except Exception as e:
                st.error(f"Gagal convert PDF {filename}: {e}")
