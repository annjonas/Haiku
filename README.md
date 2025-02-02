# Haiku

Haiku to projekt który ma na celu zaprezentowanie wykorzystania Redisa jako buforu dla zasobów, których generowanie zajmuje dużo czasu.

## Instalacja

```bash
docker-compose up --build
```

## Działanie

* Frontend (React) dzialajacy na porcie 3000
* Backend (Python) dzialajacy na porcie 5000
* Kolejka (Redis) dzialajaca na porcie 6379

Backend asynchronicznie generuje haiku, przechowuje je w buforze w Redis i obsługuje żądania Api.
Czas oczekiwania na odpowiedź zależy od ilości haiku w buforze.
Jeśli w buforze będzie więcej haiku niż żądano, zostaną one zwrócone natychmiast
Jeśli w buforze będzie mniej haiku niż żądano, zostaną one zwrócone, gdy wszystkie zostaną wygenerowane.

## Autorzy

* Szymon Nowaczyk
* Anna Jonas
* Jan Maciejewski
