# Rendez-vous passeports - Paris

## Contexte
Sur https://teleservices.paris.fr/rdvtitres/jsp/site/Portal.jsp?page=appointmentsearch&category=titres les rendez-vous apparaissent au fur et à mesure et sont très rapidement pris d'assaut. Au lieu d'actualiser sans arrêt la page, ce script permet de rafraichir automatiquement la page et de faire une alerte vocale si un nouveau rendez-vous apparaît.

## Installation
### Chromium
Installez Chrome et chromium correspondant à votre version de Chrome.
Vérifier votre version de google chrome
```
google-chrome --version
```
Allez sur cette page https://chromedriver.chromium.org/downloads copier le lien correspondant à votre version et pour votre système (par exemple
https://chromedriver.storage.googleapis.com/95.0.4638.54/chromedriver_linux64.zip)

Lancez ensuite les commandes suivantes (exemple pour Linux, adaptez le pour Mac ou Windows)
```
wget <LINK>
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
rm chromedriver_linux64.zip
```
Selenium devrait fonctionner.

### Packages
A la racine du repo, installez les packages avec pipenv
```
pipenv install
```

### Variables d'environnement
Créer un fichier .env (même structure que .env_default) et renseigner les informations
DATE_LIMIT: date maximum de rendez-vous
PASSWORD: votre mot de passe de la mairie de Paris
SELENIUM_IS_HEADLESS: 0 ou 1, si selenium tourne headless ou non
USERNAME= votre email de votre compte de la mairie de Paris

## Lancement
Lancez directement
```
pipenv run python appointment_alert.py
```
