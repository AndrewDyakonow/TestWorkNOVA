from config.settings import BASE_DIR
from pathlib import Path

# Файл конфигурации google api
CONFIG_FILE = Path(BASE_DIR, 'app', 'google', 'keys.json')

# Список сервисов, необходимых для работы
SCOPE = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
    ]

# Пресет настроек доступа
USER_PERMISSIONS = {
    "type": "user",
    "role": "writer",
    "emailAddress": "testworkfornova@gmail.com",
}
