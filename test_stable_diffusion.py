from diffusers import StableDiffusionPipeline
import torch

def test_stable_diffusion():
    # Load model
    model_id = "stabilityai/stable-diffusion-2-1"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    
    # Generate image
    prompt = "A futuristic cityscape at night"
    image = pipe(prompt).images[0]
    
    # Save image
    image.save("generated_image.png")

if __name__ == "__main__":
    test_stable_diffusion()
