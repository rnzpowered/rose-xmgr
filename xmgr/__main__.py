import logging

import uvicorn

from config import DEBUG, UVICORN_HOST, UVICORN_PORT

if __name__ == "__main__":
    uvicorn.run(
        "xmgr:app",
        host=UVICORN_HOST,
        port=UVICORN_PORT,
        workers=1,
        reload=DEBUG,
        log_level=logging.DEBUG if DEBUG else logging.INFO,
    )
