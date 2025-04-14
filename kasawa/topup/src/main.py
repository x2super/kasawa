import cloudscraper

def topup(phone, vouch):
    """
    this is get money from angpao in true money wallett this
    so easy to use and skip cloudflare if your programs is have
    """
    scaper = cloudscraper.create_scraper()
    payload = {
    "phone": phone,
    "vouch": vouch
    }

    r = scaper.post("https://api.kasawa.pro/api/wallet/topup",json=payload)
    return r.json()