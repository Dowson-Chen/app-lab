# 🧩 Design Overview – TODO App

## 📚 Data Model

**Task**
- `id: str` (UUID)
- `title: str`
- `completed: bool = False`

## 🌐 API Endpoints

- `GET /tasks` – List all tasks
- `POST /tasks` – Create new task
  - Body: `{ "title": "Buy milk" }`
- `PUT /tasks/{id}` – Mark task as complete
- `DELETE /tasks/{id}` – Delete a task

## 🔁 Sequence (Create Task Flow)

1. User sends POST `/tasks`
2. FastAPI handles request → `create_task()`
3. Validates input via Pydantic
4. Adds task to list or DB
5. Returns created task object

## 🧠 Notes / To-Do

- Add SQLite backend later
- Improve error handling
- Consider authentication later
