import os
import torch
import csv
from transformers import pipeline

def transcribe_audio_files(folder_path, output_csv_path):
    """
    Transcribe all audio files in a specific folder using Whisper model.
    
    Parameters:
    - folder_path: Path to the folder containing audio files
    - output_csv_path: Path to save the transcription results
    """
    # Detect available device
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    # Initialize transcription pipeline
    transcribe = pipeline(
        task="automatic-speech-recognition", 
        model="vasista22/whisper-kannada-small", 
        chunk_length_s=30, 
        device=device
    )
    
    # Set language configuration for Kannada
    transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(
        language="kn", 
        task="transcribe"
    )
    
    # Prepare to write results
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        # Create CSV writer
        csv_writer = csv.writer(csvfile)
        
        # Write header
        csv_writer.writerow(['Filename', 'Transcription'])
        
        # Sort files to ensure consistent processing order
        audio_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.wav')])
        
        # Counter for tracking progress
        total_files = len(audio_files)
        processed_files = 0
        
        # Iterate through audio files in the folder
        for filename in audio_files:
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Transcribe the audio file
                transcription = transcribe(file_path)["text"]
                
                # Write results to CSV
                csv_writer.writerow([filename, transcription])
                
                # Update and print progress
                processed_files += 1
                print(f"Processed {processed_files}/{total_files}: {filename}")
                
            except Exception as e:
                print(f"Error transcribing {filename}: {str(e)}")
                # Write error to CSV
                csv_writer.writerow([filename, f"Transcription Error: {str(e)}"])
    
    print(f"Transcription complete. Results saved to {output_csv_path}")

# Specific folder path and output file
folder_path = "/home/vksit/Documents/Samsung_Prism_2025/Hearing_Impaired_Data/1_HI_High/F16"
output_csv_path = "/home/vksit/Documents/Samsung_Prism_2025/Hearing_Impaired_Data/1_HI_High/F16_transcriptions.csv"

# Run the transcription
transcribe_audio_files(folder_path, output_csv_path)