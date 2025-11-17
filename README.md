# Simple Chat Project with WebSocket (Daphne)

This project is a simple real-time chat backend built with Django, Channels, and Daphne.
Users can register, authenticate via JWT, and join a public chat room where messages
are exchanged instantly without being stored in the database.

## Features
- User registration and login
- JWT-based authentication
- Real-time public chat
- WebSocket backend using Django Channels
- ASGI server using Daphne
- Swagger API documentation

## Project Structure

├── account/  
├── chat/  
├── chat_sock/  
├── manage.py  
├── requirements.txt  
└── README.md

## WebSocket Endpoint
WebSocket URL:
ws://localhost:8000/ws/chat/

### Example: Client → Server (Valid JSON)
```json
{
  "message": "hello, how are you?"
}
```
### Example: Server → Client (Valid JSON)
```json
{
  "message": "hello, how are you?",
  "username": "alireza",
  "time": "11/17/2025 21:14:34"
}
```
## Installation

1. Clone the repository
```
git clone https://github.com/alirezkarami/chat-socket
cd chat-socket
```

2. Create virtual environment
```
python -m venv venv
source venv/bin/activate     (Linux/macOS)
venv\Scripts\activate        (Windows)
```
3. Install dependencies
```
pip install -r requirements.txt
```

4. Apply migrations
```
python manage.py migrate
```
5. Optional: Create superuser
```
python manage.py createsuperuser
```
## Run With Daphne
daphne -p 8000 chat_sock.asgi:application

WebSocket available at:

`ws://localhost:8000/ws/chat/`
## Swagger Docs
`http://localhost:8000/api/docs`
