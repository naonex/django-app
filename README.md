# 環境構築手順

#### プロジェクトカレントディレクトリでpython仮想環境作成
`py -m venv .venv`

#### 仮想環境に入る
`.venv\Scripts\activate`

#### django含む必要なライブラリインストール
(venv) `pip install -r requirements.txt`

#### DBマイグレーション
(venv) `python manage.py migrate`

#### 付録：管理者アカウント作成
(venv) `python manage.py createsuperuser`

---
## djangoサービス起動 ※vscodeの実行とデバッグから開始・終了も可
(venv) `python djangoApp\manage.py runserver` ...（ctrl + c で終了）
#### ポート指定したい時の例：
(venv) `python djangoApp\manage.py runserver 8080` ...（ちなみにデフォだと8000で起動）

`localhost:8000(デフォの場合)` にアクセスし、ログインページに行けたらOK。  
ログインして確認してね！アカウントはローカルDB管理なので適当に作成してもらってOKです！

---
# ※初回構築時のコマンド例

#### djangoインストール
(venv) `python -m pip install Django`

#### 使用するライブラリインストール
(venv) `pip install requests`

#### プロジェクトを作成する
(venv) `django-admin startproject djangoApp`

#### アプリケーションをつくる
(venv) `python djangoApp\manage.py startapp ffmpeg`
