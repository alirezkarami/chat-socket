# Simple Chat Project with WebSocket (Daphne)

This project is a simple chat service where users can communicate in a **public room** in **real-time**.  
The implementation is **backend only**, and messages are exchanged instantly between users without storing them in a database.

---

## Project Features

- User registration and login (**Authentication**)
- Session management with **JWT Token**
- A public room for real-time messaging
- WebSocket implementation using **Django Channels** and server run with **Daphne**
- API documentation with **Swagger**

---

## WebSocket Endpoint


### Example Sent Message
```json
{
    "message": "hello, how are you?",
    "user": "alireza",
    "time": "11/17/2025 21:14:34"
}


## Running the Project with Daphne

1. **Install dependencies:**
```bash
pip install -r requirements.txt

```bash
daphne -p 8000 chat_sock.asgi:application
