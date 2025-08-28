# Nested Dictionary API

## Deskripsi

Project ini adalah sebuah API sederhana berbasis **Flask** yang mengubah input berupa array 1 dimensi menjadi struktur data bersarang tiga level berdasarkan:

- `category`
- `sub_category`
- Data user (`id`, `name`)

Contoh input:

```json
[
  { "id": 1, "name": "Alice", "category": "A", "sub_category": "X" },
  { "id": 2, "name": "Bob", "category": "B", "sub_category": "Y" },
  { "id": 3, "name": "Charlie", "category": "A", "sub_category": "Z" },
  { "id": 4, "name": "David", "category": "B", "sub_category": "X" }
]
```

Contoh output:

```json
{
  "A": {
    "X": [
      {
        "id": 1,
        "name": "Alice"
      }
    ],
    "Z": [
      {
        "id": 3,
        "name": "Charlie"
      }
    ]
  },
  "B": {
    "Y": [
      {
        "id": 2,
        "name": "Bob"
      }
    ],
    "X": [
      {
        "id": 4,
        "name": "David"
      }
    ]
  }
}
```

---

## Persyaratan

- Python 3.8+
- Flask

---

## Instalasi

1. Clone repository ini
   ```bash
   git clone https://github.com/username/array-parsing-and-formating.git
   cd array-parsing-and-formating
   ```
2. Install dependency
   ```bash
   pip install flask
   ```

---

## Menjalankan Server

```bash
python main.py
```

Secara default server akan berjalan di:

```
http://127.0.0.1:5000/
```

---

## Endpoint

### `POST /api/category`

- **Request Body (JSON)**:

```json
[
  { "id": 1, "name": "Alice", "category": "A", "sub_category": "X" },
  { "id": 2, "name": "Bob", "category": "B", "sub_category": "Y" }
]
```

- **Response (JSON)**:

```json
{
  "A": {
    "X": [
      {
        "id": 1,
        "name": "Alice"
      }
    ]
  },
  "B": {
    "Y": [
      {
        "id": 2,
        "name": "Bob"
      }
    ]
  }
}
```

Output JSON akan selalu dikembalikan dalam **satu baris** agar lebih ringkas.

---

## Catatan

- Hanya menerima **POST request**.

---

## Lisensi

MIT License
