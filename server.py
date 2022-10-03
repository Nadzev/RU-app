import logging
import os

import uvicorn as uvicorn

from dotenv import load_dotenv

from src.ui.http import app
print('executando')

# logger = logging.getLogger("uvicorn.error")
# print(logger.info)
if __name__ == "__main__":
    path_env = "config/.env"
    load_dotenv(path_env)
    uvicorn.run(
        app,
        host=os.getenv("API_HOST", "localhost"),
        log_level=logging.INFO
    )
