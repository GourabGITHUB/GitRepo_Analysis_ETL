# lightweight base image
FROM python@sha256:191da4756f0fc10fff1abe721141ba4fa03aa2633a6df3da25fdc2408de40f13
# set working dir inside container
WORKDIR /app
#create user for pip and create dir for output
RUN useradd -m noroot && mkdir /app/output
#swith to user
USER noroot
# copy requirements first to install
COPY requirements.txt .
#Change ownership of the app directory to noroot
RUN chown -R noroot:noroot /app
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy all modular scripts
COPY . .
# define entrypoint and pass args during docker run
ENTRYPOINT ["python", "run_pipeline.py"]
