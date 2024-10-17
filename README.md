# Flask + Vite + Nginx: Microservices Setup

## Project Overview

This project demonstrates how to integrate a Flask back-end with a Vite front-end development server and deploy it in production using Nginx as a reverse proxy.

## Features

- **Flask (Back-End)**: Python-based web framework for serving APIs and handling back-end logic.
- **Vite (Front-End)**: Fast and modern front-end build tool for rapid development.
- **Nginx (Production)**: Configured as a reverse proxy for routing API requests to Flask and serving static assets in production.

## Project Structure

```
.
├── backend                    # Flask back-end
│   └── app.py                 # Main Flask app
├── Dockerfile                 # Docker Compose
├── entrypoint.sh
├── frontend                   # Vite front-end
│   ├── eslint.config.js
│   ├── index.html             # Main front-end entry
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   └── vite.svg
│   ├── README.md
│   ├── src
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── assets
│   │   │   └── react.svg
│   │   ├── index.css
│   │   └── main.jsx
│   └── vite.config.js      # Vite configuration
├── nginx.conf              # Nginx configuration
└── requirements.txt        # Python dependencies
```
