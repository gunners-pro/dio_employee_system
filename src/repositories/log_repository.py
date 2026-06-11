import os
from azure.data.tables import TableServiceClient
from azure.core.credentials import AzureNamedKeyCredential

class LogRepository:
    def __init__(self, table_name: str):
        AZURE_TABLE_URL = os.getenv("AZURE_TABLE_URL")
        AZURE_TABLE_KEY = os.getenv("AZURE_TABLE_KEY")
        AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")

        if not AZURE_TABLE_URL or not AZURE_TABLE_KEY or not AZURE_ACCOUNT_NAME:
            raise RuntimeError("AZURE_TABLE_URL, AZURE_TABLE_KEY or AZURE_ACCOUNT_NAME environment variable not set.")

        credential = AzureNamedKeyCredential(AZURE_ACCOUNT_NAME, AZURE_TABLE_KEY)
        service = TableServiceClient(endpoint=AZURE_TABLE_URL, credential=credential)
        self.table_client = service.get_table_client(table_name)

    def add(self, entity: dict):
        self.table_client.create_entity(entity)

    def list_all(self) -> list:
        return list(self.table_client.list_entities())