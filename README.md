# 📝 Task Manager API

A simple REST API for task management with full CRUD operations support.

## 🚀 Features

- ✅ Get all tasks
- ✅ Get a single task by ID
- ✅ Create new task
- ✅ Update task
- ✅ Delete task
- ✅ Data validation
- ✅ Error handling

## 📋 Task Structure

```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

## 🔌 API Endpoints

### 1. Get All Tasks
```
GET /tasks
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "completed": false
  },
  {
    "id": 2,
    "title": "Walk the dog",
    "completed": true
  }
]
```

### 2. Get Task by ID
```
GET /tasks/:id
```

**Example:**
```bash
GET /tasks/1
```

**Response (200):**
```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

**Response (404):**
```json
{
  "error": "Task not found"
}
```

### 3. Create New Task
```
POST /tasks
Content-Type: application/json
```

**Request Body:**
```json
{
  "title": "Do laundry"
}
```

**Response (201):**
```json
{
  "id": 4,
  "title": "Do laundry",
  "completed": false
}
```

**Validation:**
- `title` is required
- `title` cannot be empty

### 4. Update Task
```
PATCH /tasks/:id
Content-Type: application/json
```

**Request Body (partial update):**
```json
{
  "completed": true
}
```

**Or:**
```json
{
  "title": "Buy groceries and cook dinner",
  "completed": false
}
```

**Response (200):**
```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": true
}
```

### 5. Delete Task
```
DELETE /tasks/:id
```

**Response:** `204 No Content`

## 💻 Local Setup

### Requirements
- Python 3.8+

### Installation and Running

1. **Clone the repository**
```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the server**
```bash
python app.py
```

Server will start at `http://localhost:5000`

## 🧪 Testing the API

### Using curl

**Get all tasks:**
```bash
curl http://localhost:5000/tasks
```

**Create a task:**
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "New task"}'
```

**Update a task:**
```bash
curl -X PATCH http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

**Delete a task:**
```bash
curl -X DELETE http://localhost:5000/tasks/1
```

### Using Postman

1. Import the collection (or create manually)
2. Use `http://localhost:5000` as base URL
3. Test all endpoints

## 🌐 Deploy to Railway (from mobile!)

### Step 1: Create GitHub Repository

1. **Via browser:**
   - Go to [github.com](https://github.com)
   - Click "New repository"
   - Name it, e.g.: `task-manager-api`
   - Click "Create repository"

2. **Upload files:**
   - On the repository page click "uploading an existing file"
   - Drag all project files
   - Click "Commit changes"

**OR use GitHub Mobile app:**
   - Install GitHub Mobile from App Store/Google Play
   - Create repository via app
   - Upload files

### Step 2: Deploy to Railway

1. **Go to [railway.app](https://railway.app)**
   - Sign up via GitHub

2. **Create new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Select your `task-manager-api` repository

3. **Railway will automatically:**
   - Detect Python application
   - Install dependencies from `requirements.txt`
   - Start the application via `Procfile`

4. **Get public URL:**
   - In project settings find "Settings"
   - Click "Generate Domain"
   - You'll get a URL like: `https://task-manager-api-production.up.railway.app`

5. **Done!** 🎉
   - Now your friends can use the API via this link
   - Example: `https://your-project.up.railway.app/tasks`

### Railway Free Tier:
- $5/month free (enough for testing)
- Automatic deployment on GitHub push

## 📱 Alternative Deployment Platforms

### Render.com
- Even simpler than Railway
- 750 hours/month free
- [render.com](https://render.com)

### Fly.io
- Also has a free tier
- [fly.io](https://fly.io)

## 🛠️ Tech Stack

- **Python 3.x**
- **Flask** - web framework
- **Flask-CORS** - CORS support
- **Gunicorn** - production server

## 📚 Usage Examples

### JavaScript (fetch)
```javascript
// Get all tasks
fetch('https://your-project.up.railway.app/tasks')
  .then(response => response.json())
  .then(data => console.log(data));

// Create a task
fetch('https://your-project.up.railway.app/tasks', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: 'New task from JavaScript'
  }),
})
  .then(response => response.json())
  .then(data => console.log(data));
```

### Python (requests)
```python
import requests

# Get all tasks
response = requests.get('https://your-project.up.railway.app/tasks')
print(response.json())

# Create a task
new_task = {'title': 'New task from Python'}
response = requests.post(
    'https://your-project.up.railway.app/tasks',
    json=new_task
)
print(response.json())
```

## 🎯 Error Handling

API returns clear error messages:

- **400 Bad Request** - invalid data format
- **404 Not Found** - task not found
- **405 Method Not Allowed** - invalid HTTP method
- **500 Internal Server Error** - server error

**Example error response:**
```json
{
  "error": "Task not found"
}
```

## 📝 License

MIT License - feel free to use this project however you want!

## 🤝 Contact

Questions? Create an issue in the repository!

---

**Built with ❤️ and Claude AI**
