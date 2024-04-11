from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)  # headless false para ver o processo
    contexto = navegador.new_context(record_video_dir='./video', record_video_size={"width": 1920, "height": 1080})
    pagina = contexto.new_page()

    pagina.goto("https://www.veneza.com.br/")
    pagina.locator('xpath=/html/body/div/main/div[3]/section/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/span[1]').click()
    pagina.locator('xpath=/html/body/div/main/div[3]/section/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/ul/li[1]/a/span').click()
    time.sleep(1)  # tem que esperar para clicar
    pagina.locator('xpath=/html/body/div/main/div[3]/section/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/span[2]').click()
    pagina.locator('xpath=/html/body/div/main/div[3]/section/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/ul/li[2]/a/span[1]').click()
    time.sleep(1)  # tem que esperar para clicar
    pagina.locator('xpath=/html/body/div/main/div[3]/section/div[2]/div/div[3]/a').click()
    time.sleep(1)  # tem que esperar para clicar
    pagina.locator('xpath=/html/body/div/main/div[3]/section/div[5]/div[4]/button').click()
    time.sleep(2)  # tem que esperar para clicar
    pagina.locator('xpath=/html/body/div/main/div[3]/section/div[5]/div[4]/button').click()

    # Espera um pouco para garantir que o vídeo tenha tempo para ser finalizado
    time.sleep(3)

    navegador.close()