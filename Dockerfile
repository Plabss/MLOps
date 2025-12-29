# 1. Start with a Base Image (The Foundation)
# We choose a lightweight version of Python 3.9
FROM python:3.9-slim

# 2. Set the Working Directory (The Kitchen Counter)
# This creates a folder inside the container where we will work
WORKDIR /app

# 3. Copy the Ingredients (Transfer files)
# Copy everything from your current folder (.) to the container's folder (.)
COPY . .

# 4. Install Dependencies (Prep work)
# This runs pip inside the container
RUN pip install -r requirements.txt

# 5. The Start Command (Serve the dish)
# This is the command that runs when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]