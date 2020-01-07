FROM rabbitmq:3-management

#COPY bunny.sh ./

#ENTRYPOINT [ "bunny.sh"]

ADD bunny.sh /.
#WORKDIR /usr/local/bin
RUN rabbitmq-plugins enable --offline rabbitmq_management
ENTRYPOINT ["bash","bunny.sh"]

#EXPOSE 4369 25672 5672 15672
