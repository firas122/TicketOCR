# TicketOCR

A Flask API that scans a retail receipt (given as an image URL), runs it through OpenCV pre-processing + Tesseract/Nanonets OCR, and returns a structured JSON breakdown of the purchase (store, date, time, total, and line items) using retailer-specific regex parsers (currently Monoprix, Carrefour, Aziza, and City Market receipt formats).

## How it works

1. Downloads the receipt image from a given URL.
2. Runs several OpenCV pre-processing passes (grayscale, threshold, edge detection, skew correction) to improve OCR accuracy.
3. Extracts raw text via both local Tesseract OCR and the Nanonets OCR API, then picks whichever retailer-specific parse produced the most line items.
4. Matches product names against a MongoDB product catalog to auto-correct OCR typos.
5. Persists the parsed result to MongoDB and returns it as JSON.

## Setup

### Prerequisites

- Python 3.9+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and on your `PATH` (or point `TESSERACT_CMD` at the binary)
- [ImageMagick](https://imagemagick.org/) (required by the `Wand` library)
- A MongoDB database (e.g. MongoDB Atlas)
- A [Nanonets](https://nanonets.com/) OCR API key

### Installation

```sh
git clone https://github.com/firas122/TicketOCR
cd TicketOCR
pip install -r work/requirements.txt
cp .env.example .env   # then fill in MONGO_URI and NANONETS_API_KEY
```

### Running

```sh
cd work
python api.py
```

The API listens on `0.0.0.0:5000` by default, exposing a single route: `/do`.

## Usage

Send a `POST` request to `/do` with the receipt image URL and (optionally) some user metadata:

```sh
curl -X POST http://localhost:5000/do \
  -d "url=https://example.com/receipt.jpg" \
  -d "user_nom=Doe" \
  -d "user_prenom=John" \
  -d "user_email=john@example.com"
```

Response:

```json
{
    "date": "24/02/2021",
    "name": "Monoprix",
    "products": [
        {
            "pname": "TAMPON EPONGE A RE",
            "pquantity": 1,
            "ptotal": 1230.0,
            "pupri": 1230.0
        },
        {
            "pname": "YAOURT AU FRUITS",
            "pquantity": 2,
            "ptotal": 1440.0,
            "pupri": 720.0
        }
    ],
    "time": "14:02",
    "total": 5480.0
}
```

## Roadmap

- [x] Image pre-processing
- [x] OCR text extraction
- [x] Retailer-specific data classification
- [ ] Multi-ticket form support
- [ ] Machine-learning-based classification (replace hand-written regex parsers)

## License

MIT — see [LICENSE](LICENSE).
