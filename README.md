# Hello DevOps - FastAPI (Beadandó)

Egy egyszerű **FastAPI** "Hello World" alkalmazás, amely bemutatja a következő DevOps lépéseket:
- kódkészítés
- verziókövetés
- buildelés
- konténerizálás (Docker)
- választott extra: Dev Container

---

## Fájlok
- `main.py` – a FastAPI app
- `requirements.txt` – függőségek
- `Dockerfile` – image build (production)
- `.devcontainer/devcontainer.json` – devcontainer konfiguráció
- `.gitignore`, `README.md` – dokumentáció

---

## Követelmények (lokálisan)
- Git
- Docker (ha a konténert futtatod)
- Python 3.11 (ha lokálisan futtatod venv-ben)
- VS Code + Remote - Containers (ha devcontainer-t használsz)

---

## Lokális futtatás (fejlesztés)
```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows
pip install --upgrade pip
pip install -r requirements.txt
```
---

## Docker build + futtatás
```bash
docker build -t hello-devops-fastapi:v1 #buildelés
docker run -p 8000:8000 hello-devops-fastapi:v1  #konténer futtatás
```
---

## Dev Container futtatás

>Reopen in Container
```bash
uvicorn main:app --reload --host 0.0.0.0
```