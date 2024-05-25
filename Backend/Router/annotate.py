from typing import Annotated

from fastapi import Query

QUERY_LEN_8 = Annotated[str, Query(min_length=8, max_length=8)]