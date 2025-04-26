from pydantic import BaseModel
from typing import Optional, Any

class AgentCreateRequest(BaseModel):
    provider: str
    name: Optional[str] = None
    voice_id: Optional[str] = None
    voice_provider: Optional[str] = None
    first_message: Optional[str] = None
    llm_id: Optional[str] = None
    llm_version: Optional[int] = None
    voice_model: Optional[str] = None
    webhook_url: Optional[str] = None

class AgentCreateResponse(BaseModel):
    provider: str
    agent_id: str
    name: Optional[str] = None
    voice_id: Optional[str] = None
    raw_response: Any
