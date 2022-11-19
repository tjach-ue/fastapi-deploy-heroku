from fastapi import FastAPI
import cv2
from starlette.responses import StreamingResponse
import io

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/opencv/{name}")
async def say_hello(name: str):
    circle = cv2.imread('img/circle.png')
    circle = cv2.cvtColor(circle, cv2.COLOR_BGR2GRAY)
    star = cv2.imread('img/star.png')
    star = cv2.cvtColor(star, cv2.COLOR_BGR2GRAY)
    combined = cv2.subtract(star, circle)
    cv2.putText(img=combined, text=f'Hello {name}',
                org=(50, 100), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=2,
                color=(255, 255, 255), thickness=3)

    is_success, im_png = cv2.imencode(".png", combined)
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")