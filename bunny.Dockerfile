FROM rabbitmq:3-management

COPY bunny.sh .
RUN chmod +x /bunny.sh

ENTRYPOINT [ "/bunny.sh"]