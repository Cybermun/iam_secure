iam_secure/
├── docker-compose.yml        # Container orchestration file
├── keycloak/                 # Keycloak realm and config
├── flask-app/
│   ├── app.py                # Defines API routes and logic
│   ├── verify_token.py       # Verifies JWT tokens using Keycloak public key
│   ├── requirements.txt      # Required Python packages
│   └── .env                  # Secure storage for environment variables
└── README.txt                # Instructions for setup and usage


http://localhost:8080
Login as admin/admin
Show Realm: demo, Client: flask-client, User: testuser
Get access token via curl
public ➝ should work
protected ➝ fails w/o token, works with token
