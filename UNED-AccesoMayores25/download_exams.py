from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os

os.makedirs('downloads', exist_ok=True)

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": os.path.abspath('downloads'),
    "download.prompt_for_download": False,
    "safebrowsing.enabled": False
})
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

print("🌐 Abriendo navegador...")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

print("📄 Accediendo a educalive.com...")
driver.get('https://www.educalive.com/examenes-prueba-acceso-mayores-25-uned')

print("⏳ Esperando carga (5s)...")
time.sleep(5)

# Buscar PDFs
links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
print(f"📋 Encontrados {len(links)} PDFs\n")

pdf_urls = []
for link in links:
    href = link.get_attribute('href')
    text = link.text.strip()
    if href and 'pdf' in href.lower():
        pdf_urls.append(href)
        print(f"  ✓ {text[:60] or href[-40:]}")

print(f"\n⬇️  Descargando {len(pdf_urls)} archivos...\n")
for i, url in enumerate(pdf_urls, 1):
    try:
        filename = url.split('/')[-1][:50]
        print(f"  {i}. {filename}")
        driver.get(url)
        time.sleep(1)
    except Exception as e:
        print(f"     ❌ {str(e)[:40]}")

print("\n✅ Completado en: downloads/")
driver.quit()
