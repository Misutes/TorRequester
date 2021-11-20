## TOR SERVER
### For startup the app:
1. Install [python 3.9.1+](https://www.python.org/downloads/)
2. Install pipenv (shell command):
    * `pip install pipenv`
3. Install requirements (shell command):
    * `pipenv install`
4. Set env variables:
    * Open file `.env`
    * TOR_ADDRESS - address is use for tor
    * SERVER_ADDRESS - address is use for db server
    * CHECKER_ADDRESS - address is use for check service
    * TOTAL_EMAILS - how many emails handle at one time (recommend about 500)
    * RAISE_TIMEOUT - if emails not found, retry after that timeout
    * TIMEOUT - timeout after handling packs of emails
5. Run the app (shell command):
* Important! You should be at `src` directory
    * `pipenv run uvicorn main:app --port <CHOSE_YOUR_PORT>`
6. Stop the app press:
   * `Ctrl + C`

### For app docs:
Load site-page `http://127.0.0.1:<CHOSE_YOUR_PORT>/dosc`

### Using app:
Application automatically requesting server and try to handle emails. User choose quantity of emails and timeout between handling.  
* Check server status user may use `/healthz`
* Get quantity of handling operation user may use `/`
* Get log of handling operation user may use `/log`


### For request under tor
* Linux (Ubuntu)
1. `sudo add-apt-repository ppa:micahflee/ppa`
2. `sudo apt update`
3. `sudo apt install torbrowser-launcher`
* Windows
1. Install and start Tor