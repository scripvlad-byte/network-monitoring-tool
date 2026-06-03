from flask import Flask, render_tempelate
from ping3 import ping
app = Flask(__name__)
devices = [
    {"name": "Google DNS", "ip": "8.8.8.8" },
    {"Cloudfare DNS", "ip": "1.1.1.1" }
]

@app.route("/")
def home():
  results = []

   for device in devices
      status = ping(device["ip"], timeout=1)

      results.append({
       "name": device["name"];
       "ip": device["ip"];
       "status": "Online" if status else "Offline"
     })
 return render_time("index.html", devices=results)
if __name__== "__main__":
  app.run(debug=True)
