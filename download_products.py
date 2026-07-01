import urllib.request
import urllib.parse
import re
import os
import json

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

for p in products:
    query = urllib.parse.quote(p["name"])
    url = f"https://images.search.yahoo.com/search/images?p={query}"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Yahoo images often store image URLs in iurl attribute or inside JSON
        img_urls = re.findall(r'imgurl=&quot;(http[^&]+)&quot;', html)
        if not img_urls:
            img_urls = re.findall(r'"imgurl":"([^"]+)"', html)
            
        if img_urls:
            img_url = img_urls[0].replace('\\/', '/')
            print(f"Downloading {p['name']} from {img_url}")
            
            try:
                img_req = urllib.request.Request(img_url, headers=headers)
                img_data = urllib.request.urlopen(img_req, timeout=10).read()
                
                with open(f"product-images/{p['filename']}", 'wb') as f:
                    f.write(img_data)
            except Exception as e2:
                print(f"  Failed to download image directly {e2}. Trying next...")
                if len(img_urls) > 1:
                    img_url = img_urls[1].replace('\\/', '/')
                    img_req = urllib.request.Request(img_url, headers=headers)
                    img_data = urllib.request.urlopen(img_req, timeout=10).read()
                    with open(f"product-images/{p['filename']}", 'wb') as f:
                        f.write(img_data)
        else:
            print(f"No image found for {p['name']}")
            
    except Exception as e:
        print(f"Failed to fetch {p['name']}: {e}")

print("Done.")
