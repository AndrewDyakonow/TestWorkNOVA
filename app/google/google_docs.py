from app.google.settings import CONFIG_FILE, SCOPE, USER_PERMISSIONS
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from typing import Any, Union


class GoogleServicesAPI:
    """Класс для работы с Google API"""
    creds = Credentials.from_service_account_file(CONFIG_FILE, scopes=SCOPE)

    @property
    def docs_google(self):
        """Объект google docs"""
        return build("docs", "v1", credentials=self.creds)

    @property
    def drive_google(self) -> Any:
        """Объект google drive"""
        return build("drive", "v3", credentials=self.creds)

    def create_file(self, **kwargs) -> Any | None:
        """Создать файл"""
        body = {
            'title': kwargs['filename'],
        }
        try:
            file = self.docs_google.documents().create(body=body).execute()
        except Exception as error_message:
            return error_message

        self.__write_in_file(file['documentId'], **kwargs)
        self.__allow_access(file['documentId'])

    def __write_in_file(self, file_id: str, **kwargs) -> None:
        """Запись данных в файл"""
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': kwargs['body']
                }
            },
        ]
        try:
            self.docs_google.documents().batchUpdate(
                documentId=file_id,
                body={'requests': requests}
            ).execute()
        except Exception as error_message:
            print(error_message)

    def show_file_list(self) -> list[Union[None, Any]] | Any:
        """Показать список файлов"""
        try:
            doc = self.drive_google.files().list().execute()
        except Exception as text:
            return text
        return doc['files']

    def __allow_access(self, file_id: str) -> str | Any:
        """Разрешить доступ"""
        try:
            self.drive_google.permissions().create(
                        fileId=file_id,
                        body=USER_PERMISSIONS,
                        fields="id",
                    ).execute()
        except Exception as text:
            return text
        return "Доступ предоставлен"

    def delete_file(self) -> str | Any:
        """Удалить файлы"""
        try:
            for file in self.show_file_list():
                self.drive_google.files().delete(fileId=file['id']).execute()
        except Exception as text:
            return text
        return "Файл удалён"


googleAPI = GoogleServicesAPI()
