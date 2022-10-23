run APP:
    uvicorn main:app --app-dir {{APP}} --reload 
prun APP WORKERS:
    uvicorn main:app --app-dir {{APP}} --workers {{WORKERS}}