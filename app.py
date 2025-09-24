import streamlit as st
from PIL import Image, ImageOps
from pdf2image import convert_from_path
import io

st.set_page_config(page_title="Image/PDF to WebP Converter", page_icon="🖼️")

st.title("🖼️ Convert JPG/PNG/PDF ke WebP")

uploaded_file = st.file_uploader("Upload file", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    filename = uploaded_file.name

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
            images = convert_from_path(uploaded_file, dpi=200)  # list of PIL images
            for i, img in enumerate(images, start=1):
                img = img.convert("RGB")
                buf = io.BytesIO()
                img.save(buf, "WEBP", quality=80)
                byte_im = buf.getvalue()

                st.image(img, caption=f"Halaman {i}", use_column_width=True)
                st.download_button(
                    f"⬇️ Download Halaman {i} (WebP)",
                    data=byte_im,
                    file_name=f"{filename.rsplit('.',1)[0]}_page{i}.webp",
                    mime="image/webp"
                )
        except Exception as e:
            st.error(f"Gagal convert PDF: {e}")
