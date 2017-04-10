## Scrapy project for scrap odds/probability for all the teams in Champions league(Sportech challange).  

First of all you need get lib 
```
gcc libffi-devel python-devel openssl-devel if you havent.
```
Geckodriver for selenium installation
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.13.0/geckodriver-v0.13.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
export PATH=$PATH:/path-to-extracted-file/geckodriver
```
To scrap web pages you need to run
```
scrapy crawl clodds
```
