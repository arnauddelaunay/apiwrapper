FROM tiangolo/uwsgi-nginx-flask:flask

COPY . /app

# Add requirements.txt
ADD requirements.txt .

# Install app requirements
RUN pip install -r requirements.txt
