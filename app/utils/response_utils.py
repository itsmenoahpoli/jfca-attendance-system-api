from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def HTTPResponse(status_code: int, detail: tuple):
  return JSONResponse(
		status_code=status_code,
		content=jsonable_encoder(detail)
	) 