from fastapi import FastAPI, HTTPException
from config import settings
from schemas.agent import AgentCreateRequest, AgentCreateResponse
from services.vapi_service import create_agent_vapi
from services.retell_service import create_agent_retell

app = FastAPI(title="Unified Agent Creation API")

@app.post("/create-agent", response_model=AgentCreateResponse)
async def create_agent(request: AgentCreateRequest):
    provider = request.provider.lower()
    if provider == "vapi":
        return await create_agent_vapi(request)
    elif provider == "retell":
        return await create_agent_retell(request)
    else:
        raise HTTPException(status_code=400, detail="Invalid provider specified. Must be 'vapi' or 'retell'.")
