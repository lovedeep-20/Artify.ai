import streamlit as st
import requests
from together import Together
import os
import dotenv
import sys
from logger.logging_file import get_logger

# Initialize the logger
logger = get_logger()

# Load environment variables from .env file
dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY") or st.secrets["API_KEY"]

# Validate the API key and initialize Together client
try:
    if not API_KEY:
        raise ValueError("API_KEY not found in environment variables. Please add it to your .env file.")
    client = Together(api_key=API_KEY)
    logger.info("Together client initialized successfully.")
except Exception as e:
    st.error(f"Initialization Error: {e}")
    logger.error(f"Initialization Error: {e}")

def validate_inputs(prompt, negative_prompt, width, height, steps, num_outputs):
    """Ensures all inputs meet requirements before generating images."""
    if not prompt:
        st.warning("Please provide a prompt.")
        logger.warning("Prompt is empty.")
        return False
    if not (width > 0 and height > 0):
        st.warning("Invalid image resolution dimensions.")
        logger.warning("Invalid resolution dimensions.")
        return False
    if not (1 <= steps <= 10):
        st.warning("Steps should be between 1 and 10.")
        logger.warning("Steps value is out of range.")
        return False
    if not (1 <= num_outputs <= 4):
        st.warning("You can generate between 1 to 4 images only.")
        logger.warning("Number of outputs is out of range.")
        return False
    return True

def generate_images(prompt, negative_prompt, width, height, steps, num_outputs):
    """Generate images using the Together API and display in Streamlit."""
    if not validate_inputs(prompt, negative_prompt, width, height, steps, num_outputs):
        logger.info("Input validation failed.")
        return

    # Display loading spinner while generating the image
    with st.spinner("Generating image..."):
        try:
            logger.info("Starting image generation.")
            response = client.images.generate(
                prompt=prompt,
                model="black-forest-labs/FLUX.1-schnell",
                width=width,
                height=height,
                steps=steps,
                n=num_outputs,
                response_format="url"
            )
            if not response or not response.data:
                raise ValueError("No images were generated. Check your inputs and try again.")
            
            logger.info(f"{len(response.data)} images generated successfully.")
            # Store the generated images in session state
            st.session_state.images = response.data  # Save images to session state
            logger.info("Images stored in session state.")
        
        except Exception as e:
            st.error(f"Error: {e}")
            logger.error(f"Image generation error: {e}")

def display_images():
    """Display images and download buttons from session state."""
    if 'images' in st.session_state:
        for index, img_data in enumerate(st.session_state.images):
            display_image_with_download(img_data.url, index)  # Pass index here
    else:
        st.warning("No images to display.")

def display_image_with_download(img_url, index):
    """Displays the image in Streamlit with a download option if retrieval is successful."""
    try:
        st.image(img_url, caption="Generated Image")
        image_response = requests.get(img_url)
        
        if image_response.status_code == 200:
            # Add a unique key for each download button using the index
            st.download_button(
                "Download Image",
                image_response.content,
                file_name=f"generated_image_{index}.png",
                key=f"download_button_{index}"  # Unique key
            )
            logger.info(f"Image {index} downloaded successfully.")
        else:
            st.error("Failed to download the generated image.")
            logger.error("Image download failed.")
    except Exception as e:
        st.error(f"Image Display Error: {e}")
        logger.error(f"Image display error: {e}")

def main():
    st.title("Flux Schnell Image Generation")

    # Prompt input
    prompt = st.text_area(":orange[**Enter prompt**]", value="An astronaut riding a rainbow unicorn, cinematic, dramatic")
    negative_prompt = st.text_area(":orange[**Elements to avoid in image**]", value="the absolute worst quality, distorted features")
    resolution = st.selectbox("Resolution", ["256x256", "512x512", "1024x1024"])
    width, height = map(int, resolution.split("x"))
    steps = st.slider("Steps", 1, 4, 1)
    num_outputs = st.slider("Number of images", 1, 4, 1)

    # Generate button
    if st.button("Generate Image"):
        logger.info("Generate Image button clicked.")
        generate_images(prompt, negative_prompt, width, height, steps, num_outputs)

    # Display generated images if available
    display_images()

    # Recreate button to clear session state and allow new generation
    if st.button("Recreate"):
        st.session_state.images = []  # Clear images from session state
        logger.info("Images cleared from session state.")

if __name__ == "__main__":
    main()

