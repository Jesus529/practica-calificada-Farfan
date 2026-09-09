from flask import Flask, request, render_template_string, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Video Downloader</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: #f2f2f2;
            padding: 50px;
        }

        .container {
            background: white;
            padding: 30px;
            max-width: 600px;
            margin: auto;
            border-radius: 10px;
        }

        input {
            width: 90%;
            padding: 12px;
            margin: 10px;
        }

        button {
            padding: 12px 25px;
            background: #333;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>🎥 Video Downloader</h1>

    <p>YouTube, Instagram, TikTok, Facebook y otras plataformas compatibles</p>

    <form method="POST">

        <input
            type="text"
            name="url"
            placeholder="Pega aquí la URL del video"
            required
        >

        <br>

        <button type="submit">
            Descargar
        </button>

    </form>

    {% if mensaje %}
        <p>{{ mensaje }}</p>
    {% endif %}

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():

    mensaje = ""

    if request.method == "POST":

        url = request.form.get("url")

        if not url:
            mensaje = "Debes ingresar una URL."
            return render_template_string(HTML, mensaje=mensaje)

        nombre = str(uuid.uuid4())

        salida = os.path.join(
            DOWNLOAD_FOLDER,
            nombre + ".%(ext)s"
        )

        opciones = {
            "outtmpl": salida,
            "format": "best",
            "noplaylist": True
        }

        try:

            with yt_dlp.YoutubeDL(opciones) as ydl:

                info = ydl.extract_info(url, download=True)

                archivo = ydl.prepare_filename(info)

            return send_file(
                archivo,
                as_attachment=True
            )

        except Exception as e:

            mensaje = "No se pudo descargar el video."

    return render_template_string(
        HTML,
        mensaje=mensaje
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )