# 📐 UML Diagrams – TODO App

This file contains class and flow diagrams for the TODO app.

---

## 🧩 Class Diagram – `Task`

![Task UML](https://www.plantuml.com/plantuml/png/SoWkIImgAStDuKhEIImkLWX9BCvMgEPIKD3EJB5IA2uf0Z5BCajoKk6yvFpSWfpKabIWV59-VWvNBPT3QbuAq0W0)

```plantuml
@startuml
class Task {
  +id: str
  +title: str
  +completed: bool
}
@enduml
