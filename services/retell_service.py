import httpx
from fastapi import HTTPException
from schemas.agent import AgentCreateRequest, AgentCreateResponse
from config import settings

async def create_agent_retell(request: AgentCreateRequest) -> AgentCreateResponse:
    headers = {
        "Authorization": f"Bearer {settings.RETELL_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "voice_id": "11labs-Adrian",
        "response_engine": {
            "type": "retell-llm",
            "llm_id": "llm_ee298ea789b270986c6636a02bdf",
            "version": request.llm_version or 0
        }
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(settings.RETELL_URL, headers=headers, json=body)

    if resp.status_code != 201:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)

    data = resp.json()
    return AgentCreateResponse(
        provider="retell",
        agent_id=data.get("agent_id"),
        voice_id=data.get("voice_id"),
        name=data.get("agent_name"),
        raw_response=data
    )
