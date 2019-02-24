# CooolisGather

CooolisGather是一个以celery为后端异步驱动的前渗透信息搜集框架。

## 环境

python3.6+

## 联系

rvn0xsy@gmail.com

## 安装

```sybase
git clone https://github.com/Cooolis/CooolisGather.git
cd CooolisGather
pip install -r requirements.txt
python manage.py migrate
celery worker -A CooolisGather -l debug
python manage.py runserver
```
