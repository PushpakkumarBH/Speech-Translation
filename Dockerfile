FROM python

RUN python3 -m venv /opt/speech

# Install dependencies:
COPY requirements.txt .
RUN . /opt/speech/bin/activate && pip install -r requirements.txt

# Run the application:
COPY myapp.py .
CMD . /opt/speech/bin/activate && exec python Speechrecognition.py