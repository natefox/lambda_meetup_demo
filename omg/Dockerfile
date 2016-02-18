FROM alpine
MAINTAINER Nate Fox <nfox@corpinfo.com>

RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk --update add stress@testing

CMD ["stress","--cpu","10","--timeout","600"]
