class Config :
    HOST = 'database-1.c56mxvfytstp.ap-northeast-2.rds.amazonaws.com'
    DATABASE = 'memo' # 스키마 이름
    DB_USER = 'memo_db_user' # create user 'memo_db_user'@'%' identified by '1234';
    DB_PASSWORD = '1234'

    SALT = '12312312'

    JWT_SECRET_KEY = 'hello~!by@'
    JWT_ACCESS_TOKEN_EXPIRES = False # 토큰의 만료 시간
    PROPAGATE_EXCEPTIONS = True # 명시적으로 예외를 전파하는 것에 대한 활성화