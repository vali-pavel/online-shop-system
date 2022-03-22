pushd ./services
cd auth
docker compose build
docker compose up -d

cd ..
cd user
docker compose build
docker compose up -d

cd ..
cd product
docker compose build
docker compose up -d

cd ..
cd order
docker compose build
docker compose up -d

cd ..
cd customer
docker compose build
docker compose up -d
popd
