#Pull base image
FROM kiyoto/fluentd:0.10.56-2.1.1

RUN mkdir /etc/fluent

# Copy custom fluent.conf to ship nginx logs to AWS s3
ADD fluent.conf /etc/fluent/

RUN ["/usr/local/bin/gem", "install", "fluent-plugin-record-reformer", "--no-rdoc", "--no-ri"]

RUN ["/usr/local/bin/gem", "install", "fluent-plugin-forest", "--no-rdoc", "--no-ri"]

RUN ["/usr/local/bin/gem", "install", "fluent-plugin-s3", "--no-rdoc", "--no-ri"]

ENTRYPOINT ["/usr/local/bin/fluentd", "-c", "/etc/fluent/fluent.conf","--use-v1-config"]

