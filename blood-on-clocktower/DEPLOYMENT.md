# 🚀 Deployment Guide

This guide covers multiple deployment options for the Blood on the Clocktower application.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Method 1: Local Production Deployment](#method-1-local-production-deployment)
- [Method 2: Docker Deployment](#method-2-docker-deployment)
- [Method 3: Heroku Deployment](#method-3-heroku-deployment)
- [Method 4: Railway/Render Deployment](#method-4-railwayrender-deployment)
- [Environment Variables](#environment-variables)
- [Database Considerations](#database-considerations)

---

## Prerequisites

- Python 3.10 or higher
- Git
- A server or hosting platform
- (Optional) Docker for containerized deployment

---

## Method 1: Local Production Deployment

This method runs the application on your own server using Gunicorn.

### Quick Start

1. **Clone the repository** (if not already done)
   ```bash
   cd blood-on-clocktower
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-super-secret-key-change-this
   ```

3. **Make deployment script executable**
   ```bash
   chmod +x deploy.sh
   ```

4. **Run the deployment script**
   ```bash
   ./deploy.sh
   ```

The application will be available at `http://0.0.0.0:5002`

### Manual Setup

If you prefer to set up manually:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_ENV=production
export SECRET_KEY="your-secret-key"

# Initialize database
flask db upgrade
python seed_all_editions.py  # Optional: seed game data

# Run with Gunicorn
gunicorn --bind 0.0.0.0:5002 --workers 2 --threads 4 --timeout 60 wsgi:app
```

### Running as a System Service (Linux)

Create a systemd service file at `/etc/systemd/system/botc.service`:

```ini
[Unit]
Description=Blood on the Clocktower Application
After=network.target

[Service]
Type=notify
User=your-username
WorkingDirectory=/path/to/blood-on-clocktower
Environment="FLASK_ENV=production"
Environment="SECRET_KEY=your-secret-key"
ExecStart=/path/to/blood-on-clocktower/venv/bin/gunicorn --bind 0.0.0.0:5002 --workers 2 --threads 4 --timeout 60 wsgi:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable botc
sudo systemctl start botc
sudo systemctl status botc
```

---

## Method 2: Docker Deployment

Docker provides an isolated, reproducible deployment environment.

### Using Docker Compose (Recommended)

1. **Build and start the container**
   ```bash
   docker-compose up -d
   ```

2. **Initialize the database** (first time only)
   ```bash
   docker-compose exec web flask db upgrade
   docker-compose exec web python seed_all_editions.py
   ```

3. **View logs**
   ```bash
   docker-compose logs -f web
   ```

4. **Stop the application**
   ```bash
   docker-compose down
   ```

### Using Docker Directly

```bash
# Build the image
docker build -t botc-app .

# Run the container
docker run -d \
  -p 5002:5002 \
  -e FLASK_ENV=production \
  -e SECRET_KEY=your-secret-key \
  -v $(pwd)/instance:/app/instance \
  --name botc \
  botc-app

# Initialize database (first time)
docker exec botc flask db upgrade
docker exec botc python seed_all_editions.py
```

---

## Method 3: Heroku Deployment

Heroku is a Platform-as-a-Service (PaaS) that simplifies deployment.

### Prerequisites
- Heroku account
- Heroku CLI installed

### Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables**
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set SECRET_KEY=$(openssl rand -hex 32)
   ```

4. **Deploy the application**
   ```bash
   git push heroku main
   ```

5. **Initialize the database**
   ```bash
   heroku run flask db upgrade
   heroku run python seed_all_editions.py
   ```

6. **Open your application**
   ```bash
   heroku open
   ```

### Note on Database

By default, the app uses SQLite. For Heroku, consider using PostgreSQL:

```bash
# Add PostgreSQL addon
heroku addons:create heroku-postgresql:mini

# The DATABASE_URL will be set automatically
```

Update `requirements.txt` to include:
```
psycopg2-binary==2.9.9
```

---

## Method 4: Railway/Render Deployment

### Railway

1. **Connect your GitHub repository** to Railway
2. **Set environment variables** in Railway dashboard:
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secret-key`
3. **Deploy** - Railway will automatically detect the `Procfile`
4. **Initialize database** via Railway's shell:
   ```bash
   flask db upgrade
   python seed_all_editions.py
   ```

### Render

1. **Create a new Web Service** on Render
2. **Connect your GitHub repository**
3. **Configure the service**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`
4. **Add environment variables**:
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secret-key`
5. **Deploy** and initialize database via Render shell

---

## Environment Variables

Required environment variables for production:

| Variable | Description | Example |
|----------|-------------|---------|
| `FLASK_ENV` | Application environment | `production` |
| `SECRET_KEY` | Secret key for sessions | `your-long-random-string` |
| `DATABASE_URL` | Database connection string (optional) | `postgresql://user:pass@host/db` |
| `PORT` | Port to run on (some platforms set this) | `5002` |

### Generating a Secure SECRET_KEY

```bash
# Using Python
python -c "import secrets; print(secrets.token_hex(32))"

# Using OpenSSL
openssl rand -hex 32
```

---

## Database Considerations

### SQLite (Default)

- **Pros**: Simple, no configuration needed
- **Cons**: Not suitable for high-concurrency, file-based
- **Best for**: Small deployments, single-user scenarios

### PostgreSQL (Recommended for Production)

- **Pros**: Robust, handles concurrency, production-ready
- **Cons**: Requires separate database server

To use PostgreSQL:

1. **Update requirements.txt**:
   ```
   psycopg2-binary==2.9.9
   ```

2. **Set DATABASE_URL**:
   ```bash
   export DATABASE_URL="postgresql://user:password@localhost/botc_db"
   ```

3. **Run migrations**:
   ```bash
   flask db upgrade
   ```

---

## Reverse Proxy with Nginx (Optional)

For production deployments, it's recommended to use Nginx as a reverse proxy:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5002;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Optional: Serve static files directly
    location /static {
        alias /path/to/blood-on-clocktower/app/static;
        expires 30d;
    }
}
```

---

## SSL/HTTPS

For production, always use HTTPS. Options include:

1. **Let's Encrypt** (free SSL certificates)
   ```bash
   sudo certbot --nginx -d your-domain.com
   ```

2. **Cloudflare** (free SSL proxy)

3. **Platform SSL** (Heroku, Railway, Render provide free SSL)

---

## Monitoring and Logs

### View Application Logs

- **Local**: Gunicorn outputs to stdout/stderr
- **Docker**: `docker-compose logs -f web`
- **Heroku**: `heroku logs --tail`
- **Railway/Render**: View logs in their dashboard

### Health Check Endpoint

The application includes a health check at the root URL (`/`). Most monitoring tools can ping this endpoint.

---

## Backup and Maintenance

### Backup SQLite Database

```bash
# Local
cp instance/botc.db instance/botc.db.backup

# Docker
docker cp botc:/app/instance/botc.db ./backup-$(date +%Y%m%d).db
```

### Database Migrations

When updating the application:

```bash
# Pull latest code
git pull

# Run migrations
flask db upgrade

# Restart application
sudo systemctl restart botc  # or docker-compose restart
```

---

## Troubleshooting

### Application won't start

1. Check environment variables are set correctly
2. Verify database connection
3. Check logs for error messages

### Database errors

1. Ensure database is initialized: `flask db upgrade`
2. Check file permissions for SQLite
3. Verify DATABASE_URL for PostgreSQL

### Port already in use

```bash
# Find process using port 5002
lsof -i :5002

# Kill the process
kill -9 <PID>
```

---

## Security Checklist

- [ ] Set a strong `SECRET_KEY`
- [ ] Use HTTPS in production
- [ ] Disable `DEBUG` mode (`FLASK_ENV=production`)
- [ ] Use environment variables for sensitive data
- [ ] Regular database backups
- [ ] Keep dependencies updated
- [ ] Use a reverse proxy (Nginx/Apache)
- [ ] Implement rate limiting (if needed)
- [ ] Regular security audits

---

## Support

For issues or questions:
- Check application logs
- Review this documentation
- Check Flask and Gunicorn documentation

---

**Good luck with your deployment! 🎭**
