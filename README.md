# Multiple Transcription 
This project provides a Python script to automatically transcribe multiple Kannada audio files from a folder using Hugging Face’s Whisper model. Transcription results are saved in a CSV file.


# Overview
The script uses a fine-tuned Whisper model (`vasista22/whisper-kannada-medium`) to batch-process `.wav` files from a given folder and output their transcriptions into a single CSV.


# Features
- Batch transcription of `.wav` files
- Outputs `Filename` and `Transcription` in a CSV
- Automatically uses GPU if available
- Handles errors file-by-file and shows progress
- Kannada language-specific decoding setup


# Model Used
- **Model**: [`vasista22/whisper-kannada-medium`](https://huggingface.co/vasista22/whisper-kannada-medium)
- **Architecture**: Whisper
- **Language**: Kannada (set using forced decoder prompts)


# Files in This Repository
multiple-transcription/
- transcribe_folder.py # Main Python script
- README.md # Project documentation


# Setup Instructions
1. **Install dependencies**:
   ```bash
   pip install torch transformers

2. Edit file paths in transcribe_folder.py:
   a) folder_path = "/path/to/your/audio/folder";
   b) output_csv_path = "/path/to/save/output.csv"

3. Run the script:
   python transcribe_folder.py


# Output Example
| Filename    | Transcription             |
| ----------- | ------------------------  |
| `file1.wav` | ನಾನು ಒಳ್ಳೆಯವಳಾಗಿ ಇದ್ದೇನೆ  |
| `file2.wav` | ನಿಮ್ಮ ಹೆಸರು ಏನು?         |


# License
  This project is for academic and educational use only.
  Model license belongs to its original author on Hugging Face.


# Acknowledgements
 1. Hugging Face Transformers.
 2. vasista22 Whisper Kannada Model.

