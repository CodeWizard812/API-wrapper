from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
    VAPI_API_KEY: str = os.getenv("VAPI_API_KEY")
    RETELL_API_KEY: str = os.getenv("RETELL_API_KEY")
    VAPI_URL: str = "https://api.vapi.ai/assistant"
    RETELL_URL: str = "https://api.retellai.com/create-agent"

settings = Settings()
