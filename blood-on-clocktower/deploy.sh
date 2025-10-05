#!/bin/bash

# Production deployment script for Blood on the Clocktower app
# This script sets up and runs the application in production mode

set -e  # Exit on error

echo "🚀 Starting deployment..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: No .env file found. Using defaults."
    echo "💡 Copy .env.example to .env and configure it for production."
fi

# Set production environment
export FLASK_ENV=production

# Initialize database if needed
if [ ! -f "instance/botc.db" ]; then
    echo "🗄️  Initializing database..."
    flask db upgrade
    
    # Ask if user wants to seed the database
    read -p "Do you want to seed the database with game data? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🌱 Seeding database..."
        python seed_all_editions.py
    fi
fi

# Run database migrations
echo "🔄 Running database migrations..."
flask db upgrade

# Start the application with gunicorn
echo "✅ Starting application with gunicorn..."
echo "🌐 Application will be available at http://0.0.0.0:5002"
echo "Press Ctrl+C to stop the server"
echo ""

gunicorn --bind 0.0.0.0:5002 --workers 2 --threads 4 --timeout 60 --access-logfile - --error-logfile - "wsgi:app"
