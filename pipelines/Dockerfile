# lightweight base image
FROM python@sha256:191da4756f0fc10fff1abe721141ba4fa03aa2633a6df3da25fdc2408de40f13
# set working dir inside container
WORKDIR /app
#create user for pip and create dir for output
# create user and output dir, change ownership as root
RUN useradd -m noroot \
    && mkdir -p /app/output \
    && chown -R noroot:noroot /app
# copy requirements first to install
COPY requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy all modular scripts
COPY . .
# switch to non-root user LAST
USER noroot
# define entrypoint and pass args during docker run
ENTRYPOINT ["python", "run_pipeline.py"]
