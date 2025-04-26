# AI Agent API Wrapper

This project provides a **common API** built with **FastAPI** to create AI agents across two different platforms: **Vapi** and **Retell**.

Instead of the user interacting separately with two APIs, they now have **one unified API** where they can specify which provider to use.

---

## Features
- Single endpoint to create agents either on **Vapi** or **Retell**
- Standardized request body
- Clean and scalable project structure
- Handles HTTP errors properly
- Async calls for better performance (using `httpx`)

---

## Tech Stack
- **FastAPI** (Python Web Framework)
- **httpx** (Async HTTP Requests)
- **Pydantic** (Request/Response Validation)

---

## Setup Instructions

### 1. Clone the Repository
```bash
https://github.com/CodeWizard812/API-wrapper.git
cd API-wrapper
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file:

```env
VAPI_API_KEY=your_vapi_api_key_here
RETELL_API_KEY=your_retell_api_key_here
```
OR update `config.py` directly if not using `.env`
---

## API Usage

### Endpoint:
```http
POST /create-agent
```

### Request Body:
```json
{
  "provider": "vapi" | "retell", (Mandatory)
  "name": "Agent Name",            (Optional)
  "first_message": "Hello, how can I help you?", (Optional)
  "voice_id": "your-voice-id",       (Optional)
  "voice_provider": "azure" | "elevenlabs" | "other", (Optional)
  "llm_version": 0 (Optional, only for Retell)
  "llm_id": "llm-xxxxx" (Optional, only for Retell already added in code)
}
```

- **provider**: `vapi` or `retell` (choose which platform to create agent on)
- **name**: Name of the agent
- **first_message**: (For Vapi) Starting message
- **voice_id**: Voice ID you want to assign
- **voice_provider**: (Optional) Provider for voice (Azure, ElevenLabs, etc.)
- **llm_version**: (Optional, for Retell only) Version of the LLM engine


### Sample `curl` Request
```bash
curl -X POST http://localhost:8000/create-agent \
-H "Content-Type: application/json" \
-d '{
  "provider": "vapi",
  "name": "TestBot",
  "first_message": "Hi there!",
  "voice_id": "en-US-Wavenet-D"
}'
```

---

## Running Locally

```bash
uvicorn main:app --reload
```

The API will start at: `http://127.0.0.1:8000`

---

## Project Structure
```
.
├── config.py
├── .env
├── main.py
├── requirements.txt
├── services
│   ├── vapi_service.py
│   └── retell_service.py
├── schemas
│   └── agent.py
└── README.md
```

---

## Notes
- Ensure you use **valid API keys** and **valid voice IDs**.
- For Retell, make sure you have a **working LLM ID** before creating an agent. Create it using CREATE RETELL LLM.


---

## Author
Shirish Manoj Bobde✨

---

# Happy Coding! 🚀

