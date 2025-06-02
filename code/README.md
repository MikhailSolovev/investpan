1. Change envs to your valid API keys in .env: `OPENAI_API_KEY`, `FINNHUBAPI_KEY`
2. Export envs
```shell
export $(cat .env | xargs)   
```
2. Run command:
```shell
uvicorn main:app --reload
```
3. Go to swagger `http://127.0.0.1:8000/docs`