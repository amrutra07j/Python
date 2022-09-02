import requests
from bs4 import BeautifulSoup
import smtplib
ama = requests.get("https://www.amazon.in/Redmi-Stealth-Additional-Exchange-Included/dp/B09T39K9YL/?_encoding=UTF8&pd_rd_w=hUPbZ&content-id=amzn1.sym.ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_p=ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_r=H8H741P08KKWVDQ75N02&pd_rd_wg=M8IDb&pd_rd_r=1134bb1c-321d-43b3-98cf-43e86c0e7b63&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1", headers={"Accept-Language":"en-US,en;q=0.9,fr;q=0.8,kn;q=0.7", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
soup = BeautifulSoup(ama.text, "html.parser")
price = soup.find(class_="a-price a-text-price a-size-medium apexPriceToPay")
GMAIL = "udemyt07@gmail.com"
Y_EMAIL = "udemyt07@yahoo.com"
Y_PASSWORD = "xmztmmahhsfnmboj"
PASSWORD = "Tyrion@07"
if float(price.getText().split('₹')[1].replace(',', '')) < 20000:
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as server:
        server.starttls()
        server.login(user=Y_EMAIL, password=Y_PASSWORD)
        server.sendmail(Y_EMAIL, "msdraj52@gmail.com", f"Subject:Amazon Buy\n\nYour wish for Redmi note 11 pro 5g is completed with price of {float(price.getText().split('₹')[1].replace(',', ''))}")
        print("Sent Mail")