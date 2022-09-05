# import dependencies
import gradio as gr

# open Gradio interface
gr.Interface.load("spaces/carolineec/informativedrawings").launch(server_name="0.0.0.0", server_port=8080)