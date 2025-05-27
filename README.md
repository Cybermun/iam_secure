Project Structure
iam-secure/
├── docker-compose.yml
├── Makefile
├── config/
│   └── keycloak/
│       └── demo-realm.json
├── flask-app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── scripts/                  
│   └── configure_keycloak.sh
└── README.md


http://localhost:8080
Login as admin/admin
Show Realm: demo, Client: flask-client, User: testuser
Get access token via curl
public ➝ should work
protected ➝ fails w/o token, works with token
