uvicorn main:app --reload

(--reload) ->> when you read something is your code this reload function a autometically reload your page. You dont need to reload further.

Website -> dynamic or Static

Dynamic -> CRUD (C -> Creat, R -> Read, U -> Update, D -> Delete)

                          HTTP methods
            -----------------------------------------
            
            post -> Creat (C)
            get -> Read (R)
            put -> update (U)
            delete -> Delete (U)


+ ==> Path parameter

+ ==> In FastAPI, the HTTPException is a standard Python exception used to return structured HTTP error responses to the client. When raised, FastAPI automatically stops the current request and sends an HTTP error with the specified status code and detail message. 


+ =>> status code 

✅ Common HTTP Status Codes (FastAPI)
2xx (Success)

200 OK → request successful (GET এর জন্য বেশি)

201 Created → নতুন data create হয়েছে (POST)

204 No Content → delete successful, কিন্তু response body নাই

3xx (Redirect)

301 Moved Permanently → URL change হয়ে গেছে

302 Found → temporary redirect

4xx (Client Error)

400 Bad Request → ভুল request / invalid input

401 Unauthorized → login/token লাগবে

403 Forbidden → permission নাই

404 Not Found → resource পাওয়া যায়নি

422 Unprocessable Entity → validation error (FastAPI তে খুব common)

5xx (Server Error)

500 Internal Server Error → server error

503 Service Unavailable → server down / overload