FROM alpine:3.14.3

# Install dependencies
# NOTE: GNU sed is required by make install
RUN apk add --no-cache make git bash sed

WORKDIR /collection

RUN adduser -D user && chown -R user .
USER user
RUN git clone "https://github.com/veracioux/tuterm-collection" /collection

WORKDIR /app

# Install tuterm
USER root
COPY . .
RUN make install PREFIX=/usr

WORKDIR /collection

USER user
CMD sh
