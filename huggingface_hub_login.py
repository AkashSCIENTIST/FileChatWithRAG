from huggingface_hub.hf_api import HfFolder
from dotenv import load_dotenv
import os

HfFolder.save_token(os.environ['HF_ACCESS_KEY'])