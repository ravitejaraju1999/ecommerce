from golang:1.22-alpine as builder

workdir /app

copy . .

run go mod download

run go build -o product-catalog  ./

from alpine as release
workdir /app
copy ./products ./products
copy --from=builder /app/product-catalog ./

expose ${product_catalog_port}

env product_catalog_port=8088

entrypoint ["./product-catalog"]
