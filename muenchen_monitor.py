import requests

URI = "https://www56.muenchen.de/termin/index.php?option=s1"
HEADERS = { "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www56.muenchen.de",
            "Connection": "keep-alive",
            "Referer": "https://www56.muenchen.de/termin/?option=s1",
            "Cookie": "_et_coid=124256f7ae526ede36f04688a0851582; __utma=167456418.1180009072.1569152735.1569784646.1570264930.5; _utmz=167456418.1569152735.1.1.utmcsr=duckduckgo.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _gads=ID=901da83302ffab5d:T=1569152735:S=ALNI_MaM4cAPcZFXUEv1zQjREDXTbzpdLQ; PHPSESSID=cf0h4aqls3p1lssbkh36bp9394",
            "Upgrade-Insecure-Requests": "1" }

DATA = "step=WEB_APPOINT_SEARCH_BY_CASETYPES&CASETYPES%5BAn-+oder+Ummeldung+-+Einzelperson%5D=0&CASETYPES%5BAn-+oder+Ummeldung+-+Einzelperson+mit+eigenen+Fahrzeugen%5D=0&CASETYPES%5BAn-+oder+Ummeldung+-+Familie%5D=0&CASETYPES%5BAn-+oder+Ummeldung+-+Familie+mit+eigenen+Fahrzeugen%5D=1&CASETYPES%5BAbmeldung+%28Einzelperson+oder+Familie%29%5D=0&CASETYPES%5BFamilienstands%C3%A4nderung%2F+Namens%C3%A4nderung%5D=0&CASETYPES%5BAntrag+Personalausweis%5D=0&CASETYPES%5BAntrag+Reisepass%2FExpressreisepass%5D=0&CASETYPES%5BAntrag+vorl%C3%A4ufiger+Reisepass%5D=0&CASETYPES%5BAntrag+oder+Verl%C3%A4ngerung%2FAktualisierung+Kinderreisepass%5D=0&CASETYPES%5BAusweisdokumente+-+Familie+%28Minderj%C3%A4hrige+und+deren+gesetzliche+Vertreter%29%5D=0&CASETYPES%5BNachtr%C3%A4gliche+Anschriften%C3%A4nderung+Personalausweis%2FReisepass%2FeAT%5D=0&CASETYPES%5BNachtr%C3%A4gliches+Einschalten+eID+%2F+Nachtr%C3%A4gliche+%C3%84nderung+PIN%5D=0&CASETYPES%5BWiderruf+der+Verlust-+oder+Diebstahlanzeige+von+Personalausweis+oder+Reisepass%5D=0&CASETYPES%5BVerlust-+oder+Diebstahlanzeige+von+Personalausweis%5D=0&CASETYPES%5BVerlust-+oder+Diebstahlanzeige+von+Reisepass%5D=0&CASETYPES%5BGewerbezentralregisterauskunft+beantragen+%E2%80%93+nat%C3%BCrliche+Person%5D=0&CASETYPES%5BGewerbezentralregisterauskunft+beantragen+%E2%80%93+juristische+Person%5D=0&CASETYPES%5BBis+zu+5+Beglaubigungen+Unterschrift%5D=0&CASETYPES%5BBis+zu+5+Beglaubigungen+Dokument%5D=0&CASETYPES%5BBis+zu+20+Beglaubigungen%5D=0&CASETYPES%5BEintragung+%C3%9Cbermittlungssperre+-+Information%5D=0&CASETYPES%5BMeldebescheinigung+-+Information%5D=0&CASETYPES%5BHaushaltsbescheinigung+-+Information%5D=0&CASETYPES%5BMelderegisterauskunft+-+Information%5D=0&CASETYPES%5BF%C3%BChrungszeugnis+beantragen+-+Information%5D=0&CASETYPES%5BFahrzeug+wieder+anmelden%5D=0&CASETYPES%5BFahrzeug+au%C3%9Fer+Betrieb+setzen%5D=0&CASETYPES%5BAdress%C3%A4nderung+in+Fahrzeugpapiere+eintragen+lassen%5D=0&CASETYPES%5BNamens%C3%A4nderung+in+Fahrzeugpapiere+eintragen+lassen%5D=0"
result = requests.post(URI, data=DATA, headers=HEADERS)

with open("/media/green/hda/dev/tiramisu/result.html", "w") as f:
    f.write(result.text)
