FROM quay.io/centos/centos:stream8

RUN dnf -y install httpd
COPY info.txt /var/www/httpd
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]
