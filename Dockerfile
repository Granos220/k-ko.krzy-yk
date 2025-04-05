# Używamy obrazu Pythona
FROM python:3.11-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik z grą do kontenera
COPY kolko.krzyzyk.py .

# Domyślna komenda do uruchomienia gry
CMD ["python", "kolko.krzyzyk.py"]
