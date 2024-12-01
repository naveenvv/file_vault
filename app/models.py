from pydantic import BaseModel
from typing import Optional

class FileValute(BaseModel):
    id: str
    client: str
    reference_id: Optional[str] = ""
    request_type: Optional[str] = ""
    link: str
    file_name: str
    file_path: str
    bucket_link: str

    def save(self):
        # Save to DynamoDB
        pass

    @classmethod
    def get(cls, user_id: str):
        # Get from DynamoDB
        pass