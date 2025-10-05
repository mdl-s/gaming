# 🚀 Quick Deployment Guide

## Fastest Way to Deploy (Local)

```bash
# 1. Configure environment
cp .env.example .env
nano .env  # Edit and set your SECRET_KEY

# 2. Run deployment script
chmod +x deploy.sh
./deploy.sh
```

That's it! Your app will be running at `http://0.0.0.0:5002`

---

## Docker (Recommended for Servers)

```bash
# Build and run
docker-compose up -d

# Initialize database (first time only)
docker-compose exec web flask db upgrade
docker-compose exec web python seed_all_editions.py

# Check status
docker-compose ps
```

Access at: `http://localhost:5002`

---

## Heroku (Cloud Deployment)

```bash
# Login and create app
heroku login
heroku create your-app-name

# Configure
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=$(openssl rand -hex 32)

# Deploy
git push heroku main

# Initialize database
heroku run flask db upgrade
heroku run python seed_all_editions.py

# Open app
heroku open
```

---

## Important Notes

### Required Environment Variables

- `FLASK_ENV=production`
- `SECRET_KEY=your-secret-key` (generate with: `openssl rand -hex 32`)

### First-Time Setup

Always run these after deployment:
```bash
flask db upgrade              # Create database tables
python seed_all_editions.py   # Load game characters
```

### Check Deployment

Visit your app URL. You should see the Blood on the Clocktower home page.

---

For detailed deployment options, see [DEPLOYMENT.md](DEPLOYMENT.md)
