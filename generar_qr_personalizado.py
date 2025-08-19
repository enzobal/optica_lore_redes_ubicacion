import qrcode
from PIL import Image

# URL a la que debe llevar el QR
url = "http://127.0.0.1:8000/"  # Cambiar por el dominio real cuando esté online

# Crear objeto QR con configuraciones
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño (1 = más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección de errores (permite poner logo)
    box_size=10,  # Tamaño de cada cuadro
    border=4,  # Grosor del borde blanco
)

qr.add_data(url)
qr.make(fit=True)

# Generar imagen base (color degradado manual luego)
img_qr = qr.make_image(fill_color="#2C5364", back_color="white").convert("RGB")

# Abrir el logo
logo_path = "static/img/logo_optica.png"  # Ruta a tu logo
logo = Image.open(logo_path)

# Ajustar tamaño del logo
logo_size = 80
logo = logo.resize((logo_size, logo_size))

# Pegar logo en el centro del QR
pos = ((img_qr.size[0] - logo_size) // 2, (img_qr.size[1] - logo_size) // 2)
img_qr.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)

# Guardar el QR final
img_qr.save("qr_optica_personalizado.png")

print("✅ QR personalizado generado: qr_optica_personalizado.png")
