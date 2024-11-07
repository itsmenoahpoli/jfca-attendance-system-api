
from pydantic import BaseModel, constr
from typing import Annotated

class SendSmsDTO(BaseModel):
	message: Annotated[str, constr(min_length=1)]
	number: Annotated[str, constr(min_length=11)]