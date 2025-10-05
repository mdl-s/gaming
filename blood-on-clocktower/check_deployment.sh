#!/bin/bash

# Deployment readiness checker
# This script verifies that your application is ready for deployment

echo "🔍 Checking deployment readiness..."
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0
WARNINGS=0

# Check Python version
echo "📌 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION found"
else
    echo -e "${RED}✗${NC} Python 3 not found"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# Check if requirements.txt exists
echo "📌 Checking requirements.txt..."
if [ -f "requirements.txt" ]; then
    echo -e "${GREEN}✓${NC} requirements.txt exists"
    if grep -q "gunicorn" requirements.txt; then
        echo -e "${GREEN}✓${NC} Gunicorn is in requirements"
    else
        echo -e "${RED}✗${NC} Gunicorn missing from requirements"
        ERRORS=$((ERRORS + 1))
    fi
else
    echo -e "${RED}✗${NC} requirements.txt not found"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# Check deployment files
echo "📌 Checking deployment files..."
FILES=("Procfile" "wsgi.py" "deploy.sh" "Dockerfile" "docker-compose.yml" ".env.example")
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file exists"
    else
        echo -e "${YELLOW}!${NC} $file not found"
        WARNINGS=$((WARNINGS + 1))
    fi
done
echo ""

# Check for .env file
echo "📌 Checking environment configuration..."
if [ -f ".env" ]; then
    echo -e "${GREEN}✓${NC} .env file exists"
    
    # Check if SECRET_KEY is set
    if grep -q "SECRET_KEY=" .env && ! grep -q "SECRET_KEY=your-secret-key-here" .env; then
        echo -e "${GREEN}✓${NC} SECRET_KEY appears to be configured"
    else
        echo -e "${YELLOW}!${NC} SECRET_KEY needs to be set in .env"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Check if FLASK_ENV is set
    if grep -q "FLASK_ENV=production" .env; then
        echo -e "${GREEN}✓${NC} FLASK_ENV set to production"
    else
        echo -e "${YELLOW}!${NC} FLASK_ENV should be set to 'production' in .env"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo -e "${YELLOW}!${NC} .env file not found (copy from .env.example)"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# Check if app directory exists
echo "📌 Checking application structure..."
if [ -d "app" ]; then
    echo -e "${GREEN}✓${NC} app/ directory exists"
    
    if [ -f "app/__init__.py" ]; then
        echo -e "${GREEN}✓${NC} app/__init__.py exists"
    else
        echo -e "${RED}✗${NC} app/__init__.py not found"
        ERRORS=$((ERRORS + 1))
    fi
    
    if [ -f "app/models.py" ]; then
        echo -e "${GREEN}✓${NC} app/models.py exists"
    else
        echo -e "${RED}✗${NC} app/models.py not found"
        ERRORS=$((ERRORS + 1))
    fi
else
    echo -e "${RED}✗${NC} app/ directory not found"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# Check for database migrations
echo "📌 Checking database setup..."
if [ -d "migrations" ]; then
    echo -e "${GREEN}✓${NC} migrations/ directory exists"
else
    echo -e "${YELLOW}!${NC} migrations/ directory not found (run: flask db init)"
    WARNINGS=$((WARNINGS + 1))
fi

if [ -f "instance/botc.db" ]; then
    echo -e "${GREEN}✓${NC} Database file exists"
else
    echo -e "${YELLOW}!${NC} Database not initialized (run: flask db upgrade)"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# Check for seed scripts
echo "📌 Checking seed scripts..."
if [ -f "seed_all_editions.py" ] || [ -f "seed_data.py" ]; then
    echo -e "${GREEN}✓${NC} Seed scripts found"
else
    echo -e "${YELLOW}!${NC} No seed scripts found"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# Check if Docker is available (optional)
echo "📌 Checking optional tools..."
if command -v docker &> /dev/null; then
    echo -e "${GREEN}✓${NC} Docker is available"
else
    echo -e "${YELLOW}!${NC} Docker not found (optional, needed for Docker deployment)"
fi

if command -v heroku &> /dev/null; then
    echo -e "${GREEN}✓${NC} Heroku CLI is available"
else
    echo -e "${YELLOW}!${NC} Heroku CLI not found (optional, needed for Heroku deployment)"
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✅ All checks passed! Ready for deployment!${NC}"
    echo ""
    echo "Next steps:"
    echo "  1. Review DEPLOYMENT_SUMMARY.md for deployment options"
    echo "  2. Choose your deployment method"
    echo "  3. Run: ./deploy.sh (for local deployment)"
    echo ""
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠️  Ready with $WARNINGS warning(s)${NC}"
    echo ""
    echo "You can proceed with deployment, but review the warnings above."
    echo ""
else
    echo -e "${RED}❌ Found $ERRORS error(s) and $WARNINGS warning(s)${NC}"
    echo ""
    echo "Please fix the errors before deploying."
    echo ""
fi

exit $ERRORS
