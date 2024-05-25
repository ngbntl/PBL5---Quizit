from typing import Annotated

from fastapi import Query

QUERY_GROUP_ID = Annotated[str, Query(min_length=8, max_length=8)]