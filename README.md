# Installation
```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```


# Run PetStore API
```
docker run -d -e SWAGGER_URL=http://localhost \
  -e SWAGGER_BASE_PATH=/v3 -p 80:8080 swaggerapi/petstore
  ```

# Run performance test
```
locust -f tests/petstore.py --master --headless -u 1 -r 1
```

```
locust -f tests/petstore.py --worker --master-host=localhost
```