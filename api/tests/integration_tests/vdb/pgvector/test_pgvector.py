from core.rag.datasource.vdb.pgvector.pgvector import PGVector, PGVectorConfig
from core.rag.models.document import Document
from tests.integration_tests.vdb.test_vector_store import (
    AbstractVectorTest,
    get_example_text,
    setup_mock_redis,
)


class PGVectorTest(AbstractVectorTest):
    def __init__(self):
        super().__init__()
        self.vector = PGVector(
            collection_name=self.collection_name,
            config=PGVectorConfig(
                host="localhost",
                port=5433,
                user="postgres",
                password="mlchainai123456",
                database="mlchain",
            ),
        )


def test_pgvector(setup_mock_redis):
    PGVectorTest().run_all_tests()
