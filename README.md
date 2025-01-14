# Entertainment Manager 🎬📚🎶

A modular platform to manage and organize your **comics**, **movies**, **music**, and **books**. Built with a modern tech stack for scalability, maintainability, and extensibility, this project showcases best practices in full-stack development.

---

## 🚀 Features

### 🖼️ Comics Management
- Add, list, edit, and delete comics.
- Local file upload and storage.

### 🎥 Movies Management
- Organize movies by title, director, and genre.
- Intuitive and user-friendly interface.

### 🎵 Music Management
- Manage tracks by artist or album.
- Advanced search and filter options.

### 📚 Books Management
- Track books by title and author.
- Customizable lists for easy access.

### 🌐 RESTful API
- Well-documented endpoints for integration.
- Real-time data access for a seamless user experience.

---

## 🛠️ Technologies Used

### Backend
- **Flask**: For a robust RESTful API.
- **PostgreSQL**: Relational database for storing and querying data.
- **SQLAlchemy**: ORM for database interactions.
- **Docker**: To containerize the backend services.

### Frontend
- **React**: For building a dynamic and responsive user interface.
- **TailwindCSS**: For modern, fast, and consistent styling.

### DevOps
- **Docker Compose**: To orchestrate the backend, frontend, and database containers.

---

## 🏗️ Project Architecture

This project is built with a **modular architecture**, dividing responsibilities into clean, independent components:

1. **Backend**:
   - Flask API with routes organized by domain (comics, movies, music, books).
   - Centralized PostgreSQL database with SQLAlchemy ORM.

2. **Frontend**:
   - A React application styled with TailwindCSS.
   - Clean, responsive, and user-friendly UI.

3. **Infrastructure**:
   - Dockerized setup for consistent deployment and seamless development workflow.

---

## 🛠️ How to Run the Project

This project uses Docker for easy setup and deployment. Follow these steps:

### Prerequisites
- Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/entertainment-manager.git
   cd entertainment-manager
