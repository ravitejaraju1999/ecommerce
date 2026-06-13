from eclipse-temurin:21-jdk as builder
workdir /app
copy . .

run chmod +x gradlew
run ./gradlew
run ./gradlew downloadRepos

copy ./pb ./proto

run chmod +x gradlew

run ./gradlew installDist -PprotoSourceDir=./proto

#####################################################

from eclipse-temurin:21-jre
workdir /app

copy --from=builder /app/build/install/opentelemetry-demo-ad ./build/install/opentelemetry-demo-ad




env AD_PORT=9099

entrypoint ["./build/install/opentelemetry-demo-ad/bin/Ad"]





