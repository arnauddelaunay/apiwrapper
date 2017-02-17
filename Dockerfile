FROM tiangolo/uwsgi-nginx-flask:flask

COPY . /app

# Add requirements.txt
ADD requirements.txt .

# Install app requirements
RUN pip install -r requirements.txt

# Run app using gunicorn
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:5000", "main"]