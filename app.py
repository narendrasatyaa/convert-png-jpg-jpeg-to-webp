import streamlit as st
from PIL import Image, ImageOps
import io
import zipfile
import os

st.set_page_config(page_title="Image to WebP Converter", page_icon="🖼️")

st.title("🖼️ Convert JPG/PNG ke WebP (Multiple Files + ZIP Download)")

uploaded_files = st.file_uploader(
    "Upload gambar (bisa lebih dari 1)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for uploaded_file in uploaded_files:
            filename = uploaded_file.name
            st.write(f"📂 File: **{filename}**")

            try:
                # buka gambar
                img = Image.open(uploaded_file)
                img = ImageOps.exif_transpose(img).convert("RGB")

                # simpan ke buffer webp
                buf = io.BytesIO()
                img.save(buf, "WEBP", quality=80)
                byte_im = buf.getvalue()

                # preview + tombol download individual
                st.image(img, caption="Preview", use_column_width=True)
                st.download_button(
                    "⬇️ Download WebP",
                    data=byte_im,
                    file_name=filename.rsplit(".", 1)[0] + ".webp",
                    mime="image/webp"
                )

                # tambahkan ke zip
                zip_file.writestr(filename.rsplit(".", 1)[0] + ".webp", byte_im)

            except Exception as e:
                st.error(f"Gagal memproses {filename}: {e}")

    # finalize zip
    zip_buffer.seek(0)
    st.download_button(
        "⬇️ Download Semua (ZIP)",
        data=zip_buffer,
        file_name="converted_images.zip",
        mime="application/zip"
    )

