import qrcode

# URL del sitio (en este caso el local de Django)
url = "http://127.0.0.1:8000/"

# Crear el QR
img = qrcode.make(url)

# Guardar en archivo
img.save("qr_optica.png")

print("✅ Código QR generado como 'qr_optica.png'. Escanealo y abrirá el sitio.")
