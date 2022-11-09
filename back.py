"""Background operations with using Redis and YOLOv5 to read new tasks
and hidden number automaticly. At the end, Redis add new file back.
"""

import io
import redis
import torch
from PIL import Image, ImageDraw


with redis.Redis() as client:
    while True:
        image_data = client.brpop('image')[1]
        with Image.open(io.BytesIO(image_data)) as im_pil:
            rgb_im = im_pil.convert('RGB')
            model = torch.hub.load(
                'yolov5',
                'custom',
                path='yolov5/nomera.pt',
                device='cpu',
                source='local'
            )
            results = model(rgb_im)
            if results.xyxy[0].nelement() != 0:
                coords = (
                    results.pandas().xyxy[0].loc[0]['xmin'],
                    results.pandas().xyxy[0].loc[0]['ymin'],
                    results.pandas().xyxy[0].loc[0]['xmax'],
                    results.pandas().xyxy[0].loc[0]['ymax']
                )
                draw = ImageDraw.Draw(rgb_im)
                draw.rectangle((coords), (0, 0, 0))
                img_byte_arr = io.BytesIO()
                rgb_im.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()
                client.lpush('answer', img_byte_arr)
