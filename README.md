# stepik homework

python = 3.6.9
selenium 3.14.0

## install
### Настройка временного окружения
python3 -m venv selenium_env
source selenium_env/bin/activate

pip install selenium==3.14.0
Chromedriver:
https://sites.google.com/a/chromium.org/chromedriver/downloads

unzip chromedriver_linux64.zip

Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:

sudo mv chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
