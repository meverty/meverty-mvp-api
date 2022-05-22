# Meverty API

API for Meverty Service

## How To Test

### Local Test

```
npm install
pip3 install -r requirements.txt
```


Dependency.py에서 DBConfig 의존성을 LocalDBConfig로 주입합니다.
Local DB를 이용하기 위해서는 sqlite3가 설치되어 있어야 합니다.

```
def configure(binder):
    binder.bind(MemberService, to = MemberService, scope=singleton)
    binder.bind(DBConfig, to = RemoteDBConfig, scope=singleton)
```

이후 serverless를 이용해 로컬 서버를 실행합니다.
```
serverless wsgi serve
```

### Dev Stage Deploy
Dependency.py에서 DBConfig 의존성을 RemoteDBConfig로 주입합니다.
```
def configure(binder):
    binder.bind(MemberService, to = MemberService, scope=singleton)
    binder.bind(DBConfig, to = RemoteDBConfig, scope=singleton)
```

이후 Lambda에서 다음 환경변수들을 설정해 줍니다.
```
DB_HOST
DB_ID
DB_PASSWORD
DB_PORT (3306)
DB_NAME (v1: meverty-api, dev: meverty-dev)
```
이후 Pull Request를 보내면 자동으로 dev stage에 배포됩니다.

### Troubleshooting
Lambda에 deploy할 때 500 Internal Server Error >> No module named 'wsgi-handler' 상황이 발생하면
package-lock.json과 node-modules폴더를 삭제하고 다시 npm install을 실행한다.