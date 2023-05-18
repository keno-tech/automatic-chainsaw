import webuiapi
from random import randint
from time import sleep
import csv


HOST = '127.0.0.1'
PORT = 7860

api = webuiapi.WebUIApi(host=HOST, port=PORT)
options = {}
options['sd_model_checkpoint'] = "meinamix_meinaV9.safetensors [eac6c08a19]"
api.set_options(options)

positive_prompts = ["1girl", "medium breats", "wallpaper", "light particles"]
negative_prompts = ["worst quality:2", "interlocked fingers", "sketch", "mutated fingers", "4 fingers"]

try:
    with open('input.csv', 'r') as input_file:
        reader = csv.reader(input_file)
        rows = list(reader)
        # Read today's prompt
        today_prompt = ",".join(rows[0])
        print(today_prompt)
    
    # Delete used
    with open('input.csv', 'w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerows(rows[1:])
        
except Exception as e:
    print(e)

positive_prompts.append(today_prompt)
n_images = 50
for _ in range(n_images):
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




