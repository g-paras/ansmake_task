<h1 align="center">ANSMAKE Assessment</h1>

## Setup
```sh
git clone https://github.com/g-paras/ansmake_task.git
cd ansmake_task
pip install -r requirements.txt
python manage.py runserver
```

## API Endpoints

`GET`: `https://ansmakeapi.herokuapp.com/task/all/`

Returns
```json
{
  "data": [
    {
      "id": 1, 
      "name": "task_name", 
      "description": "task_description", 
      "email": "john@gmail.com", 
      "createdAt": "2022-06-02T18:16:10.808Z"
    }
  ]
}
```

`POST`: `https://ansmakeapi.herokuapp.com/task/new/`

body
```json
{
  "name": "task_name",
  "description": "task_description",
  "email": "email"
}
```
Returns
```
Task successfully created
```
