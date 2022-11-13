FROM python

RUN python3 -m venv flask

# Install dependencies:
COPY requirements.txt .
RUN . flask/bin/activate && pip install -r requirements.txt

# Run the application:
COPY server.py .
CMD . flask/bin/activate && exec python server.py