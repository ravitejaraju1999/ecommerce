FROM eclipse-temurin:21-jdk AS builder

WORKDIR /app

COPY . .

RUN chmod +x gradlew

# If build.gradle expects protoSourceDir
RUN cp -r pb proto

RUN ./gradlew installDist -PprotoSourceDir=./proto

#####################################################

FROM eclipse-temurin:21-jre

WORKDIR /app

COPY --from=builder \
    /app/build/install/opentelemetry-demo-ad \
    ./build/install/opentelemetry-demo-ad

ENV AD_PORT=9099

EXPOSE 9099

ENTRYPOINT ["./build/install/opentelemetry-demo-ad/bin/Ad"]