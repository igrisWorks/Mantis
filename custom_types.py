import pydantic

class RAGChunkAndSrc(pydantic.BaseModel):
    chunks: list[str]
    source: str = None

class RAGUpsertResult(pydantic.BaseModel):
    ingested : int

class RAGSerachResult(pydantic.BaseModel):
    contexts: list[str]
    sources: list[str]

class RAGQueryResult(pydantic.BaseModel):
    answer: str
    sources: list[str]
    num_contexts: int