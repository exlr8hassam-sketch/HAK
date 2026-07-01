from duckduckgo_search import DDGS
import requests
import os
import time

products = [
    {"id": 1, "name": "Golden Pearl Brightening Rice Kit", "filename": "golden_pearl_rice_kit.jpg"},
    {"id": 2, "name": "Garnier Vitamin C Brightening Set", "filename": "garnier_vitamin_c.jpg"},
    {"id": 3, "name": "Miss Rose Velvet Matte Lipstick", "filename": "miss_rose_lipstick.jpg"},
    {"id": 4, "name": "Sadoer Pores Purify 4-in-1 Cream", "filename": "sadoer_cream.jpg"},
    {"id": 5, "name": "Adidas Skincare Deal Bundle", "filename": "adidas_skincare.jpg"},
    {"id": 6, "name": "Lux Skincare Deal Set", "filename": "lux_skincare.jpg"},
    {"id": 7, "name": "Macley Korean Glass Skin Serum", "filename": "macley_serum.jpg"},
    {"id": 8, "name": "Rivaj Matte Foundation", "filename": "rivaj_foundation.jpg"},
    {"id": 9, "name": "Heaven Beauty Contour Kit", "filename": "heaven_beauty_contour.jpg"},
    {"id": 10, "name": "Garnier Centella Defense Toner", "filename": "garnier_toner.jpg"},
    {"id": 11, "name": "Skin White Deal Set", "filename": "skin_white_deal.jpg"},
    {"id": 12, "name": "Fair Menz Grooming Kit", "filename": "fair_menz_grooming.jpg"}
]

os.makedirs('product-images', exist_ok=True)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

with DDGS() as ddgs:
    for p in products:
        print(f"Searching for {p['name']}...")
        try:
            results = ddgs.images(p['name'], max_results=3)
            success = False
            for r in results:
                img_url = r['image']
                try:
                    img_data = requests.get(img_url, headers=headers, timeout=10).content
                    with open(f"product-images/{p['filename']}", 'wb') as f:
                        f.write(img_data)
                    print(f"  Downloaded from {img_url}")
                    success = True
                    break
                except Exception as e:
                    print(f"  Failed URL {img_url}: {e}")
            if not success:
                print(f"  Could not download any image for {p['name']}")
        except Exception as e:
            print(f"  Search failed for {p['name']}: {e}")
        time.sleep(1)

print("Done.")
