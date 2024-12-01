from pynamodb.models import Model
from pynamodb.attributes import  UnicodeAttribute, UTCDateTimeAttribute
from typing import Optional

class FileVault(Model):
    class Meta:
        table_name = "filevault"
        region = "us-east-1"
    
    id =  UnicodeAttribute(hash_key=True)
    client = UnicodeAttribute()
    reference_id = UnicodeAttribute(null=True)
    request_type = UnicodeAttribute(null=True)
    link= UnicodeAttribute()
    file_name= UnicodeAttribute()
    file_path= UnicodeAttribute()
    bucket_link= UnicodeAttribute()
    created_at = UTCDateTimeAttribute()
    modified_at = UTCDateTimeAttribute()

class FileVaultEvent(Model):
    class Meta:
        table_name = "filevault_event"
        region = "us-east-1"
    
    id =  UnicodeAttribute(hash_key=True)
    status= UnicodeAttribute()
    created_at = UTCDateTimeAttribute()