#!/bin/bash

# Setup environment file with secure SECRET_KEY

echo "🔧 Setting up environment file..."

if [ -f ".env" ]; then
    echo "⚠️  .env file already exists!"
    read -p "Do you want to overwrite it? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled."
        exit 0
    fi
fi

# Generate a secure SECRET_KEY
SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")

# Create .env file
cat > .env << EOF
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=$SECRET_KEY

# Database Configuration
# For production, you can use PostgreSQL instead of SQLite
# DATABASE_URL=postgresql://user:password@localhost/botc_db

# Optional: Port configuration (default: 5000)
# PORT=5002
EOF

echo "✅ .env file created successfully!"
echo ""
echo "Your SECRET_KEY has been generated and saved."
echo ""
echo "🔒 Important: Keep this file secure and never commit it to git!"
echo ""
echo "Next steps:"
echo "  1. Review the .env file if needed"
echo "  2. Run: ./deploy.sh to start the application"
echo ""
