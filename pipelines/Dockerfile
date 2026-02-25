# lightweight base image
FROM python@sha256:191da4756f0fc10fff1abe721141ba4fa03aa2633a6df3da25fdc2408de40f13
# set working dir inside container
WORKDIR /app
#create user for pip
RUN useradd -m noroot
#swith to user
USER noroot
# copy requirements first to install
COPY requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy all modular scripts
COPY . .
# define entrypoint and pass args during docker run
ENTRYPOINT ["python", "run_pipeline.py"]
