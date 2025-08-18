<h1 align="center"/>rose-xmgr</h1>

<p align="center">Backend for managing xray-core nodes, based on Marzban</p>
<br/>

<p align="center">English / <a href="README.md">Русский</a></p>

# Configuration

> You can set settings below using environment variables or placing them in `.env` file.

| Variable                                 | Description                                                                                                              |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| SUDO_USERNAME                            | Superuser's username                                                                                                     |
| SUDO_PASSWORD                            | Superuser's password                                                                                                     |
| SQLALCHEMY_DATABASE_URL                  | Database URL ([SQLAlchemy's docs](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls))                    |
| UVICORN_HOST                             | Bind application to this host (default: `0.0.0.0`)                                                                       |
| UVICORN_PORT                             | Bind application to this port (default: `8000`)                                                                          |
| UVICORN_UDS                              | Bind application to a UNIX domain socket                                                                                 |
| UVICORN_SSL_CERTFILE                     | SSL certificate file to have application on https                                                                        |
| UVICORN_SSL_KEYFILE                      | SSL key file to have application on https                                                                                |
| UVICORN_SSL_CA_TYPE                      | Type of authority SSL certificate. Use `private` for testing self-signed CA (default: `public`)                          |
| XRAY_JSON                                | Path of Xray's json config file (default: `xray_config.json`)                                                            |
| XRAY_EXECUTABLE_PATH                     | Path of Xray binary (default: `/usr/local/bin/xray`)                                                                     |
| XRAY_ASSETS_PATH                         | Path of Xray assets (default: `/usr/local/share/xray`)                                                                   |
| XRAY_SUBSCRIPTION_URL_PREFIX             | Prefix of subscription URLs                                                                                              |
| XRAY_FALLBACKS_INBOUND_TAG               | Tag of the inbound that includes fallbacks, needed in the case you're using fallbacks                                    |
| XRAY_EXCLUDE_INBOUND_TAGS                | Tags of the inbounds that shouldn't be managed and included in links by application                                      |
| CUSTOM_TEMPLATES_DIRECTORY               | Customized templates directory (default: `app/templates`)                                                                |
| CLASH_SUBSCRIPTION_TEMPLATE              | The template that will be used for generating clash configs (default: `clash/default.yml`)                               |
| SUBSCRIPTION_PAGE_TEMPLATE               | The template used for generating subscription info page (default: `subscription/index.html`)                             |
| HOME_PAGE_TEMPLATE                       | Decoy page template (default: `home/index.html`)                                                                         |
| TELEGRAM_API_TOKEN                       | Telegram bot API token  (get token from [@botfather](https://t.me/botfather))                                            |
| TELEGRAM_ADMIN_ID                        | Numeric Telegram ID of admin (use [@userinfobot](https://t.me/userinfobot) to found your ID)                             |
| TELEGRAM_PROXY_URL                       | Run Telegram Bot over proxy                                                                                              |
| JWT_ACCESS_TOKEN_EXPIRE_MINUTES          | Expire time for the Access Tokens in minutes, `0` considered as infinite (default: `1440`)                               |
| DOCS                                     | Whether API documents should be available on `/docs` and `/redoc` or not (default: `False`)                              |
| DEBUG                                    | Debug mode for development (default: `False`)                                                                            |
| WEBHOOK_ADDRESS                          | Webhook address to send notifications to. Webhook notifications will be sent if this value was set.                      |
| WEBHOOK_SECRET                           | Webhook secret will be sent with each request as `x-webhook-secret` in the header (default: `None`)                      |
| NUMBER_OF_RECURRENT_NOTIFICATIONS        | How many times to retry if an error detected in sending a notification (default: `3`)                                    |
| RECURRENT_NOTIFICATIONS_TIMEOUT          | Timeout between each retry if an error detected in sending a notification in seconds (default: `180`)                    |
| NOTIFY_REACHED_USAGE_PERCENT             | At which percentage of usage to send the warning notification (default: `80`)                                            |
| NOTIFY_DAYS_LEFT                         | When to send warning notifaction about expiration (default: `3`)                                                         |
| USERS_AUTODELETE_DAYS                    | Delete expired (and optionally limited users) after this many days (Negative values disable this feature, default: `-1`) |
| USER_AUTODELETE_INCLUDE_LIMITED_ACCOUNTS | Whether to include limited accounts in the auto-delete feature (default: `False`)                                        |
| USE_CUSTOM_JSON_DEFAULT                  | Enable custom JSON config for ALL supported clients (default: `False`)                                                   |
| USE_CUSTOM_JSON_FOR_V2RAYNG              | Enable custom JSON config only for V2rayNG (default: `False`)                                                            |
| USE_CUSTOM_JSON_FOR_STREISAND            | Enable custom JSON config only for Streisand (default: `False`)                                                          |
| USE_CUSTOM_JSON_FOR_V2RAYN               | Enable custom JSON config only for V2rayN (default: `False`)                                                             |

# Documentation

The [Marzban Documentation](https://gozargah.github.io/marzban) provides all the essential guides to get you started,
available in three languages: Farsi, English, and Russian. This documentation requires significant effort to cover all
aspects of the project comprehensively. We welcome and appreciate your contributions to help us improve it. You can
contribute on this [GitHub repository](https://github.com/Gozargah/gozargah.github.io).

# API

Marzban provides a REST API that enables developers to interact with Marzban services programmatically. To view the API
documentation in Swagger UI or ReDoc, set the configuration variable `DOCS=True` and navigate to the `/docs` and
`/redoc`.

# License

Based on [Gozargah/Marzban](https://github.com/Gozargah/Marzban).
