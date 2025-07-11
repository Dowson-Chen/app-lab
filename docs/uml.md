# 📐 UML Diagrams – TODO App

This file contains class and flow diagrams for the TODO app.

---

## 🧩 Class Diagram – `Task`

```plantuml
@startuml
class Task {
  +id: str
  +title: str
  +completed: bool
}
@enduml
