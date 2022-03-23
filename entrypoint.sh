pushd ./services
cd auth
docker compose build
docker compose up -d auth_api

cd ..
cd user
docker compose build
docker compose up -d db user_api

cd ..
cd product
docker compose build
docker compose up -d db product_api

cd ..
cd order
docker compose build
docker compose up -d order_api

cd ..
cd customer
docker compose build
docker compose up -d db customer_api
popd
