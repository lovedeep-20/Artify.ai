import streamlit as st

def main():
    # Title centered and styled
    st.markdown("<h1 style='text-align: center; font-size: 3em;'>Artify.ai</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 2em;'>AI Image Generation with FLUX</h2><hr>", unsafe_allow_html=True)
    
    st.image("assets/girl-closeup.png", caption="Image generated using FLUX model", use_column_width=True)

    # Introduction to FLUX
    st.header("What is FLUX?")
    st.write(
        "FLUX is a series of advanced AI models developed by Black Forest Labs, designed to generate high-quality images from textual prompts. "
        "These models leverage deep learning techniques to understand and interpret natural language, creating detailed visual outputs that match user descriptions."
    )
    
    # Placeholder for FLUX Image
    st.image("assets/flux-comp2.png", use_column_width=True)
    st.image("assets/flux-comp4.png", use_column_width=True)
    st.image("assets/flux-comp6.png", caption="FLUX Models Overview", use_column_width=True)

    # How FLUX Works
    st.header("How FLUX Works")
    st.write(
        "FLUX operates by utilizing complex neural network architectures that have been trained on vast datasets of images and their corresponding textual descriptions. "
        "When a user inputs a prompt, the model analyzes the text to identify key concepts and relationships, then synthesizes this information to generate a coherent and relevant image. "
        "The process involves several steps, including text encoding, image generation, and fine-tuning to enhance visual quality and fidelity to the prompt."
    )
    
    # Placeholder for How FLUX Works Image
    st.image("assets/working_flux.webp", caption="How FLUX Works", use_column_width=True)

    # Explanation of Stable Diffusion
    st.header("Relation to Stable Diffusion")
    st.write(
        "Stable Diffusion is a specific type of generative model used for image synthesis that shares similarities with the FLUX models. "
        "Both frameworks employ diffusion processes to iteratively refine an image from random noise based on a given text prompt. "
        "In essence, Stable Diffusion adds a layer of stability and coherence to the image generation process, ensuring that the final output aligns closely with the user's intent while minimizing artifacts and inconsistencies."
    )

    # What the App Demonstrates
    st.header("What This App Demonstrates")
    st.write(
        "This application serves as a practical demonstration of the FLUX image generation capabilities. Users can input their creative prompts and see the model generate images in real time, showcasing the following features:"
    )
    st.write(
        "- **User-Friendly Interface**: Easily enter prompts and adjust settings such as resolution and number of outputs."
    )
    st.write(
        "- **Image Generation**: Experience the state-of-the-art performance of FLUX models in generating diverse and high-quality images."
    )
    st.write(
        "- **Download Options**: Users can download the generated images for personal or professional use."
    )
    st.write(
        "By exploring this app, users gain insights into the potential of AI in creative domains and can experiment with different prompts to see the versatility of FLUX."
    )

if __name__ == "__main__":
    main()
