# 📊 Student Marks API

This is a simple and efficient **FastAPI** application deployed on **Vercel** that returns student marks based on their unique identifiers.

---

## 🚀 Live Demo

🔗 [your-app-mybx-3bmcxqbgl-sahilthecoder502s-projects.vercel.app](your-app-mybx-3bmcxqbgl-sahilthecoder502s-projects.vercel.app)

---

## 🔍 Features

- 🔄 Accepts multiple student names via query parameters
- 📘 Returns corresponding marks or `null` if not found
- 🌐 CORS-enabled for frontend integration
-  GET requests from any origin.
- ⚡ Powered by **FastAPI** and deployed on **Vercel**

---

## 🧪 Example Usage

### ✅ Request
``` https://your-app.vercel.app/api?name=X&name=Y```


✅ Response
 then  output like
 { "marks": [10, 20] }```


 🛠️ Technologies Used
FastAPI

Uvicorn

Vercel (for deployment)

```
├── main.py               # FastAPI application
├── requirements.txt      # List of dependencies
├── vercel.json           # (Optional) Vercel config file
└── README.md             # Project documentation ```
```


📦 Installation (Local Development)

1. Clone the Repository
git clone https://github.com/yourusername/student-marks-api.git
cd student-marks-api

2. Install Requirements
   pip install -r requirements.txt
3. Run the App Locally
 uvicorn main:app --reload
Visit: http://127.0.0.1:8000/api?name=RY&name=F

☁️ Deployment (on Vercel)
Push your code to a GitHub repo.

Connect the repo to Vercel.

Set the root directory if needed.

Vercel will auto-detect FastAPI and deploy it.

Use the /api endpoint for queries.

Note: You may need a vercel.json file if your structure is custom. Here's an example:
```
 {
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

✍️ Author
Sahil Kumar
📧 bt23ece015@nituk.ac.in
🔗 [LinkedIn](https://www.linkedin.com/in/sahil-kumar-1645a3324?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BsZ9%2BLcdJRjif4SB7%2FFO1%2BQ%3D%3D)
💻 [GitHub](https://github.com/24f2000164/)

📄 License
This project is licensed under the MIT License.


 
