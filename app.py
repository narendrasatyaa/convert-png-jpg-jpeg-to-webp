import streamlit as st
from PIL import Image, ImageOps
import io

st.set_page_config(page_title="Image to WebP Converter", page_icon="🖼️")

st.title("🖼️ Convert JPG/PNG ke WebP")

uploaded_file = st.file_uploader("Upload file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    filename = uploaded_file.name

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
