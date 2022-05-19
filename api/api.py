from fastapi import FastAPI

from .responses import CustomJSONResponse


app = FastAPI(default_response_class=CustomJSONResponse)


@app.get('/')
async def test_view():
    return {'OK': True}
