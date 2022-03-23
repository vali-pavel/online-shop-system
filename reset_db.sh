pushd ./services

cd user
docker compose run db_reset

cd ..
cd product
docker compose run db_reset

cd ..
cd customer
docker compose run db_reset

popd
