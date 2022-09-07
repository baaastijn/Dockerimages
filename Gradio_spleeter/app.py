import gradio as gr
import os
import random2
from spleeter.separator import Separator
from transformers import pipeline, AutoModelForCTC, Wav2Vec2Processor, Wav2Vec2ProcessorWithLM

# Initiate a file separator with 2 stems (instruments and vocals) and 16khz bitrate, required for ASR
separator = Separator('spleeter:2stems-16kHz')

# Initiate Speech to text model with Wave2Vec english
# https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english
pipe = pipeline("automatic-speech-recognition", "jonatasgrosman/wav2vec2-large-xlsr-53-english")

# Gradio function to split audio stems, transcribe vocals and return their filepaths
def extract_stems(audio):
    
    # initiate a unique folder name for splitted files
    foldername = str(random2.randrange(100000000))

    # Separate audio input. Synchronous is true to wait for the end of split before going further
    separator.separate_to_file(audio, "output/", filename_format= foldername + "/{instrument}.wav", synchronous=True)
    
    # build filepaths for vocals and accompaniment files
    vocals = f"./output/"+ foldername +"/vocals.wav"
    accompaniment = f"./output/"+ foldername +"/accompaniment.wav"
    
    # Get a transcript of the vocals, by using the huggingface pipeline
    transcript = pipe(vocals, chunk_length_s=10, decoder=None)
    
    return vocals, accompaniment, transcript

# Launch a Gradio interface
# Input is an audio file, 
# Output is two audio files and a transcript

title = "Demo: Deezer Spleeter + english Automatic Speech Recognition"
description = "<p>This demo is a basic interface for <a href='https://research.deezer.com/projects/spleeter.html' target='_blank'>Deezer Spleeter</a>.</p><p>It uses the Spleeter library for separate audio file in two stems : accompaniments and vocals.</p><p>Once splitted, it performs ASR (Automatic Speech Recognition) based on a Wav2vec2 english model.</p>"
examples = [["examples/" + mp3] for mp3 in os.listdir("examples/")]

demo = gr.Interface(
    fn=extract_stems, 
    inputs=gr.Audio(source="upload", type="filepath"),
    outputs=[gr.Audio(label="Vocals stem", source="upload", type="filepath"), gr.Audio(label="Accompaniment stem", source="upload", type="filepath"), gr.Textbox(label="Wave2vec2 Automatic Speech Recognition (English)")],
    title=title,
    description=description,
    examples=examples,
    allow_flagging="never"
    )

demo.launch(server_name="0.0.0.0", server_port=8080)