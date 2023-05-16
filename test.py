import webuiapi
from random import randint

HOST = '127.0.0.1'
PORT = 7860

api = webuiapi.WebUIApi(host=HOST, port=PORT)
options = {}
options['sd_model_checkpoint'] = "meinamix_meinaV9.safetensors [eac6c08a19]"
api.set_options(options)

positive_prompts = ["1girl", "medium breats", "(asuna sword art online)", "rapier", "wallpaper", "orange hair", "(sword)"]
negative_prompts = ["worst quality:2"]

from time import sleep
for _ in range(4):
    result = api.txt2img(prompt= ",".join(positive_prompts),
                        negative_prompt=",".join(negative_prompts),
                        seed=-1,
                        cfg_scale=7,
                        sampler_index="DPM++ SDE Karras",
                        steps=40,
                        enable_hr=True,
                        hr_scale=2,
                        hr_upscaler="R-ESRGAN 4x+ Anime6B",
                        hr_second_pass_steps=10,
                        hr_resize_x=1024,
                        hr_resize_y=1024,
                        denoising_strength=0.3,
                        save_images=True,
                        )
    sleep(5)


