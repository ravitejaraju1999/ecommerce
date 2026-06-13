# Build stage
FROM golang:1.22-alpine AS builder

WORKDIR /app

COPY . .

RUN go mod download
RUN go build -o product-catalog ./


# Release stage
FROM alpine AS release

WORKDIR /app

# Copy built binary from builder
COPY --from=builder /app/product-catalog ./

# Copy any other required files
COPY ./products ./products

# Set environment variable in proper KEY=VALUE format
ENV PRODUCT_CATALOG_PORT=8088

# Set entrypoint
ENTRYPOINT ["./product-catalog"]