#!/bin/bash
#
#

echo ""
echo "Mock Service"

curl http://127.0.0.1:8080
curl http://127.0.0.1:8081
curl http://127.0.0.1:8082

echo ""
echo "Test Default"

curl http://127.0.0.1:80


echo ""
echo "Test Hash String"

curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-1.local:1080/cas/api/auth"}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-2.local:1080/cas/api/auth"}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-3.local:1080/cas/api/auth"}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-4.local:1080/cas/api/auth"}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-5.local:1080/cas/api/auth"}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-6.local:1080/cas/api/auth"}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-7.local:1080/cas/api/auth"}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-8.local:1080/cas/api/auth"}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": "http://apis-9.local:1080/cas/api/auth"}' http://127.0.0.1:80


echo ""
echo "Test Hash integer"

curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 0}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 1}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 2}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 4}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 5}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 6}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 7}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 8}' http://127.0.0.1:80
curl -X POST -H "Content-Type: application/json" -d '{"apiUrl": 9}' http://127.0.0.1:80
