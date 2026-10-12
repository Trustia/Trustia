import urllib.request
import json
import urllib.parse
import time
import os

headers = {'User-Agent': 'TrustiaBot/1.0 (info@trustia.ai)'}

def search_and_download():
    dest_dir = r'C:\Users\Asus\Desktop\Trustia\Kurumsal\Medya\Canva_Icin_Kapak_Fotolari'
    
    # Specific curated top-tier autonomous car images on Wikimedia Commons:
    # 1. Waymo One Jaguar I-Pace (LiDAR on roof, clean road shot)
    # 2. Cruise Origin autonomous shuttle
    # 3. Baidu Apollo autonomous taxi
    targets = [
        ('Waymo autonomous car', '05_Waymo_Jaguar_Otonom_LiDAR.jpg'),
        ('Motional autonomous', '06_Motional_L4_Robotaxi.jpg'),
        ('Zoox autonomous vehicle', '07_Zoox_Otonom_Shuttle.jpg')
    ]
    
    for query, filename in targets:
        time.sleep(2)
        url = f'https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrlimit=10&prop=imageinfo&iiprop=url|size'
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
            
            pages = data.get('query', {}).get('pages', {})
            best_img = None
            for pid, p in pages.items():
                if 'imageinfo' in p and p['imageinfo']:
                    info = p['imageinfo'][0]
                    # Filter for JPG/PNG and landscape high res
                    if info.get('width', 0) >= 2000 and (info['url'].lower().endswith('.jpg') or info['url'].lower().endswith('.png')):
                        best_img = info['url']
                        break
            
            if best_img:
                dest = os.path.join(dest_dir, filename)
                print(f"Downloading {filename} from {best_img}...")
                img_req = urllib.request.Request(best_img, headers=headers)
                with urllib.request.urlopen(img_req) as img_resp, open(dest, 'wb') as out_f:
                    out_f.write(img_resp.read())
                print(f"Saved {filename} ({os.path.getsize(dest)} bytes)")
            else:
                print(f"No match for {query}")
        except Exception as e:
            print(f"Error for {query}: {e}")

if __name__ == '__main__':
    search_and_download()
