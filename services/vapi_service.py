import httpx
from fastapi import HTTPException
from schemas.agent import AgentCreateRequest, AgentCreateResponse
from config import settings

async def create_agent_vapi(request: AgentCreateRequest) -> AgentCreateResponse:
    headers = {
        "Authorization": f"Bearer {settings.VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {}
    if request.name:
        body["name"] = request.name
    if request.first_message:
        body["firstMessage"] = request.first_message
    if request.voice_id:
        body["voice"] = {
            "provider": request.voice_provider or "azure",
            "voiceId": request.voice_id
        }
    # Additional mappings for other common or optional fields can be added here

    async with httpx.AsyncClient() as client:
        resp = await client.post(settings.VAPI_URL, headers=headers, json=body)
    if resp.status_code != 201:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    data = resp.json()
    return AgentCreateResponse(
        provider="vapi",
        agent_id=data.get("id"),
        name=data.get("name"),
        voice_id=request.voice_id,
        raw_response=data
    )
