from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure Cloud Computing</title>
    </head>
    <body>
        <h1>Welcome to Azure Cloud Computing</h1>
        <h2>Python Flask Application</h2>
        <p>Successfully deployed using Azure App Service!</p>

        <h3>Cloud Service Models</h3>
        <ul>
            <li>IaaS - Azure Virtual Machines</li>
            <li>PaaS - Azure App Service</li>
            <li>SaaS - Google Drive</li>
        </ul>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

