FROM rabbitmq:3-management

COPY bunny.sh .
RUN chmod +x /bunny.sh

# needed to set up users and start rabbit-server afterwards.
ENTRYPOINT [ "/bunny.sh" ]