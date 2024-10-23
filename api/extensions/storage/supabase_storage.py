import io
from collections.abc import Generator
from pathlib import Path

from supabase import Client

from configs import mlchain_config
from extensions.storage.base_storage import BaseStorage


class SupabaseStorage(BaseStorage):
    """Implementation for supabase obs storage."""

    def __init__(self):
        super().__init__()
        if mlchain_config.SUPABASE_URL is None:
            raise ValueError("SUPABASE_URL is not set")
        if mlchain_config.SUPABASE_API_KEY is None:
            raise ValueError("SUPABASE_API_KEY is not set")
        if mlchain_config.SUPABASE_BUCKET_NAME is None:
            raise ValueError("SUPABASE_BUCKET_NAME is not set")

        self.bucket_name = mlchain_config.SUPABASE_BUCKET_NAME
        self.client = Client(supabase_url=mlchain_config.SUPABASE_URL, supabase_key=mlchain_config.SUPABASE_API_KEY)
        self.create_bucket(id=mlchain_config.SUPABASE_BUCKET_NAME, bucket_name=mlchain_config.SUPABASE_BUCKET_NAME)

    def create_bucket(self, id, bucket_name):
        if not self.bucket_exists():
            self.client.storage.create_bucket(id=id, name=bucket_name)

    def save(self, filename, data):
        self.client.storage.from_(self.bucket_name).upload(filename, data)

    def load_once(self, filename: str) -> bytes:
        content = self.client.storage.from_(self.bucket_name).download(filename)
        return content

    def load_stream(self, filename: str) -> Generator:
        def generate(filename: str = filename) -> Generator:
            result = self.client.storage.from_(self.bucket_name).download(filename)
            byte_stream = io.BytesIO(result)
            while chunk := byte_stream.read(4096):  # Read in chunks of 4KB
                yield chunk

        return generate()

    def download(self, filename, target_filepath):
        result = self.client.storage.from_(self.bucket_name).download(filename)
        Path(result).write_bytes(result)

    def exists(self, filename):
        result = self.client.storage.from_(self.bucket_name).list(filename)
        if result.count() > 0:
            return True
        return False

    def delete(self, filename):
        self.client.storage.from_(self.bucket_name).remove(filename)

    def bucket_exists(self):
        buckets = self.client.storage.list_buckets()
        return any(bucket.name == self.bucket_name for bucket in buckets)
