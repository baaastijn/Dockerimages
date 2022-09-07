# import dependencies
import gradio as gr

# open Gradio interface
gr.Interface.load("spaces/baaastien/Spleeter_and_ASR").launch(server_name="0.0.0.0", server_port=8080)